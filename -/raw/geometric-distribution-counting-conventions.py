"""Plot the two geometric counting conventions; emit a PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5 (pyproject.toml).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    p = 0.3
    q = 1 - p
    t = np.arange(1, 11)
    masses = p * q ** (t - 1)
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.6), dpi=110,
                             sharey=True, facecolor="white")
    for ax, x, color in zip(axes, (t, t - 1), ("#256393", "#ba6021")):
        ax.bar(x, masses, color=color, width=0.7)
        ax.set_xticks(x)
        ax.set_ylim(0, 0.35)
        ax.set_yticks(np.arange(0, 0.36, 0.1))
        ax.grid(axis="y", alpha=0.22)
        ax.set_axisbelow(True)
        ax.set_facecolor("white")
        ax.text(x[0], masses[0] + 0.012, "0.30", ha="center", fontsize=10)
        ax.text(x[3], masses[3] + 0.012, "0.1029", ha="center", fontsize=10)
    axes[0].set_title("Count every attempt: T = 1, 2, …", pad=12)
    axes[1].set_title("Count only failures: F = 0, 1, …", pad=12)
    axes[0].set_xlabel("First-success attempt k")
    axes[1].set_xlabel("Preceding failures j = k − 1")
    axes[0].set_ylabel("Probability mass")
    fig.suptitle("One experiment, two counting conventions  (p = 0.3)",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.075, "T = 4 and F = 3 are the same event: three failures, then success.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.023,
             f"Ten masses shown in each panel; omitted tail in each = 0.7¹⁰ ≈ {q**10:.5f}.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.24, top=0.79, wspace=0.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
