"""Original string modes and numerical tracer graph; write the PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The graph represents the supplied numerical matrix, not the source sketch.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    figure = plt.figure(figsize=(11.5, 5.6), layout="constrained", facecolor="white")
    grid = figure.add_gridspec(3, 2, width_ratios=(1.15, 1), hspace=0.13)
    samples = np.arange(5)
    smooth = np.linspace(0, 4, 501)
    colors = ("#3266a8", "#16836f", "#b86325")
    names = ("Highest frequency: k = 3", "Middle frequency: k = 2", "Fundamental: k = 1")
    for row, (mode, color, name) in enumerate(zip((3, 2, 1), colors, names)):
        axis = figure.add_subplot(grid[row, 0])
        values = np.sin(mode * np.pi * samples / 4) / np.sqrt(2)
        values[[0, -1]] = 0
        values[np.abs(values) < 1e-14] = 0
        axis.axhline(0, color="0.65", lw=0.9)
        axis.plot(smooth, np.sin(mode * np.pi * smooth / 4) / np.sqrt(2), color=color, lw=1.4, alpha=0.7)
        axis.plot(samples, values, "o", color=color, markersize=6)
        axis.plot((0, 4), (0, 0), "s", color="black", markersize=5)
        axis.set(xlim=(-0.08, 4.08), ylim=(-0.93, 0.93), xticks=samples, yticks=(-0.7, 0, 0.7), ylabel="Displacement")
        axis.set_title(name, fontsize=12, loc="left", pad=5)
        axis.grid(axis="x", alpha=0.16)
        axis.spines[["top", "right"]].set_visible(False)
        if row == 2:
            axis.set_xlabel("Position x (fixed ends at 0 and 4)")
        else:
            axis.tick_params(labelbottom=False)

    axis = figure.add_subplot(grid[:, 1])
    axis.set_aspect("equal")
    axis.set(xlim=(-0.6, 3.6), ylim=(-0.9, 3.8))
    axis.axis("off")
    axis.set_title("Numerical four-box transport", fontsize=13, pad=7)
    positions = {1: (0.2, 2.7), 2: (2.8, 2.7), 3: (2.8, 0.5), 4: (0.2, 0.5)}
    for index, (x, y) in positions.items():
        axis.add_patch(FancyBboxPatch((x - 0.48, y - 0.37), 0.96, 0.74, boxstyle="round,pad=0.02", facecolor="#edf3f8", edgecolor="#34495e", lw=1.5))
        axis.text(x, y, f"Box {index}\n$c_{index}$", ha="center", va="center", fontsize=12)

    def arrow(start, end, rate, label_position, bend=0):
        axis.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16, lw=1.8, color="#34495e", connectionstyle=f"arc3,rad={bend}"))
        axis.text(*label_position, str(rate), ha="center", va="center", fontsize=12, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})

    arrow((0.72, 2.83), (2.28, 2.83), 2, (1.5, 3.12), bend=-0.12)
    arrow((2.28, 2.57), (0.72, 2.57), 1, (1.5, 2.28), bend=-0.12)
    arrow((2.8, 2.3), (2.8, 0.91), 1, (3.05, 1.6))
    arrow((2.28, 0.63), (0.72, 0.63), 2, (1.5, 0.91), bend=-0.12)
    arrow((0.72, 0.37), (2.28, 0.37), 1, (1.5, 0.08), bend=-0.12)
    arrow((0.2, 0.91), (0.2, 2.3), 1, (-0.07, 1.6))
    axis.text(1.5, 1.6, "$c_1=c_2=c_3=c_4$\nis stationary", ha="center", va="center", fontsize=11, color="#234c3e")
    axis.text(1.5, -0.49, "Arrow j → i is labelled by Aᵢⱼ\nColumn sums zero: total inventory conserved", ha="center", va="center", fontsize=10)
    figure.suptitle("Fixed-string mode shapes and a closed tracer system", fontsize=15)
    figure.savefig(Path.cwd() / "paper-3-q5-string-modes-and-four-box-transport.png", dpi=120, facecolor="white", transparent=False)
    plt.close(figure)


if __name__ == "__main__":
    main()
