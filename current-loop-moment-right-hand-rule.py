"""Draw current circulation and the oriented loop moment.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.5), facecolor="white")
    blue, orange = "#1965a6", "#a84c16"
    for ax, sense in zip(axes, (1, -1), strict=True):
        ax.set_aspect("equal")
        ax.set_xlim(-1.65, 1.65)
        ax.set_ylim(-1.55, 1.55)
        ax.axis("off")
        ax.add_patch(Circle((0, 0), 1, facecolor="#edf5fb", edgecolor=blue, lw=2.5))
        for start in np.deg2rad([10, 130, 250]):
            angles = np.linspace(start, start + sense * 0.68, 40)
            x, y = np.cos(angles), np.sin(angles)
            ax.plot(x, y, color=blue, lw=3)
            ax.add_patch(FancyArrowPatch((x[-3], y[-3]), (x[-1], y[-1]),
                                        arrowstyle="-|>", mutation_scale=20,
                                        lw=2.2, color=blue))
        ax.text(1.12, 0.25, "$I$", color=blue, fontsize=17)
        ax.text(0, -0.64, "enclosed area $A$", ha="center", color="#31475a")
        ax.add_patch(Circle((0, 0.12), 0.20, fill=False, edgecolor=orange, lw=2))
        if sense == 1:
            ax.plot(0, 0.12, "o", ms=6, color=orange)
            label = "Counterclockwise current"
            thumb = "Thumb: moment out of the page"
        else:
            ax.plot([-0.10, 0.10], [0.02, 0.22], color=orange, lw=2)
            ax.plot([-0.10, 0.10], [0.22, 0.02], color=orange, lw=2)
            label = "Clockwise current"
            thumb = "Thumb: moment into the page"
        ax.text(0, 0.47, r"$\mathbf{m}=IA\,\widehat{\mathbf{n}}$", ha="center",
                color=orange, fontsize=15)
        ax.set_title(label, pad=12, fontsize=14, weight="bold")
        ax.text(0, -1.25, thumb, ha="center", color=orange, fontsize=11)
        ax.text(0, -1.48, "Right fingers curl along $I$", ha="center", fontsize=11)
    fig.suptitle("A current loop has an oriented magnetic moment", fontsize=16, weight="bold")
    fig.text(0.5, 0.015, r"Face-on views  •  Conventional current  •  Moment unit: $\mathrm{A\,m^2}$",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.05, right=0.95, top=0.83, bottom=0.10, wspace=0.20)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
