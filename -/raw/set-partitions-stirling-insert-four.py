"""Construct the seven two-block partitions of four elements, exactly.

Python 3.14 / Matplotlib 3.10. Run from _media. Gold marks element 4;
block colours and left-to-right positions are drawing aids, not labels.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def canonical(blocks):
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def insert(partition, element, block_index):
    return canonical([block + (element,) if i == block_index else block
                      for i, block in enumerate(partition)])


def draw_partition(ax, partition, x, y):
    colours = ["#1b6d97", "#975725"]
    widths = [0.39 * len(block) + 0.14 for block in partition]
    total = sum(widths) + 0.12 * (len(widths) - 1)
    cursor = x - total / 2
    for block, width, colour in zip(partition, widths, colours):
        ax.add_patch(FancyBboxPatch(
            (cursor, y - 0.27), width, 0.54,
            boxstyle="round,pad=0.02,rounding_size=0.10",
            linewidth=1.8, edgecolor=colour, facecolor="white",
        ))
        for j, element in enumerate(block):
            px = cursor + 0.265 + 0.39 * j
            ax.add_patch(Circle((px, y), 0.155,
                               facecolor="#ffcf5c" if element == 4 else "#edf3f7",
                               edgecolor="#9c6900" if element == 4 else "none"))
            ax.text(px, y, str(element), ha="center", va="center", fontsize=13)
        cursor += width + 0.12


def main():
    sources = [((1, 2), (3,)), ((1, 3), (2,)), ((1,), (2, 3))]
    outputs = [insert(p, 4, j) for p in sources for j in range(2)]
    singleton_case = ((1, 2, 3), (4,))
    assert len(set(outputs + [singleton_case])) == 7
    assert all(any(4 in block and len(block) > 1 for block in p) for p in outputs)
    assert all(sorted(e for block in p for e in block) == [1, 2, 3, 4]
               for p in outputs + [singleton_case])
    assert sum(sorted(map(len, p)) == [1, 3] for p in outputs + [singleton_case]) == 4
    fig, ax = plt.subplots(figsize=(11.2, 7.6), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    ax.set(xlim=(0, 11), ylim=(0, 7.2))
    ax.axis("off")
    ax.text(5.5, 6.9, "Build every two-block partition of {1, 2, 3, 4}", ha="center", fontsize=19, weight="bold")
    ax.text(5.5, 6.5, "Exact construction: S(4, 2) = 2 S(3, 2) + S(3, 1) = 6 + 1", ha="center", fontsize=14)
    ax.text(1.9, 5.93, "Start with 2 blocks", ha="center", fontsize=13, weight="bold")
    ax.text(6, 5.93, "Insert 4 in first block", ha="center", fontsize=13, weight="bold")
    ax.text(9.2, 5.93, "Insert 4 in second block", ha="center", fontsize=13, weight="bold")
    for i, (p, y) in enumerate(zip(sources, [5.3, 4.3, 3.3])):
        draw_partition(ax, p, 1.9, y)
        draw_partition(ax, outputs[2 * i], 6, y)
        draw_partition(ax, outputs[2 * i + 1], 9.2, y)
        ax.annotate("", xy=(4.64, y), xytext=(3.15, y),
                    arrowprops={"arrowstyle": "->", "color": "#56616a", "lw": 1.5})
    ax.plot([0.35, 10.65], [2.65, 2.65], color="#bbbbbb", lw=1)
    ax.text(5.5, 2.24, "The remaining case: give 4 its own singleton block", ha="center", fontsize=14, weight="bold")
    draw_partition(ax, ((1, 2, 3),), 1.9, 1.65)
    ax.annotate("", xy=(5.15, 1.65), xytext=(3.15, 1.65),
                arrowprops={"arrowstyle": "->", "color": "#56616a", "lw": 1.5})
    draw_partition(ax, singleton_case, 6.5, 1.65)
    ax.text(1.9, 1.06, "S(3, 1) = 1", ha="center", fontsize=13)
    ax.text(6.5, 1.06, "{{1,2,3}, {4}}", ha="center", fontsize=13)
    ax.text(5.5, 0.53, "Gold marks the distinguished element 4. Each outcome appears exactly once.", ha="center", fontsize=12)
    ax.text(5.5, 0.16, "Block order and colours are display conventions; the blocks remain unnamed.", ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
