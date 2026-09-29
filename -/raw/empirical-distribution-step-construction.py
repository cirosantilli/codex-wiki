"""Explain empirical counting and ties; tested with Python 3.14 / Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    sample = np.array([1, 1, 2, 4, 6])
    values, counts = np.unique(sample, return_counts=True)
    cumulative = np.cumsum(counts)
    heights = cumulative / sample.size
    edges = np.r_[0, values, 7]
    blue, orange = "#1767a1", "#c36b13"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False})
    fig, (rug, ax) = plt.subplots(
        2, 1, figsize=(9, 5.9), sharex=True,
        gridspec_kw={"height_ratios": [1, 3.5], "hspace": 0.15},
        layout="constrained", facecolor="white",
    )
    fig.suptitle("From five observations to four jumps", fontsize=17)
    rug.scatter(sample, [0.35, 0.70, 0.35, 0.35, 0.35], s=90, color=orange)
    rug.text(1.2, 0.70, "two observations at 1", va="center", color=orange)
    rug.text(4.7, 0.72, "sample: [1, 1, 2, 4, 6]", va="center")
    rug.set_ylim(0, 1)
    rug.set_yticks([])
    rug.set_ylabel("Observed\nvalues", rotation=0, ha="right", va="center")
    rug.spines[["left", "right", "bottom"]].set_visible(False)
    rug.tick_params(axis="x", bottom=False)
    levels = np.r_[0, heights]
    for left, right, height in zip(edges[:-1], edges[1:], levels):
        ax.hlines(height, left, right, color=blue, lw=2.7)
    previous = np.r_[0, heights[:-1]]
    ax.vlines(values, previous, heights, color=blue, alpha=0.45, linestyle=":")
    ax.scatter(values, previous, s=65, facecolor="white", edgecolor=blue, zorder=4)
    ax.scatter(values, heights, s=65, color=blue, zorder=5)
    ax.annotate("tie: one jump of 2/5", xy=(1, 0.2), xytext=(2.2, 0.12),
                arrowprops={"arrowstyle": "->", "color": orange}, color=orange)
    ax.annotate(r"$F_5(3)=3/5$", xy=(3, 0.6), xytext=(3.15, 0.40),
                arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    ax.scatter([3], [0.6], marker="x", s=60, color=blue, zorder=6)
    ax.text(0.03, 0.96, "filled = value at the jump\nopen = excluded height",
            transform=ax.transAxes, va="top", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 6})
    ax.set_xlim(0, 7)
    ax.set_ylim(-0.045, 1.08)
    ax.set_xticks(range(8))
    ax.set_yticks(np.arange(6) / 5, ["0", "1/5", "2/5", "3/5", "4/5", "1"])
    ax.set_xlabel(r"Threshold $x$ (count observations $\leq x$)")
    ax.set_ylabel(r"Empirical fraction $F_5(x)$")
    ax.grid(axis="y", alpha=0.2)
    count_ax = ax.secondary_yaxis("right", functions=(lambda y: 5*y, lambda y: y/5))
    count_ax.set_yticks(range(6))
    count_ax.set_ylabel("Cumulative count")
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
