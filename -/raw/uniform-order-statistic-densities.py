"""Exact minimum, median and maximum densities; opaque basename PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from math import factorial
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 5
    t = np.linspace(0, 1, 1201)
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.6, 5.3), dpi=110)
    for r, color, name, law, mean in [
        (1, "#246bce", "Minimum", "Beta(1,5)", "1/6"),
        (3, "#21845b", "Median", "Beta(3,3)", "1/2"),
        (5, "#ac5930", "Maximum", "Beta(5,1)", "5/6"),
    ]:
        density = factorial(n) / (factorial(r - 1) * factorial(n - r))
        density *= t ** (r - 1) * (1 - t) ** (n - r)
        ax.plot(t, density, color=color, linewidth=2.5,
                label=f"{name}, r={r}: {law}; mean {mean}")
    ax.set(xlim=(0, 1), ylim=(0, 5.3), xlabel="Order statistic value t",
           ylabel="Probability density", title="Five independent Uniform(0,1) observations")
    ax.set_xticks(np.linspace(0, 1, 6))
    ax.set_yticks(range(6))
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", fontsize=10, framealpha=0.95)
    ax.annotate(r"$30t^2(1-t)^2$", xy=(0.5, 1.875), xytext=(0.5, 2.5),
                ha="center", color="#21845b", arrowprops={"arrowstyle": "->", "color": "#21845b"})
    fig.text(0.5, 0.065, "Each curve has area 1. Density can exceed 1; endpoint probabilities are zero.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.10, right=0.97, bottom=0.20, top=0.89)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
