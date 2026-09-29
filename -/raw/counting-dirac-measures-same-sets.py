"""Original analytical comparison of three measures on Borel subsets of R.

Tested environment: Python 3.14.4, matplotlib 3.10.7; no external data.
Run from _media; the output filename follows this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 14, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10.8, 5.3), dpi=110)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    blue, orange, green = "#245e8e", "#b34f00", "#237344"
    ax.text(0.035, 0.945, "Same sets, three measuring rules", fontsize=21, weight="bold")
    ax.text(0.035, 0.885, "Analytical illustration on the Borel subsets of the real line", fontsize=13)
    for x, label in [(0.035, "Set"), (0.375, "Position on the line"),
                     (0.645, r"Counting $\#$"), (0.795, r"Dirac $\delta_1$"),
                     (0.94, r"Lebesgue $\lambda$")]:
        ax.text(x, 0.805, label, ha="left" if x == 0.035 else "center", fontsize=13, weight="bold")

    rows = [
        (r"$\varnothing$", "empty", ("0", "0", "0")),
        (r"$\{0\}$", "singleton", ("1", "0", "0")),
        (r"$\{0,1,2\}$", "finite", ("3", "1", "0")),
        (r"$[0,2]$", "interval", (r"$\infty$", "1", "2")),
        (r"$\mathbb{Q}\cap[0,2]$", "rational", (r"$\infty$", "1", "0")),
    ]
    line_positions = (0.275, 0.38, 0.485)
    for i, (label, kind, values) in enumerate(rows):
        y = 0.715 - i * 0.13
        ax.axhline(y + 0.06, xmin=0.025, xmax=0.985, color="#d8dee4", lw=0.8)
        ax.text(0.035, y, label, va="center", fontsize=18)
        if kind == "empty":
            ax.text(0.38, y, "No points", ha="center", va="center", color="#536170", fontsize=13)
        elif kind == "rational":
            ax.text(0.38, y + 0.012, "Countably infinite", ha="center", va="center", fontsize=12)
            ax.text(0.38, y - 0.028, "and dense in [0, 2]", ha="center", va="center", fontsize=12)
        else:
            ax.plot([0.255, 0.505], [y, y], color="#aab5bf", lw=1)
            for number, px in enumerate(line_positions):
                ax.plot([px, px], [y - 0.012, y + 0.012], color="#8996a3", lw=1)
                ax.text(px, y - 0.032, str(number), ha="center", va="top", fontsize=11)
            if kind == "interval":
                ax.plot([line_positions[0], line_positions[2]], [y, y], color=blue, lw=6, solid_capstyle="round")
            points = (0,) if kind == "singleton" else (0, 1, 2)
            for point in points:
                ax.scatter([line_positions[point]], [y], s=70, color=orange if point == 1 else blue, zorder=4)
        for x, value in zip((0.645, 0.795, 0.94), values):
            if value == "0":
                ax.add_patch(Rectangle((x - 0.034, y - 0.041), 0.068, 0.082, facecolor="#e5f3e9", edgecolor="none"))
            ax.text(x, y, value, ha="center", va="center", fontsize=21, color=green if value == "0" else "#182838")
    ax.text(0.035, 0.078, "Orange selects the point 1; green zeros identify null sets for that column.", fontsize=13)
    ax.text(0.035, 0.033, "The rational set is named symbolically: a finite dot drawing cannot show all its points.", fontsize=12, color="#536170")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
