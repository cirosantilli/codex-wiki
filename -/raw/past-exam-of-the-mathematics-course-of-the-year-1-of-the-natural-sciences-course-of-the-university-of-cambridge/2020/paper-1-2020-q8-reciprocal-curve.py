"""Original Q8 sketch; Python 3.14, NumPy and Matplotlib (root pyproject.toml).

Write the PNG basename in the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(7.2, 4.4), layout="constrained")
    fig.set_facecolor("white")
    x = np.linspace(0.2, 8.0, 1500)
    ax.plot(x, x**-2 - x**-1, color="#176b9b", lw=2.2)
    ax.axhline(0, color="0.3", lw=0.9)
    ax.axvline(0, color="0.3", lw=0.9)
    ax.scatter([1, 2], [0, -0.25], color=["#176b9b", "#b83c32"], zorder=5)
    ax.annotate("$(1,0)$", (1, 0), xytext=(15, 12), textcoords="offset points")
    ax.annotate("minimum $(2,-1/4)$", (2, -0.25), xytext=(35, -18),
                textcoords="offset points", arrowprops={"arrowstyle": "->"})
    ax.annotate("$y\\to+\\infty$", (0.49, 2.12), xytext=(0.95, 1.55),
                arrowprops={"arrowstyle": "->"})
    ax.text(5.5, 0.09, "$y\\to0$ from below", fontsize=11)
    ax.set(xlim=(-0.1, 8.0), ylim=(-0.48, 2.2), xlabel="$x$", ylabel="$y$",
           title="$y=x^{-2}-x^{-1}$ for $x>0$")
    ax.grid(alpha=0.16)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
