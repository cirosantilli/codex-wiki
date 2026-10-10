"""Draw the summation-loop contract; run from _media to write the PNG there.

Tested with Python 3.14, matplotlib 3.10.7. No external assets.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, ax = plt.subplots(figsize=(10.8, 7.8), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.91, bottom=0.045)
    ax.set(xlim=(0, 10), ylim=(0, 8.4))
    ax.axis("off")
    ink, blue, orange, green = "#23334a", "#266ca0", "#bc641d", "#21795f"
    fig.suptitle("A contract becomes four proof obligations", fontsize=19, weight="bold", y=0.975)
    fig.text(0.5, 0.927, "Exact mathematical integers • sequential steps • n stays unchanged",
             ha="center", color=ink, fontsize=12)

    def box(x, y, w, h, text, edge, fill):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.09",
                                   facecolor=fill, edgecolor=edge, linewidth=1.6))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=ink,
                linespacing=1.65)

    def arrow(points, color=ink):
        for start, end in zip(points[:-2], points[1:-1]):
            ax.plot([start[0], end[0]], [start[1], end[1]], color=color, lw=1.7)
        ax.add_patch(FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>",
                                    mutation_scale=14, linewidth=1.7, color=color))

    box(3.15, 7.25, 3.7, 0.75, "Precondition\n" + r"$n\in\mathbb{Z},\quad n\geq0$", blue, "#eef6fd")
    box(3.15, 5.9, 3.7, 0.7, "Initialize:  i = 0;  s = 0", ink, "#f5f6f8")
    box(2.8, 4.4, 4.4, 0.85, "Loop head: invariant I\n" + r"$0\leq i\leq n,\quad 2s=i(i+1)$", blue, "#e5f1fc")
    diamond = [(5, 3.85), (6.1, 3.15), (5, 2.45), (3.9, 3.15)]
    ax.add_patch(Polygon(diamond, facecolor="#fff4e6", edgecolor=orange, lw=1.7))
    ax.text(5, 3.15, "i < n ?", ha="center", va="center", fontsize=16, weight="bold", color=ink)
    box(3.15, 0.9, 3.7, 0.85, "Body (in this order)\ni = i + 1;  s = s + i", orange, "#fff4e6")
    box(7.65, 2.57, 2.0, 1.2, "Return s\n" + r"$i=n$" + "\n" + r"$2s=n(n+1)$", green, "#eaf6ef")

    arrow([(5, 7.16), (5, 6.69)])
    arrow([(5, 5.81), (5, 5.34)])
    arrow([(5, 4.31), (5, 3.86)])
    arrow([(5, 2.44), (5, 1.84)], orange)
    arrow([(6.12, 3.15), (7.54, 3.15)], green)
    arrow([(3.06, 1.32), (1.9, 1.32), (1.9, 4.82), (2.7, 4.82)], blue)

    ax.text(5.15, 2.1, "true", va="center", color=orange, fontsize=12)
    ax.text(6.82, 3.38, "false", ha="center", color=green, fontsize=12)
    ax.text(0.25, 6.18, "1  Establish I\nat initialization", color=blue, va="center", linespacing=1.5)
    ax.text(0.25, 3.35, "2  Restore I\nafter both\nassignments", color=blue, va="center", linespacing=1.5)
    ax.text(7.65, 4.65, "3  I + false condition\ngives the answer", color=green, va="center", linespacing=1.5)
    ax.text(7.5, 1.25, "4  Prove progress\n" + r"$V=n-i\quad\to\quad V-1$" + "\nnonnegative integer",
            color=orange, va="center", linespacing=1.65)
    ax.text(5, 0.18, "I holds at condition checks; it need not hold between the two assignments.",
            ha="center", va="center", color=ink, fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
