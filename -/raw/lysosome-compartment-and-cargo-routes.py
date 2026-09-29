"""Draw an original lysosome route schematic; write the PNG to the current directory.

Tested with Python 3.14 and matplotlib 3.10.7. Geometry is illustrative.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch


INK = "#25384a"
BLUE = "#2875a8"
GREEN = "#227e68"
PURPLE = "#8053a0"


def box(ax, x, y, width, height, text, color, face):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
                              boxstyle="round,pad=0.12,rounding_size=0.15",
                              linewidth=1.6, edgecolor=color, facecolor=face))
    ax.text(x + width / 2, y + height / 2, text,
            ha="center", va="center", fontsize=12, color=INK, linespacing=1.5)


def arrow(ax, start, end, color=INK, rad=0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=16, linewidth=1.8, color=color,
                                connectionstyle=f"arc3,rad={rad}"))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(12, 7.6), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.04, top=0.91)
    ax.set(xlim=(0, 13), ylim=(0, 8.8), aspect="equal")
    ax.axis("off")
    fig.suptitle("Lysosome: cargo delivery, digestion and reuse", fontsize=19,
                 color=INK, y=0.975)

    box(ax, 0.25, 6.25, 2.1, 1.0, "Outside material\nendocytosis", BLUE, "#eff7fc")
    box(ax, 3.35, 6.25, 2.05, 1.0, "Endosome\nsorting", BLUE, "#eff7fc")
    arrow(ax, (2.55, 6.75), (3.15, 6.75), BLUE)
    arrow(ax, (4.4, 7.45), (4.4, 8.05), BLUE)
    ax.text(4.4, 8.25, "Return to cell membrane", ha="center", fontsize=11, color=BLUE)
    arrow(ax, (5.6, 6.75), (8.0, 5.65), BLUE)

    box(ax, 0.25, 3.65, 2.1, 1.1, "Own cytoplasm\nmacroautophagy", GREEN, "#eff9f5")
    box(ax, 3.35, 3.65, 2.05, 1.1, "Autophagosome\nenclosed cargo", GREEN, "#eff9f5")
    arrow(ax, (2.55, 4.2), (3.15, 4.2), GREEN)
    arrow(ax, (5.6, 4.2), (7.5, 4.2), GREEN)

    box(ax, 0.25, 1.1, 2.1, 1.05, "ER → Golgi\nnew enzymes", PURPLE, "#f7f0fa")
    box(ax, 3.35, 1.1, 2.05, 1.05, "Enzyme supply\nvia endosomes", PURPLE, "#f7f0fa")
    arrow(ax, (2.55, 1.62), (3.15, 1.62), PURPLE)
    arrow(ax, (5.6, 1.62), (8.1, 2.9), PURPLE)

    ax.add_patch(Ellipse((9.8, 4.55), 4.15, 3.8,
                         facecolor="#fff6e9", edgecolor="#b27028", linewidth=4))
    ax.text(9.8, 5.45, "Lysosome", ha="center", fontsize=18, weight="bold", color=INK)
    ax.text(9.8, 4.85, "Acidic lumen", ha="center", fontsize=14, color="#94531a")
    for x, y in ((8.8, 4.05), (9.65, 3.9), (10.55, 4.1)):
        ax.plot(x, y, marker="*", markersize=16, color=PURPLE)
    ax.text(9.8, 3.3, "Acid hydrolases", ha="center", color=PURPLE)
    ax.text(10.2, 7.8, "ATP-driven H⁺ entry", ha="center", color="#94531a")
    arrow(ax, (10.2, 7.4), (10.2, 6.05), "#94531a")
    ax.text(12.3, 4.6, "Cytosol", ha="center", rotation=90, color=INK)
    arrow(ax, (10.15, 2.6), (10.15, 1.65), "#b27028")
    ax.text(10.15, 1.1, "Small digestion products\nexported for reuse",
            ha="center", va="center", color=INK, linespacing=1.5)
    ax.text(6.5, 0.12, "Schematic routes; no physical scale, timing or measured cargo counts",
            ha="center", fontsize=10, color="#53616c")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
