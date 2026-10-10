"""Draw five clockwise steps from nine modulo twelve.

Run from _media to write the PNG to CWD. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (distribution build 3.10.7+dfsg1).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(5.8, 5.5), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.14, top=0.85)
    theta = np.linspace(0, 2 * np.pi, 361)
    ax.plot(np.sin(theta), np.cos(theta), color="#d3d9df", linewidth=2)
    positions = np.arange(12)
    angles = positions * np.pi / 6
    xs, ys = np.sin(angles), np.cos(angles)
    steps = (9 + np.arange(6)) % 12
    for position in positions:
        active = position in steps
        color = "#18734d" if position == 2 else "#2462a0"
        ax.scatter(xs[position], ys[position], s=350,
                   color=color if active else "#edf0f3", zorder=3)
        ax.text(xs[position], ys[position], str(position), ha="center",
                va="center", color="white" if active else "#46515c",
                weight="bold", zorder=4)
    for start in range(9, 14):
        arc_angles = np.linspace(start * np.pi / 6 + 0.11,
                                 (start + 1) * np.pi / 6 - 0.11, 30)
        arc_x, arc_y = 0.82 * np.sin(arc_angles), 0.82 * np.cos(arc_angles)
        ax.plot(arc_x, arc_y, color="#2462a0", linewidth=2.5)
        ax.add_patch(FancyArrowPatch((arc_x[-4], arc_y[-4]),
                                     (arc_x[-1], arc_y[-1]),
                                     arrowstyle="-|>", mutation_scale=14,
                                     color="#2462a0", linewidth=2.5))
    ax.text(0, 0.14, "Five clockwise steps", ha="center", fontsize=13)
    ax.text(0, -0.13, r"$9+5=14\equiv2\ (\mathrm{mod}\ 12)$", ha="center", fontsize=16)
    ax.text(-1.35, 0, "Start", ha="center", va="center", color="#2462a0")
    ax.text(1.29, 0.52, "End", ha="center", va="center", color="#18734d")
    ax.set(xlim=(-1.6, 1.6), ylim=(-1.22, 1.22), aspect="equal")
    ax.axis("off")
    fig.suptitle("Clock addition modulo twelve", fontsize=16, y=0.96)
    fig.text(0.5, 0.065, "0 occupies the usual twelve-o'clock position",
             ha="center", color="#46515c", fontsize=11)
    fig.savefig(Path.cwd() / "modular-clock-addition.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
