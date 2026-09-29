"""Exact count laws for five draws from four red and six blue objects.

Run from the desired output directory; writes the matching opaque PNG to CWD.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(11.6, 5.8), dpi=100, facecolor="white")
    grid = fig.add_gridspec(1, 2, width_ratios=(0.8, 1.35),
                           left=0.055, right=0.975, bottom=0.13, top=0.83,
                           wspace=0.3)
    population = fig.add_subplot(grid[0, 0])
    chart = fig.add_subplot(grid[0, 1])
    red, blue = "#b83237", "#337ca8"
    for index in range(10):
        x, y = index % 5, 1 - index // 5
        population.add_patch(Circle((x, y), 0.28,
                                   facecolor=red if index < 4 else blue,
                                   edgecolor="white", linewidth=1.5))
        population.text(x, y, str(index + 1), ha="center", va="center",
                        color="white", weight="bold", fontsize=11)
    population.set(xlim=(-0.5, 4.5), ylim=(-2.5, 1.65), aspect="equal")
    population.axis("off")
    population.set_title("The finite population", fontsize=14, pad=15)
    population.text(2, -0.65, "4 red + 6 blue\nChoose 5 draws", ha="center",
                    va="top", linespacing=1.5)
    population.text(2, -1.55,
                    "Without replacement:\nred first → next red chance 3/9\n"
                    "blue first → next red chance 4/9",
                    ha="center", va="top", fontsize=11, linespacing=1.4)
    k = np.arange(6)
    hg = np.array([comb(4, int(j)) * comb(6, 5 - int(j)) / comb(10, 5)
                   if j <= 4 else 0 for j in k])
    bn = np.array([comb(5, int(j)) * 0.4**j * 0.6**(5-j) for j in k])
    chart.bar(k - 0.18, hg, width=0.36, color="#247c68",
              label="Without replacement: hypergeometric")
    chart.bar(k + 0.18, bn, width=0.36, color="#e2a449",
              label="With replacement: binomial")
    chart.set(xlabel="Number of red draws K", ylabel="Probability",
              xticks=k, ylim=(0, 0.59))
    chart.grid(axis="y", alpha=0.18)
    chart.set_axisbelow(True)
    chart.legend(loc="upper right", frameon=False, fontsize=10)
    chart.text(0.98, 0.78, "Both means = 2\nVariances: 2/3 vs 6/5",
               transform=chart.transAxes, ha="right", va="top", fontsize=11)
    chart.annotate("5 red impossible\nwithout replacement",
                   xy=(5 - 0.18, 0), xytext=(4.15, 0.28),
                   arrowprops={"arrowstyle": "->", "color": "#444"},
                   ha="center", fontsize=10)
    fig.suptitle("Replacement changes the spread, even when the mean stays the same",
                 fontsize=16, y=0.965)
    fig.text(0.52, 0.035,
             "Exact probabilities from counting; no simulation or normal approximation.",
             ha="center", fontsize=11, color="#444")
    fig.savefig(Path.cwd() / "hypergeometric-versus-binomial.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
