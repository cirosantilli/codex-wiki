"""Plot y'=x-y, constant-slope loci, and exact initial-value solutions.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5:
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../isoclines-linear-direction-field.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8, 6.6), layout="constrained", facecolor="white")
    x = np.linspace(-0.5, 3.25, 900)
    xx, yy = np.meshgrid(np.linspace(-0.4, 3.2, 19), np.linspace(-1.6, 4.1, 24))
    slope = xx - yy
    half_dx = 0.085 / np.sqrt(1 + slope**2)
    half_dy = slope * half_dx
    start = np.stack((xx - half_dx, yy - half_dy), axis=-1)
    end = np.stack((xx + half_dx, yy + half_dy), axis=-1)
    segments = np.stack((start, end), axis=-2).reshape(-1, 2, 2)
    ax.add_collection(LineCollection(segments, colors="#a9b1ba", linewidths=1.1))

    for k in [-1, 0, 1, 2]:
        ax.plot(x, x - k, "--", color="#555b63", linewidth=1.4, zorder=2)
        label_x = {-1: 2.96, 0: 3.0, 1: 3.0, 2: 3.0}[k]
        ax.text(label_x, label_x - k + 0.12, f"k = {k}", fontsize=11,
                ha="right", color="#454b53", bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})

    colors = ["#1b7e52", "#235eab", "#a645a2", "#d65b16"]
    for y0, color in zip([-1, 0, 1, 2], colors):
        a = y0 + 1
        trajectory = x - 1 + a * np.exp(-x)
        ax.plot(x, trajectory, color=color, linewidth=2.3, zorder=3,
                label=rf"$y(0)={y0}$" + (" (also k = 1)" if a == 0 else ""))
        ax.scatter([0], [y0], s=35, color=color, edgecolors="white", zorder=5)
        if a > 0:
            turning_x = np.log(a)
            ax.scatter([turning_x], [turning_x], marker="s", s=42,
                       facecolors="white", edgecolors=color, linewidths=1.6, zorder=5)

    ax.annotate("Nullcline y = x\nfield slope = 0; line slope = 1", xy=(1.9, 1.9),
                xytext=(0.42, 3.6), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#454b53"},
                bbox={"facecolor": "white", "edgecolor": "#d0d3d7", "pad": 5})
    ax.set(xlim=(-0.5, 3.25), ylim=(-1.75, 4.25), xlabel="x", ylabel="y",
           title=r"Isoclines and solution graphs for $y'=x-y$")
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="#d1d5db", linewidth=0.8, zorder=0)
    ax.axvline(0, color="#d1d5db", linewidth=0.8, zorder=0)
    handles, labels = ax.get_legend_handles_labels()
    handles += [Line2D([], [], color="#555b63", linestyle="--", label="Isoclines: x − y = k"),
                Line2D([], [], color="#555b63", marker="s", markerfacecolor="white", linestyle="none", label="Horizontal tangent")]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(1.02, 1),
              fontsize=10.5, frameon=False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
