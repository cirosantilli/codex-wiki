"""Draw an original modular rehash; emit PNG to the working directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def draw_rehash():
    keys = list(range(12))
    old = [[k for k in keys if k % 8 == j] for j in range(8)]
    new = [[k for k in keys if k % 16 == j] for j in range(16)]
    assert old == [[0, 8], [1, 9], [2, 10], [3, 11], [4], [5], [6], [7]]
    assert new == [[k] for k in range(12)] + [[], [], [], []]
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.set(xlim=(-.9, 16.2), ylim=(-1.0, 6.2))
    ax.axis("off")
    blue, orange = "#2878a0", "#cc681e"
    for groups, base, step, bottom in [(old, 0, 2, 3.5), (new, 0, 1, .45)]:
        for j, group in enumerate(groups):
            x = base + step * j
            # A visible empty destination is a bucket, not a missing object.
            ax.add_patch(Rectangle((x - .39, bottom), .78, .7 * max(1, len(group)),
                                   fill=False, edgecolor="#9faab2", linewidth=1))
            ax.text(x, bottom - .22, str(j), ha="center", va="top", fontsize=10)
            for r, key in enumerate(group):
                color = blue if key < 8 else orange
                ax.add_patch(Rectangle((x - .36, bottom + .03 + .7 * r), .72, .64,
                                       facecolor=color, edgecolor="white"))
                ax.text(x, bottom + .35 + .7 * r, str(key), ha="center", va="center", fontsize=11, color="white", weight="bold")
    for key in range(8, 12):
        start = (2 * (key % 8), 3.45)
        end = (key, 1.2)
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13,
                                    linewidth=1.4, color=orange, connectionstyle="arc3,rad=.06", alpha=.9))
    ax.text(7.5, 5.45, "Before: m = 8, n = 12, α = 1.5", ha="center", fontsize=14)
    ax.text(15.7, 4.25, "key labels\ninside boxes", ha="center", fontsize=10, color="#4a5055")
    ax.text(3.2, 2.2, "Recompute every index\nhₘ(k) = k mod m", ha="center", fontsize=12,
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    ax.text(7.5, -.35, "After: m = 16, n = 12, α = 0.75; buckets 12–15 are empty", ha="center", fontsize=12)
    fig.suptitle("Resizing redistributes records; it does not insert new keys", fontsize=16, y=.97)
    fig.text(.5, .035, "Blue keys keep their indices; orange keys 8–11 move. Numbers below boxes are bucket indices.", ha="center", fontsize=10, color="#4a5055")
    fig.subplots_adjust(left=.04, right=.97, bottom=.105, top=.9)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    draw_rehash()
