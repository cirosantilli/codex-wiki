"""Original mutual-repression phase planes; writes basename PNG to caller CWD."""
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def symmetric_root(lam):
    low, high = 0.0, lam
    for _ in range(80):
        middle = (low + high) / 2
        if middle * (1 + middle) ** 2 < lam:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def panel(ax, lam, title):
    grid = np.linspace(0, 3.6, 24)
    x, y = np.meshgrid(grid, grid)
    dx, dy = lam / (1 + y) ** 2 - x, lam / (1 + x) ** 2 - y
    ax.streamplot(grid, grid, dx, dy, color="#b5bfc7", density=.8, linewidth=.8, arrowsize=.8)
    yy = np.linspace(0, 3.6, 700)
    ax.plot(lam / (1 + yy) ** 2, yy, color="#256e9b", lw=2, label=r"$\dot x=0$")
    ax.plot(yy, lam / (1 + yy) ** 2, color="#c97632", lw=2, label=r"$\dot y=0$")
    r = symmetric_root(lam)
    if lam > 4:
        small = (lam - 2 - math.sqrt((lam - 2) ** 2 - 4)) / 2
        large = 1 / small
        ax.plot([0, 3.6], [0, 3.6], "--", color="#667488", lw=1, label="stable separatrix")
        ax.scatter([small, large], [large, small], s=70, color="#327644", zorder=4, label="stable equilibria")
        ax.scatter([r], [r], s=80, marker="X", color="#9b3944", zorder=5, label="saddle")
    else:
        ax.scatter([r], [r], s=70, color="#327644", zorder=4, label="stable equilibrium")
    ax.set(xlim=(0, 3.6), ylim=(0, 3.6), xlabel=r"$x$", ylabel=r"$y$", title=title)
    ax.set_aspect("equal")
    ax.legend(fontsize=8, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.8), constrained_layout=True, facecolor="white")
    panel(axes[0], 2, r"One stable state: $m=n=2,\ \lambda=2$")
    panel(axes[1], 5, r"Two stable states: $m=n=2,\ \lambda=5$")
    fig.suptitle("Mutual repression: nullclines and flow", fontsize=15)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
