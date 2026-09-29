"""Original function graphs distinguishing intermediate-value hypotheses.

Run from _media using Python 3.14, matplotlib 3.10.7, numpy 2.3.5:
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../intermediate-value-continuous-jump-tangent.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.2), layout="constrained", facecolor="white")
    blue, red, green = "#235eab", "#b43b30", "#167a50"
    x = np.linspace(-1.5, 1.5, 601)
    axes[0].plot(x, x**3 - x, color=blue, linewidth=2.6)
    axes[0].scatter([-1, 0, 1], [0, 0, 0], color=blue, s=38, zorder=4)
    axes[0].scatter([-1.5, 1.5], [-1.875, 1.875], color=blue, s=38, zorder=4)
    axes[0].set(title=r"Continuous: $h(x)=x^3-x$", xlim=(-1.65, 1.65), ylim=(-2.35, 2.35))
    axes[0].set_xticks([-1.5, -1, 0, 1, 1.5])
    axes[0].text(0.5, 0.96, "Opposite endpoint signs\nThree interior roots", transform=axes[0].transAxes, ha="center", va="top", fontsize=10)

    axes[1].plot([-1, 0], [-1, -1], color=red, linewidth=2.6)
    axes[1].plot([0, 1], [1, 1], color=red, linewidth=2.6)
    axes[1].scatter([0], [-1], facecolors="white", edgecolors=red, linewidths=2, s=65, zorder=4)
    axes[1].scatter([-1, 0, 1], [-1, 1, 1], color=red, s=38, zorder=4)
    axes[1].set(title=r"Jump: $j(x)=-1$ or $1$", xlim=(-1.15, 1.15), ylim=(-1.7, 1.7))
    axes[1].text(0.5, 0.96, "Opposite endpoint signs\nNo root", transform=axes[1].transAxes, ha="center", va="top", fontsize=10)
    axes[1].set_xticks([-1, 0, 1])
    axes[1].set_yticks([-1, 0, 1])

    x = np.linspace(-1, 1, 401)
    axes[2].plot(x, x**2, color=green, linewidth=2.6)
    axes[2].scatter([-1, 0, 1], [1, 0, 1], color=green, s=38, zorder=4)
    axes[2].set(title=r"Tangent: $t(x)=x^2$", xlim=(-1.15, 1.15), ylim=(-0.3, 1.55))
    axes[2].text(0.5, 0.96, "Same endpoint sign\nOne double root", transform=axes[2].transAxes, ha="center", va="top", fontsize=10)
    axes[2].set_xticks([-1, 0, 1])
    axes[2].set_yticks([0, 0.5, 1])

    for ax in axes:
        ax.axhline(0, color="#737b83", linewidth=1, zorder=0)
        ax.axvline(0, color="#d5dbe0", linewidth=1, zorder=0)
        ax.set(xlabel="x", ylabel="Function value")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Original mathematical examples — no measured data", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
