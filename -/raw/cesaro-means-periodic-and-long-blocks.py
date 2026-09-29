"""Exact examples showing periodic averaging and failure for longer blocks."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.9), dpi=110)
    fig.patch.set_facecolor("white")
    fig.suptitle("Bounded partial sums need not have convergent averages", fontsize=18, y=0.98)
    m = np.arange(1, 37)
    periodic = np.tile([0, 2, 1], 12)
    axes[0].step(m, periodic, where="mid", color="#747d89", alpha=0.8, label="partial sums 0, 2, 1, …")
    axes[0].plot(m, np.cumsum(periodic)/m, color="#216da2", marker="o", markersize=3, label="Cesàro means")
    axes[0].axhline(1, color="#d07e20", linestyle="--", label="limit 1")
    axes[0].set_title("A repeated cycle has a stable average", fontsize=13)
    blocks = np.concatenate([np.full(3**j, j%2) for j in range(9)])
    count = np.arange(1, len(blocks)+1)
    mean = np.cumsum(blocks)/count
    axes[1].step(count, blocks, where="post", color="#747d89", alpha=0.8, label="partial sums: blocks of 0 and 1")
    axes[1].plot(count, mean, color="#216da2", linewidth=2, label="Cesàro means")
    ends = np.cumsum([3**j for j in range(9)])
    axes[1].scatter(ends, mean[ends-1], color="#d07e20", s=35, zorder=5, label="end of each block")
    axes[1].axhline(0.25, color="#b6875c", linestyle=":", linewidth=1)
    axes[1].axhline(0.75, color="#b6875c", linestyle=":", linewidth=1)
    axes[1].set_xscale("log", base=3)
    axes[1].set_title("Block lengths 1, 3, 9, 27, … prevent a limit", fontsize=13)
    for ax in axes:
        ax.set_xlabel("number of included partial sums (N + 1)", fontsize=11)
        ax.grid(alpha=0.20)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(fontsize=9, loc="lower right")
    axes[0].set_ylim(-0.12, 2.15)
    axes[1].set_ylim(-0.10, 1.10)
    fig.text(0.5, 0.025, "Both are exact constructed sequences, not measured data. Long later blocks can keep changing the average.", ha="center", fontsize=11)
    fig.subplots_adjust(left=0.055, right=0.98, top=0.80, bottom=0.17, wspace=0.22)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
