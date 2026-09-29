"""Enumerate the sixteen states of a four-edge classical Ising ring.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the opaque PNG is written to the current directory.
"""

from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    states = {d: [] for d in (0, 2, 4)}
    for spins in product((1, -1), repeat=4):
        walls = sum(spins[i] != spins[(i + 1) % 4] for i in range(4))
        states[walls].append(spins)
    assert [len(states[d]) for d in (0, 2, 4)] == [2, 12, 2]

    fig = plt.figure(figsize=(11, 7), dpi=100, facecolor="white")
    fig.suptitle("Four spins, four distinct edges, sixteen configurations", y=0.96, fontsize=17)
    columns = fig.add_gridspec(1, 3, width_ratios=(1.1, 3.2, 1.1),
                              left=0.03, right=0.97, top=0.82, bottom=0.16, wspace=0.13)
    points = np.array([[-0.55, 0.55], [0.55, 0.55], [0.55, -0.55], [-0.55, -0.55]])
    for col, walls in enumerate((0, 2, 4)):
        panel = fig.add_subplot(columns[col])
        panel.axis("off")
        panel.set_title(f"{walls} walls  |  {len(states[walls])} states\n"
                        + {0: r"$H=-4J$", 2: r"$H=0$", 4: r"$H=+4J$"}[walls],
                        fontsize=14, pad=12)
        rows, cols = (4, 3) if walls == 2 else (2, 1)
        for n, spins in enumerate(states[walls]):
            row, smallcol = divmod(n, cols)
            height = 0.92 / rows
            width = 0.96 / cols
            y = 0.04 + (rows - row - 1) * height
            ax = panel.inset_axes([0.02 + smallcol * width, y, width, height])
            ax.set(xlim=(-0.85, 0.85), ylim=(-0.85, 0.85), aspect="equal")
            ax.axis("off")
            for i in range(4):
                j = (i + 1) % 4
                broken = spins[i] != spins[j]
                ax.plot(points[[i, j], 0], points[[i, j], 1],
                        color="#b93b47" if broken else "#9ca6ae",
                        linestyle="--" if broken else "-", linewidth=2.2, zorder=1)
            for (x, y), spin in zip(points, spins):
                ax.add_patch(Circle((x, y), 0.17,
                                   facecolor="#246caa" if spin == 1 else "#ca691b",
                                   edgecolor="white", linewidth=1.2, zorder=2))
                ax.text(x, y, "+" if spin == 1 else "−", color="white",
                        ha="center", va="center", fontsize=13, weight="bold", zorder=3)
    handles = [Line2D([], [], marker="o", linestyle="", color="#246caa", label=r"spin $+1$"),
               Line2D([], [], marker="o", linestyle="", color="#ca691b", label=r"spin $-1$"),
               Line2D([], [], linestyle="--", color="#b93b47", label=r"domain wall: cost $2J$")]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.06), ncol=3, frameon=False)
    fig.text(0.5, 0.035, r"Zero field, $J>0$. Vertex labels remain fixed; rotations are distinct microstates.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
