"""Balanced box counts; tested with Python 3.14 and matplotlib 3.10.7.

Write pigeonhole-distribution-counts.png in the current working directory.
"""

from math import ceil
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def draw_case(ax, counts, total, columns, title):
    assert sum(counts) == total
    assert max(counts) == ceil(total / len(counts))
    orange, blue = "#b34e16", "#196a96"
    for i, count in enumerate(counts):
        row, col = divmod(i, columns)
        x, y = col * 1.5, -row * 2.0
        color = orange if count == max(counts) else blue
        ax.add_patch(Rectangle((x, y), 1.16, 1.20, facecolor="#fafbfd",
                               edgecolor=color, linewidth=1.6))
        for j in range(count):
            cx = x + 0.34 + (j % 2) * 0.48
            cy = y + 0.36 + (j // 2) * 0.48
            ax.add_patch(Circle((cx, cy), 0.135, facecolor=color,
                                edgecolor="white", linewidth=0.8))
        ax.text(x + 0.58, y - 0.22, f"Box {i + 1}: {count}",
                ha="center", va="top", fontsize=10, color="#283644")
    rows = ceil(len(counts) / columns)
    ax.set_xlim(-0.3, (columns - 1) * 1.5 + 1.46)
    ax.set_ylim(-(rows - 1) * 2 - 0.70, 1.58)
    ax.set_aspect("equal")
    ax.set_anchor("N")
    ax.axis("off")
    ax.set_title(title, fontsize=14, pad=16, color="#283644")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.8), dpi=120,
                             facecolor="white")
    draw_case(axes[0], [2] + [1] * 11, 13, 6,
              r"13 objects / 12 boxes: $\lceil13/12\rceil=2$")
    draw_case(axes[1], [4, 4, 3, 3, 3, 3, 3], 23, 4,
              r"23 objects / 7 boxes: $\lceil23/7\rceil=4$")
    fig.suptitle("Balanced counts attain the pigeonhole bound", fontsize=17,
                 y=0.95, color="#283644")
    fig.text(0.5, 0.065,
             "Each chip is one object. Orange boxes attain the largest count; no box exceeds it.",
             ha="center", fontsize=11, color="#283644")
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.17, top=0.79,
                        wspace=0.17)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Counts checked: 13 = 2 + 11; 23 = 4 + 4 + 5*3; maxima 2 and 4.")


if __name__ == "__main__":
    main()
