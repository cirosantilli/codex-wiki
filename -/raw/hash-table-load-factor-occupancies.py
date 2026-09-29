"""Draw two original twelve-record placements; emit PNG to the working directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def draw_occupancies():
    placements = [list(range(12)), list(range(0, 177, 16))]
    lengths = [np.bincount(np.array(keys) % 8, minlength=8) for keys in placements]
    assert [v.tolist() for v in lengths] == [[2, 2, 2, 2, 1, 1, 1, 1], [12, 0, 0, 0, 0, 0, 0, 0]]
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.4), dpi=120, facecolor="white")
    colors = ["#2878a0", "#cc681e"]
    titles = ["Balanced: keys 0, 1, …, 11", "Concentrated: keys 0, 16, …, 176"]
    for ax, counts, color, title in zip(axes, lengths, colors, titles):
        ax.set_facecolor("white")
        for j, count in enumerate(counts):
            ax.add_patch(Rectangle((j - .35, 0), .7, 12, fill=False, edgecolor="#c4cbd1", linewidth=.8))
            for r in range(int(count)):
                ax.add_patch(Rectangle((j - .35, r + .05), .7, .9, facecolor=color, edgecolor="white", linewidth=.7))
            ax.text(j, count + .28, str(count), ha="center", va="bottom", fontsize=11, weight="bold", color=color)
        ax.axhline(1.5, color="#4c4759", linestyle=(0, (4, 3)), linewidth=1.6)
        ax.text(7.5, 1.7, "α = 1.5", ha="right", va="bottom", fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
        ax.set(xlim=(-.65, 7.65), ylim=(0, 13.5), xticks=range(8), yticks=[0, 2, 4, 6, 8, 10, 12], xlabel="Bucket index")
        ax.set_title(title, fontsize=12, pad=13)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=10)
    axes[0].set_ylabel("Records in bucket", fontsize=11)
    fig.suptitle("Eight buckets, twelve records: identical load factor", fontsize=16, y=.97)
    fig.text(.5, .095, "Mean occupancy = 12 / 8 = 1.5 in both; maximum chain length = 2 or 12", ha="center", fontsize=12)
    fig.text(.5, .045, "Outlines include empty buckets. Colored squares are records, not timings.", ha="center", fontsize=10, color="#4a5055")
    fig.subplots_adjust(left=.075, right=.98, bottom=.23, top=.84, wspace=.21)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    draw_occupancies()
