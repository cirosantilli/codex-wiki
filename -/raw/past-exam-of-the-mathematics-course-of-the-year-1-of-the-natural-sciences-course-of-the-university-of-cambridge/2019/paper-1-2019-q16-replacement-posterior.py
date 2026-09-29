"""Original posterior curves; Python 3.14, NumPy and Matplotlib from root pyproject.

Writes the PNG basename in the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    r = np.linspace(0, 1, 500)
    fig, ax = plt.subplots(figsize=(5.8, 4.4), layout="constrained")
    fig.set_facecolor("white")
    ax.plot(r, r, "--", color="0.4", label="prior $r$")
    for n, color in [(4, "#176b9b"), (8, "#b83c32"), (20, "#528353")]:
        ax.plot(r, r*(n-1)/(n-r), color=color, lw=2, label=f"posterior, $N={n}$")
    ax.scatter([0, 1], [0, 1], color="0.2", s=22, zorder=5)
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="replacement probability $r$",
           ylabel="$P(R\\mid\\overline{B}_1\\cap B_2)$",
           title="Two different colours favour no replacement")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.16)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
