"""Draw a zero-indexed min-heap; tested with Python 3.14 / matplotlib 3.10.7.

Run from _media to write binary-heap-array-and-tree.png there.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


VALUES = (2, 5, 3, 9, 7, 8, 4)
COLORS = ("#006b8f", "#955400", "#267547", "#7b4397",
          "#955400", "#267547", "#267547")


def check_heap(values):
    """Check dense level-order shape, inverse indices, and every heap edge."""
    present = set(range(len(values)))
    for i in present:
        if i:
            parent = (i - 1) // 2
            assert parent in present
            assert i in (2 * parent + 1, 2 * parent + 2)
            assert values[parent] <= values[i]
        left, right = 2 * i + 1, 2 * i + 2
        assert right not in present or left in present
    return len(values) - 1 if values else 0


def main():
    assert check_heap(VALUES) == 6
    assert VALUES != tuple(sorted(VALUES))
    assert VALUES[-1] == 4 and max(VALUES) == 9
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6.8), facecolor="white")
    ax.set(xlim=(-0.3, 9.7), ylim=(-0.45, 6.35), aspect="equal")
    ax.axis("off")
    ax.text(4.7, 6.05, "Binary min-heap: an array is also a tree",
            ha="center", fontsize=18, weight="bold", color="#173244")
    ax.text(0.1, 5.48, "index i", fontsize=11, color="#475569")
    ax.text(0.1, 4.84, "key A[i]", fontsize=11, color="#475569")
    for i, key in enumerate(VALUES):
        x = 1.65 + i
        ax.add_patch(Rectangle((x - 0.45, 4.48), 0.9, 0.7,
                               facecolor="#f3f7fa", edgecolor=COLORS[i],
                               linewidth=1.8))
        ax.text(x, 5.48, str(i), ha="center", color=COLORS[i], weight="bold")
        ax.text(x, 4.84, str(key), ha="center", va="center", fontsize=17)
    positions = {0: (4.65, 3.75), 1: (2.4, 2.55), 2: (6.9, 2.55),
                 3: (1.3, 1.3), 4: (3.5, 1.3), 5: (5.8, 1.3),
                 6: (8.0, 1.3)}
    for child in range(1, len(VALUES)):
        parent = (child - 1) // 2
        x0, y0 = positions[parent]
        x1, y1 = positions[child]
        ax.plot([x0, x1], [y0, y1], color="#9baebc", linewidth=1.8, zorder=1)
    for i, (x, y) in positions.items():
        ax.add_patch(Circle((x, y), 0.31, facecolor="white",
                            edgecolor=COLORS[i], linewidth=2, zorder=3))
        ax.text(x, y, str(VALUES[i]), ha="center", va="center",
                fontsize=16, zorder=4)
        ax.text(x, y - 0.53, f"i = {i}", ha="center", fontsize=11,
                color=COLORS[i], weight="bold")
    ax.text(8.6, 3.7, "root\ni = 0", ha="center", va="center", color="#006b8f")
    ax.text(0.1, 0.25, "Children: 2i + 1, 2i + 2       Parent: floor((i − 1) / 2), i > 0",
            fontsize=12, color="#173244")
    ax.text(0.1, -0.18, "Parent key ≤ child key.  Not sorted: 5 > 3.  Last key 4 is not the maximum 9.",
            fontsize=11, color="#173244")
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.02, top=0.99)
    fig.savefig(Path.cwd() / "binary-heap-array-and-tree.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("7 dense indices; 6 heap-order edges; index 4 has parent 1; "
          "root minimum 2; last key 4 != maximum 9")


if __name__ == "__main__":
    main()
