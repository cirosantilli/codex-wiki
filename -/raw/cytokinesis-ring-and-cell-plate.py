"""Original sectional cartoons of cytokinesis. Python 3.14; matplotlib 3.10.7, numpy 2.3.5."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle
import numpy as np


BOUNDARY = "#265b79"
CYTOPLASM = "#eef6fa"
NUCLEUS = "#7154a5"
RING = "#c65b13"
PLATE = "#287b43"


def nucleus(ax, x, y=0):
    ax.add_patch(Circle((x, y), 0.24, facecolor="#e8ddf6", edgecolor=NUCLEUS, lw=1.7))
    ax.text(x, y, r"$2n$" + "\n" + r"$2C$", ha="center", va="center", fontsize=11, color=NUCLEUS)


def frame(ax):
    ax.set(xlim=(-1.8, 1.8), ylim=(-1.05, 1.22), aspect="equal")
    ax.axis("off")


def animal(ax, stage):
    if stage == 0:
        ax.add_patch(Ellipse((0, 0), 2.65, 1.5, fc=CYTOPLASM, ec=BOUNDARY, lw=2))
        waist = 0.70
    elif stage == 1:
        angle = np.linspace(0, 2 * np.pi, 301)
        x = 1.35 * np.cos(angle)
        y = 0.75 * np.sin(angle) * (1 - 0.76 * np.exp(-(x / 0.48) ** 2))
        ax.add_patch(Polygon(np.column_stack((x, y)), closed=True, fc=CYTOPLASM, ec=BOUNDARY, lw=2))
        waist = 0.18
    else:
        for x in (-0.78, 0.78):
            ax.add_patch(Ellipse((x, 0), 1.22, 1.35, fc=CYTOPLASM, ec=BOUNDARY, lw=2))
        waist = None
    for x in (-0.78, 0.78):
        nucleus(ax, x)
    if waist is not None:
        for y in (-waist, waist):
            ax.plot((-0.13, 0.13), (y, y), color=RING, lw=6, solid_capstyle="round")
    if stage == 1:
        ax.annotate("Furrow", (0.03, waist), (0.48, 0.92), fontsize=11, color=RING,
                    arrowprops={"arrowstyle": "->", "color": RING}, ha="center")


def plant(ax, stage):
    ax.add_patch(Rectangle((-1.35, -0.75), 2.7, 1.5, fc=CYTOPLASM, ec=PLATE, lw=5))
    ax.add_patch(Rectangle((-1.29, -0.69), 2.58, 1.38, fill=False, ec=BOUNDARY, lw=1.3))
    for x in (-0.78, 0.78):
        nucleus(ax, x)
    if stage == 0:
        for y in (-0.22, 0, 0.22):
            ax.add_patch(Circle((0, y), 0.065, fc="#b3dabc", ec=PLATE, lw=1))
    else:
        length = 0.39 if stage == 1 else 0.73
        ax.plot((0, 0), (-length, length), color=PLATE, lw=5)
        if stage == 1:
            for sign in (-1, 1):
                ax.annotate("", (0, sign * 0.65), (0, sign * 0.44),
                            arrowprops={"arrowstyle": "->", "color": PLATE, "lw": 1.8})
        else:
            for x in (-0.045, 0.045):
                ax.plot((x, x), (-0.69, 0.69), color=BOUNDARY, lw=1)


def main():
    fig, axes = plt.subplots(2, 3, figsize=(10.8, 6.5), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.055, right=0.97, top=0.81, bottom=0.15, hspace=0.50, wspace=0.22)
    fig.suptitle("Cytokinesis changes the boundary around two existing nuclei", y=0.97, fontsize=17)
    fig.text(0.5, 0.895, "Animal: inward furrow       •       Plant: outward cell plate", ha="center", fontsize=13)
    for stage in range(3):
        for row in range(2):
            frame(axes[row, stage])
        animal(axes[0, stage], stage)
        plant(axes[1, stage], stage)
        axes[0, stage].set_title(["Ring at the surface", "Furrow deepens", "Separate daughters"][stage], fontsize=12, pad=0)
        axes[1, stage].set_title(["Vesicles at the center", "Plate grows outward", "New wall and boundaries"][stage], fontsize=12, pad=0)
        fig.text([0.184, 0.511, 0.837][stage], 0.105,
                 ["1 cell, 2 nuclei", "1 cell, partition forming", "2 cells, 1 nucleus each"][stage],
                 ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Nuclear DNA total: 4C throughout. Orange: ring intersections. Green: plant partition.\nSectional cartoons; sizes and stage spacing are illustrative.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
