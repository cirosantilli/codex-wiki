#!/usr/bin/env python3
"""Oxford A6 2021, Q3(a): original rational-function sketch.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (repository dependencies).
Run in the output directory; writes 2021-roots.png to the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    eps = 0.15
    small = 2 * eps / (1 + np.sqrt(1 - 4 * eps**2))
    large = 1 / small
    x = np.linspace(-8, 10, 2401)
    fig, ax = plt.subplots(figsize=(8.2, 4.0), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.plot(x, x / (1 + x**2), color="#176aa5", lw=2,
            label=r"$F(x)=x/(1+x^2)$")
    ax.axhline(0, color="#888888", lw=0.8)
    ax.axvline(0, color="#888888", lw=0.8)
    ax.axhline(eps, color="#b45224", ls="--", lw=1.4,
               label=rf"$\epsilon={eps}$")
    ax.scatter([small, large], [eps, eps], color="#b45224", zorder=5)
    ax.scatter([-1, 1], [-0.5, 0.5], color="#176aa5", zorder=5)
    for root, label, offset in [(small, r"$x_-$", (15, -30)),
                                 (large, r"$x_+$", (10, 15))]:
        ax.annotate(label, (root, eps), xytext=offset,
                    textcoords="offset points", fontsize=12,
                    arrowprops={"arrowstyle": "->", "color": "#b45224"})
    ax.annotate(r"$(-1,-1/2)$", (-1, -0.5), xytext=(-85, 18),
                textcoords="offset points", fontsize=10,
                arrowprops={"arrowstyle": "->"})
    ax.annotate(r"$(1,1/2)$", (1, 0.5), xytext=(38, -5),
                textcoords="offset points", fontsize=10,
                arrowprops={"arrowstyle": "->"})
    ax.set(xlim=(-8, 10), ylim=(-0.61, 0.65), xlabel="$x$", ylabel="$F(x)$")
    ax.grid(alpha=0.16)
    ax.legend(loc="upper right", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path("2021-roots.png"), dpi=115,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
