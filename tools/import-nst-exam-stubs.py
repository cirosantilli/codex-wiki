#!/usr/bin/env python3
"""Import numbered NST question trees, never statements, figures or answers.

Existing paper files are never overwritten. Update the catalogue's explicit
answer-coverage decisions before importing newly discovered sources.
"""

import argparse
from dataclasses import dataclass, field
import json
from pathlib import Path
import re


REPO = Path(__file__).resolve().parent.parent
DEST = REPO / "past-exam-of-the-natural-sciences-course-of-the-university-of-cambridge"
TOKEN = re.compile(
    r"\\(?P<command>question|q|partq|examsection|sect|section|subsection|subsubsection|textbf)\*?"
    r"\{(?P<argument>[^{}\n]{1,120})\}"
    r"|\\(?P<fixed>sectiona|sectionb)\b"
    r"|\\(?P<enumeration>begin|end)\{enumerate\}(?P<options>\[[^\]\n]*\])?"
    r"|\\(?P<item>item)\b(?:\[(?P<item_label>[^\]\n]+)\])?"
    r"|\((?P<plain>[a-z]|[ivx]{2,6})\)"
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


def question_tree(source, title):
    source = source.split(r"\begin{document}", 1)[1].split(r"\end{document}", 1)[0]
    source = re.sub(r"(?<!\\)%[^\n]*", "", source)
    # This supplied list consists of integration identities, not exam subparts.
    source = re.sub(r"\[You may find the following results useful:[\s\S]*?\]", "", source)
    root = Node(title, kind="paper")
    section, question, part, roman_parent = None, None, None, None
    stack = []
    last_end = 0
    for match in TOKEN.finditer(source):
        command, argument = match["command"], match["argument"]
        section_label = None
        if match["fixed"]:
            section_label = match["fixed"][-1].upper()
        elif command in {"examsection", "sect"}:
            section_label = argument
        elif command in {"section", "subsection", "subsubsection", "textbf"}:
            hit = re.fullmatch(r"Section\s+([A-E])", argument, re.I)
            if hit:
                section_label = hit[1].upper()
        if section_label:
            if stack:
                raise ValueError("Section begins inside an enumeration")
            section = root.child("Section " + section_label, "section")
            question = part = roman_parent = None
        elif command in {"question", "q", "section", "subsection", "textbf"} and re.fullmatch(
            r"(?:Question\s+)?[A-E]?\d+\.?", argument or "", re.I
        ):
            if stack:
                raise ValueError("Question begins inside an enumeration")
            label = re.sub(r"^Question\s+|\.$", "", argument, flags=re.I)
            question = (section or root).child(label, "question")
            part = roman_parent = None
        elif command == "partq":
            if question is None:
                raise ValueError("Part without a question")
            part = question.child(argument.strip("()"))
            roman_parent = None
        elif match["enumeration"] == "begin":
            if question is None:
                raise ValueError("Enumeration before the first question")
            options = match["options"] or ""
            style = next((s for s in ["roman", "arabic", "alph"] if "\\" + s in options), None)
            if style is None:
                raise ValueError("Enumeration needs an explicit numbering style")
            start = re.search(r"start\s*=\s*(\d+)", options)
            parent = stack[-1]["current"] if stack else (part or question)
            # A restarted outer enumerate continues the question's alphabetic parts.
            if not stack and style == "alph":
                parent = question
            stack.append(dict(parent=parent, current=None, style=style,
                              counter=int(start[1]) - 1 if start else 0))
        elif match["enumeration"] == "end":
            if not stack:
                raise ValueError("Unmatched end of enumeration")
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
            if line_prefix.strip() and source[last_end:match.start()].strip():
                continue
            label = match["plain"]
            is_roman = len(label) > 1 or (label == "i" and not any(c.title == "h" for c in question.children))
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
    if not any(node.kind == "question" for node in walk(root)):
        raise ValueError("No questions found")
    return root


def walk(node):
    yield node
    for child in node.children:
        yield from walk(child)


def render(tree, source):
    blocks = [f"= {tree.title}\n{{scope}}", source]
    for node in list(walk(tree))[1:]:
        capitalization = "{c}\n" if re.fullmatch(r"[A-E]\d+", node.title) else ""
        blocks.append(f"= {node.title}\n{capitalization}{{parent={node.parent.title}}}\n{{scope}}")
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
        folder = DEST / course["path"]
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
                title = "Paper " + paper if paper else year
                output = folder / year / ("paper-" + paper + ".bigb") if paper else folder / (year + ".bigb")
                tree = question_tree(path.read_text(), title)
                counts["questions"] += sum(n.kind == "question" for n in walk(tree))
                counts["parts"] += sum(n.kind == "part" for n in walk(tree))
                if rel not in catalogue["papers"]:
                    raise ValueError(f"Source links and solution coverage need cataloguing: {rel}")
                source = catalogue["papers"][rel]
                if output.exists():
                    # Compare header trees only: future authored solution prose is preserved.
                    actual = re.findall(r"^= .*\n(?:\{[^\n]*\}\n)*", output.read_text(), re.M)
                    expected = re.findall(r"^= .*\n(?:\{[^\n]*\}\n)*", render(tree, source), re.M)
                    if actual != expected:
                        raise ValueError(f"Header tree differs from transcription: {output}")
                    counts["checked"] += 1
                elif args.check:
                    raise ValueError(f"Missing paper tree: {output}")
                else:
                    output.parent.mkdir(parents=True, exist_ok=True)
                    output.write_text(render(tree, source))
                    counts["created"] += 1
                years.add(year)
                if paper:
                    papers = [p.stem for p in output.parent.glob("paper-*.bigb")]
                    index = output.parent / "index.bigb"
                    includes = "\n".join(f"\\Include[{p}]" for p in sorted(papers)) + "\n"
                    old = index.read_text() if index.exists() else f"= {year}\n{{scope}}\n\n"
                    current = re.findall(r"^\\Include\[(paper-\d+)\]$", old, re.M)
                    if current == sorted(papers):
                        continue
                    if args.check:
                        raise ValueError(f"Outdated paper index: {index}")
                    else:
                        old = re.sub(r"^\\Include\[paper-\d+\]\n?", "", old, flags=re.M)
                        index.write_text(old.rstrip() + "\n\n" + includes)
        if years:
            update_index(folder / "index.bigb", course["exam_title"], course.get("note", ""), years, args.check)
    print(json.dumps(counts))


if __name__ == "__main__":
    main()
