"""Original spherical lunar-phase geometry. Run from the desired PNG directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Earth is at (0, 0); sunlight arrives from +x. Eclipses are excluded.
Observed disks have north up and sky-right = (sin(theta), -cos(theta), 0).
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np


def observed_disk(theta, resolution=301):
    """Binary direct-sunlight mask from visible sphere normals, not flux."""
    q = np.linspace(-1, 1, resolution)
    u, v = np.meshgrid(q, q)
    inside = u * u + v * v <= 1
    z = np.sqrt(np.maximum(0, 1 - u * u - v * v))
    # n = u*sky_right + v*north + z*toward_Earth; s = (+1, 0, 0).
    lit = u * np.sin(theta) - z * np.cos(theta) > 1e-12
    rgba = np.ones((*u.shape, 4))
    rgba[inside, :3] = (0.24, 0.28, 0.34)
    rgba[inside & lit, :3] = (1.0, 0.84, 0.40)
    return rgba


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 6.2), facecolor="white")
    grid = fig.add_gridspec(2, 2, width_ratios=[1.04, 1.25],
                            left=0.035, right=0.99, bottom=0.16,
                            top=0.84, wspace=0.10)
    ax = fig.add_subplot(grid[:, 0])
    ax.set_aspect("equal")
    ax.set_xlim(-2.8, 3.1)
    ax.set_ylim(-2.75, 2.75)
    ax.axis("off")
    ax.set_title("Orbit seen from above north", pad=12)
    ax.add_patch(Circle((0, 0), 2, fill=False, color="#96a3b2", lw=1.5))
    for theta in np.arange(8) * np.pi / 4:
        x, y = 2 * np.cos(theta), 2 * np.sin(theta)
        ax.plot([0, x], [0, y], color="#c4cbd3", lw=0.8, zorder=0)
        ax.add_patch(Circle((x, y), 0.20, facecolor="#3d4757", edgecolor="none"))
        ax.add_patch(Wedge((x, y), 0.20, -90, 90, facecolor="#ffd66a"))
        ax.add_patch(Circle((x, y), 0.20, fill=False, edgecolor="#263345", lw=0.7))
        number = int(round(theta / (np.pi / 4))) + 1
        ax.text(2.46 * np.cos(theta), 2.46 * np.sin(theta), str(number),
                ha="center", va="center", weight="bold", color="#263345")
    ax.add_patch(Circle((0, 0), 0.30, facecolor="#3575ab", edgecolor="#234761"))
    ax.text(0, -0.51, "Earth\n(0, 0)", ha="center", va="top", fontsize=10)
    arc = np.linspace(np.deg2rad(12), np.deg2rad(35), 40)
    ax.plot(1.65 * np.cos(arc), 1.65 * np.sin(arc), color="#285b85", lw=1.8)
    ax.annotate("", xy=(1.65*np.cos(arc[-1]), 1.65*np.sin(arc[-1])),
                xytext=(1.65*np.cos(arc[-4]), 1.65*np.sin(arc[-4])),
                arrowprops={"arrowstyle": "->", "color": "#285b85", "lw": 1.8})
    for y in [-0.75, 0.75]:
        ax.annotate("", xy=(2.40, y), xytext=(3.03, y),
                    arrowprops={"arrowstyle": "->", "color": "#a46f08", "lw": 1.4})
    ax.text(2.7, 1.10, "Sun at +x\n(off panel)", ha="center", fontsize=10)
    ax.text(-1.9, -2.68, "Every orbital globe is lit on its +x half.", fontsize=10)

    disks = grid[:, 1].subgridspec(2, 4, wspace=0.12, hspace=0.46)
    labels = ["New", "Waxing\ncrescent", "First\nquarter", "Waxing\ngibbous",
              "Full", "Waning\ngibbous", "Last\nquarter", "Waning\ncrescent"]
    for i, label in enumerate(labels):
        dax = fig.add_subplot(disks[i // 4, i % 4])
        theta = i * np.pi / 4
        dax.imshow(observed_disk(theta), extent=(-1, 1, -1, 1), origin="lower")
        dax.add_patch(Circle((0, 0), 1, fill=False, edgecolor="#263345", lw=0.8))
        dax.set_aspect("equal")
        dax.axis("off")
        dax.set_title(f"{i+1}. {label}", fontsize=10, pad=8)
        k = (1 - np.cos(theta)) / 2
        dax.text(0, -1.22, f"k = {k:.3f}", ha="center", fontsize=10)
    fig.suptitle("Lunar phases: one illuminated hemisphere, eight views", fontsize=16, y=0.97)
    fig.text(0.73, 0.88, "Apparent disks from Earth • north up", ha="center", fontsize=11)
    fig.text(0.5, 0.075,
             "Positions 1–8 proceed counterclockwise. Waxing is bright on sky-right in this convention.\n"
             "Spherical, distant-Sun model • no eclipses • sizes and distances not to scale • k is disk area fraction",
             ha="center", va="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
