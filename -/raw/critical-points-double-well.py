"""Plot local versus global extrema of x**4 - 2*x**2.

Run from _media; save the matching opaque PNG in the current directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(7.4, 4.8), dpi=120,
                           constrained_layout=True, facecolor="white")
    ax.set_facecolor("white")
    x = np.linspace(-1.8, 1.8, 721)
    ax.plot(x, x**4 - 2*x**2, color="#235789", linewidth=2.8,
            label=r"$f(x)=x^4-2x^2$")
    ax.axhline(-1, color="#287a51", linestyle="--", linewidth=1.5,
               label=r"global lower bound: $f(x)\geq -1$")
    ax.axhline(0, color="#aaaaaa", linewidth=0.8, zorder=0)
    ax.axvline(0, color="#aaaaaa", linewidth=0.8, zorder=0)
    ax.scatter([-1, 1], [-1, -1], s=65, color="#287a51", zorder=5)
    ax.scatter([0], [0], s=65, color="#b63c45", zorder=5)
    for point, text_x in [(-1, -1.55), (1, 0.7)]:
        ax.annotate(f"({point}, -1)\nstrict local minimum\nglobal minimum",
                    xy=(point, -1), xytext=(text_x, 0.7), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": "#287a51"})
    ax.annotate("(0, 0)\nstrict local maximum", xy=(0, 0),
                xytext=(-0.5, 2.6), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#b63c45"})
    ax.text(0.5, 0.98, "Both tails rise without bound: no global maximum on R",
            transform=ax.transAxes, ha="center", va="top", fontsize=10)
    ax.set(xlim=(-1.8, 1.8), ylim=(-1.45, 4.5), xlabel=r"$x$",
           ylabel=r"$f(x)$", title="Three stationary points, two kinds of extrema")
    ax.set_xticks([-1.5, -1, 0, 1, 1.5])
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14),
              fontsize=10, frameon=False)
    fig.savefig(Path.cwd() / "critical-points-double-well.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
