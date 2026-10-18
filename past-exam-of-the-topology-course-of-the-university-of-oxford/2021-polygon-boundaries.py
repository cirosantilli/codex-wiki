"""Generate the 2021 topology polygon explanation in the current directory.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media/past-exam-of-the-topology-course-of-the-university-of-oxford.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def arrow(ax, start, end, label, offset):
    start, end = np.asarray(start), np.asarray(end)
    mid = (start + end) / 2
    direction = (end - start) / np.linalg.norm(end - start)
    ax.annotate(
        "", xy=mid + 0.16 * direction, xytext=mid - 0.16 * direction,
        arrowprops={"arrowstyle": "->", "color": "#26364b", "lw": 1.7},
    )
    ax.text(*(mid + np.asarray(offset)), label, ha="center", va="center", fontsize=13)


def draw_panel(ax, points, classes, paired, free, title, count):
    points = np.asarray(points, dtype=float)
    ax.add_patch(Polygon(points, closed=True, facecolor="#f0f3f7", edgecolor="#26364b", lw=1.8))
    for start, end, name, offset in paired:
        arrow(ax, points[start], points[end], name, offset)
    for start, end, name in free:
        p, q = points[start], points[end]
        ax.plot([p[0], q[0]], [p[1], q[1]], color="#c26a10", lw=4, solid_capstyle="round")
        mid = (p + q) / 2
        ax.text(mid[0] - 0.18, mid[1] - 0.18, name, color="#8b4908", ha="center", va="center", fontsize=12)
    centroid = points.mean(axis=0)
    for index, (point, name) in enumerate(zip(points, classes)):
        color = "#165eaa" if name == "P" else "#973b8b"
        ax.scatter(*point, c=color, s=38, zorder=4)
        outward = point - centroid
        outward /= np.linalg.norm(outward)
        ax.text(*(point + 0.23 * outward), f"$v_{index}$: {name}", fontsize=10, color=color, ha="center", va="center")
    ax.set_title(title, fontsize=14, pad=12)
    ax.text(1, -0.68, count, ha="center", va="top", fontsize=11, linespacing=1.6)
    ax.set(xlim=(-0.6, 2.6), ylim=(-1.25, 2.55), aspect="equal")
    ax.axis("off")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 5.0), facecolor="white")
    draw_panel(
        axes[0], [(0, 2), (2, 2), (2, 0), (1, 0), (0, 1)], ["P"] * 5,
        [(4, 0, "$a$", (-0.18, 0)), (2, 1, "$a$", (0.18, 0)),
         (0, 1, "$b$", (0, 0.2)), (3, 2, "$b$", (0, -0.2))],
        [(3, 4, "$e$")], "3(b)(ii): pentagon",
        r"$V=1,\ E=3,\ F=1,\ \chi=-1$" "\nBoundary: one loop $e$ at $P$",
    )
    draw_panel(
        axes[1], [(0, 2), (1, 2), (2, 1), (2, 0), (1, 0), (0, 1)], ["P", "Q", "P", "Q", "P", "Q"],
        [(5, 0, "$a$", (-0.18, 0)), (3, 2, "$a$", (0.18, 0)),
         (0, 1, "$b$", (0, 0.2)), (4, 3, "$b$", (0, -0.2))],
        [(1, 2, "$e$"), (4, 5, "$f$")], "3(b)(iii): hexagon",
        r"$V=2,\ E=4,\ F=1,\ \chi=-1$" "\nBoundary: $P$ to $Q$ along $e$, back along $f$",
    )
    fig.suptitle("The orange free edges form one boundary circle in each quotient", fontsize=14, y=0.98)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(Path("2021-polygon-boundaries.png"), dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
