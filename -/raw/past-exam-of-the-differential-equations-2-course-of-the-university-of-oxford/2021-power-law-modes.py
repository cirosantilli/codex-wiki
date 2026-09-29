#!/usr/bin/env python3
"""Oxford A6 2021, Q3(b): exact sum and power-law contributions.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (repository dependencies).
Run in the output directory; writes 2021-power-law-modes.png there.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    eps = 0.08
    x = np.linspace(0.65, 4.0, 3201)
    fast = x ** (-1 / eps)
    xmin = eps ** (-eps / (1 + eps))
    ymin = (1 + eps) * xmin
    fig, ax = plt.subplots(figsize=(8.2, 4.2), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.plot(x, fast + x, color="#176aa5", lw=2, label=r"$y=x^{-1/\epsilon}+x$")
    ax.plot(x, fast, color="#b45224", ls="--", lw=1.6, label=r"$x^{-1/\epsilon}$")
    ax.plot(x, x, color="#555555", ls=":", lw=1.8, label="$x$")
    ax.scatter([1, xmin], [2, ymin], color="#176aa5", s=24, zorder=5)
    ax.annotate(r"$(1,2)$", (1, 2), xytext=(0.88, 3.5), fontsize=10,
                arrowprops={"arrowstyle": "->"})
    ax.annotate("minimum", (xmin, ymin), xytext=(1.50, 0.53), fontsize=10,
                arrowprops={"arrowstyle": "->"})
    ax.annotate(r"$y\to\infty$ as $x\to0^+$", (0.83, 10),
                xytext=(1.12, 8.8), fontsize=10,
                arrowprops={"arrowstyle": "->"})
    ax.set(xlim=(0.65, 4), ylim=(0, 11), xlabel="$x$", ylabel="$y$",
           title=rf"Exact solution, $\epsilon={eps}$")
    ax.legend(loc="upper right", fontsize=10)
    ax.grid(alpha=0.16)
    ax.spines[["top", "right"]].set_visible(False)
    inset = ax.inset_axes([0.50, 0.35, 0.46, 0.36])
    z = np.linspace(0.94, 1.42, 801)
    inset.plot(z, z + z ** (-1 / eps), color="#176aa5", lw=1.7)
    inset.plot(z, z ** (-1 / eps), color="#b45224", ls="--", lw=1.2)
    inset.plot(z, z, color="#555555", ls=":", lw=1.5)
    inset.axvline(1, color="#aaaaaa", lw=0.7)
    inset.scatter([xmin], [ymin], color="#176aa5", s=18)
    inset.set(xlim=(0.94, 1.42), ylim=(0, 3.5), title="Crossover near $x=1$")
    inset.tick_params(labelsize=8)
    inset.title.set_fontsize(9)
    inset.grid(alpha=0.12)
    fig.savefig(Path("2021-power-law-modes.png"), dpi=115,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
