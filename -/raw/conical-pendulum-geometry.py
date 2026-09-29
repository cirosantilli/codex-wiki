"""Generate an original ideal conical-pendulum schematic, not measured data.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
The matching PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import numpy as np


def arrow(ax, start, end, color, dashed=False):
    ax.annotate("", xy=end, xytext=start, arrowprops={
        "arrowstyle": "-|>", "color": color, "lw": 2.2,
        "linestyle": "--" if dashed else "-", "mutation_scale": 16,
    })


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    blue, orange, green, gray = "#235d9f", "#c65b16", "#167146", "#747b82"
    theta = np.deg2rad(40)
    radius, drop = np.sin(theta), np.cos(theta)
    fig, axes = plt.subplots(1, 3, figsize=(11.6, 4.8))
    fig.subplots_adjust(left=0.035, right=0.98, bottom=0.20, top=0.80, wspace=0.32)
    fig.suptitle("Conical pendulum: geometry and forces", fontsize=18, y=0.97)
    fig.text(0.5, 0.885, r"Illustrative ideal geometry: $\theta=40^\circ$; no measured data", ha="center")
    for ax in axes:
        ax.set_aspect("equal")
        ax.axis("off")

    ax = axes[0]
    ax.set_title("Side view", fontsize=14, pad=12)
    ax.set_xlim(-0.78, 0.88)
    ax.set_ylim(-0.31, 1.08)
    ax.plot([-0.17, 0.17], [drop, drop], color="black", lw=4)
    ax.plot([0, 0], [0, drop], "--", color=gray, lw=1.4)
    ax.plot([-radius, radius], [0, 0], color=gray, lw=1.6)
    ax.plot([0, -radius], [drop, 0], "--", color=gray, lw=1.2)
    ax.plot([0, radius], [drop, 0], color=blue, lw=2.5)
    ax.add_patch(Circle((radius, 0), 0.035, color=blue, zorder=5))
    ax.add_patch(Arc((0, drop), 0.38, 0.38, theta1=270, theta2=310, color="black"))
    ax.text(0.085, drop - 0.24, r"$\theta$", ha="center")
    ax.text(0.43, 0.44, r"$\ell$", color=blue, fontsize=15)
    ax.text(0.0, drop + 0.085, "fixed pivot", ha="center", fontsize=11)
    ax.annotate("", xy=(-0.20, drop), xytext=(-0.20, 0), arrowprops={"arrowstyle": "<->", "color": gray})
    ax.text(-0.26, drop / 2, r"$h$", ha="right", va="center", fontsize=15)
    ax.annotate("", xy=(radius, -0.15), xytext=(0, -0.15), arrowprops={"arrowstyle": "<->", "color": gray})
    ax.text(radius / 2, -0.24, r"$r$", ha="center", fontsize=15)
    ax.text(-0.06, -0.08, "centre", ha="right", fontsize=10)

    ax = axes[1]
    ax.set_title("Top view", fontsize=14, pad=12)
    ax.set_xlim(-0.85, 1.0)
    ax.set_ylim(-0.9, 0.9)
    ax.add_patch(Circle((0, 0), radius, fill=False, color=blue, lw=2))
    ax.plot(0, 0, "o", color="black", ms=4)
    ax.add_patch(Circle((radius, 0), 0.035, color=blue, zorder=5))
    arrow(ax, (radius, 0), (radius, 0.53), blue)
    ax.text(radius + 0.09, 0.38, r"$v$", color=blue, fontsize=15)
    arrow(ax, (radius, 0), (0.10, 0), green)
    ax.text(0.36, -0.17, r"$a=\omega^2r$", color=green, ha="center", fontsize=11)
    q = radius / np.sqrt(2)
    ax.plot([0, -q], [0, q], "--", color=gray)
    ax.text(-q / 2 - 0.08, q / 2, r"$r$", fontsize=15)
    ax.text(0, -0.79, "One full turn takes period P", ha="center", fontsize=11)

    ax = axes[2]
    ax.set_title("Forces on the bob", fontsize=14, pad=12)
    ax.set_xlim(-1.4, 0.57)
    ax.set_ylim(-1.3, 1.35)
    tx = -np.tan(theta)
    arrow(ax, (0, 0), (tx, 1), blue)
    arrow(ax, (0, 0), (0, -1), orange)
    arrow(ax, (0, 0), (tx, 0), green, dashed=True)
    ax.plot([tx, 0, 0], [1, 1, 0], ":", color=gray, lw=1.5)
    ax.plot(0, 0, "o", color="black", ms=5)
    ax.text(tx - 0.04, 1.11, r"$T$", color=blue, fontsize=15)
    ax.text(0.1, -0.75, r"$mg$", color=orange, fontsize=15)
    ax.text(0.09, 0.54, r"$T\cos\theta$" + "\n" + r"$=mg$", va="center", fontsize=11)
    ax.text(-0.63, -0.27, "net inward force\n" + r"$T\sin\theta=m\omega^2r$", color=green, ha="center", va="top", fontsize=11)
    ax.add_patch(Arc((0, 0), 0.6, 0.6, theta1=90, theta2=130, color=gray))
    ax.text(-0.17, 0.34, r"$\theta$", fontsize=12)
    fig.text(0.5, 0.10, r"$r=\ell\sin\theta$     $h=\ell\cos\theta$     Solid force arrows: tension and weight; dashed: their resultant", ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
