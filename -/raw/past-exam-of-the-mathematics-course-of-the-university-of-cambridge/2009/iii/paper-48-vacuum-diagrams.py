"""Quartic vacuum diagrams; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Write the PNG basename to the caller CWD; honor the caller MPLCONFIGDIR.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def arc(ax, left, right, height):
    t = np.linspace(0, 1, 250)
    ax.plot(left + (right-left)*t, height*np.sin(np.pi*t),
            color="#176b9c", lw=2)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.1), dpi=100,
                             facecolor="white")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-1.45, 1.45)
        ax.set_ylim(-.9, .9)
        ax.axis("off")
    a = .65
    for x in (-a, a):
        for y in (-.27, .27):
            axes[0].add_patch(Circle((x, y), .27, fill=False,
                                    edgecolor="#176b9c", lw=2))
    for x, sign in ((-a, -1), (a, 1)):
        axes[1].add_patch(Circle((x + sign*.27, 0), .27, fill=False,
                                edgecolor="#176b9c", lw=2))
    for height in (-.32, .32):
        arc(axes[1], -a, a, height)
    for height in (-.55, -.18, .18, .55):
        arc(axes[2], -a, a, height)
    for ax, title, symmetry in zip(axes,
            ("Disconnected", "Two joining lines", "Four joining lines"),
            (128, 16, 48)):
        ax.plot([-a, a], [0, 0], "o", color="#222222", ms=7, zorder=5)
        ax.set_title(title, fontsize=13, pad=12)
        ax.text(0, -.78, rf"$S={symmetry}$", ha="center", fontsize=14)
    fig.subplots_adjust(left=.02, right=.98, bottom=.05, top=.90, wspace=.08)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False, dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    main()
