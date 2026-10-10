"""Original apparatus and reasoning diagram for Rappaport's 1961 experiment.

Python 3.14; matplotlib 3.10.7 and numpy 2.3.5. Geometry is illustrative,
not a tracing of the paper's figures or a record of measured dimensions.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle
import numpy as np


BLUE = "#265b79"
GREEN = "#287b43"
ORANGE = "#c65b13"
PURPLE = "#7154a5"


def aster(ax, x, y, size=0.20):
    for angle in np.linspace(0, 2 * np.pi, 9, endpoint=False):
        ax.plot((x, x + size * np.cos(angle)), (y, y + size * np.sin(angle)), color=GREEN, lw=1)
    ax.add_patch(Circle((x, y), 0.045, fc=GREEN, ec=GREEN))


def spindle(ax, first, second):
    ax.plot((first[0], second[0]), (first[1], second[1]), color=GREEN, lw=2.6)
    aster(ax, *first)
    aster(ax, *second)


def main():
    fig = plt.figure(figsize=(11, 6.8), dpi=100, facecolor="white")
    fig.suptitle("Where can a furrow form?", y=0.965, fontsize=17)
    axes = [fig.add_axes((x, 0.33, 0.28, 0.46)) for x in (0.045, 0.36, 0.675)]
    for ax in axes:
        ax.set(xlim=(-1.7, 1.7), ylim=(-1.65, 1.9), aspect="equal")
        ax.axis("off")

    ax = axes[0]
    ax.set_title("Manipulation", fontsize=13)
    ax.add_patch(Rectangle((-1.50, -0.62), 3, 0.17, fc="#dce4e8", ec=BLUE, lw=1.2))
    ax.add_patch(Ellipse((0, -0.10), 2.20, 0.75, fc="#eef6fa", ec=BLUE, lw=2))
    ax.plot((0, 0), (0.1, 1.8), color="#69747c", lw=3)
    ax.add_patch(Circle((0, -0.02), 0.43, fc="#c9d2d9", ec="#69747c", lw=1.5))
    ax.annotate("Sphere\non needle", (0.33, 0.1), (0.6, 0.86), ha="center", fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#69747c"})
    ax.annotate("", (-0.47, 0.15), (-0.47, 1.18), arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 2})
    ax.text(0, -0.92, "Floor", ha="center", fontsize=11)
    ax.add_patch(Polygon([(-0.35, -1.55), (0.35, -1.55), (0.22, -1.20), (-0.22, -1.20)], fc="#dce4e8", ec=BLUE))
    ax.text(0.48, -1.40, "Objective\nbelow", ha="left", va="center", fontsize=10)

    ax = axes[1]
    ax.set_title("First division", fontsize=13)
    ax.add_patch(Circle((0, 0), 1.30, fc="#eef6fa", ec=BLUE, lw=2))
    ax.add_patch(Circle((0, 0), 0.70, fc="#c9d2d9", ec="#69747c", lw=1.3))
    spindle(ax, (-0.48, 0.91), (0.48, 0.91))
    ax.annotate("", (0, 0.80), (0, 1.56), arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 2})
    ax.text(0, -1.62, "Torus → horseshoe", ha="center", fontsize=11)

    ax = axes[2]
    ax.set_title("Later division", fontsize=13)
    angles = np.linspace(0.65 * np.pi, 2.35 * np.pi, 241)
    outer = np.column_stack((1.30 * np.cos(angles), 1.30 * np.sin(angles)))
    inner = np.column_stack((0.70 * np.cos(angles[::-1]), 0.70 * np.sin(angles[::-1])))
    ax.add_patch(Polygon(np.vstack((outer, inner)), fc="#eef6fa", ec=BLUE, lw=2))
    for sign in (-1, 1):
        spindle(ax, (sign * 1.00, 0.56), (sign * 0.78, -0.66))
        ax.add_patch(Circle((sign * 0.97, -0.04), 0.12, fc="#e8ddf6", ec=PURPLE))
    ax.plot((0, 0), (-1.31, -0.70), color=ORANGE, lw=4)
    ax.annotate("Extra furrow", (0, -0.95), (0, -1.60), ha="center", fontsize=11, color=ORANGE,
                arrowprops={"arrowstyle": "->", "color": ORANGE})
    ax.text(0, 1.70, "End daughters omitted", ha="center", fontsize=10)

    fig.text(0.5, 0.255, "Control timing", ha="center", fontsize=12)
    fig.text(0.5, 0.165, "Different spindles → extra furrow\nNo intervening chromosomes", ha="center", fontsize=13,
             bbox={"boxstyle": "round,pad=0.55", "facecolor": "#eef6fa", "edgecolor": BLUE})
    fig.text(0.5, 0.055, "Original apparatus and logic schematic; rays symbolic; not to scale.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
