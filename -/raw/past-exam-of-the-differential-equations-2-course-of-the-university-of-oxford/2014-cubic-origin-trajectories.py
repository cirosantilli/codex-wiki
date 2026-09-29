"""Exact implicit trajectories of the cubic local approximation.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7, declared in
the repository pyproject.toml. Writes the matching PNG into the CWD.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radius = 0.32
    grid = np.linspace(-radius, radius, 240)
    xx, yy = np.meshgrid(grid, grid)
    u = xx * (xx**2 + yy**2)
    v = 2 * yy**3
    speed = np.maximum(np.hypot(u, v), 1.0e-20)

    fig, ax = plt.subplots(figsize=(6.4, 5.7), layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.streamplot(grid, grid, u / speed, v / speed, color="#aab6be",
                  density=1.15, linewidth=0.6, arrowsize=0.9, zorder=1)
    for constant in [-10, -6, -3, 3, 6, 10]:
        for ysign in [-1, 1]:
            y = ysign * np.linspace(1.0e-5, radius, 1200)
            denominator = 1 - constant * y
            valid = denominator > 0
            y = y[valid]
            x = np.abs(y) / np.sqrt(denominator[valid])
            valid = x <= radius
            for xsign in [-1, 1]:
                ax.plot(xsign * x[valid], y[valid], color="#1766a5",
                        alpha=0.82, lw=1.0, zorder=2)
    ax.plot(grid, grid, color="#c26513", lw=1.8, label="Diagonals: C=0", zorder=3)
    ax.plot(grid, -grid, color="#c26513", lw=1.8, zorder=3)
    ax.axhline(0, color="#303030", lw=1.1, label="Invariant axes", zorder=3)
    ax.axvline(0, color="#303030", lw=1.1, zorder=3)
    for direction in [-1, 1]:
        ax.annotate("", xy=(direction * 0.23, 0), xytext=(direction * 0.13, 0),
                    arrowprops={"arrowstyle": "-|>", "color": "#303030"})
        ax.annotate("", xy=(0, direction * 0.23), xytext=(0, direction * 0.13),
                    arrowprops={"arrowstyle": "-|>", "color": "#303030"})
    ax.scatter([0], [0], color="#b52225", s=38, zorder=5)
    ax.text(0.03, 0.96, "$x^2-y^2=Cx^2y$\nOrigin repels in forward time",
            transform=ax.transAxes, va="top", fontsize=10,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.92})
    ax.set(xlim=(-radius, radius), ylim=(-radius, radius), xlabel="x", ylabel="y",
           title="Cubic local approximation: trajectories and outward flow")
    ax.set_aspect("equal")
    ax.legend(loc="lower right", fontsize=9, framealpha=0.95)
    ax.grid(alpha=0.13)
    fig.savefig(Path("2014-cubic-origin-trajectories.png"), dpi=135, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
