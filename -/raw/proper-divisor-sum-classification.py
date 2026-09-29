"""Classify n=1,...,30 by proper-divisor sums; write basename PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Reproduce: make _media/proper-divisor-sum-classification.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    ns = np.arange(1, 31)
    sums = np.array([sum(d for d in range(1, n) if n % d == 0) for n in ns])
    fig, ax = plt.subplots(figsize=(8.2, 5.3), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.plot([0, 31], [0, 31], color="#555555", linestyle="--",
            linewidth=1.5, label=r"Perfect line: $s(n)=n$", zorder=2)
    for mask, color, marker, label in [
        (sums < ns, "#245a81", "o", r"Deficient: $s(n)<n$"),
        (sums == ns, "#287344", "D", r"Perfect: $s(n)=n$"),
        (sums > ns, "#b3541c", "^", r"Abundant: $s(n)>n$"),
    ]:
        ax.scatter(ns[mask], sums[mask], color=color, marker=marker,
                   s=64, edgecolors="white", linewidths=0.7,
                   label=label, zorder=3)
    for n, label, offset in [
        (1, "1: empty sum = 0", (14, 13)),
        (6, "6: s = 6", (-31, 33)),
        (8, "8: s = 7", (20, -23)),
        (12, "12: s = 16", (-24, 30)),
        (28, "28: s = 28", (-91, 12)),
    ]:
        ax.annotate(label, (n, sums[n - 1]), xytext=offset,
                    textcoords="offset points", fontsize=11,
                    bbox={"boxstyle": "round,pad=0.25", "fc": "white", "ec": "none"},
                    arrowprops={"arrowstyle": "-", "color": "#666666"}, zorder=4)
    ax.set(xlim=(0, 31), ylim=(-2, 45), xlabel=r"Positive integer $n$",
           ylabel=r"Sum of positive proper divisors $s(n)=\sigma(n)-n$")
    ax.set_xticks([1, 5, 10, 15, 20, 25, 30])
    ax.set_yticks(np.arange(0, 41, 10))
    ax.grid(alpha=0.16, zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=11)
    ax.xaxis.label.set_size(13)
    ax.yaxis.label.set_size(13)
    ax.set_title("Proper-divisor sums: compare each total with its number",
                 fontsize=15, pad=14)
    ax.legend(loc="upper left", fontsize=10, frameon=True, facecolor="white",
              framealpha=1, edgecolor="#dddddd")
    fig.subplots_adjust(left=0.12, right=0.97, bottom=0.14, top=0.88)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
