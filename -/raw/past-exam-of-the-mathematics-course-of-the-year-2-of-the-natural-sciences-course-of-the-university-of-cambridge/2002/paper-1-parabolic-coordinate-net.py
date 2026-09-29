"""Requested parabolic coordinate levels; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from the desired output directory; the PNG is written in the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(7.4, 6.1), dpi=120, layout="constrained")
    y = np.linspace(-5.5, 5.5, 1200)
    for c, style in [(1, "-"), (2, "--")]:
        ax.plot(c - y*y/(4*c), y, style, color="#1674a5", lw=1.8, label=rf"$u^2={c}$")
        ax.plot(y*y/(4*c) - c, y, style, color="#c96522", lw=1.8, label=rf"$v^2={c}$")
    ax.plot([-4.7, 0], [0, 0], color="#1674a5", lw=3.4, label=r"$u^2=0$")
    ax.plot([0, 4.7], [0, 0], color="#c96522", lw=3.4, label=r"$v^2=0$")
    ax.scatter([0], [0], color="black", s=25, zorder=5)
    ax.annotate("Common focus", (0, 0), (0.25, 0.6), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "0.3"})
    for c in [1, 2]:
        ax.scatter([c, -c], [0, 0], color=["#1674a5", "#c96522"], s=22, zorder=5)
    ax.axvline(0, color="0.65", lw=0.7, zorder=0)
    ax.set(xlim=(-4.7, 4.7), ylim=(-4.7, 4.7), xlabel="$x$", ylabel="$y$",
           title="Confocal orthogonal parabolas")
    ax.set_aspect("equal")
    ax.grid(alpha=0.15)
    ax.legend(loc="upper center", ncol=3, fontsize=10, framealpha=0.95)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
