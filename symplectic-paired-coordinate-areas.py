"""Draw symplectic coordinate pairs; output the matching PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Polygon
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    a = np.array([2, 1, 1, 1])
    b = np.array([1, 1, 0, 2])
    j = np.block([[np.zeros((2, 2), dtype=int), np.eye(2, dtype=int)],
                  [-np.eye(2, dtype=int), np.zeros((2, 2), dtype=int)]])
    areas = [int(a[i] * b[i + 2] - a[i + 2] * b[i]) for i in range(2)]
    assert areas == [-1, 1] and a @ j @ b == sum(areas) == 0
    fig, axes = plt.subplots(1, 3, figsize=(11.2, 4.8),
                             gridspec_kw={"width_ratios": [1, 1, 1.05]})
    fig.set_facecolor("white")
    for i, ax in enumerate(axes[:2]):
        x, y = a[[i, i + 2]], b[[i, i + 2]]
        ax.add_patch(Polygon([np.zeros(2), x, x + y, y],
                             facecolor="#e7d8eb" if areas[i] < 0 else "#d3e9df",
                             edgecolor="#555555", linewidth=1.2))
        for v, color, label, offset in [(x, "#176397", "$a$", (6, -16)),
                                        (y, "#b74a28", "$b$", (7, 6))]:
            ax.annotate("", v, (0, 0), arrowprops={"arrowstyle": "->", "color": color, "lw": 2.5})
            ax.annotate(label, v, xytext=offset, textcoords="offset points", color=color, fontsize=13)
        ax.set(xlim=(-.35, 3.6), ylim=(-.35, 3.6), aspect="equal",
               xlabel=rf"$q_{i + 1}$ (along $e_{i + 1}$)",
               ylabel=rf"$p_{i + 1}$ (along $f_{i + 1}$)",
               title=f"Pair {i + 1}: signed area {areas[i]:+d}")
        ax.set_xticks(range(4)); ax.set_yticks(range(4))
        ax.grid(alpha=.17)
        ax.spines[["top", "right"]].set_visible(False)
    ax = axes[2]
    cmap = ListedColormap(["#d9bcdf", "#ffffff", "#b8dfce"])
    ax.imshow(j, cmap=cmap, norm=BoundaryNorm([-1.5, -.5, .5, 1.5], 3))
    names = ["$e_1$", "$e_2$", "$f_1$", "$f_2$"]
    ax.set_xticks(range(4), names); ax.set_yticks(range(4), names)
    for row in range(4):
        for col in range(4):
            ax.text(col, row, str(j[row, col]), ha="center", va="center", fontsize=14)
    ax.set_title("Pairing matrix $J$")
    ax.set_xlabel("Second input"); ax.set_ylabel("First input")
    ax.set_xticks(np.arange(-.5, 4, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 4, 1), minor=True)
    ax.grid(which="minor", color="#888888", linewidth=.6)
    ax.tick_params(which="minor", length=0)
    fig.suptitle("Four-dimensional symplectic coordinates: two paired planes", fontsize=16, y=.97)
    fig.text(.5, .035, r"$a=(2,1,1,1)^T,\quad b=(1,1,0,2)^T,\quad \omega(a,b)=-1+1=0$",
             ha="center", fontsize=13)
    fig.subplots_adjust(left=.065, right=.985, bottom=.2, top=.78, wspace=.42)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
