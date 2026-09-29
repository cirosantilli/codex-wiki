"""Exact toy pooling CV curves, independent claims versus one common shock.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Writes the matching opaque PNG basename into the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.2, 5.8))
    n = np.logspace(0, 4, 300)
    ax.loglog(n, 3 / np.sqrt(n), color="#2166ac", lw=3,
              label="Independent claims: 3 / √n")
    ax.loglog(n, np.full_like(n, 3), color="#c96c18", lw=3, linestyle="--",
              label="One common shock: 3 for every n")
    for size, label in [(1, "300%"), (100, "30%"), (10000, "3%")]:
        cv = 3 / np.sqrt(size)
        ax.plot(size, cv, "o", color="#2166ac", markersize=7)
        ax.annotate(label, (size, cv), xytext=(8, 9), textcoords="offset points",
                    color="#2166ac", weight="bold")
    ax.set_xlim(0.7, 18000)
    ax.set_ylim(0.02, 6)
    ax.set_xticks([1, 10, 100, 1000, 10000], ["1", "10", "100", "1,000", "10,000"])
    ax.set_yticks([0.03, 0.1, 0.3, 1, 3], ["3%", "10%", "30%", "100%", "300%"])
    ax.set_xlabel("Number of policies n (log scale)")
    ax.set_ylabel("Relative variability = SD / expected loss (log scale)")
    ax.grid(which="major", alpha=0.2)
    ax.legend(loc="lower left", framealpha=1, fontsize=11)
    fig.suptitle("Toy pooling: the mean stays the same per policy", fontsize=16, weight="bold", y=0.98)
    ax.set_title("£1,000 claim with 10% probability • £100 expected loss per policy", fontsize=12, pad=16)
    fig.text(0.5, 0.04, "Independent total: mean £100n, SD £300√n • Common-shock total: mean £100n, SD £300n",
             ha="center", fontsize=11)
    fig.text(0.5, 0.005, "Exact model curves from invented assumptions; not measured data or a solvency guarantee.",
             ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.08, 1, 0.94))
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
