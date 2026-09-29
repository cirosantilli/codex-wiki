"""Draw radius-three word metric balls for four and eight lattice moves.

Run from _media: python ../word-metric-lattice-balls.py
Writes word-metric-lattice-balls.png to the current directory.
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5 (root pyproject.toml).
"""

import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def draw_panel(ax, diagonal, path):
    points = [(x, y) for x in range(-4, 5) for y in range(-4, 5)]
    inside = [(x, y) for x, y in points
              if (max(abs(x), abs(y)) if diagonal else abs(x) + abs(y)) <= 3]
    outline = [(-3, -3), (3, -3), (3, 3), (-3, 3)] if diagonal else [
        (0, -3), (3, 0), (0, 3), (-3, 0)]
    ax.add_patch(Polygon(outline, closed=True, facecolor="#e9f2fa",
                         edgecolor="#3374a0", lw=2.2, zorder=0))
    positive_steps = [(1, 0), (0, 1)] + ([(1, 1), (1, -1)] if diagonal else [])
    for x, y in points:
        for dx, dy in positive_steps:
            q = (x + dx, y + dy)
            if q in points:
                ax.plot([x, q[0]], [y, q[1]], color="#c6d0d9", lw=0.65, zorder=1)
    ax.scatter(*zip(*points), s=16, c="#b2bdc6", zorder=2)
    ax.scatter(*zip(*inside), s=38, c="#276d9c", zorder=3)
    ax.plot(*zip(*path), color="#be4b13", lw=3.1, marker="o", ms=6, zorder=4)
    ax.scatter([0, 2], [0, 3], s=90, c="white", edgecolors="#be4b13",
               linewidths=2.2, zorder=5)
    ax.annotate("(0, 0)", (0, 0), xytext=(-38, -20), textcoords="offset points",
                fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.annotate("(2, 3)", (2, 3), xytext=(-7, 17), textcoords="offset points",
                fontsize=11, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.set(xlim=(-4.4, 4.4), ylim=(-4.4, 4.4), aspect="equal",
           xticks=range(-4, 5), yticks=range(-4, 5), xlabel="first coordinate",
           ylabel="second coordinate")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(length=0, labelsize=10)
    if diagonal:
        title = "Eight moves: axes and diagonals\n" + r"$\ell_\infty$ ball: 49 lattice points"
        summary = r"$|(m,n)|_T=\max(|m|,|n|)$" + "\nRoute to (2, 3): 3 steps"
    else:
        title = "Four moves: horizontal and vertical\n" + r"$\ell_1$ ball: 25 lattice points"
        summary = r"$|(m,n)|_S=|m|+|n|$" + "\nRoute to (2, 3): 5 steps"
    ax.set_title(title, fontsize=14, pad=14, linespacing=1.6)
    assert len(inside) == (49 if diagonal else 25)
    return summary


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 6.2), dpi=100)
    fig.suptitle("Radius 3 means at most three allowed moves", fontsize=18, y=0.97)
    left = draw_panel(axes[0], False, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)])
    right = draw_panel(axes[1], True, [(0, 0), (1, 1), (2, 2), (2, 3)])
    fig.text(0.275, 0.13, left, ha="center", fontsize=12, linespacing=1.7)
    fig.text(0.775, 0.13, right, ha="center", fontsize=12, linespacing=1.7)
    fig.text(0.5, 0.035, "Blue region: the ball's outline; blue points: its lattice elements.\n"
             "Orange: a shortest route. Every edge, including a diagonal, costs one step.",
             ha="center", fontsize=11, color="#344a5e", linespacing=1.5)
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.28, top=0.79, wspace=0.2)
    fig.savefig("word-metric-lattice-balls.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
