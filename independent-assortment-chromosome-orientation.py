"""Draw two relative homolog orientations, with no crossing over.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The two modes identify whole-pole reversal; each has probability one half.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

COLORS = {"A": "#2468a2", "B": "#2468a2", "a": "#d26722", "b": "#d26722"}


def chromosome(ax, x, y, allele, replicated):
    length = 0.72 if allele.upper() == "A" else 0.48
    if replicated:
        for sign in (-1, 1):
            ax.plot([x - sign * 0.13, x + sign * 0.13],
                    [y - length / 2, y + length / 2], color=COLORS[allele],
                    lw=4, solid_capstyle="round")
    else:
        ax.plot([x, x], [y - length / 2, y + length / 2],
                color=COLORS[allele], lw=4, solid_capstyle="round")
    ax.text(x, y + length / 2 + 0.09, allele, ha="center", fontsize=12)


def main():
    fig, ax = plt.subplots(figsize=(11.5, 6.1), dpi=120)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 7.8))
    ax.axis("off")
    ax.text(6, 7.63, "Independent assortment across different meioses",
            ha="center", va="top", fontsize=18, weight="bold")
    ax.text(6, 7.05,
            "AaBb: A/a and B/b on different chromosome pairs; no crossing over",
            ha="center", fontsize=12)
    ax.text(2, 6.54, "Relative orientation in meiosis I",
            ha="center", fontsize=12, weight="bold")
    ax.text(8.25, 6.54, "Four products after meiosis II",
            ha="center", fontsize=12, weight="bold")
    for y, left_b, right_b, products in [
            (4.86, "B", "b", ("AB", "AB", "ab", "ab")),
            (2.16, "b", "B", ("Ab", "Ab", "aB", "aB"))]:
        ax.add_patch(Ellipse((2, y), 3.1, 1.95, edgecolor="#96a2ad",
                             facecolor="white", lw=1.5))
        ax.plot([2, 2], [y - 0.88, y + 0.88], ls="--", lw=1, color="#96a2ad")
        for xx, alleles in [(1.2, ("A", left_b)), (2.8, ("a", right_b))]:
            chromosome(ax, xx, y + 0.37, alleles[0], True)
            chromosome(ax, xx, y - 0.42, alleles[1], True)
        ax.text(0.15, y, "½", ha="center", fontsize=18, weight="bold")
        ax.annotate("", xy=(4.93, y), xytext=(3.7, y),
                    arrowprops=dict(arrowstyle="->", color="#53616c", lw=1.8))
        for x, product in zip((5.7, 7.35, 9.0, 10.65), products):
            ax.add_patch(Ellipse((x, y), 1.25, 1.45, edgecolor="#96a2ad",
                                 facecolor="white", lw=1.5))
            chromosome(ax, x - 0.21, y, product[0], False)
            chromosome(ax, x + 0.21, y, product[1], False)
            ax.text(x, y - 1.0, product, ha="center", fontsize=13, weight="bold")
    ax.text(6, 0.57, "Across divisions:  P(AB) = P(Ab) = P(aB) = P(ab) = ¼",
            ha="center", fontsize=13, weight="bold")
    ax.text(6, 0.06,
            "Fix A at the left pole: reversing both poles gives the same product set.\n"
            "Colors identify parental origin. Symmetric division model; not four functional eggs.",
            ha="center", va="top", fontsize=10, color="#35434f")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
