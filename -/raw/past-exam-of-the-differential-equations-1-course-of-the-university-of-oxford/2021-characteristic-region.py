"""Oxford A1 (2021), Q1(b)(iii): run from the desired PNG output directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0.0, 1.8, 500)
    lower, upper = -x, 2 * x**2 - x
    fig, ax = plt.subplots(figsize=(6.4, 4.8), layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.fill_between(x, lower, upper, color="#e0effa", label="Region determined by the data")
    ax.plot(x, lower, color="#215a86", lw=2, label=r"$y=-x$ and $y=2x^2-x$")
    ax.plot(x, upper, color="#215a86", lw=2)
    for r in (-0.75, -0.4, 0.4, 0.75):
        y = (r + 1) * x**2 - x
        ax.plot(x, y, color="#8cb4cf", lw=0.9)
        x0, x1 = 1.25, 1.36
        ax.annotate("", (x1, (r + 1) * x1**2 - x1),
                    (x0, (r + 1) * x0**2 - x0),
                    arrowprops={"arrowstyle": "->", "color": "#527f9f", "lw": 1.2})
    ax.plot(x, x**2 - x, "--", color="#c94a30", lw=2, label=r"Corner: $y=x^2-x$")
    ax.plot([1, 1], [-1, 1], color="#202020", lw=3, label=r"Initial data: $x=1$, $-1\leq y\leq1$")
    ax.scatter([0], [0], facecolors="white", edgecolors="black", s=45, zorder=6)
    ax.annotate("Origin excluded", (0, 0), (0.12, 0.6), fontsize=9,
                arrowprops={"arrowstyle": "->", "lw": 0.8})
    ax.set(xlim=(-0.08, 1.86), ylim=(-2, 5), xlabel=r"$x$", ylabel=r"$y$",
           title=r"Characteristic region, $\beta=1$")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper left", fontsize=8.5, framealpha=1)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
