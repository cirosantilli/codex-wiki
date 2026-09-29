"""Original teaching diagram; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG basename to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def box(ax, xy, width, height, text, color, size=12):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor="#334155", linewidth=1.3))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=size, color="#172033")


def arrow(ax, start, end, color="#334155"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=17, linewidth=1.7, color=color))


def main():
    va, pte_bytes, page_bytes = 0x1234, 4, 256
    i, j, offset = va >> 12, (va >> 8) & 15, va & 255
    root_record, leaf_record = 0x8000 + i * pte_bytes, 0x9000 + j * pte_bytes
    pa = 7 * page_bytes + offset
    assert (i, j, offset, root_record, leaf_record, pa) == (1, 2, 52, 0x8004, 0x9008, 0x0734)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6.6), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.6))
    ax.axis("off")
    ax.text(5, 6.3, "Two-level address walk: user read at 0x1234",
            ha="center", fontsize=17, weight="bold")
    ax.text(5, 5.9, "Chosen model: 16-bit addresses · 256-byte pages · 4-byte entries",
            ha="center", fontsize=12)
    box(ax, (0.7, 4.8), 2.1, 0.75, f"bits 15–12: {i:04b}\nroot index = {i}", "#dbeafe")
    box(ax, (2.85, 4.8), 2.1, 0.75, f"bits 11–8: {j:04b}\nlower index = {j}", "#dcfce7")
    box(ax, (5, 4.8), 4.25, 0.75, f"bits 7–0: {offset:08b}\noffset = 0x{offset:02x} = {offset} bytes", "#fff1cf")
    arrow(ax, (1.75, 4.75), (1.75, 3.65))
    arrow(ax, (3.9, 4.75), (5.15, 3.65), "#15803d")
    box(ax, (0.45, 2.0), 3.0, 1.6,
        f"ROOT TABLE · base 0x8000\nentry [{i}] at 0x{root_record:04x}\n→ lower table 0x9000\npresent · user · R/W · no X", "#dbeafe", 12)
    box(ax, (4.05, 2.0), 3.0, 1.6,
        f"LOWER TABLE · base 0x9000\nentry [{j}] at 0x{leaf_record:04x}\n→ data frame 0x07\npresent · user · R only · no X", "#dcfce7", 12)
    arrow(ax, (3.48, 2.8), (4.0, 2.8))
    ax.text(3.74, 3.85, "1. read pointer", ha="center", fontsize=11)
    box(ax, (7.7, 2.0), 1.85, 1.6,
        "DATA FRAME\nbase 0x0700\n+ offset 0x34\n= 0x0734", "#fff1cf", 12)
    arrow(ax, (7.08, 2.8), (7.65, 2.8))
    ax.text(7.35, 3.85, "2. read mapping", ha="center", fontsize=11)
    arrow(ax, (8.6, 4.75), (8.6, 3.65), "#a16207")
    box(ax, (0.65, 0.65), 8.65, 0.85,
        "User read allowed at BOTH entries → read data byte 0x0734\nUser write denied by lower entry → protection fault", "#f1f5f9", 13)
    ax.text(5, 0.18, "Table records are at 0x8004 and 0x9008; the requested data is at 0x0734.",
            ha="center", fontsize=11)
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
