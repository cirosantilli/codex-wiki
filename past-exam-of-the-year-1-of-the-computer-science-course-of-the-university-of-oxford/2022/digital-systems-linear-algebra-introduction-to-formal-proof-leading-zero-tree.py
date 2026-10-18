"""Original leading-zero summary tree. Python 3.14, matplotlib 3.10.

Write the identically named PNG to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(8, 4.4), dpi=100, facecolor="white")
    ax.set(xlim=(-0.6, 7.6), ylim=(-0.5, 3.9))
    ax.axis("off")
    bits = "00000101"
    positions = []
    for level in range(4):
        length = 2**level
        nodes = []
        for start in range(0, 8, length):
            block = bits[start:start + length]
            count = len(block) - len(block.lstrip("0"))
            value = format(count, f"0{level + 1}b")
            nodes.append((start + (length - 1) / 2, level, value, length))
        positions.append(nodes)
    for level in range(1, 4):
        for index, (x, y, _, _) in enumerate(positions[level]):
            for child in positions[level - 1][2 * index:2 * index + 2]:
                highlighted = level == 3 and child[0] > x
                ax.plot([child[0], x], [child[1] + 0.20, y - 0.24],
                        color="#c65f13" if highlighted else "#a8b3bd",
                        linewidth=2.5 if highlighted else 1.2, zorder=1)
    for level, nodes in enumerate(positions):
        for x, y, value, length in nodes:
            selected = (level == 3 or (level == 2 and x > 3.5))
            width = 0.64 if level == 0 else 1.12
            rect = FancyBboxPatch(
                (x - width / 2, y - 0.22), width, 0.44,
                boxstyle="round,pad=0.04", linewidth=1.4,
                facecolor="#fff0df" if selected else "#edf5fc",
                edgecolor="#c65f13" if selected else "#466b88", zorder=2)
            ax.add_patch(rect)
            text = value if level == 0 else f"{length} bits: {value}"
            ax.text(x, y, text, ha="center", va="center", fontsize=11,
                    family="DejaVu Sans Mono", zorder=3)
    ax.text(3.5, 3.7, "Leading-zero counts for 00000101", ha="center",
            fontsize=15, weight="bold", color="#18364c")
    ax.text(3.5, -0.43, "Input bits:   0      0      0      0      0      1      0      1",
            ha="center", fontsize=10, family="DejaVu Sans Mono", color="#34495e")
    ax.text(3.5, 3.37, "Root: 0101 = 5      First output bit = all-zero flag",
            ha="center", fontsize=11)
    fig.subplots_adjust(left=0.04, right=0.98, bottom=0.08, top=0.98)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white",
                transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
