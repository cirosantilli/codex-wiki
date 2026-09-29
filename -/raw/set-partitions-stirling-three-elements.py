"""Draw an exact enumeration, not measured data. Python 3.14 / Matplotlib 3.10.

Run from _media; outlines and colours separate blocks but do not label them.
"""

from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def enumerate_partitions(n):
    """Enumerate canonical restricted-growth words independently of S(n,k)."""
    if n == 0:
        return [()]
    partitions = []
    for word in product(range(n), repeat=n):
        if word[0] != 0:
            continue
        if any(word[i] > 1 + max(word[:i]) for i in range(1, n)):
            continue
        partitions.append(tuple(
            tuple(i + 1 for i, label in enumerate(word) if label == j)
            for j in range(max(word) + 1)
        ))
    return partitions


def draw_partition(ax, partition, x, y):
    colours = ["#1b6d97", "#975725", "#6f519b"]
    widths = [0.43 * len(block) + 0.17 for block in partition]
    total = sum(widths) + 0.13 * (len(widths) - 1)
    cursor = x - total / 2
    for block, width, colour in zip(partition, widths, colours):
        ax.add_patch(FancyBboxPatch(
            (cursor, y - 0.29), width, 0.58,
            boxstyle="round,pad=0.025,rounding_size=0.12",
            linewidth=2, edgecolor=colour, facecolor="white",
        ))
        for j, element in enumerate(block):
            px = cursor + 0.30 + 0.43 * j
            ax.add_patch(Circle((px, y), 0.17, facecolor="#f2f5f7", edgecolor="none"))
            ax.text(px, y, str(element), ha="center", va="center", fontsize=14)
        cursor += width + 0.13
    notation = "{" + ", ".join("{" + ",".join(map(str, b)) + "}" for b in partition) + "}"
    ax.text(x, y - 0.53, notation, ha="center", va="center", fontsize=13)


def main():
    partitions = enumerate_partitions(3)
    assert len(partitions) == 5
    assert [sum(len(p) == k for p in partitions) for k in (1, 2, 3)] == [1, 3, 1]
    fig, ax = plt.subplots(figsize=(10.4, 6.4), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.03, top=0.98)
    ax.set(xlim=(0, 10), ylim=(0, 6.1))
    ax.axis("off")
    ax.text(5, 5.78, "All five set partitions of {1, 2, 3}", ha="center", fontsize=20, weight="bold")
    ax.text(5, 5.37, "Exact enumeration • elements are distinct; blocks are unnamed", ha="center", fontsize=13)
    for k, y in [(1, 4.4), (2, 2.8), (3, 1.2)]:
        row = [p for p in partitions if len(p) == k]
        label = (f"{k} block" + ("s" if k > 1 else "") + f"   →   {len(row)} "
                 + ("possibility" if len(row) == 1 else "possibilities"))
        ax.text(0.08, y + 0.53, label, fontsize=12, color="#333333")
        positions = [5] if len(row) == 1 else [1.7, 5, 8.3]
        for p, x in zip(row, positions):
            draw_partition(ax, p, x, y)
    ax.text(5, 0.12, "Reordering blocks or elements within a block gives the same partition.", ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
