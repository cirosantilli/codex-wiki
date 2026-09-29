"""Display a bounded sequence with two distinct subsequential limits.

The terms are exact stipulated formulas, not experimental observations.
Run in the output directory; package versions are in pyproject.toml.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def verify():
    for n in range(1, 1001):
        x = Fraction((-1) ** n) + Fraction(1, n + 1)
        assert -1 < x < 2
        assert abs(x - (-1) ** n) == Fraction(1, n + 1)


def main():
    verify()
    n = np.arange(1, 61)
    x = (-1.0) ** n + 1 / (n + 1)
    fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=125, layout="constrained")
    fig.set_facecolor("white")
    for even, color, label in ((True, "#0072b2", "Even indices: limit +1"),
                                (False, "#d55e00", "Odd indices: limit -1")):
        choose = (n % 2 == 0) == even
        ax.vlines(n[choose], 0, x[choose], color=color, alpha=0.28, linewidth=1)
        ax.scatter(n[choose], x[choose], s=22, color=color, label=label, zorder=4)
    ax.axhline(1, color="#0072b2", linestyle="--", linewidth=1.6)
    ax.axhline(-1, color="#d55e00", linestyle="--", linewidth=1.6)
    ax.axhline(0, color="#888888", linewidth=0.6)
    ax.set(xlim=(0, 61), ylim=(-1.16, 1.62), xlabel=r"Original index $n$", ylabel=r"$x_n$",
           title=r"$x_n=(-1)^n+1/(n+1)$: bounded, but not convergent")
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(alpha=0.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
