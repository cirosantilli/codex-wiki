"""Cubic one-loop two-point graph; Python 3.14 / matplotlib 3.10.7.

Write the PNG basename to the caller CWD; honor the caller MPLCONFIGDIR.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(5.6, 2.7), dpi=100, facecolor="white")
    ax.set_facecolor("white")
    t = np.linspace(0, 1, 300)
    for sign in (-1, 1):
        ax.plot(-.7 + 1.4*t, sign*.55*np.sin(np.pi*t), color="#176b9c", lw=2.2)
    ax.plot([-1.5, -.7], [0, 0], color="#333333", lw=2.2)
    ax.plot([.7, 1.5], [0, 0], color="#333333", lw=2.2)
    ax.plot([-.7, .7], [0, 0], "o", color="#222222", ms=7)
    ax.annotate("$p$", xy=(-.95, .10), xytext=(-1.40, .10),
                arrowprops=dict(arrowstyle="->", lw=1), fontsize=13)
    ax.annotate("$p$", xy=(1.40, .10), xytext=(.95, .10),
                arrowprops=dict(arrowstyle="->", lw=1), fontsize=13)
    ax.text(0, .64, "$k$", ha="center", fontsize=14)
    ax.text(0, -.80, "$k+p$", ha="center", fontsize=14)
    ax.set_title("Cubic two-point bubble: symmetry factor 2", fontsize=13, pad=15)
    ax.set_aspect("equal")
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.0, 1.0)
    ax.axis("off")
    fig.subplots_adjust(left=.03, right=.97, bottom=.03, top=.83)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
