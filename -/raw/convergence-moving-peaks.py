"""Plot shrinking continuous tents with fixed integral one half.

Run from the desired output directory; writes convergence-moving-peaks.png.
Dependencies: NumPy and Matplotlib from the root pyproject.toml.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def tent(x, n):
    """Height n, support [0, 1/n], peak at 1/(2*n)."""
    x = np.asarray(x)
    return np.maximum(0, n - 2*n*n*np.abs(x - 1/(2*n)))


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3), dpi=130,
                             constrained_layout=True)
    fig.patch.set_facecolor("white")
    colors = ["#2964a3", "#279078", "#c28b18", "#a64d79"]
    for n, color in zip((1, 2, 4, 8), colors):
        # Include the vertices exactly: resolution must not miss the peaks.
        x = np.array([0, 1/(2*n), 1/n, 1.0])
        axes[0].plot(x, tent(x, n), lw=2.3, color=color, label=f"n = {n}")
        axes[0].fill_between(x, tent(x, n), color=color, alpha=.07)
    axes[0].plot([0, 1], [0, 0], ls="--", color="#252525", lw=2,
                 label="pointwise limit = 0")
    axes[0].set(xlim=(-.015, 1.025), ylim=(-.25, 8.55), xlabel="x",
                ylabel=r"$g_n(x)$", title="Narrower tents get taller: area stays 1/2")
    axes[0].legend(loc="upper right", fontsize=9, framealpha=1)
    axes[0].text(.40, 3.45, "width = 1/n\nheight = n\narea = (1/2)(1/n)n", fontsize=11,
                 bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95})

    n = np.arange(1, 17)
    axes[1].plot(n, tent(.2, n), "o-", lw=2, ms=4, color="#2964a3",
                 label=r"fixed input $x=0.2$: $g_n(x)$")
    axes[1].plot(n, tent(1/(2*n), n), "o-", lw=2, ms=4, color="#a64d79",
                 label=r"moving input $x_n=1/(2n)$: $g_n(x_n)=n$")
    axes[1].set(xlim=(.5, 16.5), ylim=(-.5, 17), xlabel="n", ylabel="value",
                title="Pointwise control misses a moving peak")
    axes[1].legend(loc="upper left", fontsize=9, framealpha=1)
    axes[1].text(5.7, 3.1, "At every fixed x > 0,\nthe tent is eventually zero.\nAt x = 0, it is always zero.",
                 fontsize=10, bbox={"facecolor": "white", "edgecolor": "none", "alpha": .95})
    for ax in axes:
        ax.set_facecolor("white")
        ax.grid(alpha=.18)
    fig.savefig(Path.cwd() / "convergence-moving-peaks.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
