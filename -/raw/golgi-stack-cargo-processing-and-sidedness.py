"""Draw a Golgi stack and its membrane-sided processing geometry.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media; the opaque
PNG is written to the current directory. Shapes and toy chains are original.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


MEMBRANE = "#237fa1"
LUMEN = "#e5f5fa"
CYTOSOL = "#fff5df"
CARGO = "#78449a"
PROTEIN = "#c46b16"
INK = "#243744"


def label(ax, x, y, text, size=12, **kwargs):
    ax.text(x, y, text, color=INK, fontsize=size, va="center", **kwargs)


def arrow(ax, start, end, color=INK, **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                               mutation_scale=15, color=color, lw=1.7, **kwargs))


def main():
    fig, ax = plt.subplots(figsize=(14, 8.2), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 14), ylim=(0, 8.2), aspect="equal")
    ax.axis("off")
    label(ax, 7, 7.85, "Golgi polarity, cargo processing and membrane sides", 21,
          ha="center", fontweight="bold")
    label(ax, 4.0, 7.30, "Stack: enclosed sacs separated by cytosol", 14, ha="center")
    ax.add_patch(FancyBboxPatch((1.0, 2.7), 6.3, 4.2, boxstyle="round,pad=0.1",
                              fc=CYTOSOL, ec="none"))
    for i, y in enumerate([6.05, 5.10, 4.15, 3.20]):
        x = 1.45 + 0.12 * i
        ax.add_patch(FancyBboxPatch((x, y), 5.0, 0.53,
                                  boxstyle="round,pad=0.04,rounding_size=0.23",
                                  fc=LUMEN, ec=MEMBRANE, lw=2.4))
        for cx in [2.30, 3.15, 4.15]:
            ax.add_patch(Circle((cx, y + 0.26), 0.085, fc=CARGO, ec="none"))
        # A stipulated protein: cytosolic tail above; carbohydrate below.
        ax.plot([5.30, 5.30], [y + 0.33, y + 0.78], color=PROTEIN, lw=4,
                solid_capstyle="round")
        ax.plot([5.30, 5.55], [y + 0.34, y + 0.16], color=PROTEIN, lw=2)
        ax.add_patch(Circle((5.55, y + 0.16), 0.06, fc=PROTEIN, ec="none"))
    label(ax, 1.1, 6.78, "cis: entry from ER", 12)
    label(ax, 6.72, 4.91, "medial", 11, rotation=90, ha="center")
    arrow(ax, (0.62, 6.35), (0.62, 3.3))
    label(ax, 0.25, 4.9, "functional order", 11, rotation=90, ha="center")
    label(ax, 1.65, 2.72, "trans: exit / trans-Golgi network", 12)
    arrow(ax, (3.9, 2.46), (2.0, 1.92))
    arrow(ax, (4.0, 2.46), (5.85, 1.92))
    label(ax, 1.9, 1.57, "cell surface or\nsecretory granules", 12, ha="center")
    label(ax, 5.95, 1.57, "lysosome\nroute", 12, ha="center")
    # Enlargement: only a local patch, so it does not prescribe a carrier.
    ax.plot([7.65, 7.65], [1.35, 7.40], color="#d7dee1", lw=1)
    label(ax, 10.7, 7.25, "Local membrane enlargement", 14, ha="center")
    ax.add_patch(FancyBboxPatch((8.25, 3.30), 5.15, 3.2, boxstyle="round,pad=0.04",
                              fc=LUMEN, ec="none"))
    ax.add_patch(FancyBboxPatch((8.25, 1.95), 5.15, 1.3, boxstyle="round,pad=0.04",
                              fc=CYTOSOL, ec="none"))
    ax.plot([8.25, 13.40], [3.26, 3.26], color=MEMBRANE, lw=8)
    label(ax, 8.55, 6.18, "Golgi lumen", 14, fontweight="bold")
    label(ax, 8.55, 2.27, "cytosol", 14, fontweight="bold")
    ax.plot([11.5, 11.5], [2.75, 4.60], color=PROTEIN, lw=6,
            solid_capstyle="round")
    ax.plot([11.5, 11.82, 12.15], [4.6, 4.96, 5.23], color=PROTEIN, lw=2.5)
    for x, y in [(11.82, 4.96), (12.15, 5.23)]:
        ax.add_patch(Circle((x, y), 0.12, fc=PROTEIN, ec="white", lw=1))
    label(ax, 12.25, 5.75, "lumen-facing\ncarbohydrate", 11, ha="center")
    label(ax, 12.3, 2.72, "cytosolic tail", 11, ha="center")
    ax.add_patch(Circle((9.45, 4.9), 0.30, fc="#3b9b67", ec="white"))
    label(ax, 9.45, 5.46, "enzyme", 12, ha="center")
    arrow(ax, (9.88, 4.9), (11.48, 4.96), color="#3b9b67")
    label(ax, 9.55, 3.73, "accessible from lumen", 11, ha="center")
    label(ax, 10.7, 1.27, "Toy processing:  X–A  →  X  →  X–B", 13, ha="center")
    ax.text(7, 0.45, "Original schematic • sizes, numbers and arrows are illustrative • no measured trajectory",
            color=INK, fontsize=11, ha="center", va="center")
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
