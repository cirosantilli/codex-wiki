"""Draw abstract link/open-reference lifetimes; Python 3.14 / matplotlib 3.10.7.

Run from _media; write only the matching PNG in the current directory.
The names, references and unlink/close operations are Python-only models.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


INK = "#203040"
BLUE = "#155d8a"
GREEN = "#186a52"
ORANGE = "#935017"


def stages():
    inode = {"number": 42, "contents": b"hello\n"}
    names = {"a": inode, "b": inode}
    descriptions = [{"inode": inode, "position": 0}]
    result = []

    def capture():
        links, opens = len(names), len(descriptions)
        retained = bool(links or opens)
        result.append({"names": tuple(names), "links": links, "opens": opens,
                       "retained": retained})
        if descriptions:
            assert descriptions[0]["inode"]["contents"] == b"hello\n"
        if not retained:
            inode.clear()  # Reclamation in the model, never a filesystem operation.

    capture()
    del names["a"]
    capture()
    del names["b"]
    capture()
    assert descriptions[0]["inode"]["contents"] == b"hello\n"
    descriptions.clear()
    capture()
    assert [(s["links"], s["opens"]) for s in result] == [(2, 1), (1, 1), (0, 1), (0, 0)]
    assert [s["retained"] for s in result] == [True, True, True, False]
    assert not inode
    return result


def main():
    snapshots = stages()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(12, 6.1), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 13), ylim=(0, 6.5))
    ax.axis("off")

    def label(x, y, text, size=12, color=INK, weight="normal"):
        ax.text(x, y, text, ha="center", va="center", fontsize=size,
                color=color, weight=weight, linespacing=1.6)

    def box(x, y, w, h, text, color, fill, size=12):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.035",
                                   edgecolor=color, facecolor=fill, linewidth=1.5))
        label(x + w / 2, y + h / 2, text, size=size, color=color)

    label(6.5, 6.08, "Removing names does not close an open file", 21, weight="bold")
    label(6.5, 5.6, "L = hard links • O = live open file descriptions • one descriptor, fd 3", 12)
    xs = (0.25, 3.5, 6.75, 10)
    headings = ("Initial state", "Name a removed", "Last name removed", "Last reference closed")
    for x, s, heading in zip(xs, snapshots, headings):
        middle = x + 1.35
        color = GREEN if s["links"] else ORANGE if s["opens"] else "#596675"
        label(middle, 4.82, heading, 12, weight="bold")
        box(x, 4.06, 2.7, 0.5, f"L = {s['links']}      O = {s['opens']}", color, "#f5f7f9", 14)
        names_text = ", ".join(s["names"]) if s["names"] else "none"
        label(middle, 3.6, f"Names: {names_text}", 13)
        if s["retained"]:
            box(x + 0.1, 2.31, 2.5, 0.9, "Inode 42 retained\n6 bytes: hello + newline", color, "#edf4f1", 11)
            box(x + 0.1, 0.92, 2.5, 0.75, "fd 3 → open description\n→ same file", BLUE, "#edf4fa", 11)
            ax.add_patch(FancyArrowPatch((middle, 1.73), (middle, 2.25),
                                        arrowstyle="-|>", mutation_scale=15,
                                        linewidth=1.5, color=BLUE))
            status = "Still named and readable" if s["links"] else "Unnamed, still readable"
        else:
            box(x + 0.1, 2.31, 2.5, 0.9, "Inode and data blocks\nreclaimed", color, "#f5f7f9", 12)
            label(middle, 1.3, "fd 3 closed\nNo open reference", 12, color)
            status = "Storage becomes reusable"
        label(middle, 0.4, status, 11, color)

    for left, right, operation in zip(xs, xs[1:], ('unlink("a")', 'unlink("b")', "close(3)")):
        # Arrows and labels sit above the cards, away from their state contents.
        start, end = left + 2.4, right + 0.3
        ax.add_patch(FancyArrowPatch((start, 5.16), (end, 5.16), arrowstyle="-|>",
                                    mutation_scale=15, linewidth=1.6, color=INK))
        label((start + end) / 2, 5.37, operation, 10)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)
    print("Abstract stages: (2,1) → (1,1) → (0,1) → (0,0); retained: yes, yes, yes, no.")


if __name__ == "__main__":
    main()
