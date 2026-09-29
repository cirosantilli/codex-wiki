#!/usr/bin/env python3
"""Import numbered NST question trees, never statements, figures or answers.

Existing paper files are never overwritten. Update the catalogue's explicit
answer-coverage decisions before importing newly discovered sources.
"""

import argparse
from dataclasses import dataclass, field
import json
import hashlib
from pathlib import Path
import re


REPO = Path(__file__).resolve().parent.parent
TOKEN = re.compile(
    r"\\(?P<command>question|q|partq|partheading|examsection|sect|section|subsection|subsubsection|paragraph|textbf)\*?"
    r"\{(?P<argument>[^{}\n]{1,120})\}"
    r"|\\(?P<fixed>sectiona|sectionb)\b"
    r"|\\(?P<enumeration>begin|end)\{(?P<environment>enumerate|parts|subparts)\}(?P<options>\[[^\]\n]*\])?"
    r"|\\(?P<item>item)\b(?:\[(?P<item_label>[^\]\n]+)\])?"
    r"|\((?P<plain>[a-z]|[ivx]{2,6}|\d+)\)"
)


@dataclass
class Node:
    title: str
    parent: "Node | None" = None
    kind: str = "part"
    children: list = field(default_factory=list)

    def child(self, title, kind="part"):
        if any(c.title == title for c in self.children):
            raise ValueError(f"Repeated label {title!r} under {self.title!r}")
        node = Node(title, self, kind)
        self.children.append(node)
        return node


def roman(n):
    result = ""
    for value, text in [(100, "c"), (90, "xc"), (50, "l"), (40, "xl"),
                        (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]:
        while n >= value:
            result += text
            n -= value
    return result


def number(n, style):
    if style == "roman":
        return roman(n)
    if style == "arabic":
        return str(n)
    result = ""
    while n:
        n, digit = divmod(n - 1, 26)
        result = chr(97 + digit) + result
    return result


def reviewed_numbering_tree(source, title, definition, source_sha256):
    """Accept reviewed labels only, guarded against a changed source transcription."""
    digest = hashlib.sha256(source.encode()).hexdigest()
    if digest != source_sha256:
        raise ValueError("Reviewed numbering tree source hash does not match")
    root = Node(title, kind="paper")
    def append(parent, entries):
        if not isinstance(entries, list):
            raise ValueError("Reviewed numbering children must be a list")
        for item in entries:
            if set(item) != {"title", "kind", "children"}:
                raise ValueError("Reviewed numbering nodes contain labels only")
            label, kind = item["title"], item["kind"]
            if kind not in {"section", "question", "part"} or not re.fullmatch(
                r"(?:Section [A-Z0-9]+(?:\([ivx]+\))?|[A-E]?\d+(?:\.\d+)*[A-Z]?|[a-z]+(?: \([A-Za-z0-9 ]{1,64}\))?|[A-Z]+)", label
            ):
                raise ValueError(f"Unsupported reviewed label/kind: {label!r}/{kind!r}")
            child = parent.child(label, kind)
            append(child, item["children"])
    append(root, definition)
    if not any(n is not root and not n.children and n.kind != "section" for n in walk(root)):
        raise ValueError("Reviewed numbering tree contains no tasks")
    return root


def question_tree(source, title, *, reference_enumerations=(), inline_subparts=False,
                  numbering_tree=None, source_sha256=None):
    """Read labels only; ambiguous inline/reference lists require paper options."""
    if numbering_tree is not None:
        if reference_enumerations or inline_subparts:
            raise ValueError("Reviewed trees cannot be combined with inferred parser options")
        return reviewed_numbering_tree(source, title, numbering_tree, source_sha256)
    if source_sha256 is not None:
        raise ValueError("Source hash without a reviewed numbering tree")
    source = re.sub(r"(?<!\\)%[^\n]*", "", source)
    preamble, source = source.split(r"\begin{document}", 1)
    source = source.split(r"\end{document}", 1)[0]
    # Read only these literal declarations, never execute or expand arbitrary TeX.
    custom_options = dict(re.findall(
        r"\\newenvironment\{(parts|subparts)\}\{\s*\\begin\{enumerate\}"
        r"(\[[^\]\n]*\])\s*\}\{\s*\\end\{enumerate\}\s*\}", preamble
    ))
    prefix = re.search(
        r"\\newcommand\{\\question\}\[1\]\{\s*\\clearpage\s*"
        r"\\section\*?\{([A-E])#1\}\s*\}", preamble
    )
    question_prefix = prefix[1] if prefix else ""
    # An unstyled list can contain supplied data instead of tasks. Its exact
    # question/part path must be explicitly reviewed; all other such lists fail.
    references = {tuple(path) for path in reference_enumerations}
    used_references = set()
    # This supplied list consists of integration identities, not exam subparts.
    source = re.sub(r"\[You may find the following results useful:[\s\S]*?\]", "", source)
    inline_labels = set()
    # Inline labels need an explicit paper-level review: elsewhere the same
    # typography may denote equations, cases or references rather than subparts.
    for line in re.finditer(r"[^\n]+", source) if inline_subparts else ():
        for pattern, formatter in [(r"[ivx]+", roman), (r"\d+", str)]:
            labels = list(re.finditer(r"(?<![\w)])\((" + pattern + r")\)", line[0]))
            if len(labels) >= 2 and [m[1] for m in labels] == [formatter(i) for i in range(1, len(labels) + 1)]:
                inline_labels.update(line.start() + m.start() for m in labels)
    root = Node(title, kind="paper")
    section, question, part, roman_parent = None, None, None, None
    stack = []
    last_end = 0
    for match in TOKEN.finditer(source):
        command, argument = match["command"], match["argument"]
        if stack and stack[-1].get("reference"):
            if match["enumeration"] == "begin":
                raise ValueError("Nested enumeration inside a reviewed reference list")
            if match["enumeration"] == "end":
                if match["environment"] != stack[-1]["environment"]:
                    raise ValueError("Mismatched reference-list environment")
                stack.pop()
            continue
        section_label = None
        if match["fixed"]:
            section_label = match["fixed"][-1].upper()
        elif command in {"examsection", "sect"}:
            section_label = argument
        elif command in {"section", "subsection", "subsubsection", "textbf"}:
            hit = re.fullmatch(r"Section\s+([A-E]|[IVX]+|\d+)(?:\s+[^{}]*)?", argument, re.I)
            if hit:
                section_label = hit[1].upper()
        if section_label:
            if stack:
                raise ValueError("Section begins inside an enumeration")
            section = root.child("Section " + section_label, "section")
            question = part = roman_parent = None
        elif command == "paragraph" and (combined := re.fullmatch(
            r"(?:Question\s+)?([A-E]?\d+)((?:\([a-z0-9]+\))+)", argument, re.I
        )):
            if stack:
                raise ValueError("Paragraph label begins inside an enumeration")
            parent = section or root
            if question is None or question.title != combined[1]:
                question = parent.child(combined[1], "question")
            labels = re.findall(r"\(([^)]+)\)", combined[2])
            part = question
            for i, label in enumerate(labels):
                existing = next((c for c in part.children if c.title == label), None)
                part = existing if existing and i < len(labels) - 1 else part.child(label)
            roman_parent = None
        elif command in {"question", "q", "section", "subsection", "textbf"} and re.fullmatch(
            r"(?:Question\s+)?[A-E]?\d+\.?", argument or "", re.I
        ):
            if stack:
                raise ValueError("Question begins inside an enumeration")
            label = re.sub(r"^Question\s+|\.$", "", argument, flags=re.I)
            if command == "question" and label.isdigit():
                label = question_prefix + label
            question = (section or root).child(label, "question")
            part = roman_parent = None
        elif command == "partheading":
            # The practical notebooks print complete labels such as A1a.
            # A whole-question mark heading, e.g. D12, adds no new node.
            if question is None or stack:
                raise ValueError("Practical part heading without an outer question")
            if argument != question.title:
                labelled = re.fullmatch(r"([A-E]?\d+)([a-z])", argument)
                if labelled is None or labelled[1] != question.title:
                    raise ValueError(f"Practical part label does not match its question: {argument}")
                part = question.child(labelled[2])
                roman_parent = None
        elif command == "partq":
            if question is None:
                raise ValueError("Part without a question")
            part = question.child(argument.strip("()"))
            roman_parent = None
        elif match["enumeration"] == "begin":
            if question is None:
                raise ValueError("Enumeration before the first question")
            options = match["options"] or ""
            environment = match["environment"]
            if environment != "enumerate":
                if environment not in custom_options or options:
                    raise ValueError(f"Unsupported declaration/options for {environment}")
                options = custom_options[environment]
            style = next((s for s in ["roman", "arabic", "alph"] if "\\" + s in options), None)
            if style is None:
                node = part or question
                path = []
                while node is not root:
                    path.append(node.title)
                    node = node.parent
                path = tuple(reversed(path))
                if environment == "enumerate" and not options and path in references and path not in used_references:
                    used_references.add(path)
                    stack.append(dict(reference=True, environment=environment))
                    continue
                raise ValueError("Enumeration needs an explicit numbering style or reviewed reference path")
            start = re.search(r"start\s*=\s*(\d+)", options)
            parent = stack[-1]["current"] if stack else (part or question)
            if parent is None:
                raise ValueError("Nested enumeration before its parent item")
            # A restarted outer enumerate continues the question's alphabetic parts.
            if not stack and style == "alph":
                parent = question
            stack.append(dict(parent=parent, current=None, style=style,
                              environment=environment,
                              counter=int(start[1]) - 1 if start else 0))
        elif match["enumeration"] == "end":
            if not stack:
                raise ValueError("Unmatched end of enumeration")
            if match["environment"] != stack[-1]["environment"]:
                raise ValueError("Mismatched enumeration environment")
            stack.pop()
            part = stack[-1]["current"] if stack else None
            roman_parent = None
        elif match["item"] and stack:
            frame = stack[-1]
            frame["counter"] += 1
            label = (match["item_label"] or number(frame["counter"], frame["style"])).strip("().")
            part = frame["parent"].child(label)
            frame["current"] = part
            roman_parent = None
        elif match["plain"] and question:
            line_prefix = source[source.rfind("\n", 0, match.start()) + 1:match.start()]
            inline = match.start() in inline_labels
            if match["plain"].isdigit() and not inline:
                continue
            if not inline and line_prefix.strip() not in ("", "EITHER", "OR") and source[last_end:match.start()].strip():
                continue
            label = match["plain"]
            is_roman = inline or len(label) > 1 or (label == "i" and not any(c.title == "h" for c in question.children))
            if is_roman:
                if label == "i" or roman_parent is None:
                    roman_parent = (stack[-1]["current"] if stack else part) or question
                part = roman_parent.child(label)
            else:
                part = question.child(label)
                roman_parent = None
        else:
            continue
        last_end = match.end()
    if stack:
        raise ValueError("Unclosed enumeration")
    if used_references != references:
        raise ValueError(f"Unused reviewed reference paths: {sorted(references - used_references)}")
    if not any(node.kind == "question" for node in walk(root)):
        raise ValueError("No questions found")
    return root


def walk(node):
    yield node
    for child in node.children:
        yield from walk(child)


def render(tree, source, *, title2=None, fixedcaps=False, root_parent=None):
    metadata = "{scope}" + ("\n{c}" if fixedcaps else "")
    if title2:
        if "\n" in title2 or "{" in title2 or "}" in title2:
            raise ValueError("Paper subtitle must be plain single-line text")
        metadata += f"\n{{title2={title2}}}"
    blocks = [f"= {tree.title}\n{metadata}", source]
    for node in list(walk(tree))[1:]:
        # Some papers repeat printed a/b labels within one question. Keep the
        # reviewed qualifier in metadata so it does not change the printed label.
        qualified = re.fullmatch(r"([a-z]+) \(([A-Za-z0-9 ]{1,64})\)", node.title)
        title = qualified[1] if qualified else node.title
        disambiguate = f"\n{{disambiguate={qualified[2]}}}" if qualified else ""
        capitalization = "{c}\n" if re.fullmatch(r"(?:[A-E]\d+|\d+[A-Z])", node.title) else ""
        parent = root_parent if node.parent is tree and root_parent else node.parent.title
        blocks.append(f"= {title}\n{capitalization}{{parent={parent}}}{disambiguate}\n{{scope}}")
        if not node.children and node.kind != "section":
            blocks.append(f"= Solution\n{{parent={node.title}}}")
    return "\n\n".join(blocks) + "\n"


def update_index(path, title, note, years, check):
    includes = "\n".join(f"\\Include[{year}]" for year in sorted(years, reverse=True))
    if path.exists():
        old = path.read_text()
        current = re.findall(r"^\\Include\[(\d{4})\]$", old, re.M)
        if current == sorted(years, reverse=True):
            return
        if check:
            raise ValueError(f"Outdated year index: {path}")
        old = re.sub(r"^\\Include\[\d{4}\]\n?", "", old, flags=re.M)
        path.write_text(old.rstrip() + "\n\n" + includes + "\n")
    elif check:
        raise ValueError(f"Missing index: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"= {title}\n\n" + (note + "\n\n" if note else "") + includes + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-root", type=Path,
                        default=REPO.parent / "exams/cambridge-exams/tex/nst")
    parser.add_argument("--check", action="store_true", help="check existing trees without writing")
    args = parser.parse_args()
    catalogue = json.loads(Path(__file__).with_name("nst-exam-catalog.json").read_text())
    known_courses = {c["source_path"] for c in catalogue["courses"]}
    discovered = {"/".join(p.relative_to(args.tex_root).parts[:2])
                  for p in args.tex_root.rglob("*.tex")}
    if discovered - known_courses:
        raise ValueError(f"Course placement and coverage need cataloguing: {sorted(discovered - known_courses)}")
    counts = dict(created=0, checked=0, skipped=0, questions=0, parts=0)
    for course in catalogue["courses"]:
        folder = REPO / course["path"]
        years = set()
        if course.get("existing_mathematics"):
            years = {p.name for p in folder.iterdir() if p.is_dir() and p.name.isdigit()}
        else:
            for path in sorted((args.tex_root / course["source_path"]).rglob("*.tex")):
                rel = path.relative_to(args.tex_root).as_posix()
                year = next(p for p in path.relative_to(args.tex_root).parts if re.fullmatch(r"\d{4}(?:\.tex)?", p)).removesuffix(".tex")
                if year in course.get("skip_years", []):
                    counts["skipped"] += 1
                    continue
                paper = path.stem if path.stem != year else None
                paper_options = catalogue.get("paper_options", {}).get(rel, {})
                paper = paper_options.get("paper", paper)
                title = paper_options.get("title", "Paper " + paper if paper else year)
                render_options = {key: paper_options[key] for key in ("title2", "fixedcaps", "root_parent")
                                  if key in paper_options}
                output = folder / year / ("paper-" + paper + ".bigb") if paper else folder / (year + ".bigb")
                # Keep already authored trees, but do not create duplicates when
                # the course advertises student answers for this paper's year.
                if catalogue.get("availability", {}).get(rel, {}).get("decision") == "skip" and not output.exists():
                    counts["skipped"] += 1
                    continue
                tree = question_tree(path.read_text(), title,
                                     **catalogue.get("parser_options", {}).get(rel, {}))
                counts["questions"] += sum(n.kind == "question" for n in walk(tree))
                counts["parts"] += sum(n.kind == "part" for n in walk(tree))
                if rel not in catalogue["papers"]:
                    raise ValueError(f"Source links and solution coverage need cataloguing: {rel}")
                source = catalogue["papers"][rel]
                if output.exists():
                    # Compare header trees only: future authored solution prose is preserved.
                    actual = re.findall(r"^= .*\n(?:\{[^\n]*\}\n)*", output.read_text(), re.M)
                    expected = re.findall(r"^= .*\n(?:\{[^\n]*\}\n)*", render(tree, source, **render_options), re.M)
                    if actual != expected:
                        raise ValueError(f"Header tree differs from transcription: {output}")
                    counts["checked"] += 1
                elif args.check:
                    raise ValueError(f"Missing paper tree: {output}")
                else:
                    output.parent.mkdir(parents=True, exist_ok=True)
                    output.write_text(render(tree, source, **render_options))
                    counts["created"] += 1
                years.add(year)
                if paper:
                    papers = [p.stem for p in output.parent.glob("paper-*.bigb")]
                    index = output.parent / "index.bigb"
                    includes = "\n".join(f"\\Include[{p}]" for p in sorted(papers)) + "\n"
                    old = index.read_text() if index.exists() else f"= {year}\n{{scope}}\n\n"
                    current = re.findall(r"^\\Include\[(paper-[^\]\n]+)\]$", old, re.M)
                    if current == sorted(papers):
                        continue
                    if args.check:
                        raise ValueError(f"Outdated paper index: {index}")
                    else:
                        old = re.sub(r"^\\Include\[paper-[^\]\n]+\]\n?", "", old, flags=re.M)
                        index.write_text(old.rstrip() + "\n\n" + includes)
        if years:
            update_index(folder / "index.bigb", course["exam_title"], course.get("note", ""), years, args.check)
    print(json.dumps(counts))


if __name__ == "__main__":
    main()
