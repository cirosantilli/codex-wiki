"""Draw an original dipole-counting model; emit a PNG in the working directory.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.8), dpi=120)
    fig.patch.set_facecolor("white")
    fig.suptitle("Same individual moments, different magnetization", fontsize=17, y=0.96)
    blue, orange = "#17649b", "#bf5815"
    patterns = (np.array([1, 1, -1, 1, 1, -1, 1, 1]), np.ones(8, dtype=int))
    for ax, signs, title, net in zip(
        axes, patterns, ("Six up, two down", "All eight up"), (4, 8), strict=True
    ):
        ax.set_aspect("equal")
        ax.set_xlim(-0.3, 4.3)
        ax.set_ylim(-1.55, 2.8)
        ax.axis("off")
        ax.set_title(title, pad=11, fontsize=14)
        ax.add_patch(Rectangle((0, 0), 4, 2.2, facecolor="#f3f8fc", edgecolor=blue, lw=1.5, linestyle="--"))
        ax.text(3.88, 2.35, r"Same volume $\Delta V$", ha="right", color=blue)
        for i, sign in enumerate(signs):
            x, y = 0.5 + i % 4, 0.55 + i // 4 * 1.1
            ax.add_patch(FancyArrowPatch((x, y - 0.34 * sign), (x, y + 0.34 * sign), arrowstyle="-|>", mutation_scale=17, lw=2.4, color=blue if sign > 0 else orange))
            ax.plot(x, y, "o", color="#44515a", ms=3)
        ax.text(2, -0.36, rf"$\sum_i\mathbf{{m}}_i = {net}m_0\widehat{{\mathbf{{z}}}}$", ha="center", fontsize=15)
        ax.text(2, -0.87, rf"$\mathbf{{M}} = \frac{{{net}m_0}}{{\Delta V}}\widehat{{\mathbf{{z}}}}$", ha="center", fontsize=16)
    fig.text(0.5, 0.045, r"Every arrow has magnitude $m_0$.  Reorientation changes the vector sum.", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.035, right=0.985, top=0.83, bottom=0.14, wspace=0.12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
