"""Original occupation schematic; tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; write the matching PNG to the current working directory.
Circles represent spin-resolved states in the upper panels and localized
occupancies in the lower cartoons, not an empirical band dispersion.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


BLUE = "#246bb1"
ORANGE = "#c45e16"
GRAY = "#d1dae2"
X = np.linspace(0.20, 0.92, 7)


def row(ax, y, occupied):
    ax.plot([0.15, 0.98], [y, y], color=GRAY, lw=2, zorder=1)
    for x, filled in zip(X, occupied, strict=True):
        ax.scatter(x, y, s=165, facecolor=BLUE if filled else "white",
                   edgecolor=BLUE if filled else ORANGE, linewidth=1.8, zorder=3)


def arrow(ax, start, end, color=ORANGE):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2})


def main():
    full = np.ones(7, dtype=bool)
    empty = np.zeros(7, dtype=bool)
    hole = full.copy()
    hole[3] = False
    promoted = empty.copy()
    promoted[3] = True
    shifted = full.copy()
    shifted[2] = False
    assert full.sum() == hole.sum() + promoted.sum() == 7
    assert (~hole).sum() == (~shifted).sum() == 1
    assert shifted[3] and hole[2]

    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axs = plt.subplots(2, 2, figsize=(10, 6.4), facecolor="white")
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.13, top=0.85,
                        wspace=0.22, hspace=0.58)
    for ax in axs.flat:
        ax.set(xlim=(0, 1.08), ylim=(0, 1.05))
        ax.axis("off")

    ax = axs[0, 0]
    ax.set_title("Unexcited band occupation", loc="left", fontweight="bold")
    row(ax, 0.72, empty)
    row(ax, 0.24, full)
    ax.text(0.16, 0.85, "Conduction band: empty")
    ax.text(0.16, 0.36, "Valence band: full")
    arrow(ax, (0.055, 0.16), (0.055, 0.86), color="#555555")
    ax.text(0.02, 0.52, "Energy", rotation=90, va="center", ha="center")
    ax.text(0.16, 0.02, "7 electrons; no electron hole")

    ax = axs[0, 1]
    ax.set_title("One electron promoted", loc="left", fontweight="bold")
    row(ax, 0.72, promoted)
    row(ax, 0.24, hole)
    ax.text(0.16, 0.85, "Conduction electron: −e")
    ax.text(0.16, 0.36, "Missing valence electron: +e")
    arrow(ax, (X[3], 0.42), (X[3], 0.66))
    ax.text(0.16, 0.02, "6 + 1 = 7 electrons; net pair charge = 0")

    ax = axs[1, 0]
    ax.set_title("Local vacancy moves when an electron fills it", loc="left",
                 fontweight="bold", fontsize=10)
    row(ax, 0.76, hole)
    row(ax, 0.24, shifted)
    arrow(ax, (X[2], 0.91), (X[3], 0.91), color=BLUE)
    ax.text(0.08, 0.94, "electron →", color=BLUE, fontsize=10)
    arrow(ax, (X[3], 0.49), (X[2], 0.49))
    ax.text(0.65, 0.48, "← hole", color=ORANGE, fontsize=10)
    ax.text(0.16, 0.02, "Before and after: 6 electrons, 1 hole")

    ax = axs[1, 1]
    ax.set_title("Recombination fills the hole", loc="left", fontweight="bold")
    row(ax, 0.76, promoted)
    row(ax, 0.24, hole)
    arrow(ax, (X[3], 0.69), (X[3], 0.31), color=BLUE)
    ax.text(0.63, 0.51, "Energy leaves", fontsize=10)
    ax.text(0.16, 0.02, "After: full valence band, empty conduction band")

    fig.suptitle("Electron holes: missing occupation, positive charge, mobile vacancy",
                 fontsize=14, y=0.96)
    fig.text(0.5, 0.055, "Filled blue = occupied   |   Open orange = empty\n"
             "Qualitative schematic; lower panels are local cartoons, not Bloch-state trajectories.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
