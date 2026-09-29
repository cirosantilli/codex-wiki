"""Plot pointwise convergence and exact uniform error bounds for x**n.

Run from the desired output directory; writes pointwise-uniform-convergence.png.
Dependencies: NumPy and Matplotlib from the root pyproject.toml.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.4), dpi=130,
                             constrained_layout=True)
    fig.patch.set_facecolor("white")
    x = np.linspace(0, 1, 1601)
    colors = ["#2964a3", "#279078", "#c28b18", "#a64d79"]
    for n, color in zip((1, 5, 20, 100), colors):
        axes[0].plot(x, x**n, color=color, lw=2, label=f"n = {n}")
    axes[0].plot([0, 1], [0, 0], color="#252525", ls="--", lw=2,
                 label="pointwise limit")
    axes[0].scatter([1], [0], facecolors="white", edgecolors="#252525",
                    s=60, zorder=8)
    axes[0].scatter([1], [1], color="#252525", s=40, zorder=8)
    axes[0].axvline(.8, color="#777777", lw=1.4, ls=":")
    axes[0].text(.775, .57, "a = 0.8", rotation=90, ha="right", color="#555555")
    axes[0].set(xlim=(0, 1.035), ylim=(-.055, 1.08), xlabel="x",
                ylabel=r"$f_n(x)=x^n$", title="Each fixed x converges; near 1, error persists")
    axes[0].legend(loc="upper left", fontsize=9, framealpha=1)

    n = np.arange(1, 41)
    axes[1].semilogy(n, np.ones_like(n), color="#a64d79", lw=2.3,
                     label=r"on $[0,1]$: error supremum = 1")
    axes[1].semilogy(n, .8**n, color="#2964a3", lw=2.6,
                     label=r"on $[0,0.8]$: error maximum = $0.8^n$")
    axes[1].axhline(.01, color="#777777", ls="--", lw=1.5,
                    label="tolerance 0.01")
    axes[1].scatter([20], [.8**20], color="#2964a3", zorder=5)
    axes[1].annotate("n = 20: 0.011529215…\nn = 21 meets tolerance",
                     xy=(20, .8**20), xytext=(4, .0007), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#555555"},
                     bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95})
    axes[1].set(xlim=(1, 40), ylim=(.0001, 1.5), xlabel="n",
                ylabel=r"worst error $\sup_x|f_n(x)-f(x)|$ (log scale)",
                title="Restricting the domain gives a uniform bound")
    axes[1].legend(loc="upper right", fontsize=9, framealpha=1)
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=.18)
    fig.savefig(Path.cwd() / "pointwise-uniform-convergence.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
