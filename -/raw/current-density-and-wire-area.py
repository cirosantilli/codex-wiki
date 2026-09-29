"""Two fixed-current cross sections and their densities; opaque PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    area_mm2 = np.array([1.0, 2.0])
    current_a = 2.0
    density = current_a / (area_mm2 * 1e-6)
    colors = ["#2268a5", "#bd5a22"]
    fig, (slices, bars) = plt.subplots(1, 2, figsize=(10.8, 5.2), dpi=100)

    # Square transverse slices share a spatial scale, so area is literal.
    centers = [2.65, 0.6]
    for area, center, color in zip(area_mm2, centers, colors):
        side = np.sqrt(area)
        slices.add_patch(Rectangle((-side / 2, center - side / 2), side, side,
                                   facecolor=color, alpha=0.18,
                                   edgecolor=color, linewidth=2))
        slices.plot(0, center, "o", color=color, markersize=9)
        slices.text(1.0, center + 0.12, rf"$A={area:g}\ \mathrm{{mm^2}}$",
                    va="center", color=color, fontsize=14)
        slices.text(1.0, center - 0.3, "$I=2$ A out of the page",
                    va="center", fontsize=11)
    slices.plot([-0.75, 0.25], [-0.65, -0.65], color="#303840", linewidth=2)
    slices.plot([-0.75, -0.75], [-0.71, -0.59], color="#303840")
    slices.plot([0.25, 0.25], [-0.71, -0.59], color="#303840")
    slices.text(-0.25, -0.88, "1 mm", ha="center", fontsize=11)
    slices.set(xlim=(-1.1, 3.7), ylim=(-1.1, 3.6), aspect="equal")
    slices.axis("off")
    slices.set_title("Transverse slices at the same scale", fontsize=13,
                     weight="bold", pad=12)

    bars.barh([1, 0], density, color=colors, height=0.5)
    bars.set_yticks([1, 0], [r"$A=1\ \mathrm{mm^2}$", r"$A=2\ \mathrm{mm^2}$"])
    for y, value, color in zip([1, 0], density, colors):
        bars.text(value + 0.06e6, y, rf"${value / 1e6:g}\times10^6$",
                  va="center", color=color, fontsize=14)
    bars.set(xlim=(0, 2.8e6), ylim=(-0.7, 1.7),
             xlabel=r"Current density $j=I/A$ (A/m$^2$)")
    bars.set_xticks([0, 1e6, 2e6], ["0", r"$1\times10^6$", r"$2\times10^6$"])
    bars.set_title("Twice the area gives half the density", fontsize=13,
                   weight="bold", pad=12)
    bars.grid(axis="x", alpha=0.2)
    bars.set_axisbelow(True)
    bars.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Same current, different local transport intensity", fontsize=16,
                 weight="bold", y=0.97)
    fig.text(0.5, 0.87, "Two separate cases: uniform normal flow, I = 2 A in each",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.16, top=0.73, wspace=0.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
