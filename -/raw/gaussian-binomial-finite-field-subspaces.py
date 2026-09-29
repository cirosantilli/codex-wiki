"""Render all pivot patterns of two-dimensional subspaces of F_2^4."""
from itertools import combinations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig, axes = plt.subplots(2, 3, figsize=(12, 6.4), dpi=110)
    fig.patch.set_facecolor("white")
    fig.suptitle(r"Counting two-dimensional subspaces of $\mathbb{F}_2^4$", fontsize=19, y=0.98)
    counts = []
    for ax, pivots in zip(axes.flat, combinations(range(4), 2)):
        free = 0
        for row in range(2):
            for col in range(4):
                is_free = col > pivots[row] and col not in pivots
                if is_free:
                    text, fill = "*", "#f3c66c"
                    free += 1
                elif col == pivots[row]:
                    text, fill = "1", "#b6d7ed"
                else:
                    text, fill = "0", "#f7f8fa"
                ax.add_patch(Rectangle((col, 1-row), 1, 1, facecolor=fill, edgecolor="#b7bcc3", linewidth=1))
                ax.text(col+0.5, 1.5-row, text, ha="center", va="center", fontsize=22)
        counts.append(2**free)
        ax.set(xlim=(-0.08, 4.08), ylim=(-0.20, 2.16), aspect="equal")
        ax.set_title(f"Pivot columns {pivots[0]+1}, {pivots[1]+1}", fontsize=14, pad=8)
        ax.text(2, -0.42, rf"{free} free entries: $2^{free}={2**free}$ subspaces", ha="center", fontsize=12)
        ax.axis("off")
    assert sum(counts) == 35
    fig.text(0.5, 0.035, r"Each * independently takes 0 or 1. Unique reduced row echelon forms give $16+8+4+4+2+1=35$.", ha="center", fontsize=13)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.86, bottom=0.13, hspace=0.48, wspace=0.20)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
