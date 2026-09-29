"""Draw monotone limit brackets and their exact errors; write the PNG to cwd.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    blue, orange, green = "#176ba0", "#b65320", "#277842"
    n = np.arange(1, 21)
    lower, upper = 1 - 1 / n, 1 + 1 / n
    assert np.all(np.diff(lower) > 0) and np.all(np.diff(upper) < 0)
    assert np.all(lower < 1) and np.all(upper > 1)
    assert np.all(np.abs(lower[n >= 6] - 1) < 0.2)
    assert np.all(np.abs(upper[n >= 6] - 1) < 0.2)

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.5), dpi=120,
                             facecolor="white")
    ax = axes[0]
    ax.axhspan(0.8, 1.2, color=green, alpha=0.12,
               label=r"Tolerance band: $1\pm0.2$")
    ax.axhline(1, color="#38444e", linestyle="--", linewidth=1.4,
               label=r"Common limit $L=1$")
    ax.plot(n, lower, "o-", color=blue, markersize=4.5,
            label=r"Increasing: $a_n=1-1/n$")
    ax.plot(n, upper, "o-", color=orange, markersize=4.5,
            label=r"Decreasing: $b_n=1+1/n$")
    ax.axvline(6, color=green, linestyle=":", linewidth=1.5)
    ax.text(6.3, 0.08, r"$n\geq6$: both errors $<0.2$", color=green,
            fontsize=10)
    ax.set(xlim=(0.5, 20.5), ylim=(-0.08, 2.1), xlabel="Index n",
           ylabel="Sequence value", title="Two directions, one limiting destination")
    ax.set_xticks([1, 6, 10, 15, 20])
    ax.legend(loc="upper right", fontsize=9, framealpha=1)

    m = np.arange(1, 17)
    reciprocal_error = 1 / m
    geometric_error = 2.0 ** (-m)
    ax = axes[1]
    ax.semilogy(m, reciprocal_error, "o-", color=blue, markersize=4.5,
                label=r"$|1-(1-1/n)|=1/n$")
    ax.semilogy(m, geometric_error, "s-", color=orange, markersize=4,
                label=r"$|1-(1-2^{-n})|=2^{-n}$")
    ax.axhline(0.01, color=green, linestyle="--", linewidth=1.2,
               label="Tolerance 0.01")
    ax.annotate(r"$n=7$: $2^{-7}<0.01$", xy=(7, 2.0 ** -7),
                xytext=(8, 0.0012), fontsize=10, color=orange,
                arrowprops={"arrowstyle": "->", "color": orange})
    ax.text(0.04, 0.07, r"$1/n<0.01$ first at $n=101$", color=blue,
            transform=ax.transAxes, fontsize=10)
    ax.set(xlim=(0.5, 16.5), ylim=(8e-6, 2), xlabel="Index n",
           ylabel="Absolute error (log scale)",
           title="Convergence can have very different speeds")
    ax.set_xticks([1, 4, 7, 10, 13, 16])
    ax.legend(loc="upper right", fontsize=9, framealpha=1)
    for ax in axes:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.2)
    fig.suptitle("Bounded monotone sequences: limiting brackets and exact errors",
                 fontsize=14, y=0.97)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.14, top=0.83,
                        wspace=0.28)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
