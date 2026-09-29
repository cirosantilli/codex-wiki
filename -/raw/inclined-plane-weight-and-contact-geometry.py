"""Original incline geometry; tested with Python 3.14 and matplotlib 3.10.7.

Run from _media; writes the matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Polygon
import numpy as np


def arrow(ax, start, delta, color, label, offset):
    end = start + delta
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color,
                            "lw": 2.5, "mutation_scale": 18})
    ax.text(*(end + offset), label, color=color, fontsize=14,
            ha="center", va="center")


def main():
    theta = np.deg2rad(30)
    up = np.array([np.cos(theta), np.sin(theta)])
    normal = np.array([-np.sin(theta), np.cos(theta)])
    down = -up
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), dpi=120)
    fig.set_facecolor("white")
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.set_xlim(-2.0, 2.0)
        ax.set_ylim(-1.9, 1.9)
        ax.axis("off")

    ax = axes[0]
    anchor = np.array([0., -0.2])
    ax.plot(*np.array([anchor - 1.7 * up, anchor + 1.7 * up]).T,
            color="#667085", lw=4)
    center = anchor + 0.25 * normal
    corners = [center + x * up + y * normal
               for x, y in [(-0.42, -0.25), (0.42, -0.25),
                            (0.42, 0.25), (-0.42, 0.25)]]
    ax.add_patch(Polygon(corners, facecolor="#edf2f7", edgecolor="#667085"))
    arrow(ax, center, np.array([0., -1.25]), "#222222", r"$mg$",
          np.array([0.24, -0.02]))
    arrow(ax, center, 1.25 * np.cos(theta) * normal, "#087f8c", r"$N$",
          np.array([-0.18, 0.08]))
    arrow(ax, center, 0.3 * 1.25 * np.cos(theta) * up, "#bd3d54", r"$f_k$",
          np.array([0.23, 0.04]))
    base = anchor - 1.7 * up
    ax.plot([base[0], base[0]+1], [base[1], base[1]], color="#98a2b3", lw=1)
    ax.add_patch(Arc(base, 1.05, 1.05, theta1=0, theta2=30,
                     color="#667085", lw=1.2))
    ax.text(base[0]+0.65, base[1]+0.13, r"$\theta$", fontsize=14)
    ax.set_title("Actual forces: downhill sliding", fontsize=14, pad=14)
    ax.text(0, -1.72, "Three interactions on the block", fontsize=12,
            ha="center", color="#475467")

    ax = axes[1]
    start = np.array([0.4, 0.9])
    weight = np.array([0., -1.8])
    parallel = 1.8 * np.sin(theta) * down
    inward = -1.8 * np.cos(theta) * normal
    arrow(ax, start, parallel, "#d57919", r"$mg\sin\theta$",
          np.array([-0.35, 0.20]))
    arrow(ax, start + parallel, inward, "#3274b5", r"$mg\cos\theta$",
          np.array([0.54, -0.24]))
    ax.annotate("", xy=start + weight, xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": "#222222",
                            "lw": 2, "linestyle": "--", "mutation_scale": 18})
    ax.text(0.65, 0.0, r"$mg$", fontsize=14)
    ax.plot(*np.array([start, start - 0.63 * normal]).T,
            color="#3274b5", ls=":", lw=1.5)
    ax.add_patch(Arc(start, 0.78, 0.78, theta1=270, theta2=300,
                     color="#667085", lw=1.2))
    ax.text(0.58, 0.40, r"$\theta$", fontsize=14)
    ax.set_title("Weight resolved into two components", fontsize=14, pad=14)
    ax.text(0, -1.72, "The two components sum to the weight", fontsize=12,
            ha="center", color="#475467")
    fig.suptitle("Inclined plane: contact and gravity geometry", fontsize=17, y=0.98)
    fig.subplots_adjust(left=0.03, right=0.98, bottom=0.06, top=0.85, wspace=0.14)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
