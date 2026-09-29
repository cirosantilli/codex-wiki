"""Illustrate polynomial approximation of a continuous corner.

Run from the media output directory; the PNG uses this script's basename.
Tested with the Python, NumPy and Matplotlib versions in pyproject.toml.
"""

from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def bernstein_corner(x, n):
    """Evaluate the finite Bernstein sum, including both endpoints."""
    return sum(
        abs(k / n - 0.5) * comb(n, k) * x**k * (1 - x) ** (n - k)
        for k in range(n + 1)
    )


def main():
    x = np.linspace(0, 1, 1601)
    fig, ax = plt.subplots(figsize=(8.6, 4.6), dpi=125, layout="constrained")
    fig.set_facecolor("white")
    ax.plot(x, abs(x - 0.5), color="black", linewidth=2.5, label=r"Target $|x-1/2|$")
    for n, color in zip((2, 10, 50, 200), ("#cc6677", "#e69f00", "#0072b2", "#009e73")):
        ax.plot(x, bernstein_corner(x, n), color=color, linewidth=1.9, label=rf"$B_{{{n}}}f$")
    ax.scatter([0.5], [0.25], s=35, color="#cc6677", zorder=5)
    ax.annotate(r"$B_2f(1/2)=1/4$", xy=(0.5, 0.25), xytext=(0.60, 0.31),
                arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=11)
    ax.set(xlim=(0, 1), ylim=(-0.015, 0.535), xlabel=r"$x$", ylabel="Function value",
           title="Smooth polynomials can approach a continuous corner")
    ax.grid(alpha=0.22)
    ax.legend(loc="upper center", fontsize=10, ncol=3)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
