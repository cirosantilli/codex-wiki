"""Contrast equal-intensity point laws; Python 3.14 / NumPy 2.3.5 / Matplotlib 3.10.7.

Run from _media; deterministic illustrative samples and exact probability masses.
"""

from math import exp, factorial
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    rng = np.random.default_rng(107)
    colors = ["#276c9b", "#c78515", "#964f9d"]
    fig = plt.figure(figsize=(10.2, 5.3), layout="constrained")
    grid = fig.add_gridspec(3, 2, width_ratios=[1, 1.25])
    fig.suptitle("Same mean density, different spacing and count laws", fontsize=16)
    samples = [
        np.arange(0.32, 8, 1),
        np.sort(rng.uniform(0, 8, rng.poisson(8))),
        np.sort(rng.uniform(0, 8, rng.poisson(16))),
    ]
    labels = ["Shifted lattice", "Unit-rate Poisson", "Shared-rate Cox: R = 2 shown"]
    for i, (points, label, color) in enumerate(zip(samples, labels, colors)):
        ax = fig.add_subplot(grid[i, 0])
        ax.axvspan(0, 1, color="#eeeeee")
        ax.hlines(0, 0, 8, color="#888888", linewidth=1)
        ax.scatter(points, np.zeros_like(points), color=color, s=32, zorder=3)
        ax.set_title(label, loc="left", color=color, fontsize=11)
        ax.set_xlim(-0.1, 8.1)
        ax.set_ylim(-0.6, 0.6)
        ax.set_yticks([])
        ax.spines[["top", "left", "right", "bottom"]].set_visible(False)
        ax.set_xticks([0, 1, 2, 4, 6, 8])
        if i == 0:
            ax.text(0.5, -0.3, "W", ha="center", fontsize=10)
        if i == 2:
            ax.set_xlabel("Position (one possible realization per row)", fontsize=10)
            ax.text(0, -0.53, "Cox also gives an empty realization with probability 1/2.", fontsize=9)

    ax = fig.add_subplot(grid[:, 1])
    k = np.arange(8)
    masses = [
        (k == 1).astype(float),
        np.array([exp(-1) / factorial(int(j)) for j in k]),
        np.array([0.5 * exp(-2) * 2 ** int(j) / factorial(int(j)) for j in k]),
    ]
    masses[2][0] += 0.5
    width = 0.24
    for i, (p, color, name, variance) in enumerate(zip(
        masses, colors, ["Lattice", "Poisson", "Shared-rate Cox"], [0, 1, 2],
    )):
        ax.bar(k + (i - 1) * width, p, width=width, color=color,
               label=f"{name}: variance {variance}")
    ax.set_title(r"Exact law of $N_W$, $W=[0,1)$")
    ax.set_ylabel("Probability")
    ax.set_xlabel("Count k")
    ax.set_xticks(k)
    ax.set_ylim(0, 1.22)
    ax.text(3, 1.08, r"All have $\mathbb{E}[N_W]=1$", ha="center", fontsize=13)
    ax.legend(loc="upper right", bbox_to_anchor=(1, 0.86), fontsize=10, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.18)
    ax.set_axisbelow(True)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
