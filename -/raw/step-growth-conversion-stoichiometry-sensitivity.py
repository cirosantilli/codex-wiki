"""Plot original ideal bifunctional step-growth sensitivities; run from _media.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.2), facecolor="white")
    p = np.linspace(0.9, 0.9999, 1600)
    colors = ["#285da8", "#178249", "#b34b15"]
    for r, color in zip([1.0, 0.99, 0.95], colors):
        xn = (1 + r) / (1 + r - 2 * r * p)
        axes[0].plot(p, xn, color=color, lw=2.3, label=rf"$r={r:g}$")
    for pp, xx in [(0.95, 20), (0.98, 50), (0.995, 200)]:
        axes[0].scatter(pp, xx, color=colors[0], s=30, zorder=4)
        axes[0].annotate(f"({pp:g}, {xx})", (pp, xx), xytext=(-8, 10),
                         textcoords="offset points", ha="right", fontsize=10)
    axes[0].set(xlim=(0.9, 1.0), ylim=(7, 12000), yscale="log",
                xlabel="Conversion p of limiting A groups", ylabel=r"Number-average degree $X_n$",
                title="Late conversion controls chain length")
    axes[0].legend(loc="upper left", frameon=False)
    excess_percent = np.geomspace(0.01, 5, 1000)
    r = 1 - excess_percent / 100
    cap = (1 + r) / (1 - r)
    axes[1].plot(excess_percent, cap, color="#7a3989", lw=2.3)
    for imbalance, xx in [(1, 199), (5, 39)]:
        axes[1].scatter(imbalance, xx, color="#7a3989", s=32, zorder=4)
        axes[1].annotate(f"{imbalance}% → {xx}", (imbalance, xx), xytext=(-8, 12),
                         textcoords="offset points", ha="right", fontsize=11)
    axes[1].axhline(200, color="#6f7479", ls="--", lw=1)
    axes[1].text(0.014, 240, r"Target $X_n=200$", color="#54595f", fontsize=11)
    axes[1].set(xscale="log", yscale="log", xlim=(0.01, 5.5), ylim=(30, 25000),
                xlabel=r"Initial group imbalance $100(1-r)$ (%)",
                ylabel=r"Ceiling $X_n$ at $p=1$",
                title="Excess B leaves a chain-length ceiling")
    axes[1].set_xticks([0.01, 0.1, 1, 5], ["0.01", "0.1", "1", "5"])
    for ax in axes:
        ax.grid(True, which="major", color="#dddddd", lw=0.7)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Ideal linear step growth: high conversion AND balanced groups", fontsize=16)
    fig.text(0.5, 0.015,
             r"$r=A_0/B_0\leq1$; $p$ counts reacted A groups; $X_n$ counts both feed species. No rings or branching.",
             ha="center", fontsize=11)
    fig.tight_layout(rect=(0, 0.07, 1, 0.92), w_pad=2.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
