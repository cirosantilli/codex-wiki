"""Construct a majority-block diagram. Tested on Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. Run from _media; emits this script's basename as PNG.
"""
from pathlib import Path
from itertools import product

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import FancyArrowPatch
import numpy as np


def example():
    signs = np.array([[1, 1, -1], [1, -1, -1], [-1, 1, 1]])
    positive = np.array([[1, 1, -1], [1, -1, 1], [-1, 1, -1]])
    spins = np.empty((9, 9), dtype=int)
    for row in range(3):
        for col in range(3):
            tile = np.rot90(positive, (row + 2 * col) % 4) * signs[row, col]
            spins[3 * row:3 * row + 3, 3 * col:3 * col + 3] = tile
    blocked = np.sign(spins.reshape(3, 3, 3, 3).sum(axis=(1, 3)))
    assert np.array_equal(blocked, signs)
    return spins, blocked


def checks():
    patterns = np.array(list(product((-1, 1), repeat=9)))
    totals = patterns.sum(axis=1)
    assert (totals != 0).all()
    assert np.count_nonzero(totals > 0) == 256
    spins, blocked = example()
    # Separate slicing checks the reshape convention used to construct the diagram.
    expected = [[np.sign(spins[3*r:3*r+3, 3*c:3*c+3].sum())
                 for c in range(3)] for r in range(3)]
    assert np.array_equal(blocked, expected)
    return {"majority_patterns": len(patterns), "positive_majorities": 256,
            "negative_majorities": 256, "block_sums":
            spins.reshape(3, 3, 3, 3).sum(axis=(1, 3)).tolist()}


def grid(ax, cells, extent):
    n = len(cells)
    ax.imshow(cells, cmap=ListedColormap(["#386aa0", "#c8584b"]),
              vmin=-1, vmax=1, extent=(0, extent, extent, 0),
              interpolation="nearest")
    for pos in np.linspace(0, extent, n + 1):
        ax.plot([pos, pos], [0, extent], color="white", lw=0.9)
        ax.plot([0, extent], [pos, pos], color="white", lw=0.9)
    for row in range(n):
        for col in range(n):
            ax.text((col+.5)*extent/n, (row+.5)*extent/n,
                    "+" if cells[row, col] > 0 else "−", color="white",
                    ha="center", va="center", fontsize=11 if n == 9 else 16)
    ax.set_xlim(-.1, 9.1)
    ax.set_ylim(9.1, -.1)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    print(checks())
    spins, blocked = example()
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 4.8), facecolor="white")
    axes = [fig.add_axes([x, .20, .265, .64]) for x in (.035, .365, .695)]
    grid(axes[0], spins, 9)
    grid(axes[1], blocked, 9)
    grid(axes[2], blocked, 3)
    for pos in (0, 3, 6, 9):
        axes[0].plot([pos, pos], [0, 9], color="#242b37", lw=1.5)
        axes[0].plot([0, 9], [pos, pos], color="#242b37", lw=1.5)
    labels = [("1  Resolve the spins", "9 × 9 sites; spacing a"),
              ("2  Keep each majority", "3 × 3 variables; spacing 3a"),
              ("3  Rescale coordinates", "x′ = x/3; spacing a again")]
    for ax, (title, detail) in zip(axes, labels):
        ax.text(0, 1.10, title, transform=ax.transAxes, fontsize=12, weight="bold")
        ax.text(0, 1.02, detail, transform=ax.transAxes, fontsize=10, color="#434d5d")
    for start, end, label in [(.305, .363, "sum"), (.635, .693, "rescale")]:
        fig.add_artist(FancyArrowPatch((start, .52), (end, .52),
                       transform=fig.transFigure, arrowstyle="-|>",
                       mutation_scale=18, lw=1.6, color="#434d5d"))
        fig.text((start+end)/2, .57, label, ha="center", fontsize=9)
    axes[2].text(0, 4.3, "Same nine signs.\nSmaller coordinate extent.\nNo physical compression.",
                 fontsize=10, va="top", color="#434d5d", linespacing=1.6)
    fig.text(.05, .13, "Each 3 × 3 block has five spins of its majority sign and four of the other sign.", fontsize=11)
    fig.text(.05, .065, "Constructed configuration: the coarse probabilities still require summing microscopic Boltzmann weights.",
             fontsize=10, color="#434d5d")
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
