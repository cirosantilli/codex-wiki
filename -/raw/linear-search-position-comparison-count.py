"""Plot exact equality counts; tested with Python 3.14 and matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 8
    indices = np.arange(n)
    counts = indices + 1
    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.bar(indices, counts, width=0.65, color="#447eaa", label="First matching index j: C = j + 1")
    absent_position = n + 0.6
    ax.bar(absent_position, n, width=0.65, color="#d28a44", label="Absent: C = n")
    mean = (n + 1) / 2
    ax.axhline(mean, color="#317452", linestyle="--", linewidth=2,
               label="Uniform unique successful target: mean = 4.5")
    for index, count in zip(indices, counts):
        ax.text(index, count + 0.13, str(count), ha="center", fontsize=11)
    ax.text(absent_position, n + 0.13, str(n), ha="center", fontsize=11)
    ax.set_xticks([*indices, absent_position], [*map(str, indices), "absent"])
    ax.set_yticks(np.arange(10))
    ax.set_ylim(0, 10.8)
    ax.set_xlabel("First matching index (zero-based), or absent result", fontsize=11)
    ax.set_ylabel("Number of target-entry equality checks", fontsize=11)
    ax.set_title("Linear search: position determines comparisons (n = 8)", fontsize=14, pad=12)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.grid(axis="y", alpha=0.2)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
