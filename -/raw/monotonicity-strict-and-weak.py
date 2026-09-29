"""Compare four monotonicity examples; write an opaque PNG to cwd.

Uses the repository's Python 3.14, NumPy, and Matplotlib environment.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1.4, 1.4, 701)
    plateau_x = np.linspace(-1, 2, 601)
    plateau = np.clip(plateau_x, 0, 1)
    step = (x >= 0).astype(float)
    assert np.all(np.diff(x**3) > 0)
    assert np.all(np.diff(-x**3) < 0)
    assert np.all(np.diff(plateau) >= 0) and np.any(np.diff(plateau) == 0)
    assert np.all(np.diff(step) >= 0)
    assert np.array_equal(np.clip([-1, 0, 0.5, 1, 2], 0, 1), [0, 0, 0.5, 1, 1])

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 7.4), dpi=120, facecolor="white")
    blue, orange = "#246b9e", "#b4611c"
    axes[0, 0].plot(x, x**3, color=blue, lw=2.7)
    axes[0, 0].scatter([0], [0], color=blue, s=40, zorder=4)
    axes[0, 0].set(title="Strictly increasing\n" + r"$f(x)=x^3$", ylim=(-3, 3))
    axes[0, 1].plot(plateau_x, plateau, color=orange, lw=2.7)
    axes[0, 1].set(title="Nondecreasing, with flat portions\n" + r"$p(x)=\min(1,\max(0,x))$",
                   ylim=(-0.15, 1.15), yticks=[0, 0.5, 1])
    ax = axes[1, 0]
    ax.plot([-1.4, 0], [0, 0], color=orange, lw=2.7)
    ax.plot([0, 1.4], [1, 1], color=orange, lw=2.7)
    ax.scatter([0], [0], s=85, facecolors="white", edgecolors=orange, linewidths=2, zorder=5)
    ax.scatter([0], [1], s=85, facecolors=orange, edgecolors=orange, linewidths=2, zorder=5)
    ax.set(title="Nondecreasing, with a jump\n" + r"$F(x)=0\ (x<0),\quad F(x)=1\ (x\geq0)$",
           ylim=(-0.2, 1.25), yticks=[0, 0.5, 1], xlim=(-1.4, 1.4))
    ax.annotate("Included: F(0) = 1", xy=(0, 1), xytext=(0.26, 0.68),
                arrowprops={"arrowstyle": "->", "color": orange}, fontsize=10)
    axes[1, 1].plot(x, -x**3, color=blue, lw=2.7)
    axes[1, 1].scatter([0], [0], color=blue, s=40, zorder=4)
    axes[1, 1].set(title="Strictly decreasing\n" + r"$f(x)=-x^3$", ylim=(-3, 3))
    notes = ["No equal outputs for distinct inputs.",
             "Equal outputs are allowed on flat intervals.",
             "Open circle excluded; filled circle included.",
             "Every larger input gives a smaller output."]
    for ax, note in zip(axes.flat, notes):
        ax.set(xlabel="Input x", ylabel="Output")
        ax.grid(color="#e5e9eb", zorder=0)
        ax.spines[["top", "right"]].set_visible(False)
        ax.text(0.5, -0.29, note, transform=ax.transAxes, ha="center", fontsize=11)
    fig.suptitle("Monotonicity compares every ordered pair of inputs", fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.085, right=0.98, top=0.86, bottom=0.12, hspace=0.86, wspace=0.27)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Checks passed: strict cubic signs, weak plateau and step ordering, plateau values.")


if __name__ == "__main__":
    main()
