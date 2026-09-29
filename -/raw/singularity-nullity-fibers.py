"""Parallel solution fibers of (x,y) -> (x+y,0); opaque PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([[1, 1], [0, 0]])
    np.testing.assert_array_equal(a @ np.array([1, -1]), [0, 0])
    np.testing.assert_array_equal(a @ np.array([1, 0]), [1, 0])
    np.testing.assert_array_equal(a @ np.array([0, 1]), [1, 0])
    colors = {0: "#246c9b", 1: "#bd572f", 2: "#298466"}
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), dpi=120)
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.22, top=0.80, wspace=0.28)
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#aaaaaa", lw=0.8)
        ax.axvline(0, color="#aaaaaa", lw=0.8)
        ax.set_aspect("equal")
        ax.spines[["top", "right"]].set_visible(False)
    x = np.linspace(-1.5, 2.5, 201)
    for c, color in colors.items():
        axes[0].plot(x, c-x, color=color, lw=2,
                     label=("Kernel: x + y = 0" if c == 0 else f"Fiber: x + y = {c}"))
        axes[1].scatter([c], [0], color=color, s=65, zorder=5)
        axes[1].text(c, -0.25, f"({c}, 0)", color=color, ha="center", fontsize=10)
    axes[0].scatter([1, 0], [0, 1], color=colors[1], s=50, zorder=5)
    axes[0].text(1.08, 0.08, "(1, 0)", color=colors[1], fontsize=10)
    axes[0].text(0.05, 1.10, "(0, 1)", color=colors[1], fontsize=10)
    axes[0].annotate("", (1.5, -0.5), (0.7, 0.3),
                     arrowprops={"arrowstyle": "->", "color": colors[1], "lw": 2})
    axes[0].text(1.55, -0.7, "Kernel direction\n(1, −1)", color=colors[1], fontsize=10)
    axes[0].set(xlim=(-1.3, 2.4), ylim=(-1.3, 2.4), xlabel="Input x", ylabel="Input y",
                title="Input: each nonempty fiber is a line")
    axes[0].legend(loc="lower left", fontsize=9, framealpha=1, facecolor="white")
    axes[1].plot([-1.3, 2.4], [0, 0], color="#777777", lw=2, zorder=2)
    axes[1].scatter([1], [1], color="#8b4299", marker="x", s=100, lw=2, zorder=5)
    axes[1].annotate("(1, 1) is unreachable\nIts fiber is empty", (1, 1),
                     xytext=(0.55, 1.65), ha="center", color="#8b4299", fontsize=11,
                     arrowprops={"arrowstyle": "->", "color": "#8b4299"})
    axes[1].text(0.55, 0.35, "Image: all (c, 0)", ha="center", color="#555555")
    axes[1].set(xlim=(-1.3, 2.4), ylim=(-1.3, 2.4), xlabel="Output coordinate 1",
                ylabel="Output coordinate 2", title="Output: one point per input fiber")
    fig.suptitle(r"$F(x,y)=(x+y,0)$: nullity 1 means one direction of solution freedom",
                 fontsize=14, y=0.97)
    fig.text(0.5, 0.09, "Both orange inputs give (1, 0). Moving along their line leaves the output unchanged.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Exact toy geometry, not measured data. Empty fibers have no solution-space dimension assigned here.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
