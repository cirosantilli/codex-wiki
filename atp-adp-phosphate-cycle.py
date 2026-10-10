"""Draw ATP/ADP component bookkeeping, not molecular structures.

Tested with Python 3.14.4 and the repository's Matplotlib/NumPy environment.
Write an opaque white same-basename PNG to cwd, as required by Makefile.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


BLUE = "#19678d"
ORANGE = "#ad5516"
INK = "#24333d"


def components(ax, x, y, count, label):
    """Boxes and circles count components; lines do not depict actual bonds."""
    ax.add_patch(FancyBboxPatch(
        (x, y - 0.27), 1.72, 0.54, boxstyle="round,pad=0.05",
        facecolor="#edf5f8", edgecolor=BLUE, linewidth=1.6,
    ))
    ax.text(x + 0.86, y, "Adenine + ribose", ha="center", va="center",
            fontsize=11, color=INK)
    ax.text(x + 0.86, y - 0.53, "adenosine", ha="center", color=BLUE,
            fontsize=11)
    previous = x + 1.77
    for i in range(count):
        center = x + 2.15 + 0.68 * i
        ax.plot([previous, center - 0.25], [y, y], color=INK, lw=1.5)
        ax.add_patch(Circle((center, y), 0.25, facecolor="#fff0df",
                            edgecolor=ORANGE, lw=1.6))
        ax.text(center, y, "P", ha="center", va="center", fontsize=12,
                color=ORANGE, weight="bold")
        ax.text(center, y - 0.53, ["α", "β", "γ"][i], ha="center",
                fontsize=12, color=ORANGE)
        previous = center + 0.25
    ax.text(x + 1.76, y + 0.63, label, ha="center", fontsize=15,
            color=BLUE, weight="bold")


def main():
    fig, ax = plt.subplots(figsize=(8.0, 5.3))
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 9.3), ylim=(0, 6.1), aspect="equal")
    ax.axis("off")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.95, bottom=0.05)
    ax.text(4.65, 5.85, "ATP ⇄ ADP: a reusable material carrier",
            ha="center", fontsize=15, weight="bold", color=INK)
    components(ax, 0.25, 3.22, 3, "ATP: 3 phosphate groups")
    components(ax, 5.03, 3.22, 2, "ADP: 2 phosphate groups")
    ax.text(8.35, 3.22, "+", ha="center", va="center", fontsize=19,
            color=INK)
    ax.add_patch(Circle((8.91, 3.22), 0.25, facecolor="#fff0df",
                        edgecolor=ORANGE, lw=1.6))
    ax.text(8.91, 3.22, "Pᵢ", ha="center", va="center", fontsize=12,
            color=ORANGE)
    ax.text(8.91, 2.69, "free", ha="center", fontsize=10, color=ORANGE)
    ax.add_patch(FancyArrowPatch(
        (2.16, 4.24), (7.05, 4.24), connectionstyle="arc3,rad=-0.08",
        arrowstyle="-|>", mutation_scale=18, color=BLUE, linewidth=2,
    ))
    ax.text(4.65, 4.95, "Hydrolysis consumes H₂O", ha="center",
            fontsize=12, color=BLUE)
    ax.text(4.65, 4.58, "Net free-energy decrease under stated conditions",
            ha="center", fontsize=10.5, color=BLUE)
    ax.add_patch(FancyArrowPatch(
        (7.05, 2.26), (2.16, 2.26), connectionstyle="arc3,rad=-0.12",
        arrowstyle="-|>", mutation_scale=18, color=ORANGE, linewidth=2,
    ))
    ax.text(4.65, 1.68, "Regeneration needs energy input", ha="center",
            fontsize=12, color=ORANGE)
    ax.text(4.65, 1.31, "The reverse net reaction forms H₂O", ha="center",
            fontsize=10.5, color=ORANGE)
    ax.text(4.65, 0.62, "Phosphate count: 3 = 2 + 1", ha="center",
            fontsize=12, color=INK)
    ax.text(4.65, 0.19, "Component schematic: connecting oxygens, charges, and shapes omitted",
            ha="center", fontsize=9.5, color="#53616a")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Phosphate bookkeeping: ATP 3 = ADP 2 + inorganic phosphate 1")


if __name__ == "__main__":
    main()
