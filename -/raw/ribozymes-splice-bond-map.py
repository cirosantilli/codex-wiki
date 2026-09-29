"""Original connectivity schematic of group I intron splicing.

Run from _media with Python 3.14, matplotlib 3.10.7 and MPLBACKEND=Agg.
No experimental data or atomic coordinates are represented.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


BLUE = "#175f92"
PURPLE = "#7550a1"
GREEN = "#237747"
ORANGE = "#c66b17"
INK = "#24333e"


def segment(ax, x, y, width, label, color):
    ax.add_patch(FancyBboxPatch(
        (x, y - 0.28), width, 0.56, boxstyle="round,pad=0.02",
        facecolor=color, edgecolor=color, linewidth=1.2,
    ))
    ax.text(x + width / 2, y, label, ha="center", va="center",
            color="white", fontsize=13)


def bond(ax, x1, x2, y, color):
    ax.plot([x1, x2], [y, y], color=color, lw=4, solid_capstyle="butt")


def arrow(ax, start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=17, lw=1.7, color=INK))


def guanosine(ax, x, y):
    ax.add_patch(Circle((x, y), 0.22, facecolor=GREEN, edgecolor=GREEN))
    ax.text(x, y, "G", ha="center", va="center", color="white", fontsize=13)


def main():
    fig, ax = plt.subplots(figsize=(10, 6.8), dpi=110, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 8.2))
    ax.axis("off")
    ax.text(5.5, 7.9, "Group I intron: two backbone-bond exchanges",
            ha="center", fontsize=18, weight="bold", color=INK)
    ax.text(5.5, 7.48, "Connectivity schematic • no atomic geometry or experimental data",
            ha="center", fontsize=11, color=INK)

    y = 6.55
    ax.text(0.3, y + 0.55, "1. Precursor + external guanosine", fontsize=13,
            color=INK, weight="bold")
    ax.text(1.45, y, "G–3′OH", color=GREEN, fontsize=14, ha="center")
    ax.text(2.6, y, "+", fontsize=18, ha="center", color=INK)
    segment(ax, 3.2, y, 1.6, "5′ exon", BLUE)
    segment(ax, 5.5, y, 2.0, "intron", PURPLE)
    segment(ax, 8.2, y, 1.6, "3′ exon", BLUE)
    bond(ax, 4.82, 5.48, y, ORANGE)
    bond(ax, 7.52, 8.18, y, ORANGE)
    ax.text(3.05, y, "5′", ha="right", va="center", fontsize=11, color=INK)
    ax.text(9.97, y, "3′", va="center", fontsize=11, color=INK)
    ax.text(5.15, y - 0.48, "first junction", ha="center", fontsize=10, color=ORANGE)
    ax.text(7.85, y - 0.48, "second junction", ha="center", fontsize=10, color=ORANGE)

    arrow(ax, (5.5, 5.65), (5.5, 5.08))
    ax.text(5.88, 5.4, "G–3′OH replaces the first junction bond",
            fontsize=11, va="center", color=INK)

    y = 4.25
    ax.text(0.3, y + 0.56, "2. Freed exon hydroxyl + G-linked intron", fontsize=13,
            color=INK, weight="bold")
    segment(ax, 1.15, y, 1.6, "5′ exon", BLUE)
    ax.text(2.95, y, "3′OH", va="center", fontsize=13, color=BLUE)
    ax.text(4.0, y, "+", fontsize=18, ha="center", color=INK)
    guanosine(ax, 5.05, y)
    segment(ax, 5.5, y, 2.0, "intron", PURPLE)
    bond(ax, 5.27, 5.48, y, GREEN)
    segment(ax, 8.2, y, 1.6, "3′ exon", BLUE)
    bond(ax, 7.52, 8.18, y, ORANGE)

    arrow(ax, (5.5, 3.55), (5.5, 2.98))
    ax.text(5.88, 3.26, "Exon 3′OH replaces the second junction bond",
            fontsize=11, va="center", color=INK)

    y = 2.25
    ax.text(0.3, y + 0.56, "3. Joined exons + linear excised intron", fontsize=13,
            color=INK, weight="bold")
    segment(ax, 1.15, y, 1.6, "5′ exon", BLUE)
    segment(ax, 3.25, y, 1.6, "3′ exon", BLUE)
    bond(ax, 2.77, 3.23, y, GREEN)
    ax.text(5.7, y, "+", fontsize=18, ha="center", color=INK)
    guanosine(ax, 6.6, y)
    segment(ax, 7.05, y, 2.0, "intron", PURPLE)
    bond(ax, 6.82, 7.03, y, GREEN)
    ax.text(9.24, y, "3′OH", va="center", fontsize=13, color=PURPLE)
    ax.text(3.0, y - 0.5, "new exon–exon bond", ha="center", color=GREEN, fontsize=11)
    ax.text(8.0, y - 0.5, "external G stays attached", ha="center", color=GREEN, fontsize=11)

    ax.plot([0.3, 10.7], [1.21, 1.21], color="#d4dbe0", lw=1)
    bond(ax, 0.55, 1.05, 0.85, ORANGE)
    ax.text(1.22, 0.85, "original junction bonds", va="center", fontsize=11, color=INK)
    bond(ax, 6.0, 6.5, 0.85, GREEN)
    ax.text(6.68, 0.85, "new backbone bonds", va="center", fontsize=11, color=INK)
    ax.text(5.5, 0.35, "Folded RNA active site and Mg²⁺ omitted; subsequent intron circularization omitted.",
            ha="center", fontsize=10.5, color=INK)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.99, bottom=0.02)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
