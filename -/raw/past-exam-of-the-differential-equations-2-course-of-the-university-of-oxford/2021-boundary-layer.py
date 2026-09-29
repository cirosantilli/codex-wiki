#!/usr/bin/env python3
"""Oxford A6 2021, Q3(c): leading composite and inner approximations.

Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (repository dependencies).
These are asymptotic profiles, not numerical or exact BVP solutions.
Run in the output directory; writes 2021-boundary-layer.png there.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(1, 2, 2401)
    fig, ax = plt.subplots(figsize=(8.2, 4.2), layout="constrained")
    fig.patch.set_facecolor("white")
    outer = np.exp(x - 1)
    for eps, color in [(0.04, "#176aa5"), (0.08, "#b45224")]:
        composite = outer - np.e * np.exp(-2 * (2 - x) / eps)
        ax.plot(x, composite, color=color, lw=2,
                label=rf"composite, $\epsilon={eps}$")
    ax.plot(x, outer, color="#555555", lw=1.6, ls="--", label="outer")
    ax.scatter([1, 2], [1, 0], color="#222222", s=24, zorder=5)
    ax.annotate("right boundary layer", (1.985, 0.85), xytext=(1.60, 0.50),
                fontsize=10, arrowprops={"arrowstyle": "->"})
    ax.set(xlim=(1, 2), ylim=(-0.05, 2.95), xlabel="$x$", ylabel="leading approximation")
    ax.grid(alpha=0.16)
    ax.legend(loc="upper left", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    inset = ax.inset_axes([0.17, 0.15, 0.35, 0.24])
    X = np.linspace(0, 3.5, 501)
    inset.plot(X, np.e * (1 - np.exp(-2 * X)), color="#3a7d44", lw=1.7)
    inset.axhline(np.e, color="#555555", ls="--", lw=0.9)
    inset.set(xlim=(0, 3.5), ylim=(0, 2.95), xlabel=r"$X=(2-x)/\epsilon$",
              title=r"Inner: $e(1-e^{-2X})$")
    inset.set_yticks([0, np.e], ["0", "$e$"])
    inset.tick_params(labelsize=8)
    inset.xaxis.label.set_fontsize(9)
    inset.title.set_fontsize(9)
    inset.grid(alpha=0.12)
    fig.savefig(Path("2021-boundary-layer.png"), dpi=115,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
