"""Plot exact fibres of R^2 -> R; run from _media with Python 3.14.

Uses repository matplotlib 3.10.7 and numpy 2.3.5 dependencies.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig = plt.figure(figsize=(9.2, 4.6), facecolor="white")
    ax = fig.add_axes((0.09, 0.17, 0.47, 0.68))
    out = fig.add_axes((0.73, 0.17, 0.20, 0.68))
    colors = ["#b47700", "#2464a0", "#a53568"]
    y = np.linspace(-2, 2, 501)
    for c, color in zip((-2, 0, 2), colors):
        x = c - 2 * y
        visible = (x >= -3.2) & (x <= 3.2)
        ax.plot(x[visible], y[visible], color=color, lw=2.5,
                label=rf"$x+2y={c}$" + (" (kernel)" if c == 0 else ""))
        # One representative connects a whole fibre to its scalar output.
        point = (c / 5, 2 * c / 5)
        ax.scatter(*point, color=color, s=35, zorder=5)
        out.scatter(0, c, color=color, s=65, zorder=5)
        fig.add_artist(ConnectionPatch(
            xyA=point, coordsA=ax.transData, xyB=(0, c), coordsB=out.transData,
            arrowstyle="->", mutation_scale=13, color=color, lw=1.4,
            alpha=0.65, zorder=0, connectionstyle="arc3,rad=-0.12"))
    ax.axhline(0, color="0.65", lw=0.8)
    ax.axvline(0, color="0.65", lw=0.8)
    ax.annotate("", xy=(2, -1), xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": colors[1], "lw": 2.5})
    ax.text(0.6, -1.85, r"null direction $(2,-1)$", color=colors[1], fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.set(xlim=(-3.2, 3.2), ylim=(-2.1, 2.1), xlabel="$x$", ylabel="$y$",
           title=r"Input: $\mathbb{R}^2$")
    ax.set_aspect("equal")
    ax.legend(loc="upper right", framealpha=0.96, fontsize=9)
    ax.grid(alpha=0.18)
    out.plot([0, 0], [-3, 3], color="0.3", lw=1.3)
    for c in (-2, 0, 2):
        out.text(0.10, c, str(c), va="center")
    out.set(xlim=(-0.3, 0.6), ylim=(-3, 3), title=r"Output: $\mathbb{R}$")
    out.axis("off")
    out.text(0.02, 2.85, "$c$", va="bottom")
    fig.suptitle(r"$S(x,y)=x+2y$: rank 1, nullity 1", y=0.98, fontsize=14)
    fig.text(0.5, 0.035, "Each entire input line gives one scalar output; only the zero fibre is the kernel.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
