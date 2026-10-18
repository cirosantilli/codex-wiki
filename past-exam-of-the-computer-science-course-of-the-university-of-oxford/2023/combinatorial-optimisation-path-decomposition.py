"""Draw an original cubic-graph path decomposition.

Tested with Python 3.14.4 and Matplotlib 3.10.7; dependencies are in the
repository's pyproject.toml. Write the opaque PNG into the current directory.
"""

from math import cos, pi, sin
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(8.8, 4.3), dpi=100, facecolor="white")
    ax = fig.add_axes((0.02, 0.06, 0.51, 0.82))
    ax.set_aspect("equal")
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-1.35, 1.95)
    ax.axis("off")
    colors = ["#1767a0", "#b45212", "#267642"]
    outer, inner = [], []
    for angle in (pi / 2, 7 * pi / 6, 11 * pi / 6):
        outer.append((1.65 * cos(angle), 1.65 * sin(angle)))
        inner.append((0.67 * cos(angle), 0.67 * sin(angle)))
    for i, color in enumerate(colors):
        ax.plot([outer[i][0], inner[i][0]], [outer[i][1], inner[i][1]],
                color=color, linewidth=4, solid_capstyle="round", zorder=1)
        for cycle in (outer, inner):
            arrow = FancyArrowPatch(cycle[i], cycle[(i + 1) % 3],
                                    arrowstyle="-|>", mutation_scale=17,
                                    shrinkA=12, shrinkB=12,
                                    linewidth=2.6, color=color, zorder=2)
            ax.add_patch(arrow)
    for points, labels in ((outer, "ABC"), (inner, "abc")):
        for point, label in zip(points, labels):
            ax.scatter(*point, s=500, facecolors="white", edgecolors="#333333",
                       linewidths=1.3, zorder=3)
            ax.text(*point, label, ha="center", va="center", fontsize=12, zorder=4)
    fig.suptitle("A perfect matching seeds three paths", y=0.97, fontsize=16)
    fig.text(0.56, 0.79, "Matching: Aa, Bb, Cc", fontsize=13)
    fig.text(0.56, 0.69, "Arrows orient both cycles.", fontsize=12)
    for y, color, path in zip((0.52, 0.39, 0.26), colors,
                              ("B — A — a — b", "C — B — b — c", "A — C — c — a")):
        fig.text(0.57, y, path, color=color, fontsize=16, weight="bold")
    fig.text(0.56, 0.10, "Each color uses exactly three edges.", fontsize=10.5)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
