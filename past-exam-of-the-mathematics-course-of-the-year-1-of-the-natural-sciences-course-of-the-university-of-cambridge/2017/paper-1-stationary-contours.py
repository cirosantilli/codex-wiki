"""Original Q14 contours, labelled by log(f); write the PNG to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    grid = np.linspace(-2, 2, 501)
    x, y = np.meshgrid(grid, grid)
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.6), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax, a in zip(axes, [1, -1]):
        ax.set_facecolor("white")
        g = (x * x + y * y) / 2 + a * x**4 / 4
        levels = [0.05, 0.125, 0.25, 0.5, 1, 2, 3] if a == 1 else [-0.5, 0, 0.1, 0.25, 0.5, 1, 2]
        contours = ax.contour(x, y, g, levels=levels, cmap="viridis", linewidths=1.2)
        ax.clabel(contours, fmt="%g", fontsize=8)
        if a == -1:
            ax.contour(x, y, g, levels=[0.25], colors=["#ba4035"], linewidths=1.8)
            ax.scatter([-1, 1], [0, 0], color="#ba4035", marker="x", s=55, linewidth=2, zorder=5, label="Saddles")
        ax.scatter(0, 0, color="#247045", s=32, zorder=5, label="Minimum")
        ax.set(xlim=(-2, 2), ylim=(-2, 2), xlabel="$x$", ylabel="$y$", title=f"$a={a}$")
        ax.set_aspect("equal")
        ax.grid(alpha=0.13)
        ax.legend(loc="lower left", fontsize=8, framealpha=0.95)
    fig.suptitle(r"Contours of $f$: numbers denote $\log f=(x^2+y^2)/2+ax^4/4$")
    fig.savefig(Path("paper-1-stationary-contours.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
