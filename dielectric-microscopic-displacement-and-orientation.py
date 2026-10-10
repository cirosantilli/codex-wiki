"""Generate an illustrative microscopic dielectric diagram (Python 3.14).

Requires the repository's matplotlib 3.10.7 and numpy 2.3.5 environment.
Run from _media; all geometry is schematic, not molecular simulation data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


NEGATIVE = "#2566a0"
POSITIVE = "#bc443c"
ARROW = "#325940"


def charge(ax, xy, sign, radius=0.075):
    color = POSITIVE if sign == "+" else NEGATIVE
    ax.add_patch(Circle(xy, radius, facecolor=color, edgecolor="white", zorder=4))
    ax.text(*xy, sign, color="white", ha="center", va="center", fontsize=11, zorder=5)


def dipole(ax, x, y, angle):
    direction = np.array([np.cos(angle), np.sin(angle)])
    midpoint = np.array([x, y])
    tail, head = midpoint - 0.23 * direction, midpoint + 0.23 * direction
    ax.add_patch(FancyArrowPatch(tail, head, arrowstyle="-|>", mutation_scale=12,
                                color=ARROW, linewidth=1.7, zorder=3))
    charge(ax, tail, "−", 0.065)
    charge(ax, head, "+", 0.065)


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(2, 2, figsize=(10, 6), dpi=110)
    fig.patch.set_facecolor("white")
    fig.suptitle("Displacement and orientation both produce polarization", fontsize=17, y=0.98)
    for ax in axes.flat:
        ax.set(xlim=(0, 4), ylim=(0, 2.35), aspect="equal")
        ax.axis("off")
        ax.set_facecolor("white")

    axes[0, 0].set_title("Charge centres coincide • zero field", fontsize=13)
    axes[0, 1].set_title("Charge centres separate • field applied", fontsize=13)
    for col, ax in enumerate(axes[0]):
        for x in (0.8, 2.0, 3.2):
            centre = x - 0.17 * col
            ax.add_patch(Circle((centre, 1.2), 0.40, facecolor="#dbeafa", edgecolor=NEGATIVE,
                                linewidth=1.5))
            ax.plot(centre, 1.2, "o", color=NEGATIVE, markersize=4, zorder=3)
            charge(ax, (x + 0.17 * col, 1.2), "+")
            if col:
                ax.add_patch(FancyArrowPatch((centre, 0.62), (x + 0.17, 0.62),
                                            arrowstyle="-|>", color=ARROW, mutation_scale=12))
        ax.text(2, 0.15, "Neutral units; positive and negative charge remain equal",
                ha="center", fontsize=10)
    axes[0, 0].text(2, 1.95, "Blue cloud: negative charge", color=NEGATIVE, ha="center", fontsize=11)
    axes[0, 1].annotate("E", xy=(3.6, 1.95), xytext=(2.8, 1.95), va="center",
                        arrowprops={"arrowstyle": "->", "color": ARROW}, color=ARROW)

    axes[1, 0].set_title("Existing dipoles • cancelling orientations", fontsize=13)
    axes[1, 1].set_title("Existing dipoles • biased orientations", fontsize=13)
    zero_angles = np.arange(8) * np.pi / 4
    biased_angles = np.deg2rad([-80, -45, -20, 10, 35, 65, 105, -60])
    for col, angles in enumerate((zero_angles, biased_angles)):
        ax = axes[1, col]
        for j, angle in enumerate(angles):
            dipole(ax, 0.55 + (j % 4) * 0.95, 1.65 - (j // 4) * 0.85, angle)
        ax.text(2, 0.14, r"$\langle\mathbf{p}\rangle=0$" if col == 0 else
                r"$\langle p_x\rangle>0$; alignment is incomplete", ha="center", fontsize=12)
    axes[1, 1].annotate("E", xy=(3.6, 2.2), xytext=(2.8, 2.2), va="center",
                        arrowprops={"arrowstyle": "->", "color": ARROW}, color=ARROW)
    fig.text(0.5, 0.02, "Schematic only • dipole arrows point from − to + • no charge flows between electrodes",
             ha="center", fontsize=11)
    fig.subplots_adjust(top=0.87, bottom=0.09, left=0.025, right=0.975, hspace=0.23, wspace=0.05)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
