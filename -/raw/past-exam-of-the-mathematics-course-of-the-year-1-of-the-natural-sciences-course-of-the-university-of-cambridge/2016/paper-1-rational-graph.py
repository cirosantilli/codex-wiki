"""Original Q9 graph; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.9), width_ratios=[1.7, 1], layout="constrained")
    fig.patch.set_facecolor("white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.axhline(0, color="#888888", linewidth=0.7)
        ax.axvline(0, color="#888888", linewidth=0.7)
        ax.grid(alpha=0.18)
        ax.set(xlabel="$x$", ylabel="$y$")
        ax.spines[["top", "right"]].set_visible(False)
    for left, right in [(-5, -1.015), (-0.985, 4)]:
        x = np.linspace(left, right, 1200)
        axes[0].plot(x, x**3/(x**3+1), color="#17638d", linewidth=2.3)
    axes[0].axvline(-1, color="#b24c30", linestyle="--", linewidth=1.3, label="$x=-1$")
    axes[0].axhline(1, color="#80713b", linestyle="--", linewidth=1.3, label="$y=1$")
    axes[0].set(xlim=(-5, 4), ylim=(-4.5, 5), title=r"$y=x^3/(x^3+1)$")
    axes[0].legend(loc="lower right", fontsize=9)
    x = np.linspace(-0.55, 0.55, 500)
    axes[1].plot(x, x**3/(x**3+1), color="#17638d", linewidth=2.3)
    axes[1].set(xlim=(-0.55, 0.55), ylim=(-0.22, 0.2), title="Stationary inflection")
    for ax in axes:
        ax.scatter(0, 0, color="#b24c30", s=30, zorder=4)
    axes[1].annotate("(0, 0)", (0, 0), xytext=(12, -23), textcoords="offset points")
    fig.savefig(Path("paper-1-rational-graph.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
