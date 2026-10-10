"""Local punctures on a line, circle, and tripod; Python 3.14, matplotlib 3.10."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(2, 3, figsize=(10, 6.1), facecolor="white")
    gray, blue, orange, green = "#c2c9cd", "#176b9b", "#d7651d", "#38936b"
    for ax in axes.flat:
        ax.set_aspect("equal")
        ax.set_xlim(-1.4, 1.4)
        ax.set_ylim(-1.35, 1.45)
        ax.axis("off")
    for col, title in enumerate(["Real line", "Circle", "Tripod junction"]):
        axes[0, col].set_title(title, fontsize=14)
    # Top row: the highlighted connected neighborhood sits inside the full space.
    ax = axes[0, 0]
    ax.plot([-1.3, 1.3], [0, 0], color=gray, lw=3)
    ax.plot([-0.65, 0.65], [0, 0], color=blue, lw=6)
    ax.scatter([-0.65, 0.65], [0, 0], s=55, facecolors="white", edgecolors=blue, zorder=4)
    ax.scatter([0], [0], s=45, color="black", zorder=5)
    ax.text(0.1, 0.16, "$p$")
    th = np.linspace(0, 2 * np.pi, 600)
    arc = np.linspace(np.pi / 2 - 0.65, np.pi / 2 + 0.65, 150)
    ax = axes[0, 1]
    ax.plot(np.cos(th), np.sin(th), color=gray, lw=3)
    ax.plot(np.cos(arc), np.sin(arc), color=blue, lw=6)
    ax.scatter(np.cos(arc[[0, -1]]), np.sin(arc[[0, -1]]), s=55,
               facecolors="white", edgecolors=blue, zorder=4)
    ax.scatter([0], [1], s=45, color="black", zorder=5)
    ax.text(0.12, 1.1, "$p$")
    directions = np.array([[0, 1], [-np.sqrt(3) / 2, -0.5], [np.sqrt(3) / 2, -0.5]])
    ax = axes[0, 2]
    for direction in directions:
        ax.plot([0, direction[0]], [0, direction[1]], color=gray, lw=3)
        endpoint = 0.65 * direction
        ax.plot([0, endpoint[0]], [0, endpoint[1]], color=blue, lw=6)
        ax.scatter(*endpoint, s=55, facecolors="white", edgecolors=blue, zorder=4)
    ax.scatter([0], [0], s=45, color="black", zorder=5)
    ax.text(0.13, 0.1, "$o$")
    # Bottom row: only the chosen neighborhood, with the center removed.
    ax = axes[1, 0]
    for lo, hi, color in [(-0.65, 0, blue), (0, 0.65, orange)]:
        ax.plot([lo, hi], [0, 0], color=color, lw=6)
        ax.scatter([lo, hi], [0, 0], s=55, facecolors="white", edgecolors=color, zorder=4)
    ax.scatter([0], [0], s=85, facecolors="white", edgecolors="black", zorder=5)
    ax = axes[1, 1]
    for lo, hi, color in [(arc[0], np.pi / 2, orange), (np.pi / 2, arc[-1], blue)]:
        angles = np.linspace(lo, hi, 100)
        ax.plot(np.cos(angles), np.sin(angles), color=color, lw=6)
        ax.scatter(np.cos([lo, hi]), np.sin([lo, hi]), s=55,
                   facecolors="white", edgecolors=color, zorder=4)
    ax.scatter([0], [1], s=85, facecolors="white", edgecolors="black", zorder=5)
    ax = axes[1, 2]
    for direction, color in zip(directions, [green, blue, orange]):
        endpoint = 0.65 * direction
        ax.plot([0, endpoint[0]], [0, endpoint[1]], color=color, lw=6)
        ax.scatter(*endpoint, s=55, facecolors="white", edgecolors=color, zorder=4)
    ax.scatter([0], [0], s=85, facecolors="white", edgecolors="black", zorder=5)
    for col, count in enumerate([2, 2, 3]):
        axes[0, col].text(0, -1.28, "Small connected open neighborhood", ha="center", fontsize=10)
        axes[1, col].text(0, -1.02, f"Center removed: {count} components", ha="center", fontsize=12)
    fig.suptitle("A local test: count the pieces after a puncture", fontsize=17, y=0.98)
    fig.text(0.5, 0.048, "Hollow dots are excluded. Colors distinguish the components after removal.", ha="center", fontsize=11)
    fig.text(0.5, 0.017, "Removing p from the whole circle leaves it connected; the local arc above splits in two.", ha="center", fontsize=11)
    fig.subplots_adjust(top=0.86, bottom=0.12, left=0.04, right=0.98, hspace=0.08, wspace=0.19)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
