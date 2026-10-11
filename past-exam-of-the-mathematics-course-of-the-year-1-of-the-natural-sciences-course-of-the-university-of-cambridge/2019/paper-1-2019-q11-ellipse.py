"""Original Q11 ellipse; Python 3.14, NumPy and Matplotlib from root pyproject.

Writes the PNG basename in the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 2*np.pi, 600)
    fig, ax = plt.subplots(figsize=(6.2, 3.9), layout="constrained")
    fig.set_facecolor("white")
    ax.plot(2*np.cos(t), 1+(2/3)*np.sin(t), color="#176b9b", lw=2)
    ax.axhline(0, color="0.5", lw=0.8)
    ax.axvline(0, color="0.5", lw=0.8)
    ax.scatter([0], [1], color="#b83c32", zorder=4)
    ax.annotate("centre $(0,1)$", (0, 1), xytext=(14, 12), textcoords="offset points")
    ax.scatter([-2, 2, 0, 0], [1, 1, 1/3, 5/3], s=18, color="#176b9b", zorder=4)
    ax.set(xlim=(-2.6, 2.6), ylim=(-0.2, 2.05), aspect="equal", xlabel="$\\mathrm{Re}\\,z$",
           ylabel="$\\mathrm{Im}\\,z$", title="$x^2+9(y-1)^2=4$")
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_yticks([0, 1/3, 1, 5/3, 2], ["0", "$1/3$", "1", "$5/3$", "2"])
    ax.grid(alpha=0.15)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
