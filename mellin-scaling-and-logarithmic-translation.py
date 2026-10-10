"""Illustrate Mellin scaling using an interval indicator and log coordinates.

Run from _media; requires Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), layout="constrained")
    colors = ["#2368a0", "#c35c22"]
    intervals = [(1.0, 4.0), (0.5, 2.0)]
    labels = [r"$f(x)=\mathbf{1}_{[1,4]}(x)$", r"$f(2x)=\mathbf{1}_{[1/2,2]}(x)$"]
    for (left, right), color, label in zip(intervals, colors, labels):
        axes[0].plot([0.0, left, left, right, right, 4.6],
                     [0, 0, 1, 1, 0, 0], color=color, lw=2.4, label=label)
        lo, hi = np.log(left), np.log(right)
        axes[1].plot([-1.5, lo, lo, hi, hi, 2.0],
                     [0, 0, 1, 1, 0, 0], color=color, lw=2.4, label=label)
    axes[0].set(xlim=(0, 4.6), ylim=(-0.12, 1.45), xlabel=r"Positive variable $x$",
                ylabel="Indicator value", title="Scaling moves both endpoints")
    axes[0].set_xticks([0, 0.5, 1, 2, 4], ["0", "½", "1", "2", "4"])
    axes[0].legend(loc="upper right", fontsize=10, frameon=False)
    axes[1].set(xlim=(-1.5, 2.0), ylim=(-0.12, 1.45), xlabel=r"Log coordinate $u=\log x$",
                title=r"Translation by $-\log 2$")
    axes[1].set_xticks([-np.log(2), 0, np.log(2), np.log(4)],
                      [r"$-\log 2$", "0", r"$\log 2$", r"$\log 4$"])
    axes[1].annotate("", xy=(-np.log(2), 1.22), xytext=(0, 1.22),
                     arrowprops={"arrowstyle": "->", "color": colors[1], "lw": 1.8})
    axes[1].text(0.2, 1.2, r"Both widths: $\log 4$", fontsize=10)
    for ax in axes:
        ax.set_yticks([0, 1])
        ax.grid(alpha=0.17)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
