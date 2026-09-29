"""Original functional schematic, not a tracing or a scale drawing.

Guillaume, Invar and elinvar (1920), printed p. 448, describes the
microscopes, water-bath rods and alternative reference arrangements.
Run from the desired output directory; only matplotlib is required.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=110, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6))
    ax.axis("off")
    ax.text(5, 5.75, "Measure the rod difference; calibrate the reference", ha="center", fontsize=16)
    for x, name in [(2.2, "Microscope 1"), (7.8, "Microscope 2")]:
        ax.add_patch(Rectangle((x - .35, 3.55), .7, .8, facecolor="#dce3eb", edgecolor="#24344a"))
        ax.add_patch(Rectangle((x - .65, 2.7), 1.3, .35, facecolor="#d1cdc5", edgecolor="#6b655d"))
        ax.plot([x + .3, x + .3], [3.05, 3.55], color="#6b655d", lw=3)
        ax.plot([x, x], [1.8, 3.55], color="#777777", ls="--")
        ax.text(x, 4.55, name, ha="center", fontsize=12)
    ax.annotate("Baseline can drift: do not assume fixed microscope spacing", xy=(5, 4.05),
                xytext=(5, 5.12), ha="center", fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#495367"})
    ax.add_patch(FancyArrowPatch((2.2, 4.1), (7.8, 4.1), arrowstyle="<->", mutation_scale=13, color="#495367"))
    ax.add_patch(Rectangle((1.15, .8), 7.7, 1.65, facecolor="#e9f4fb", edgecolor="#4e8ba5", lw=2))
    ax.text(5, .4, "Relative method: test and reference rods share a water bath", ha="center", fontsize=12)
    for y, color, label in [(1.95, "#b44c30", "Test rod"), (1.2, "#2f698b", "Calibrated reference rod")]:
        ax.plot([1.65, 8.35], [y, y], color=color, lw=9, solid_capstyle="butt")
        for x in [2.2, 7.8]:
            ax.plot([x, x], [y - .18, y + .18], color="#1c2229", lw=2)
        ax.text(5, y + .2, label, ha="center", fontsize=11, color=color)
    ax.text(5, .03, "Move each rod into the sight lines; compare its two marks. Functional reconstruction, not to scale.",
            ha="center", fontsize=10)
    fig.tight_layout(pad=1.2)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
