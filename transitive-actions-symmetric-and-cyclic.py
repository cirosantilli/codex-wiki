"""Compare S3's natural action with C3's regular action.

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
The arrows show named generators; products give the rest of each action.
"""

from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def compose(g, h):
    return tuple(g[h[i]] for i in range(3))


def check_action(elements):
    identity = (0, 1, 2)
    assert identity in elements
    assert all(compose(g, h) in elements for g in elements for h in elements)
    orbits = [{g[x] for g in elements} for x in range(3)]
    stabilizers = [[g for g in elements if g[x] == x] for x in range(3)]
    transports = [[sum(g[x] == y for g in elements) for y in range(3)] for x in range(3)]
    assert all(len(orbits[x]) * len(stabilizers[x]) == len(elements) for x in range(3))
    return orbits, stabilizers, transports


def arrow(ax, start, end, color, curvature=0):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=17,
                                shrinkA=18, shrinkB=18, linewidth=2.3,
                                connectionstyle=f"arc3,rad={curvature}", color=color))


def loop(ax, point, color, side=1):
    x, y = point
    angles = np.linspace(-2.5, 2.5, 80) if side == 1 else np.linspace(-0.6, 5.4, 80)
    center = np.array([x + side * 0.22, y + 0.22])
    curve = center[:, None] + 0.18 * np.array([np.cos(angles), np.sin(angles)])
    ax.plot(*curve, color=color, lw=1.7)
    ax.add_patch(FancyArrowPatch(curve[:, -5], curve[:, -1], arrowstyle="-|>",
                                color=color, mutation_scale=12, lw=1.7))


def main():
    s3 = list(permutations(range(3)))
    c3 = [tuple((i + k) % 3 for i in range(3)) for k in range(3)]
    so, ss, st = check_action(s3)
    co, cs, ct = check_action(c3)
    assert all(len(o) == 3 for o in so + co)
    assert all(len(h) == 2 for h in ss) and all(len(h) == 1 for h in cs)
    assert st == [[2] * 3 for _ in range(3)] and ct == [[1] * 3 for _ in range(3)]
    assert {g for g in s3 if g[0] == 1} == {(1, 0, 2), (1, 2, 0)}

    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.8), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.13, top=0.84, wspace=0.10)
    red, blue, gray = "#c74736", "#2166ac", "#737c86"
    points = np.array([[0, 0.55], [0.88, -0.66], [-0.88, -0.66]])
    for ax, labels, title in zip(axes, [("1", "2", "3"), ("0", "1", "2")],
                                  [r"$S_3$ on three points", r"$C_3$ on itself"]):
        ax.set(xlim=(-1.55, 1.55), ylim=(-2.0, 1.6), aspect="equal")
        ax.axis("off")
        ax.text(0, 1.47, title, fontsize=16, weight="bold", ha="center")
        for i in range(3):
            arrow(ax, points[i], points[(i + 1) % 3], red, curvature=-0.13)
        for p, label in zip(points, labels):
            loop(ax, p, gray)
            ax.add_patch(Circle(p, 0.16, facecolor="white", edgecolor="#243444", lw=2, zorder=5))
            ax.text(*p, label, ha="center", va="center", fontsize=15, zorder=6)
        ax.text(-0.60, 0.05, r"$r$", color=red, fontsize=15)
    arrow(axes[0], points[1], points[2], blue, curvature=0.40)
    arrow(axes[0], points[2], points[1], blue, curvature=-0.40)
    loop(axes[0], points[0], blue, side=-1)
    axes[0].text(-0.47, 0.86, r"$t$", color=blue, fontsize=15)
    axes[0].text(0, -1.24, r"$t=(23)$", color=blue, ha="center", fontsize=13)
    axes[0].text(0, -1.62, "One orbit; two transports per pair\nTransitive, not free", ha="center", fontsize=12)
    axes[1].text(0, -1.24, r"$r:x\mapsto x+1$ (mod 3)", color=red, ha="center", fontsize=13)
    axes[1].text(0, -1.62, "One orbit; one transport per pair\nFree and transitive (regular)", ha="center", fontsize=12)
    fig.suptitle("Reaching every point does not imply unique transport", y=0.965, fontsize=17)
    fig.text(0.5, 0.88, r"Left: $r=(123)$ and $t=(23)$ generate $S_3$.  Right: $r$ generates $C_3$.", ha="center", fontsize=12)
    fig.text(0.5, 0.065, "Gray loops: the identity e fixes every point in both actions.", ha="center", color=gray)
    fig.text(0.5, 0.025, r"Stabilizers: $(S_3)_1=\{e,(23)\}$  versus  $(C_3)_0=\{e\}$.", ha="center", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
