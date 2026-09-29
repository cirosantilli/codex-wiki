"""Unfolded confocal conjugate-plane ray schematic; not instrument-scale data.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes the matching basename PNG to the current working directory.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import numpy as np


BLUE = "#245ba3"
GREEN = "#187c52"
ORANGE = "#bd591d"


def pinhole(ax, x, gap=0.16):
    for lo, hi in [(-1.15, -gap), (gap, 1.15)]:
        ax.plot([x, x], [lo, hi], color="#35404c", lw=6, solid_capstyle="butt")


def lens(ax, x):
    ax.add_patch(Ellipse((x, 0), 0.16, 2.35, facecolor="#e6f0f7",
                         edgecolor="#608294", lw=1.5, zorder=4))


def ray(ax, points, color, style="-", lw=1.7):
    p = np.asarray(points)
    ax.plot(p[:, 0], p[:, 1], style, color=color, lw=lw)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 1, figsize=(10.8, 7.2))
    fig.subplots_adjust(left=0.055, right=0.98, top=0.86, bottom=0.18, hspace=0.45)
    for ax in axes:
        ax.set(xlim=(-0.7, 5.85), ylim=(-1.6, 1.6))
        ax.axis("off")
        ax.axhline(0, color="#a4abb2", lw=0.8, ls=":")
        lens(ax, 2)
    ax = axes[0]
    pinhole(ax, 0)
    ax.axvline(4, color="#949ca3", lw=1, ls="--")
    for h in [-1, 1]:
        ray(ax, [(0, 0), (2, h), (4, 0)], BLUE)
        ax.annotate("", xy=(3.25, h * 0.375), xytext=(2.7, h * 0.65),
                    arrowprops={"arrowstyle": "->", "color": BLUE})
    ax.scatter([0, 4], [0, 0], color=BLUE, s=28, zorder=7)
    ax.text(-0.5, 1.38, "A  Illumination: image the source onto the specimen", weight="bold")
    ax.text(0, -1.4, "Illumination\npinhole plane", ha="center", va="center")
    ax.text(2, -1.4, "Equivalent\nfocusing lens", ha="center", va="center")
    ax.text(4, -1.4, "Selected\nspecimen plane", ha="center", va="center")
    ax.text(4.35, 0.4, "Finite excitation spot\nin a real microscope", color=BLUE)
    ax = axes[1]
    ax.axvline(0, color="#949ca3", lw=1, ls="--")
    pinhole(ax, 4)
    ax.add_patch(Rectangle((5.18, -0.66), 0.42, 1.32, facecolor="#eef4ee",
                           edgecolor=GREEN, lw=1.5))
    for h in [-1, 1]:
        ray(ax, [(0, 0), (2, h), (4, 0), (5.18, -h * 0.59)], GREEN)
    # Ideal thin lens f=1: at object distance 2 the image distance is 2.
    # An axial point shifted toward the lens has s=1.45, s'=s/(s-1).
    obj_x = 0.55
    s = 2 - obj_x
    image_x = 2 + s / (s - 1)
    intercept = 1 - 2 / (image_x - 2)
    assert image_x > 4 and intercept > 0.16
    for h in [-1, 1]:
        ray(ax, [(obj_x, 0), (2, h), (4, h * intercept)], ORANGE, "--")
        ax.scatter([4], [h * intercept], marker="x", s=50, color=ORANGE, zorder=8)
    ray(ax, [(obj_x, 0), (5.18, 0)], ORANGE, ":", 2.5)
    ax.scatter([0], [0], s=32, color=GREEN, zorder=8)
    ax.scatter([obj_x], [0], s=32, color=ORANGE, zorder=8)
    ax.text(-0.5, 1.38, "B  Detection: image the specimen onto the receiving pinhole", weight="bold")
    ax.text(0, -1.4, "Selected\nspecimen plane", ha="center", va="center")
    ax.text(2, -1.4, "Equivalent\nimaging lens", ha="center", va="center")
    ax.text(4, -1.4, "Detection\npinhole plane", ha="center", va="center")
    ax.text(5.4, -1.4, "Detector", ha="center", va="center")
    ax.annotate("Displaced emitter", xy=(obj_x, 0.07), xytext=(0.65, 0.8), color=ORANGE,
                arrowprops={"arrowstyle": "->", "color": ORANGE}, fontsize=10)
    ax.text(4.23, 0.87, "Mask rejects\nthese rays", color=ORANGE, fontsize=10)
    fig.suptitle("Confocal selection uses corresponding positions in conjugate planes", fontsize=15)
    fig.text(0.5, 0.07,
             "Unfolded ray construction: shared objectives, beam splitters and scan relays are omitted.\n"
             "Green: selected point. Orange: displaced point, with some light still passing.\n"
             "Real diffraction spots are finite; the ideal ray intersections are not zero-width optical sections.",
             ha="center", fontsize=10)
    path = Path(__file__).stem + ".png"
    fig.savefig(path, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"path": path, "dimensions": [1188, 792],
                      "thin_lens_focal_length": 1, "selected_object_distance": 2,
                      "selected_image_distance": 2,
                      "displaced_image_position": image_x,
                      "displaced_ray_mask_height": intercept,
                      "pinhole_half_gap": 0.16, "data": "original schematic"}))


if __name__ == "__main__":
    main()
