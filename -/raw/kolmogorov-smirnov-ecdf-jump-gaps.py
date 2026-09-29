"""Exact four-point ECDF illustration; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; write the matching PNG basename to the current directory.
The points are stipulated rational values, not experimental observations.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    exact = [Fraction(1, 10), Fraction(2, 5), Fraction(4, 5), Fraction(9, 10)]
    plus = [Fraction(i, 4) - v for i, v in enumerate(exact, 1)]
    minus = [v - Fraction(i - 1, 4) for i, v in enumerate(exact, 1)]
    assert max(plus) == Fraction(3, 20)
    assert max(minus) == Fraction(3, 10)
    x = np.array([float(v) for v in exact])
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8, 5.4), layout="constrained")
    ax.plot([0, 1], [0, 1], color="#d47716", lw=2, label=r"Null CDF: $F_0(x)=x$")
    edges = np.r_[0, x, 1]
    for i in range(5):
        ax.plot(edges[i:i + 2], [i / 4] * 2, color="#1767a6", lw=2.5,
                label=r"ECDF: $F_4(x)$" if i == 0 else None)
    ax.scatter(x, np.arange(4) / 4, s=65, facecolors="white",
               edgecolors="#1767a6", linewidths=1.8, zorder=5,
               label="Open: left limit")
    ax.scatter(x, np.arange(1, 5) / 4, s=50, color="#1767a6", zorder=6,
               label="Filled: value at jump")
    ax.annotate("", xy=(0.1, 0.25), xytext=(0.1, 0.1),
                arrowprops={"arrowstyle": "<->", "color": "#32834a", "lw": 2})
    ax.annotate(r"$D_4^+=3/20$", xy=(0.1, 0.175), xytext=(0.23, 0.12),
                color="#28713e", arrowprops={"arrowstyle": "-", "color": "#28713e"})
    ax.annotate("", xy=(0.8, 0.8), xytext=(0.8, 0.5),
                arrowprops={"arrowstyle": "<->", "color": "#a72f57", "lw": 2.2})
    ax.annotate(r"$D_4^-=3/10$" + "\nSupremum from the left", xy=(0.8, 0.65),
                xytext=(0.30, 0.74), color="#a72f57",
                arrowprops={"arrowstyle": "-", "color": "#a72f57"})
    ax.set(xlim=(-0.025, 1.025), ylim=(-0.025, 1.06), xlabel=r"Threshold $x$",
           ylabel="Cumulative probability", title="Check both sides of every ECDF jump")
    ax.set_xticks([0, 0.1, 0.4, 0.8, 0.9, 1])
    ax.set_yticks(np.arange(5) / 4)
    ax.grid(alpha=0.15)
    ax.legend(loc="upper left", framealpha=1, fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
