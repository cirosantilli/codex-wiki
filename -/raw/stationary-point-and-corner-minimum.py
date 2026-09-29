"""Contrast an increasing cubic's stationary point and an absolute-value corner.

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
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.4), dpi=120,
                             constrained_layout=True, facecolor="white")
    x = np.linspace(-1.4, 1.4, 561)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#aaaaaa", linewidth=0.8, zorder=0)
        ax.axvline(0, color="#aaaaaa", linewidth=0.8, zorder=0)
        ax.set(xlim=(-1.4, 1.4), xlabel=r"$x$")
        ax.set_xticks([-1, 0, 1])
    axes[0].plot(x, x**3, color="#235789", linewidth=2.8)
    axes[0].plot([-0.65, 0.65], [0, 0], color="#b63c45",
                 linestyle="--", linewidth=2)
    axes[0].scatter([0], [0], color="#b63c45", s=60, zorder=5)
    axes[0].annotate(r"$g'(0)=0$" "\nhorizontal tangent", xy=(0, 0),
                     xytext=(-1.27, 1.5), fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "#b63c45"})
    axes[0].set(ylim=(-3, 3), ylabel=r"$g(x)$",
                title=r"$g(x)=x^3$: stationary, no extremum")
    axes[0].text(0.5, 0.04, "Strictly increasing through zero",
                 transform=axes[0].transAxes, ha="center", fontsize=10)
    axes[1].plot(x, np.abs(x), color="#287a51", linewidth=2.8)
    axes[1].scatter([0], [0], color="#b63c45", s=60, zorder=5)
    axes[1].annotate("(0, 0)\nstrict local minimum\nunique global minimum",
                     xy=(0, 0), xytext=(-0.85, 0.8), fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "#b63c45"})
    axes[1].text(-1.15, 0.42, "slope -1", rotation=-36, fontsize=10)
    axes[1].text(0.65, 0.42, "slope +1", rotation=36, fontsize=10)
    axes[1].set(ylim=(-0.2, 1.65), ylabel=r"$h(x)$",
                title=r"$h(x)=|x|$: minimum, no derivative")
    axes[1].text(0.5, 0.025, "Not a stationary point: derivative does not exist",
                 transform=axes[1].transAxes, ha="center", fontsize=9)
    fig.savefig(Path.cwd() / "stationary-point-and-corner-minimum.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
