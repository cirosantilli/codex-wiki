"""Original integration-region sketch; Python 3.14, root NumPy/Matplotlib deps.

The PNG basename is written in the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 4.3, 400)
    fig, ax = plt.subplots(figsize=(6.0, 4.6), layout="constrained")
    fig.set_facecolor("white")
    ax.fill_between(x, x/2, x, color="#e0edf2")
    ax.plot(x, x, color="#176b9b", lw=1.8)
    ax.plot(x, x/2, color="#176b9b", lw=1.8)
    ax.plot([1.5, 1.5], [0.75, 1.5], color="#b83c32", lw=3)
    ax.plot([1.8, 3.6], [1.8, 1.8], color="#567e3c", lw=3)
    ax.annotate("$x/2\\leq y\\leq x$", (1.5, 1.1), xytext=(0.3, 2.4),
                arrowprops={"arrowstyle": "->", "lw": 0.9}, color="#b83c32")
    ax.annotate("$y\\leq x\\leq 2y$", (2.7, 1.8), xytext=(2.45, 0.9),
                arrowprops={"arrowstyle": "->", "lw": 0.9}, color="#567e3c")
    ax.text(2.75, 3.1, "$y=x$", color="#176b9b")
    ax.text(3.2, 1.42, "$y=x/2$", color="#176b9b")
    ax.text(3.25, 2.4, "$D$", fontsize=16)
    ax.axhline(0, color="0.35", lw=0.9)
    ax.axvline(0, color="0.35", lw=0.9)
    ax.set(xlim=(-0.1, 4.1), ylim=(-0.1, 3.7), aspect="equal", xlabel="$x$", ylabel="$y$",
           title="Unbounded wedge and two orders of slicing")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.13)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
