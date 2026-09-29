"""Original Q5 sketch; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1, 1, 600)
    fig, ax = plt.subplots(figsize=(6.4, 4), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.plot(x, 1 - x*x, color="#17638d", linewidth=2.4)
    ax.plot(x, x*x - 1, color="#17638d", linewidth=2.4)
    ax.axhline(0, color="#888888", linewidth=0.7)
    ax.axvline(0, color="#888888", linewidth=0.7)
    ax.axhline(0.5, color="#b24c30", linestyle="--", label="$y=1/2$")
    ax.scatter([-1/np.sqrt(2), 1/np.sqrt(2)], [0.5, 0.5], color="#b24c30", s=35, zorder=5)
    ax.scatter([-1, 1, 0, 0], [0, 0, 1, -1], color="#17638d", s=20)
    ax.set(xlim=(-1.3, 1.3), ylim=(-1.25, 1.25), xlabel="$x$", ylabel="$y$", title=r"$|y|=1-x^2$")
    ax.set_aspect("equal")
    ax.grid(alpha=0.18)
    ax.legend(loc="lower right")
    fig.savefig(Path("paper-1-absolute-value.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
