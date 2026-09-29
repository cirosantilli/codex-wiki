"""Draw integer-module examples; tested with Python 3.14 and Matplotlib 3.10.

Uses the repository's existing NumPy and Matplotlib dependencies. Writes the
opaque, white-background basename PNG in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    blue, orange, gray = "#176b9d", "#c45c19", "#697780"
    fig, (grid, cycle) = plt.subplots(1, 2, figsize=(10.4, 5.2), dpi=110)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.06, right=0.96, top=0.81, bottom=0.23, wspace=0.3)
    fig.suptitle("Two modules with integer scalars", fontsize=18, y=0.98)

    grid.set_title(r"Free: $\mathbb{Z}^2$", fontsize=16, pad=18)
    points = np.array([(a, b) for a in range(-1, 5) for b in range(-1, 4)])
    grid.scatter(*points.T, s=20, color="#a8b1b6", zorder=3)
    grid.set(xlim=(-1.4, 4.4), ylim=(-1.35, 3.35))
    grid.set_xticks(range(-1, 5))
    grid.set_yticks(range(-1, 4))
    grid.grid(color="#e4e8eb", linewidth=0.8)
    grid.axhline(0, color=gray, linewidth=1)
    grid.axvline(0, color=gray, linewidth=1)
    grid.set_aspect("equal")
    for end in [(1, 0), (0, 1)]:
        grid.annotate("", xy=end, xytext=(0, 0),
                      arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2.4},
                      zorder=5)
    grid.text(1.03, -0.48, r"$e_1=(1,0)$", color=blue, fontsize=11)
    grid.text(-1.28, 1.28, r"$e_2=(0,1)$", color=blue, fontsize=11)
    grid.plot([0, 3, 3], [0, 0, 2], color=orange, linestyle="--", linewidth=2)
    grid.scatter([3], [2], s=70, color=orange, zorder=5)
    grid.text(2.0, 2.5, r"$(3,2)=3e_1+2e_2$", color=orange)
    grid.text(1.6, 0.3, r"$3e_1$", color=orange)
    grid.text(3.15, 0.9, r"$2e_2$", color=orange)
    grid.set_xlabel("First integer coordinate")
    grid.set_ylabel("Second integer coordinate")
    grid.spines[["top", "right"]].set_visible(False)

    cycle.set_title(r"Cyclic and torsion: $\mathbb{Z}/6\mathbb{Z}$", fontsize=16, pad=18)
    angles = np.pi / 2 - np.arange(6) * np.pi / 3
    positions = np.column_stack((np.cos(angles), np.sin(angles)))
    for j, start in enumerate(positions):
        end = positions[(j + 1) % 6]
        cycle.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                        connectionstyle="arc3,rad=-0.22", shrinkA=16,
                        shrinkB=16, mutation_scale=15, color=gray, lw=1.7))
    cycle.scatter(*positions.T, s=350,
                  c=[blue if j % 2 == 0 else orange for j in range(6)], zorder=4)
    for j, (x, y) in enumerate(positions):
        cycle.text(x, y, rf"$\overline{{{j}}}$", ha="center", va="center",
                   color="white", fontsize=13, zorder=5)
    cycle.text(0, 0.18, r"Each arrow: $+\overline{1}$", ha="center", fontsize=12)
    cycle.text(0, -0.17, r"$6\overline{1}=\overline{0}$", ha="center", fontsize=16)
    cycle.set(xlim=(-1.5, 1.5), ylim=(-1.45, 1.45))
    cycle.set_aspect("equal")
    cycle.axis("off")

    fig.text(0.275, 0.095, "Unique integer coordinates; no nonzero torsion",
             ha="center", fontsize=11, color=blue)
    fig.text(0.765, 0.095, r"Blue points: $\mathbb{Z}\overline{2}=\{\overline{0},\overline{2},\overline{4}\}$",
             ha="center", fontsize=12, color=blue)
    fig.text(0.765, 0.04, r"$3\overline{2}=\overline{0}$; every element is torsion",
             ha="center", fontsize=11, color=gray)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
