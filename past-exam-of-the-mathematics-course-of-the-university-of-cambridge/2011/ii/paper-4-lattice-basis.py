"""Allowed reduced planar lattice basis vectors; Python 3.14 and root deps.

The caller supplies MPLCONFIGDIR. Write only a basename PNG in cwd.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-0.5, 0.5, 500)
    edge = np.sqrt(1 - x * x)
    angle = np.linspace(0, 2 * np.pi, 600)
    fig, ax = plt.subplots(figsize=(7, 4.8), dpi=100, facecolor="white")
    ax.fill_between(x, edge, 2.0, color="#9ecae1", alpha=0.9)
    ax.fill_between(x, -2.0, -edge, color="#9ecae1", alpha=0.9)
    ax.plot(x, edge, color="#176a9a", linewidth=2)
    ax.plot(x, -edge, color="#176a9a", linewidth=2)
    for side in [-0.5, 0.5]:
        ax.plot([side, side], [np.sqrt(0.75), 2], color="#176a9a", linewidth=2)
        ax.plot([side, side], [-2, -np.sqrt(0.75)], color="#176a9a", linewidth=2)
    ax.plot(np.cos(angle), np.sin(angle), "--", color="#777777", linewidth=1)
    ax.axhline(0, color="#777777", linewidth=0.7)
    ax.axvline(0, color="#777777", linewidth=0.7)
    ax.plot([1], [0], "o", color="#a44211")
    ax.annotate(r"$w_1=(1,0)$", xy=(1, 0), xytext=(1.13, 0.28),
                arrowprops={"arrowstyle": "->"}, fontsize=11)
    ax.text(0, 1.45, r"Allowed $w_2$", ha="center", fontsize=12)
    ax.text(0, -1.45, r"Allowed $w_2$", ha="center", fontsize=12)
    ax.set_aspect("equal")
    ax.set_xlim(-1.35, 1.9)
    ax.set_ylim(-2, 2)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_title(r"$|x|\leq\frac{1}{2}$ and $x^2+y^2\geq1$; boundaries included")
    ax.grid(alpha=0.15)
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
