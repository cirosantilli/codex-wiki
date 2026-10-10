"""Draw an original representation pipeline; emit PNG into the current directory.

Tested with Python 3.14, matplotlib 3.10.7; no optional dependencies.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.4))
    ax.axis("off")
    ink, blue, green = "#243746", "#e9f2fc", "#edf7ee"

    def box(x, y, w, h, title, text, color=blue, text_size=11):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                   facecolor=color, edgecolor=ink, linewidth=1.2))
        ax.text(x+w/2, y+h-0.26, title, ha="center", va="center",
                fontsize=12, weight="bold", color=ink)
        ax.text(x+w/2, y+0.32, text, ha="center", va="center",
                fontsize=text_size, color=ink, linespacing=1.4)

    def arrow(start, end, label, offset=(0, 0)):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                    mutation_scale=14, color=ink, linewidth=1.3))
        ax.text((start[0]+end[0])/2+offset[0], (start[1]+end[1])/2+offset[1],
                label, ha="center", va="center", fontsize=10, color=ink,
                bbox=dict(facecolor="white", edgecolor="none", pad=2))

    ax.text(5, 6.1, "Translation changes representation; execution supplies values",
            ha="center", fontsize=15, weight="bold", color=ink)
    box(0.35, 4.65, 2.2, 0.95, "Source expression", "x*(2+3)-4")
    box(3.5, 4.65, 2.2, 0.95, "AST", "Sub(Mul(x, Add(2,3)), 4)", text_size=9)
    box(6.85, 4.65, 2.7, 0.95, "Folded AST", "Sub(Mul(x, 5), 4)")
    arrow((2.65, 5.1), (3.4, 5.1), "parse", (0, 0.3))
    arrow((5.8, 5.1), (6.75, 5.1), "fold 2+3", (0, 0.3))
    box(6.85, 2.45, 2.7, 1.05, "Stack instructions", "LOAD x; PUSH 5; MUL\nPUSH 4; SUB")
    arrow((8.2, 4.55), (8.2, 3.6), "translate", (0.55, 0))
    box(0.35, 2.45, 2.2, 1.05, "Tree interpreter", "input x = 7\nresult = 31", green)
    arrow((4.2, 4.55), (2.05, 3.6), "evaluate AST", (-0.25, -0.1))
    box(6.85, 0.65, 2.7, 0.9, "Instruction interpreter", "input x = 7 → result = 31", green)
    arrow((8.2, 2.35), (8.2, 1.65), "execute", (0.5, 0))
    box(3.5, 0.65, 2.2, 0.9, "Machine code", "optional further target")
    arrow((6.75, 2.85), (4.6, 1.65), "compile further\n(e.g. JIT)", (-0.25, 0))
    ax.text(3.1, 0.12, "An illustrative pipeline: individual implementations may combine or omit steps.",
            fontsize=10, color=ink)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
