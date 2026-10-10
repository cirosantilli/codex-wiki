"""Original ideal mass-distribution diagrams; no measured data.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python3 ../rotational-inertia-energy-mass-distribution.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


NAVY = "#17324d"
TEAL = "#167d9a"
ORANGE = "#bd591c"


def axis_symbol(ax, xy=(0, 0)):
    ax.add_patch(Circle(xy, 0.065, facecolor="white", edgecolor=NAVY, lw=1.5, zorder=5))
    ax.plot(*xy, ".", color=NAVY, markersize=5, zorder=6)


def main():
    plt.rcParams.update({"font.size": 11, "text.color": NAVY, "mathtext.fontset": "dejavusans"})
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.8), facecolor="white")
    fig.subplots_adjust(left=0.05, right=0.95, bottom=0.13, top=0.86, hspace=0.65, wspace=0.18)
    fig.suptitle("Same mass, different radial placement", fontsize=18, y=0.975)
    fig.text(0.5, 0.925, "Ideal model diagrams · same total mass M and reference radius R", ha="center", fontsize=11)

    for ax in axes.flat:
        ax.set_aspect("equal")
        ax.set_xlim(-1.45, 1.45)
        ax.set_ylim(-1.14, 1.14)
        ax.axis("off")

    for ax, radius, color in zip(axes[0], [1 / 3, 1], [TEAL, ORANGE]):
        ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor="#abb7c2", linestyle="--", lw=1))
        for theta in np.arange(4) * np.pi / 2:
            x, y = radius * np.cos(theta), radius * np.sin(theta)
            ax.plot([0, x], [0, y], color="#8193a3", lw=2)
            ax.add_patch(Circle((x, y), 0.105, color=color, zorder=4))
        axis_symbol(ax)
        ax.text(0.15, 0.09, "axis", fontsize=9)
        ax.annotate(r"$m=M/4$", xy=(-radius, 0), xytext=(-1.35, 0.60), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": NAVY}, ha="left")
        ax.text(0.66, -0.25, r"$R$", color="#667787")
    axes[0, 0].set_title(r"Four point masses at $R/3$", fontsize=12, pad=12)
    axes[0, 1].set_title(r"Four point masses at $R$", fontsize=12, pad=12)
    axes[0, 0].text(0.5, -0.15, r"$I=MR^2/9$", transform=axes[0, 0].transAxes, ha="center", fontsize=14, color=TEAL)
    axes[0, 1].text(0.5, -0.15, r"$I=MR^2$", transform=axes[0, 1].transAxes, ha="center", fontsize=14, color=ORANGE)

    disk, ring = axes[1]
    disk.add_patch(Circle((0, 0), 1, facecolor="#d6eef3", edgecolor=TEAL, lw=2))
    ring.add_patch(Circle((0, 0), 1, fill=False, edgecolor=ORANGE, lw=7))
    for ax in [disk, ring]:
        axis_symbol(ax)
        ax.annotate("", xy=(0.7071, -0.7071), xytext=(0.045, -0.045),
                    arrowprops={"arrowstyle": "->", "color": NAVY, "lw": 1.3})
        ax.text(0.46, -0.33, r"$R$", fontsize=12)
    disk.set_title("Uniform disc", fontsize=12, pad=12)
    ring.set_title("Ideal thin ring", fontsize=12, pad=12)
    disk.text(0.5, -0.15, r"$I=MR^2/2$", transform=disk.transAxes, ha="center", fontsize=14, color=TEAL)
    ring.text(0.5, -0.15, r"$I=MR^2$", transform=ring.transAxes, ha="center", fontsize=14, color=ORANGE)

    fig.text(0.5, 0.035, r"Axes perpendicular to the page; at a shared angular speed, $K_{\rm rot}=\frac{1}{2}I\omega^2$.", ha="center", fontsize=11)
    fig.text(0.5, 0.008, "Spokes have negligible mass; marker sizes and ring stroke are drawing conventions.", ha="center", fontsize=9)
    output = Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
