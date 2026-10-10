"""Compare a free C2 action on four points with a trivial C2 action.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
C2's two abstract elements remain distinct even in the trivial action.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch
import numpy as np


def check_c2_action(action):
    assert action[0] == tuple(range(4))
    for g in range(2):
        for h in range(2):
            for x in range(4):
                assert action[g][action[h][x]] == action[(g + h) % 2][x]
    orbits = sorted({tuple(sorted({action[g][x] for g in range(2)})) for x in range(4)})
    stabilizers = [[g for g in range(2) if action[g][x] == x] for x in range(4)]
    transports = [[sum(action[g][x] == y for g in range(2)) for y in range(4)] for x in range(4)]
    assert all(len({action[g][x] for g in range(2)}) * len(stabilizers[x]) == 2 for x in range(4))
    return orbits, stabilizers, transports


def loop(ax, point, color, side):
    x, y = point
    angles = np.linspace(-2.5, 2.5, 80) if side == 1 else np.linspace(-0.6, 5.4, 80)
    center = np.array([x + side * 0.23, y + 0.22])
    curve = center[:, None] + 0.18 * np.array([np.cos(angles), np.sin(angles)])
    ax.plot(*curve, color=color, lw=1.8)
    ax.add_patch(FancyArrowPatch(curve[:, -5], curve[:, -1], arrowstyle="-|>",
                                color=color, mutation_scale=12, lw=1.8))


def main():
    free = [(0, 1, 2, 3), (1, 0, 3, 2)]
    trivial = [(0, 1, 2, 3), (0, 1, 2, 3)]
    fo, fs, ft = check_c2_action(free)
    to, ts, tt = check_c2_action(trivial)
    assert fo == [(0, 1), (2, 3)] and to == [(0,), (1,), (2,), (3,)]
    assert fs == [[0]] * 4 and ts == [[0, 1]] * 4
    assert ft == [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    assert tt == [[2 if i == j else 0 for j in range(4)] for i in range(4)]

    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.5), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.17, top=0.85, wspace=0.1)
    blue, gray = "#2166ac", "#737c86"
    points = np.array([[-0.72, 0.54], [0.72, 0.54], [-0.72, -0.55], [0.72, -0.55]])
    for ax, title in zip(axes, ["Two pairs exchanged", "Every point fixed"]):
        ax.set(xlim=(-1.55, 1.55), ylim=(-2.0, 1.65), aspect="equal")
        ax.axis("off")
        ax.text(0, 1.48, title, ha="center", fontsize=16, weight="bold")
    for y in (0.54, -0.55):
        axes[0].add_patch(Ellipse((0, y), 2.34, 0.94, edgecolor="#a9c7a1", facecolor="#f5faf3", lw=1.5))
    for i, p in enumerate(points):
        axes[1].add_patch(Ellipse(p, 1.02, 0.90, edgecolor="#a9c7a1", facecolor="#f5faf3", lw=1.5))
        for ax in axes:
            loop(ax, p, gray, side=1)
            ax.add_patch(Circle(p, 0.15, facecolor="white", edgecolor="#243444", lw=2, zorder=5))
            ax.text(*p, str(i + 1), ha="center", va="center", fontsize=15, zorder=6)
        loop(axes[1], p, blue, side=-1)
    for i, j in [(0, 1), (2, 3)]:
        axes[0].add_patch(FancyArrowPatch(points[i], points[j], arrowstyle="<|-|>",
                                         shrinkA=18, shrinkB=18, color=blue,
                                         mutation_scale=17, lw=2.3))
        axes[0].text(0, points[i, 1] - 0.22, r"$a$", color=blue, ha="center", fontsize=15)
    axes[0].text(0, -1.50, "Two orbits of size 2\nFree, not transitive", ha="center", fontsize=13)
    axes[1].text(0, -1.50, "Four singleton orbits\nNeither free nor transitive", ha="center", fontsize=13)
    fig.suptitle(r"Two different actions of $C_2=\{e,a\}$ on four points", y=0.96, fontsize=17)
    fig.text(0.5, 0.085, "Blue arrows: a.  Gray loops: e.  Green outlines: orbits.", ha="center")
    fig.text(0.5, 0.035, r"Left: $G_x=\{e\}$ for all $x$.  Right: $G_x=\{e,a\}$ for all $x$.", ha="center", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
