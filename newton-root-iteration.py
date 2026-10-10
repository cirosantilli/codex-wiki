"""Draw Newton tangent geometry; save newton-root-iteration.png in cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.8), layout="constrained")
    fig.patch.set_facecolor("white")
    blue, orange, green = "#2166ac", "#d46514", "#25834a"

    ax = axes[0]
    t = np.linspace(0.85, 1.85, 400)
    ax.plot(t, t * t - 2, color=blue, lw=2.5, label=r"$F(t)=t^2-2$")
    x0, x1, x2 = 1.0, 1.5, 17 / 12
    assert np.isclose(x1 - (x1 * x1 - 2) / (2 * x1), x2)
    ax.plot([0.94, 1.7], [2 * 0.94 - 3, 2 * 1.7 - 3],
            color=orange, lw=1.8, label=r"Tangent at $t_0=1$")
    ax.plot([1.28, 1.74], [3 * 1.28 - 4.25, 3 * 1.74 - 4.25],
            color=green, lw=1.8, label=r"Tangent at $t_1=1.5$")
    for start, end, color in [((x0, -1), (x1, 0), orange),
                              ((x1, 0.25), (x2, 0), green)]:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2.2})
    ax.plot([x0, x0], [0, -1], ":", color="0.5")
    ax.plot([x1, x1], [0, 0.25], ":", color="0.5")
    ax.scatter([x0, x1], [-1, 0.25], c=[orange, green], zorder=5)
    ax.scatter([x1, x2], [0, 0], c=[orange, green], zorder=5)
    ax.scatter([np.sqrt(2)], [0], color="black", marker="*", s=80, zorder=6)
    ax.annotate(r"$t_0=1$", (x0, 0), xytext=(0.90, 0.24),
                arrowprops={"arrowstyle": "-", "color": "0.4"})
    ax.annotate(r"$t_1=1.5$", (x1, 0), xytext=(1.60, -0.50),
                arrowprops={"arrowstyle": "-", "color": orange}, color=orange)
    ax.annotate(r"$t_2=17/12$", (x2, 0), xytext=(1.02, 0.65),
                arrowprops={"arrowstyle": "-", "color": green}, color=green)
    ax.annotate(r"Root: $\sqrt{2}\approx1.41421$", (np.sqrt(2), 0),
                xytext=(1.09, -0.85),
                arrowprops={"arrowstyle": "-", "color": "0.3"})
    ax.set(xlim=(0.85, 1.85), ylim=(-1.25, 1.65), xlabel=r"$t$", ylabel=r"$F(t)$",
           title="Two tangent steps toward a square root")
    ax.legend(loc="upper left", fontsize=9, framealpha=1)

    ax = axes[1]
    x = np.linspace(-2.05, 1.4, 600)
    f = lambda value: value**3 - 2 * value + 2
    df = lambda value: 3 * value**2 - 2
    assert 0 - f(0) / df(0) == 1
    assert 1 - f(1) / df(1) == 0
    ax.plot(x, f(x), color=blue, lw=2.5, label=r"$F(x)=x^3-2x+2$")
    ax.plot([-0.2, 1.35], [2.4, -0.7], color=orange, lw=1.8,
            label=r"Tangent at $x_0=0$")
    ax.plot([-0.2, 1.35], [-0.2, 1.35], color=green, lw=1.8,
            label=r"Tangent at $x_1=1$")
    for start, end, color in [((0, 2), (1, 0), orange),
                              ((1, 1), (0, 0), green)]:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 2.2})
    for xx, yy in [(0, 2), (1, 1)]:
        ax.annotate("", xy=(xx, yy), xytext=(xx, 0),
                    arrowprops={"arrowstyle": "->", "linestyle": ":", "color": "0.4"})
    ax.scatter([0, 1], [2, 1], c=[orange, green], zorder=5)
    ax.scatter([0, 1], [0, 0], c=[green, orange], zorder=5)
    ax.text(0, -0.5, r"$0$", ha="center")
    ax.text(1, -0.5, r"$1$", ha="center")
    root = -1.8
    for _ in range(6):
        root -= f(root) / df(root)
    ax.scatter([root], [0], color="black", marker="*", s=80, zorder=6)
    ax.annotate(r"Root $\approx-1.76929$", (root, 0), xytext=(-1.94, 0.75),
                fontsize=10, arrowprops={"arrowstyle": "-", "color": "0.3"})
    ax.text(-1.75, -1.2, r"Iteration: $0\to1\to0\to1\to\cdots$", fontsize=11)
    ax.set(xlim=(-2.05, 1.4), ylim=(-2.65, 4.45), xlabel=r"$x$", ylabel=r"$F(x)$",
           title="A defined iteration can cycle forever")
    ax.legend(loc="upper left", fontsize=9, framealpha=1)

    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="0.25", lw=0.8, zorder=0)
        ax.grid(alpha=0.16)
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "newton-root-iteration.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
