"""Draw counterexamples to omitting either monotonicity or boundedness.

Writes an opaque PNG to cwd. Tested with Python 3.14, matplotlib 3.10.7,
and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    n = np.arange(1, 13)
    growing, alternating = n, (-1) ** n
    assert np.all(np.diff(growing) > 0)
    assert np.all(np.abs(alternating) == 1)
    assert np.any(np.diff(alternating) > 0)
    assert np.any(np.diff(alternating) < 0)

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.4), dpi=120,
                             facecolor="white")
    ax = axes[0]
    ax.plot(n, growing, "o-", color="#176ba0", markersize=5)
    ax.annotate("Keeps rising past every finite bound", xy=(12, 12),
                xytext=(1.3, 12.4), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#176ba0"})
    ax.text(0.04, 0.07, "Monotone: yes\nBounded above: no\nFinite limit: no",
            transform=ax.transAxes, fontsize=11, linespacing=1.6,
            bbox={"facecolor": "white", "edgecolor": "#d0d7dd"})
    ax.set(xlim=(0.5, 12.6), ylim=(0, 14), ylabel="Sequence value",
           title=r"Without an upper bound: $a_n=n$")

    ax = axes[1]
    ax.axhspan(-1, 1, color="#73559a", alpha=0.10)
    ax.axhline(1, color="#b65320", linestyle="--", linewidth=1)
    ax.axhline(-1, color="#73559a", linestyle="--", linewidth=1)
    ax.plot(n, alternating, color="#a9a9a9", linewidth=0.8, alpha=0.7)
    even = n % 2 == 0
    ax.scatter(n[even], alternating[even], color="#b65320", s=38,
               zorder=3, label="Even indices: value +1")
    ax.scatter(n[~even], alternating[~even], color="#73559a", s=38,
               zorder=3, label="Odd indices: value -1")
    ax.text(0.04, 0.36, "Bounded: yes\nMonotone: no\nFinite limit: no",
            transform=ax.transAxes, fontsize=11, linespacing=1.6,
            bbox={"facecolor": "white", "edgecolor": "#d0d7dd"})
    ax.set(xlim=(0.5, 12.6), ylim=(-1.45, 1.75),
           ylabel="Sequence value", yticks=[-1, 0, 1],
           title=r"Without monotonicity: $b_n=(-1)^n$")
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_xlabel("Index n")
        ax.set_xticks([1, 3, 6, 9, 12])
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.2)
    fig.suptitle("Both assumptions matter for a finite real limit", fontsize=14,
                 y=0.97)
    fig.text(0.5, 0.025, "Markers are terms; connecting segments only guide the eye.",
             ha="center", fontsize=10, color="#4b555e")
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.82,
                        wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
