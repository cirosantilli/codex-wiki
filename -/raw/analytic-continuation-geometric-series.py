"""Illustrate geometric-series convergence versus analytic continuation.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Write an opaque white same-basename PNG in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    # Check finite sums directly, their remainder, and a recentered series.
    n = np.arange(21)
    points = np.array([0.5, 0.3 + 0.4j, -0.75])
    sums = np.sum(points[:, None] ** n, axis=1)
    remainder = points**21 / (1 - points)
    assert np.max(np.abs(1 / (1 - points) - sums - remainder)) < 1e-14
    outside = np.cumsum(2.0 ** np.arange(11))
    assert np.array_equal(outside, 2.0 ** np.arange(1, 12) - 1)
    recentered = 0.5 * np.sum((-0.25) ** np.arange(25))
    assert abs(recentered - 0.4) < 1e-14

    blue, orange, red = "#186a9a", "#cb721f", "#b63a40"
    fig, (plane, real) = plt.subplots(1, 2, figsize=(10, 4.6), dpi=130)
    fig.patch.set_facecolor("white")
    plane.add_patch(Circle((0, 0), 1, facecolor="#e8f2fa", edgecolor=blue,
                           linestyle="--", linewidth=2))
    plane.axhline(0, color="0.75", lw=0.8)
    plane.axvline(0, color="0.75", lw=0.8)
    plane.scatter([1], [0], marker="x", color=red, s=75, lw=2, zorder=5)
    plane.scatter([0.5, 2], [0, 0], color=[blue, orange], s=35, zorder=5)
    plane.annotate("Pole at 1", (1, 0), (1.35, -0.62), color=red,
                   arrowprops={"arrowstyle": "->", "color": red})
    plane.text(0, 0.48, r"Series converges" + "\n" + r"$|z|<1$",
               color=blue, ha="center", fontsize=11)
    plane.text(0.5, -0.26, r"$1/2$", ha="center", color=blue)
    plane.text(2, 0.18, r"$2$", ha="center", color=orange)
    plane.text(-1.15, -1.42, "Continuation exists on both sides\nof the circle, except at the pole.",
               fontsize=10, color="0.25")
    plane.set(xlim=(-1.55, 2.65), ylim=(-1.6, 1.6), xlabel=r"$\operatorname{Re}z$",
              ylabel=r"$\operatorname{Im}z$", title="Original radius is still 1")
    plane.set_aspect("equal")

    real.axvspan(-1, 1, color="#e8f2fa")
    real.axhline(0, color="0.75", lw=0.8)
    for a, b in [(-2.1, 0.95), (1.05, 2.6)]:
        x = np.linspace(a, b, 700)
        real.plot(x, 1 / (1 - x), color=blue, lw=2.2)
    x = np.linspace(-2.1, 2.6, 700)
    real.plot(x, np.sum(x[:, None] ** np.arange(6), axis=1),
              color=orange, lw=1.6, linestyle="--", label=r"Finite sum $S_5(x)$")
    real.axvline(1, color=red, lw=1.1, linestyle=":")
    real.axvline(-1, color=blue, lw=0.8, linestyle=":")
    real.scatter([0.5, 2], [2, -1], color=blue, s=35, zorder=5)
    real.annotate(r"$F(1/2)=2$", (0.5, 2), (-1.65, 3.8), color=blue,
                  arrowprops={"arrowstyle": "->", "color": blue})
    real.annotate(r"$F(2)=-1$", (2, -1), (1.25, -4.6), color=blue,
                  arrowprops={"arrowstyle": "->", "color": blue})
    real.text(0.97, 0.87, r"$S_5(2)=63$ (off scale)" + "\n" + r"$S_N(2)\to+\infty$",
              transform=real.transAxes, ha="right", color=orange, fontsize=10)
    real.plot([], [], color=blue, lw=2.2, label=r"Continuation $F(x)=1/(1-x)$")
    real.legend(loc="lower left", fontsize=9, framealpha=1)
    real.set(xlim=(-2.1, 2.6), ylim=(-8, 8), xlabel=r"Real input $x$",
             ylabel="Value", title="Extension does not change convergence")
    real.text(0.5, -0.22, r"Shaded interval: original series converges only for $-1<x<1$",
              transform=real.transAxes, ha="center", fontsize=9)
    for ax in (plane, real):
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"Geometric series $1+z+z^2+\cdots$ and its analytic continuation", fontsize=14)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.21, top=0.81, wspace=0.34)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Verified finite-sum remainders; S_10(2)={outside[-1]:.0f}; "
          f"recentered F(-3/2)={recentered:.15g}.")


if __name__ == "__main__":
    main()
