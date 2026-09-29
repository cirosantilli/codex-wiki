"""Compare exact unit-mesh sums with an integral; run from the output directory.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


def main():
    n = 6
    integral = Fraction(n**3, 3)
    left = sum(k**2 for k in range(n))
    right = sum(k**2 for k in range(1, n + 1))
    assert (integral, left, right) == (72, 55, 91)
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.4), layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("Discrete square sums versus smooth area", fontsize=17)
    x = np.linspace(0, n, 601)
    for ax, sample, value, sign in zip(axes, (np.arange(n), np.arange(1, n + 1)),
                                      (left, right), ("−", "+")):
        ax.set_facecolor("white")
        ax.fill_between(x, 0, x**2, color="#e6e9ee", zorder=0)
        ax.bar(np.arange(n), sample**2, width=1, align="edge", color="#82bddf",
               alpha=0.65, edgecolor="#1a5a7c", linewidth=1.0)
        ax.plot(x, x**2, color="#bc493c", linewidth=2.5, zorder=3)
        ax.scatter(sample, sample**2, color="#1a5a7c", s=30, zorder=4)
        ax.set(xlim=(-0.12, 6.15), ylim=(0, 40), xticks=range(7),
               yticks=(0, 10, 20, 30, 36), xlabel="$x$", ylabel="$x^2$")
        ax.set_title(("Left endpoints: 0, …, 5" if sign == "−"
                      else "Right endpoints: 1, …, 6"), fontsize=13)
        ax.text(0.04, 0.89, f"Rectangle area = {value}\nIntegral area = 72",
                transform=ax.transAxes, va="top", fontsize=12,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.93})
        ax.text(0.5, -0.22, f"72 {sign} 18 + 1 = {value}", transform=ax.transAxes,
                ha="center", fontsize=15, fontweight="bold")
    fig.legend(handles=[Patch(facecolor="#82bddf", edgecolor="#1a5a7c",
                              label="Unit-width rectangles"),
                        plt.Line2D([], [], color="#bc493c", linewidth=2.5,
                                   label="Smooth curve $x^2$")],
               loc="outside lower center", ncols=2, frameon=False)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
