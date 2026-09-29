"""Original segment test drawings; write matching opaque PNG in cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.3), dpi=120, facecolor="white")
    disk, circle = axes
    disk.add_patch(Circle((0, 0), 1, fc="#d5eaf1", ec="#287a9d", lw=2))
    endpoints = np.array([[-0.8, 0.25], [0.8, -0.25]])
    disk.plot(*endpoints.T, "o-", color="#b85831", lw=2.5)
    disk.plot(0, 0, "o", color="#3f8e72", ms=8)
    disk.text(0, -0.64, "All points on the chord\nbelong to the disk", ha="center", fontsize=11)
    disk.set_title("Closed unit disk: convex")
    circle.add_patch(Circle((0, 0), 1, fc="none", ec="#287a9d", lw=2))
    circle.plot([-1, 1], [0, 0], "--", color="#b85831", lw=2)
    circle.plot([-1, 1], [0, 0], "o", color="#287a9d", ms=7)
    circle.plot(0, 0, "x", color="#b85831", ms=11, mew=2)
    circle.annotate("Midpoint (0,0) is missing", xy=(0, 0), xytext=(0, -0.52),
                    ha="center", arrowprops={"arrowstyle": "->", "color": "#b85831"}, fontsize=11)
    circle.set_title("Unit circle: not convex")
    for ax in axes:
        ax.axhline(0, color="#999999", lw=0.5, zorder=0)
        ax.axvline(0, color="#999999", lw=0.5, zorder=0)
        ax.set(xlim=(-1.35, 1.35), ylim=(-1.25, 1.25), xlabel="x", ylabel="y", xticks=[-1, 0, 1], yticks=[-1, 0, 1])
        ax.set_aspect("equal")
    fig.suptitle("Convexity requires the entire straight segment", fontsize=15)
    fig.subplots_adjust(left=0.075, right=0.97, bottom=0.15, top=0.82, wspace=0.3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
