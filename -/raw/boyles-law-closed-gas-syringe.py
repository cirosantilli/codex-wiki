"""Draw an original schematic of a sealed syringe and absolute sensor.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the PNG is written to the current directory.
This is an explanatory schematic, not a scale drawing of a product.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(11, 5.8), dpi=100)
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.90)
    ax.set(xlim=(0, 11), ylim=(0, 5.3), aspect="equal")
    ax.axis("off")
    fig.suptitle("Boyle's law: measure the whole sealed gas sample", fontsize=16, y=0.97)
    blue, ink, orange = "#d7edf7", "#284354", "#b45b16"

    # Sensor: the gas-facing cavity and reference vacuum share a membrane.
    ax.add_patch(Rectangle((0.55, 2.15), 1.75, 1.65, fc="white", ec=ink, lw=2))
    ax.add_patch(Rectangle((0.55, 2.15), 1.75, 0.88, fc=blue, ec="none"))
    ax.plot([0.55, 2.30], [3.03, 3.03], color=orange, lw=3)
    ax.text(1.425, 3.46, "Vacuum\nreference", ha="center", va="center", fontsize=11)
    ax.text(1.425, 2.58, "Gas cavity", ha="center", va="center", fontsize=11)
    ax.annotate("Sensing membrane", (1.7, 3.03), xytext=(0.55, 4.05),
                arrowprops={"arrowstyle": "->", "color": orange}, color=orange, fontsize=11)

    # A connecting passage belongs to the same sample as the graduated barrel.
    ax.add_patch(Rectangle((2.30, 2.4), 1.0, 0.35, fc=blue, ec=ink, lw=1.6))
    ax.add_patch(Rectangle((3.30, 2.05), 5.0, 1.15, fc="white", ec=ink, lw=2))
    ax.add_patch(Rectangle((3.30, 2.05), 3.4, 1.15, fc=blue, ec="none"))
    ax.plot([3.30, 6.70], [2.05, 2.05], color=ink, lw=2)
    ax.plot([3.30, 6.70], [3.20, 3.20], color=ink, lw=2)
    ax.add_patch(Rectangle((6.70, 2.05), 0.16, 1.15, fc=ink, ec=ink))
    ax.add_patch(Rectangle((6.86, 2.52), 2.5, 0.18, fc="#a3b1ba", ec=ink))
    ax.plot([9.36, 9.36], [2.1, 3.15], color=ink, lw=3)
    for x in [3.6, 4.0, 4.4, 4.8, 5.2, 5.6, 6.0, 6.4, 6.8, 7.2, 7.6, 8.0]:
        ax.plot([x, x], [3.20, 3.38], color=ink, lw=1)
    ax.text(5.10, 2.62, "Trapped gas\nbarrel reading Vread", ha="center", va="center")
    ax.text(5.6, 3.65, "Graduated syringe barrel", ha="center", fontsize=11)
    ax.add_patch(FancyArrowPatch((8.0, 3.8), (9.2, 3.8), arrowstyle="<->",
                                 mutation_scale=15, color=ink, lw=1.6))
    ax.text(8.6, 4.09, "Plunger changes Vread", ha="center", fontsize=11)
    ax.annotate("Seal: amount stays fixed", (6.78, 2.18), xytext=(7.05, 1.52),
                arrowprops={"arrowstyle": "->", "color": ink}, fontsize=11)

    # Readout has no invented measured value.
    ax.plot([0.6, 0.25, 0.25, 0.6], [3.55, 3.55, 4.65, 4.65], color=ink, lw=1.4)
    ax.add_patch(Rectangle((0.60, 4.37), 2.8, 0.55, fc="#f5f7f8", ec=ink, lw=1.4))
    ax.text(2.0, 4.64, "Readout: absolute p", ha="center", va="center", fontsize=11)
    ax.annotate("Unmarked gas volume Vd\n(sensor + connection)", (2.65, 2.58),
                xytext=(0.55, 1.45), arrowprops={"arrowstyle": "->", "color": ink}, fontsize=11)

    ax.add_patch(FancyArrowPatch((4.5, 1.62), (4.5, 2.02), arrowstyle="<->",
                                 mutation_scale=14, color=orange, lw=1.8))
    ax.text(5.25, 1.23, "Heat exchange with surroundings", ha="center", color=orange, fontsize=11)
    ax.text(5.5, 0.67, "Total gas volume V = Vread + Vd", ha="center", fontsize=14, color=ink)
    ax.text(5.5, 0.15, "Compare settled states at the same temperature; schematic, not to scale.",
            ha="center", fontsize=11, color="#444444")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
