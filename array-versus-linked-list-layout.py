"""Draw toy array slots and separated list nodes.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; write the matching opaque PNG in the current directory.
Addresses are teaching labels, never actual allocation addresses.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


BLUE = "#155d8a"
GREEN = "#187355"
ORANGE = "#a84b12"
INK = "#203040"


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11, 8), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 9))
    ax.axis("off")

    def text(x, y, value, size=12, color=INK, weight="normal", ha="center"):
        ax.text(x, y, value, ha=ha, va="center", fontsize=size,
                color=color, weight=weight, linespacing=1.4)

    def arrow(start, end, color=BLUE, curve=0):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                   connectionstyle=f"arc3,rad={curve}",
                                   mutation_scale=18, linewidth=1.8, color=color))

    def slots(y, values, highlight=None, addresses=False):
        for i, value in enumerate(values):
            color = ORANGE if i == highlight else BLUE
            ax.add_patch(Rectangle((2.2 + i * 1.3, y), 1.3, 0.65,
                                   facecolor="#fff1e5" if i == highlight else "#edf4fa",
                                   edgecolor=color, linewidth=1.5))
            text(2.85 + i * 1.3, y + 0.33, value or "unused", 14 if value else 11, color)
            if addresses:
                text(2.85 + i * 1.3, y - 0.3, f"i={i} · {100 + 4*i}", 11)

    text(6, 8.6, "Array indexing versus link following", 21, weight="bold")
    text(6, 8.12, "Toy labels only: no real addresses or pointer values", 12)
    text(0.5, 7.55, "Array: adjacent 4-unit slots", 15, BLUE, "bold", "left")
    slots(6.5, ["A", "B", "C", None], addresses=True)
    text(9.55, 6.85, "Read index 2 directly:\n100 + 2 × 4 = 108\nconstant-cost RAM access", 12, BLUE)
    arrow((7.55, 7.25), (5.45, 7.25))
    arrow((5.45, 7.25), (5.45, 7.18))

    text(0.5, 5.68, "Singly linked list: separately positioned nodes", 15, GREEN, "bold", "left")
    positions = {"A": (1.8, 4.05, 40), "B": (5.0, 4.8, 12), "C": (8.3, 3.95, 76)}
    for item, (x, y, position) in positions.items():
        ax.add_patch(Rectangle((x, y), 1.5, 0.7, facecolor="#eaf5ef",
                               edgecolor=GREEN, linewidth=1.5))
        text(x + 0.75, y + 0.35, f"{item} | next", 13, GREEN)
        text(x + 0.75, y - 0.25, f"position {position}", 11)
    text(0.65, 4.4, "head", 12, GREEN)
    arrow((1.15, 4.4), (1.77, 4.4), GREEN)
    arrow((3.35, 4.4), (4.96, 5.12), GREEN)
    arrow((6.55, 5.12), (8.26, 4.3), GREEN)
    arrow((9.85, 4.3), (10.48, 4.3), GREEN)
    text(10.85, 4.3, "null", 12, GREEN)
    text(6, 3.25, "Read index 2: follow A.next, then B.next (2 link steps).", 12, GREEN)

    text(0.5, 2.66, "Array insertion after B: preserve C before writing X", 15, ORANGE, "bold", "left")
    for y, values, label, highlight in [
        (1.75, ["A", "B", "C", None], "Before", None),
        (0.95, ["A", "B", "C", "C"], "Copy C", 3),
        (0.15, ["A", "B", "X", "C"], "Write X", 2),
    ]:
        slots(y, values, highlight)
        text(1.0, y + 0.33, label, 12)
    text(9.65, 1.27, "Spare capacity required.\nShift right to left:\nslot 3 ← slot 2\nthen slot 2 ← X", 12, ORANGE)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
