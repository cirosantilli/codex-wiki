"""Draw simplified symmetric meiosis; run from _media using Python 3.14.

Tested with matplotlib 3.10.7 and numpy 2.3.5. Output is written to CWD.
No crossing over, unequal cytokinesis, or developmental timing is depicted.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

BLUE, ORANGE = "#2468a2", "#d26722"


def chromosome(ax, x, y, color, length, replicated):
    if replicated:
        for sign in (-1, 1):
            ax.plot([x - sign * 0.13, x + sign * 0.13],
                    [y - length / 2, y + length / 2],
                    color=color, lw=4, solid_capstyle="round")
    else:
        ax.plot([x, x], [y - length / 2, y + length / 2],
                color=color, lw=4, solid_capstyle="round")


def cell(ax, x, y, chromosomes, width=1.65, height=1.35):
    ax.add_patch(Ellipse((x, y), width, height, facecolor="white",
                         edgecolor="#96a2ad", lw=1.5))
    spacing = 0.36 if len(chromosomes) == 4 else 0.5
    for i, (color, length, replicated) in enumerate(chromosomes):
        chromosome(ax, x + (i - (len(chromosomes) - 1) / 2) * spacing,
                   y, color, length, replicated)


def arrow(ax, start, end):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color="#53616c", lw=1.6))


def main():
    fig, ax = plt.subplots(figsize=(12, 6.2), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis("off")
    ax.text(6, 6.8, "One DNA replication, then two divisions",
            ha="center", va="top", fontsize=19, weight="bold")
    stages = [(1.25, "Before replication", "$2n=4,\\ 2C$"),
              (4.1, "After replication", "$2n=4,\\ 4C$"),
              (7.05, "After meiosis I", "$n=2,\\ 2C$ per nucleus"),
              (10.3, "After meiosis II", "$n=2,\\ C$ per nucleus")]
    for x, title, amount in stages:
        ax.text(x, 6.15, title, ha="center", fontsize=12, weight="bold")
        ax.text(x, 5.79, amount, ha="center", fontsize=12)
    unrep = [(BLUE, 0.9, False), (ORANGE, 0.9, False),
             (BLUE, 0.55, False), (ORANGE, 0.55, False)]
    rep = [(c, length, True) for c, length, _ in unrep]
    cell(ax, 1.25, 3.3, unrep, height=1.65)
    cell(ax, 4.1, 3.3, rep, height=1.65)
    pair1 = [(BLUE, 0.9, True), (ORANGE, 0.55, True)]
    pair2 = [(ORANGE, 0.9, True), (BLUE, 0.55, True)]
    cell(ax, 7.05, 4.35, pair1)
    cell(ax, 7.05, 2.25, pair2)
    for y, pair in [(5.0, pair1), (3.7, pair1), (2.4, pair2), (1.1, pair2)]:
        cell(ax, 10.3, y, [(c, length, False) for c, length, _ in pair],
             height=1.13)
    arrow(ax, (2.15, 3.3), (3.18, 3.3))
    ax.text(2.65, 4.42, "DNA\nreplication", ha="center", fontsize=11)
    for y in (4.35, 2.25):
        arrow(ax, (5.0, 3.3), (6.17, y))
    ax.text(5.62, 1.05, "Homologues\nseparate", ha="center", fontsize=11)
    for start_y, ends in [(4.35, (5.0, 3.7)), (2.25, (2.4, 1.1))]:
        for y in ends:
            arrow(ax, (7.92, start_y), (9.42, y))
    ax.text(8.63, 0.37, "Sister chromatids\nseparate", ha="center", fontsize=11)
    ax.text(1.25, 1.87, "Two homologous pairs", ha="center", fontsize=11)
    ax.text(4.1, 1.87, "Each X = one chromosome\nwith two sister chromatids",
            ha="center", fontsize=10)
    ax.text(6, -0.02,
            "Blue / orange: parental homologues. Length: pair identity. No crossing over.\n"
            "Simplified symmetric divisions; human oogenesis produces one egg, with polar bodies.",
            ha="center", va="top", fontsize=10, color="#35434f")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
