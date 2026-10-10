"""Exact counts below N, including zero; save same-basename PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Reproduce: make _media/natural-density-samples.png
"""

from math import isqrt
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def alternating_block_count(n):
    """Count A intersect {0,...,n-1}, A = union [4**k,2*4**k)."""
    count = 0
    start = 1
    while start < n:
        count += max(0, min(n, 2 * start) - start)
        start *= 4
    return count


def main():
    maximum = 4 ** 7
    n = np.arange(1, maximum + 1, dtype=np.int64)
    evens = (n + 1) // 2
    squares = np.array([isqrt(int(value) - 1) + 1 for value in n])
    blocks = np.array([alternating_block_count(int(value)) for value in n])
    low_n = np.array([4 ** k for k in range(8)], dtype=np.int64)
    high_n = 2 * low_n[:-1]
    low_counts = (low_n - 1) // 3
    high_counts = (2 * high_n - 1) // 3
    assert all(alternating_block_count(int(x)) == y
               for x, y in zip(low_n, low_counts))
    assert all(alternating_block_count(int(x)) == y
               for x, y in zip(high_n, high_counts))
    assert alternating_block_count(16) == 5
    assert alternating_block_count(32) == 21
    assert squares[9] == 4 and squares[99] == 10
    assert evens[9] == 5 and evens[10] == 6

    blue, orange, green, ink = "#246f9b", "#b76325", "#268269", "#233746"
    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 5.7), dpi=110,
                                     facecolor="white")
    left.plot(n, evens / n, color=blue, lw=1.6, label="Even integers (0 included)")
    left.plot(n, squares / n, color=orange, lw=1.6, label="Squares (0 included)")
    left.axhline(0.5, ls="--", color=blue, alpha=0.55, lw=1)
    left.set_title("Density exists: 1/2 for evens, 0 for squares", fontsize=12)
    left.legend(loc="upper right", frameon=False, fontsize=9)
    left.annotate("At N = 10: 4/10 squares", xy=(10, 0.4), xytext=(22, 0.72),
                  arrowprops={"arrowstyle": "->", "color": orange},
                  fontsize=10, color=orange)
    left.annotate("At N = 100: 10/100 squares", xy=(100, 0.1),
                  xytext=(180, 0.24),
                  arrowprops={"arrowstyle": "->", "color": orange},
                  fontsize=10, color=orange)

    right.plot(n, blocks / n, color=green, lw=1.7)
    right.scatter(low_n, low_counts / low_n, color=blue, s=28, zorder=3,
                  label=r"$N=4^k$: approaches 1/3")
    right.scatter(high_n, high_counts / high_n, color=orange, s=28, zorder=3,
                  label=r"$N=2\cdot4^k$: approaches 2/3")
    for level in [1 / 3, 2 / 3]:
        right.axhline(level, color=ink, ls="--", lw=1, alpha=0.55)
    right.set_title("No density: include [1,2), [4,8), [16,32), …", fontsize=12)
    right.legend(loc="upper right", frameon=False, fontsize=9)
    right.annotate("21/32", xy=(32, 21 / 32), xytext=(35, 0.78),
                   arrowprops={"arrowstyle": "->", "color": orange},
                   color=orange, fontsize=11)
    right.annotate("5/16", xy=(16, 5 / 16), xytext=(6, 0.15),
                   arrowprops={"arrowstyle": "->", "color": blue},
                   color=blue, fontsize=11)
    for ax in [left, right]:
        ax.set_xscale("log", base=4)
        ax.set(xlim=(1, maximum), ylim=(-0.025, 1.05),
               xlabel="N (logarithmic scale)",
               ylabel=r"Exact proportion $|S\cap\{0,\ldots,N-1\}|/N$")
        ax.set_xticks([1, 4, 16, 64, 256, 1024, 4096, 16384],
                      labels=["1", "4", "16", "64", "256", "1024", "4096", "16384"])
        ax.tick_params(axis="x", labelsize=8)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.15)
    fig.suptitle("Natural density measures proportions, not infinite cardinality",
                 fontsize=15, y=0.97, color=ink)
    fig.text(0.5, 0.055,
             "Counts use 0 ≤ n < N. The alternating-block set excludes 0."
             "  Markers show exact counts at block boundaries.",
             ha="center", fontsize=10, color=ink)
    fig.subplots_adjust(left=0.07, right=0.985, bottom=0.17,
                        top=0.82, wspace=0.22)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
