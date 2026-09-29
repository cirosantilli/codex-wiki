"""Original sparse table diagram; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG basename to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def box(ax, xy, width, height, text, color, size=12):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor="#334155", linewidth=1.2))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=size, color="#172033")


def arrow(ax, start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=16, linewidth=1.5, color="#334155"))


def main():
    clustered, scattered = [0x12, 0x13, 0xa0, 0xa1], [0x12, 0x42, 0x72, 0xa2]
    groups = [len({p // 16 for p in pages}) for pages in (clustered, scattered)]
    nodes = np.array([1 + g for g in groups])
    compact, allocated = nodes * 64, nodes * 256
    assert groups == [2, 4] and list(compact) == [192, 320] and list(allocated) == [768, 1280]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(10, 7.4), dpi=120, facecolor="white")
    ax = fig.add_axes((0.02, 0.49, 0.96, 0.49))
    ax.set(xlim=(0, 10), ylim=(0, 4))
    ax.axis("off")
    ax.text(5, 3.8, "Sparse allocation counts every table node, including the root",
            ha="center", fontsize=16, weight="bold")
    box(ax, (0.5, 1.35), 2.3, 1.7,
        "ROOT · 0x8000\n[1] → 0x9000\n[10] → 0xa000\n14 absent entries", "#dbeafe", 12)
    box(ax, (3.6, 2.25), 2.9, 0.95,
        "TABLE · 0x9000\n[2] → frame 0x07; [3] → 0x02", "#dcfce7", 11)
    box(ax, (3.6, 0.95), 2.9, 0.95,
        "TABLE · 0xa000\n[0] → frame 0x05; [1] → 0x06", "#dcfce7", 11)
    arrow(ax, (2.83, 2.45), (3.55, 2.73))
    arrow(ax, (2.83, 1.9), (3.55, 1.43))
    box(ax, (7.0, 1.35), 2.5, 1.7,
        "4 DATA FRAMES\n0x07, 0x02, 0x05, 0x06\n4 × 256 = 1024 bytes\nseparate from tables", "#fff1cf", 11)
    arrow(ax, (6.53, 2.73), (6.95, 2.45))
    arrow(ax, (6.53, 1.43), (6.95, 1.9))
    ax.text(5, 0.48, "Each lower table also has 14 absent entries. No other table nodes are allocated.",
            ha="center", fontsize=11)
    plot = fig.add_axes((0.13, 0.14, 0.83, 0.30))
    x = np.arange(3)
    packed = np.append(compact, 1024)
    rounded = np.append(allocated, 1024)
    b1 = plot.bar(x - 0.18, packed, 0.36, color="#60a5fa", label="Compact: 64 bytes / node")
    b2 = plot.bar(x + 0.18, rounded, 0.36, color="#4ade80", label="Dedicated 256-byte frame / node")
    plot.bar_label(b1, padding=3, fontsize=11)
    plot.bar_label(b2, padding=3, fontsize=11)
    plot.set_xticks(x, ["4 pages in 2 regions\nroot + 2 tables = 3 nodes",
                       "4 pages in 4 regions\nroot + 4 tables = 5 nodes",
                       "Single-level table\n256 entries × 4 bytes"])
    plot.set_ylabel("Table storage (bytes)")
    plot.set_ylim(0, 1570)
    plot.spines[["top", "right"]].set_visible(False)
    plot.set_axisbelow(True)
    plot.grid(axis="y", color="#e2e8f0")
    plot.legend(loc="upper left", fontsize=10, frameon=False)
    fig.text(0.5, 0.027, "Same four data frames in both sparse layouts; allocator metadata and TLB storage excluded.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
