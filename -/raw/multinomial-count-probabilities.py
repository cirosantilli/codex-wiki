"""All exact multinomial count patterns for n=4 and p=(0.5, 0.3, 0.2).

Writes the matching opaque PNG to CWD. Tested with Python 3.14,
NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from math import factorial
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    n, probabilities = 4, (0.5, 0.3, 0.2)
    counts = [(i, j, n-i-j) for i in range(n+1) for j in range(n+1-i)]
    masses = [
        factorial(n) / np.prod([factorial(v) for v in row])
        * np.prod([p**v for p, v in zip(probabilities, row)])
        for row in counts
    ]
    fig, ax = plt.subplots(figsize=(10.6, 6.8), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.85, bottom=0.17, top=0.8)
    for j in range(n+1):
        ax.plot([0, n-j], [j, j], color="#d8dfe4", linewidth=1, zorder=0)
    for i in range(n+1):
        ax.plot([i, i], [0, n-i], color="#d8dfe4", linewidth=1, zorder=0)
    ax.plot([0, n], [n, 0], "--", color="#7b8791", linewidth=1.2, zorder=0)
    scatter = ax.scatter([v[0] for v in counts], [v[1] for v in counts],
                         c=masses, s=1450, cmap="Blues", vmin=0, vmax=0.18,
                         edgecolors="#3b556a", linewidths=1, zorder=2)
    for (i, j, k), mass in zip(counts, masses):
        ax.text(i, j, f"{mass:.4f}", ha="center", va="center", fontsize=10,
                color="white" if mass >= 0.1 else "#17324b", zorder=3)
    ax.scatter([2], [1.2], s=180, marker="x", c="#b53637", linewidths=2, zorder=4)
    ax.annotate("Expected counts (2, 1.2, 0.8)\nNot an integer count pattern",
                xy=(2, 1.2), xytext=(2.6, 2.7), fontsize=11, ha="left",
                arrowprops={"arrowstyle": "->", "color": "#b53637"},
                color="#942e2f")
    ax.set(xlim=(-0.48, 4.55), ylim=(-0.43, 4.45), xticks=range(5),
           yticks=range(5), xlabel="First-category count N₁",
           ylabel="Second-category count N₂", aspect="equal")
    ax.text(3.45, 1.75, "N₃ = 0", rotation=-45,
            fontsize=10, color="#5b6670")
    cax = fig.add_axes([0.87, 0.23, 0.023, 0.46])
    fig.colorbar(scatter, cax=cax, label="Probability of this count pattern",
                 ticks=[0, 0.06, 0.12, 0.18])
    fig.suptitle("Multinomial counts share a fixed total", fontsize=17, y=0.965)
    fig.text(0.5, 0.895, "4 independent trials; category probabilities (0.5, 0.3, 0.2)",
             ha="center", fontsize=12)
    fig.text(0.5, 0.055,
             "Each point has N₃ = 4 − N₁ − N₂.  Labels give exact masses to 4 decimals.\n"
             "Independent trials yield dependent counts: increasing one leaves less total for the others.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.savefig(Path.cwd() / "multinomial-count-probabilities.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
