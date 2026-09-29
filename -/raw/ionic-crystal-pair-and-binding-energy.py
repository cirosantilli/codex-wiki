"""Original ionic-binding schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; the PNG is written to the current working directory.
Geometry is a schematic rock-salt plane; the potential is a stipulated model,
not a fit, a diffraction measurement, or a physical lattice-energy dataset.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def reduced_energy(x):
    """U/E0 for the stipulated n=9 attraction-plus-repulsion model."""
    return (-9 / x + x**-9) / 8


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(11.6, 6.8), dpi=100, facecolor="white")
    ax = fig.add_axes((0.04, 0.12, 0.43, 0.75))
    ax.set(xlim=(-2.9, 2.9), ylim=(-3.3, 5.2), aspect="equal")
    ax.axis("off")
    blue, orange = "#276897", "#b45419"

    def ion(x, y, positive, radius=0.27):
        ax.add_patch(Circle((x, y), radius, facecolor=blue if positive else orange,
                            edgecolor="white", linewidth=1.5))
        ax.text(x, y, "+" if positive else "−", color="white", ha="center",
                va="center", fontsize=17, weight="bold")

    ax.text(0, 4.9, "An isolated pair", ha="center", weight="bold", fontsize=15)
    ion(-1, 4.1, True, 0.33)
    ion(1, 4.1, False, 0.33)
    ax.annotate("", (0.57, 4.1), (-0.57, 4.1),
                arrowprops={"arrowstyle": "<->", "color": "#444444"})
    ax.text(0, 3.65, "one partner in this two-body model", ha="center", fontsize=11)
    ax.text(0, 2.8, "A plane through a salt crystal", ha="center", weight="bold", fontsize=15)
    for i in range(-2, 3):
        for j in range(-2, 3):
            ion(i, j, (i + j) % 2 == 0)
    ax.add_patch(Circle((0, 0), 0.37, fill=False, edgecolor="#222222", linewidth=1.4))
    ax.text(0, -2.68, "Central +: four nearest − in this plane;", ha="center", fontsize=11)
    ax.text(0, -3.08, "two more lie above and below the plane.", ha="center", fontsize=11)

    energy = fig.add_axes((0.57, 0.23, 0.39, 0.61), facecolor="white")
    x = np.linspace(0.72, 2.7, 800)
    energy.plot(x, -9 / (8 * x), "--", color=blue, lw=2, label="attraction: −9/(8x)")
    energy.plot(x, x**-9 / 8, ":", color=orange, lw=2.5, label="repulsion: 1/(8x⁹)")
    energy.plot(x, reduced_energy(x), color="#222222", lw=2.5, label="sum")
    energy.axhline(0, color="#aaaaaa", lw=0.9)
    energy.plot(1, -1, "o", color="#222222", ms=6)
    energy.annotate("stable minimum\nx = 1, U/E₀ = −1", (1, -1), (1.5, -1.45),
                    arrowprops={"arrowstyle": "->", "color": "#444444"}, fontsize=11)
    energy.set(xlim=(0.7, 2.7), ylim=(-1.8, 2.4), xlabel="Scaled separation  x = r/r₀",
               ylabel="Scaled potential energy  U/E₀", title="Competing interactions set a spacing")
    energy.legend(loc="upper right", fontsize=10, frameon=False)
    fig.suptitle("Ionic binding: pair, extended structure, and finite spacing", y=0.965,
                 fontsize=18, weight="bold")
    fig.text(0.5, 0.07, "Original schematic and synthetic n = 9 model • no measured crystal or energy data",
             ha="center", fontsize=11, color="#444444")
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
