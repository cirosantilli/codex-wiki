"""Illustrate exact variation of an original polygonal function; emit to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.arange(5)
    f = np.array([0, 2, -1, 3, 1])
    increments = np.diff(f)
    positive = np.r_[0, np.cumsum(np.maximum(increments, 0))]
    negative = np.r_[0, np.cumsum(np.maximum(-increments, 0))]
    variation = positive + negative
    assert variation[-1] == 11 and positive[-1] == 6 and negative[-1] == 5
    assert np.array_equal(f, positive - negative)
    fig = plt.figure(figsize=(10, 6), dpi=120, facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[2.2, 1])
    ax = fig.add_subplot(grid[0, 0])
    ax.plot(t, f, "o-", color="#1565a8", lw=2.3, label="Actual piecewise linear function")
    ax.plot([0, 4], f[[0, 4]], "--", color="#b14e13", label="Endpoints alone: change 1")
    for x, y in zip(t, f):
        ax.annotate(str(y), (x, y), xytext=(5, 8), textcoords="offset points")
    ax.set(xlabel="t", ylabel="f(t)", title="Net change hides direction reversals", xticks=t, ylim=(-1.6, 3.7))
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.2)
    ax = fig.add_subplot(grid[0, 1])
    for y, label, color in [(positive, "Accumulated rises P", "#237a39"), (negative, "Accumulated falls N", "#a84919"), (variation, "Total variation v = P + N", "#7654a3")]:
        ax.plot(t, y, "o-", label=label, color=color, lw=2)
    ax.set(xlabel="t", ylabel="Accumulated movement", title="Accumulated rises and falls: f = P − N", xticks=t)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.2)
    ax = fig.add_subplot(grid[1, :])
    partitions = [[0, 4], [0, 1, 3, 4], list(t)]
    sums = [int(np.abs(np.diff(f[p])).sum()) for p in partitions]
    assert sums == [1, 5, 11]
    bars = ax.barh([2, 1, 0], sums, color=["#adbad0", "#6791ba", "#1565a8"], height=0.55)
    ax.set(yticks=[2, 1, 0], yticklabels=["Partition 0, 4", "Partition 0, 1, 3, 4", "All knots 0, 1, 2, 3, 4"], xlabel="Sum of absolute sampled increments", xlim=(0, 12.4))
    for bar, value in zip(bars, sums):
        ax.text(value + 0.15, bar.get_y() + bar.get_height() / 2, str(value), va="center", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
