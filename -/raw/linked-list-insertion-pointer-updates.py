"""Draw successor preservation and incoming-link redirection.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; write the matching opaque PNG in the current directory.
All positions and references are conceptual; no user files are manipulated.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


INK = "#203040"
GREEN = "#187355"
ORANGE = "#a84b12"


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11, 8.6), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 10.4))
    ax.axis("off")

    def text(x, y, value, size=12, color=INK, weight="normal", ha="center"):
        ax.text(x, y, value, ha=ha, va="center", fontsize=size,
                color=color, weight=weight, linespacing=1.4)

    def arrow(start, end, color=GREEN):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                   mutation_scale=18, linewidth=1.9, color=color))

    text(6, 10.0, "Insert X after a known node B", 21, weight="bold")
    text(6, 9.55, "Conceptual positions stay fixed; only next references change.", 12)
    for stage, y, label in [
        (0, 7.95, "0. Before: B.next reaches C; fresh X is unlinked"),
        (1, 5.13, "1. X.next = B.next   (preserve the old successor C)"),
        (2, 2.31, "2. B.next = X   (redirect B through X)"),
    ]:
        text(0.4, y + 0.84, label, 14, INK, "bold", "left")
        positions = {"A": (1.5, y - 0.1, 40), "B": (3.8, y + 0.08, 12),
                     "C": (9.1, y + 0.08, 76), "X": (6.2, y - 0.78, 28)}
        for item, (x, bottom, position) in positions.items():
            color = ORANGE if item == "X" else GREEN
            ax.add_patch(Rectangle((x, bottom), 1.45, 0.65,
                                   facecolor="#fff1e5" if item == "X" else "#eaf5ef",
                                   edgecolor=color, linewidth=1.5))
            text(x + 0.725, bottom + 0.325, f"{item} | next", 13, color)
            text(x + 0.725, bottom - 0.26, f"position {position}", 10)
        text(0.58, y + 0.22, "head", 11, GREEN)
        arrow((1.0, y + 0.22), (1.46, y + 0.22))
        arrow((2.99, y + 0.22), (3.76, y + 0.4))
        arrow((10.59, y + 0.4), (11.04, y + 0.4))
        text(11.4, y + 0.4, "null", 11, GREEN)
        if stage < 2:
            arrow((5.29, y + 0.4), (9.06, y + 0.4))
        else:
            arrow((5.29, y + 0.3), (6.16, y - 0.38), ORANGE)
        if stage == 0:
            arrow((7.69, y - 0.46), (8.08, y - 0.46), ORANGE)
            text(8.45, y - 0.46, "null", 11, ORANGE)
        else:
            arrow((7.69, y - 0.46), (9.06, y + 0.3), ORANGE)
        text(6, y - 1.45,
             ["Reachable from head: A → B → C",
              "Reachable from head: A → B → C; X also reaches C",
              "Reachable from head: A → B → X → C"][stage], 12)
    text(6, 0.28, "Two next updates; finding B and allocating X have separate costs.", 12)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
