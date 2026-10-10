"""Functional teaching diagram; not a historical apparatus reconstruction.

Tested with Python 3.14, matplotlib 3.10.7. Run from _media.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def box(ax, xy, width, height, text, color="#eef4fa", size=11):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.03",
                              facecolor=color, edgecolor="#34495e", linewidth=1.3))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=size, linespacing=1.4)


def arrow(ax, start, end, color="#34495e", style="-"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13,
                                linewidth=1.5, color=color, linestyle=style))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(10.8, 6.3), facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis("off")
    ax.text(6, 6.75, "Compress the sample; distinguish what each channel reads",
            ha="center", fontsize=16, weight="bold")
    ax.text(6, 6.36, "Functional schematic • not to scale • no measured data",
            ha="center", color="#555555", fontsize=11)
    box(ax, (0.35, 4.85), 2.5, 0.85, "Helium-4 drive\npressure")
    arrow(ax, (2.9, 5.28), (3.35, 5.28))
    box(ax, (3.4, 4.85), 2.4, 0.85, "Coupled bellows\nand piston")
    arrow(ax, (4.6, 4.82), (4.6, 4.22))
    ax.text(3.1, 4.45, "volume decreases", ha="center", fontsize=10)
    box(ax, (3.1, 2.2), 2.95, 1.95, "Helium-3 sample\nliquid + growing solid\n\nfreezing absorbs heat",
        color="#e9f3ed", size=11)
    ax.add_patch(Rectangle((3.3, 2.4), 0.35, 0.3, facecolor="#7597b9", edgecolor="none"))
    ax.add_patch(Rectangle((3.7, 2.4), 0.35, 0.3, facecolor="#7597b9", edgecolor="none"))
    box(ax, (0.35, 2.65), 2.05, 1.0, "Dilution refrigerator\nprecooling", size=10)
    arrow(ax, (2.45, 3.15), (3.05, 3.15), style="--")
    arrow(ax, (4.6, 2.15), (4.6, 1.62))
    box(ax, (3.1, 0.55), 2.95, 1.0, "Capacitance strain gauge\npressure vs time", color="#fff1dc", size=11)
    ax.text(0.4, 1.4, "Pressure marks an anomaly;\nit does not identify its phase.",
            fontsize=10, color="#7b4c16", va="center")
    ax.plot([6.6, 6.6], [0.45, 5.85], color="#cccccc", linewidth=1)
    ax.text(9.3, 5.7, "Separate NMR configurations", ha="center", fontsize=13, weight="bold")
    box(ax, (7.15, 4.05), 4.25, 1.1, "Initial: platinum NMR thermometer\nreadout: indicated temperature", size=11)
    ax.text(9.3, 3.65, "replaced by", ha="center", fontsize=11)
    arrow(ax, (9.3, 3.45), (9.3, 3.05))
    box(ax, (7.15, 1.65), 4.25, 1.35,
        "Follow-up: sample NMR coil\nfield gradient selects sample layers\nreadout: solid and liquid signals", color="#eeeafb", size=11)
    ax.text(9.3, 0.9, "Remove gradient to resolve\nfrequency shifts directly.",
            ha="center", va="center", fontsize=11)
    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.02, top=0.98)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
