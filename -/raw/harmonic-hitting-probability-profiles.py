"""Draw exact state values; run from _media to write the matching PNG.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "codex-wiki-matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    states = np.arange(5)
    fair = states / 4
    r = 2 / 3
    biased = (1 - r ** states) / (1 - r ** 4)
    duration = states * (4 - states)
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.6), dpi=120, facecolor="white")
    blue, orange, green = "#1769aa", "#b54b14", "#247044"
    for ax in (left, right):
        ax.set_facecolor("white")
        ax.set_xlim(-0.15, 4.15)
        ax.set_xticks(states)
        ax.set_xlabel(r"Starting state $i$")
        ax.grid(alpha=0.25)
        ax.spines[["top", "right"]].set_visible(False)
    left.plot(states, fair, "o--", color=blue, linewidth=1.8, markersize=6,
              label=r"Fair: $p=0.5$, $h_i=i/4$")
    left.plot(states, biased, "s-", color=orange, linewidth=1.8, markersize=6,
              label=r"Upward bias: $p=0.6$")
    left.set_title("Which endpoint?", fontsize=14, pad=10)
    left.set_ylabel(r"Success probability $h_i=\Pr_i(T_4<T_0)$")
    left.set_ylim(-0.04, 1.08)
    left.set_yticks([0, 0.25, 0.5, 0.75, 1])
    left.annotate(r"$h_2=9/13\approx0.6923$", (2, biased[2]), xytext=(0.4, 0.92),
                  color=orange, arrowprops={"arrowstyle": "->", "color": orange}, fontsize=11)
    left.legend(loc="lower right", fontsize=10, framealpha=1)
    right.plot(states, duration, "o-", color=green, linewidth=1.8, markersize=7)
    right.set_title("How many steps? (fair walk)", fontsize=14, pad=10)
    right.set_ylabel(r"Expected steps $t_i=\mathbb{E}_i T$")
    right.set_ylim(-0.15, 4.75)
    right.set_yticks([0, 1, 2, 3, 4])
    for i, value in enumerate(duration):
        right.annotate(str(value), (i, value), xytext=(0, 9), textcoords="offset points",
                       ha="center", color=green, fontsize=12)
    right.text(0.5, 0.17, r"$t_i=i(4-i)$", transform=right.transAxes,
               ha="center", color=green, fontsize=14)
    fig.suptitle("Absorption: probability and duration answer different questions", fontsize=15, y=0.97)
    fig.text(0.5, 0.035, "Dots are the five state values; connecting lines are visual guides. Endpoints are absorbing.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.97, top=0.81, bottom=0.17, wspace=0.36)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
