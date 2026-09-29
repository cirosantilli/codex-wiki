"""Original solution diagram. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory; no source-paper artwork is used.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def main():
    positions = [1]
    for _ in range(7):
        positions.append(2 * positions[-1] % 51)
    assert positions == [1, 2, 4, 8, 16, 32, 13, 26]
    assert 2 * positions[-1] % 51 == positions[0]

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(6.4, 4.5), dpi=150, facecolor="white")
    ax.set_facecolor("white")
    theta = np.pi / 2 - np.arange(8) * np.pi / 4
    points = np.column_stack((np.cos(theta), np.sin(theta)))
    for i, point in enumerate(points):
        next_point = points[(i + 1) % 8]
        ax.add_patch(FancyArrowPatch(
            point, next_point, arrowstyle="-|>", mutation_scale=16,
            shrinkA=20, shrinkB=20, linewidth=1.8, color="#546e7a",
            connectionstyle="arc3,rad=0.06", zorder=1,
        ))
    for i, (x, y) in enumerate(points):
        ax.text(x, y, str(positions[i]), ha="center", va="center",
                fontsize=15, fontweight="bold", color="#16324f",
                bbox=dict(boxstyle="circle,pad=0.38",
                          facecolor="#ffe1aa" if i == 0 else "#e5f0f8",
                          edgecolor="#b16c00" if i == 0 else "#31688e",
                          linewidth=1.5), zorder=2)
    ax.text(0, 0.18, "52-card\nout-shuffle", ha="center", fontsize=14,
            fontweight="bold", color="#16324f")
    ax.text(0, -0.30, "i → 2i (mod 51)", ha="center", fontsize=13)
    ax.text(0, -1.43, "Zero-based positions · one arrow per shuffle",
            ha="center", fontsize=11, color="#455a64")
    ax.text(0, -1.65, "7 shuffles: 1 → 26     |     8 shuffles: 1 → 1",
            ha="center", fontsize=12, color="#16324f")
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.82, 1.45)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.04, top=0.97)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
