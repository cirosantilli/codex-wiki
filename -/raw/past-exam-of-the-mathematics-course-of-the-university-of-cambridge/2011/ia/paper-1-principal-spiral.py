"""Principal-power spiral. Tested with Python 3.14.4 and root NumPy/Matplotlib.

Write an opaque basename PNG to cwd; preserve the caller's MPLCONFIGDIR.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(-np.pi, np.pi, 2401)
    radius = np.exp(theta)
    x, y = radius * np.cos(theta), radius * np.sin(theta)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), dpi=100, facecolor="white")
    for ax in axes:
        ax.plot(x, y, color="#176a9a", linewidth=2.3)
        ax.axhline(0, color="#888888", linewidth=0.7)
        ax.axvline(0, color="#888888", linewidth=0.7)
        ax.set_aspect("equal")
        ax.set_xlabel(r"$\operatorname{Re}z$")
        ax.set_ylabel(r"$\operatorname{Im}z$")
        ax.grid(alpha=0.18)
    axes[0].set_xlim(-25, 8)
    axes[0].set_ylim(-9, 19)
    axes[0].set_title("Complete principal branch")
    axes[0].plot([-np.exp(np.pi)], [0], "o", color="#176a9a", markersize=7)
    axes[0].annotate(r"Included: $-e^{\pi}$", xy=(-np.exp(np.pi), 0),
                     xytext=(-23, -6), arrowprops={"arrowstyle": "->"}, fontsize=11)
    axes[0].annotate("", xy=(x[1900], y[1900]), xytext=(x[1800], y[1800]),
                     arrowprops={"arrowstyle": "->", "color": "#176a9a", "lw": 2})
    axes[1].set_xlim(-0.4, 1.6)
    axes[1].set_ylim(-1, 1.7)
    axes[1].set_title("Inner endpoint and passage through 1")
    axes[1].plot([-np.exp(-np.pi)], [0], "o", markerfacecolor="white",
                 markeredgecolor="#176a9a", markeredgewidth=1.8, markersize=7)
    axes[1].plot([1], [0], "o", color="#176a9a", markersize=5)
    axes[1].annotate(r"Excluded: $-e^{-\pi}$", xy=(-np.exp(-np.pi), 0),
                     xytext=(-0.3, 0.85), arrowprops={"arrowstyle": "->"}, fontsize=11)
    axes[1].annotate(r"$\theta=0$", xy=(1, 0), xytext=(1.07, -0.43),
                     arrowprops={"arrowstyle": "->"}, fontsize=11)
    fig.suptitle(r"$|z^{1+i}|=1$: $r=e^{\theta}$, $-\pi<\theta\leq\pi$", fontsize=16)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
