"""Draw filled endpoint bundles of equal etendue; output PNG to the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 7.0))
    colors = ["#2166ac", "#16846b"]
    diameters = [10.0, 20.0]
    direction_radii = [0.5, 0.25]
    angles = np.degrees(np.arcsin(direction_radii))
    for col, (diameter, p, color) in enumerate(
        zip(diameters, direction_radii, colors)
    ):
        ax = axes[0, col]
        ax.add_patch(Circle((0, 0), diameter / 2, facecolor=color, alpha=0.18))
        ax.add_patch(Circle((0, 0), diameter / 2, fill=False, edgecolor=color, lw=2))
        ax.plot([0, diameter / 2], [0, 0], color=color, lw=2)
        ax.set(xlim=(-12, 12), ylim=(-12, 12), xlabel="x (mm)", ylabel="y (mm)")
        ax.set_title(
            ("Entrance" if col == 0 else "Expanded output")
            + f": D = {diameter:g} mm\n"
            + (r"$A_1=25\pi\ \mathrm{mm}^2$" if col == 0
               else r"$A_2=100\pi\ \mathrm{mm}^2=4A_1$")
        )
        ax = axes[1, col]
        ax.add_patch(Circle((0, 0), p, facecolor=color, alpha=0.18))
        ax.add_patch(Circle((0, 0), p, fill=False, edgecolor=color, lw=2))
        ax.plot([0, p], [0, 0], color=color, lw=2)
        ax.set(xlim=(-0.65, 0.65), ylim=(-0.65, 0.65), xlabel=r"$p_x=n s_x$", ylabel=r"$p_y=n s_y$")
        ax.set_title(
            f"Direction disk: half-angle {angles[col]:.4g}°\n"
            + (r"$\pi\sin^2\theta_1=\pi/4$" if col == 0
               else r"$\pi\sin^2\theta_2=\pi/16$")
        )
    for ax in axes.flat:
        ax.set_aspect("equal")
        ax.axhline(0, color="#888888", lw=0.6, zorder=0)
        ax.axvline(0, color="#888888", lw=0.6, zorder=0)
        ax.grid(alpha=0.15)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Lossless area–angle exchange: filled bundles in n = 1", fontsize=15)
    fig.text(
        0.5, 0.025,
        r"$G=A\,\pi\sin^2\theta=25\pi^2/4=61.685\ \mathrm{mm}^2\,\mathrm{sr}$ at both ports"
        + "\nSpatial area × 4; direction-disk area ÷ 4. Endpoint schematic, not a lens prescription.",
        ha="center", va="bottom", fontsize=11,
    )
    fig.subplots_adjust(top=0.86, bottom=0.16, hspace=0.69, wspace=0.42)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
