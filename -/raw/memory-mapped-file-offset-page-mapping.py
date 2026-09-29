"""Draw file-offset translation for two-page mappings; save matching PNG to CWD.

Original teaching model, not a measured memory layout or benchmark.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


PAGE_SIZE = 4096
FILE_START = PAGE_SIZE
LENGTH = 2 * PAGE_SIZE
DISPLACEMENT = PAGE_SIZE + 37
BASES = (0x10000000, 0x20000000, 0x30000000)


def translation(base, address):
    displacement = address - base
    if not 0 <= displacement < LENGTH:
        raise ValueError("Address outside the modeled mapping")
    page, within = divmod(displacement, PAGE_SIZE)
    return FILE_START + displacement, page, within


def main():
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.4))
    ax.axis("off")
    ink, blue, purple = "#203448", "#2166ac", "#7952a3"

    def box(x, y, width, height, label, edge, fill):
        ax.add_patch(FancyBboxPatch(
            (x, y), width, height, boxstyle="round,pad=0.03",
            facecolor=fill, edgecolor=edge, linewidth=1.4,
        ))
        ax.text(x + width / 2, y + height / 2, label,
                ha="center", va="center", fontsize=10.5, color=ink,
                linespacing=1.4)

    ax.text(5, 6.08, "One file range, three mappings in two processes",
            ha="center", fontsize=16, weight="bold", color=ink)
    ax.text(5, 5.7, "Toy layout • page size 4096 bytes • file offset O = 4096 • length 8192 bytes",
            ha="center", fontsize=10.5, color=ink)
    for x, title, base, color in [
        (0.3, "Process A: shared", BASES[0], blue),
        (3.65, "Process B: shared", BASES[1], blue),
        (7, "Process B: private", BASES[2], purple),
    ]:
        ax.text(x + 1.35, 5.2, title, ha="center", fontsize=12,
                weight="bold", color=color)
        box(x, 4.15, 2.7, .8, f"Relative page 0\nbase 0x{base:08x}", color, "#f1f5fa")
        box(x, 3.05, 2.7, .8,
            f"Relative page 1\nbase 0x{base + PAGE_SIZE:08x}\nx: 0x{base + DISPLACEMENT:08x}",
            color, "#e9f1fa")
        for y, target, dash in [(4.15, (2.25, 1.65), "--"),
                                (3.05, (7.25, 1.65), "-")]:
            ax.add_patch(FancyArrowPatch(
                (x + 1.35, y - .06), target, arrowstyle="-|>",
                mutation_scale=13, linewidth=1.3, color=color,
                linestyle=dash, alpha=.8, zorder=0,
            ))
    box(.4, .85, 3.7, .75, "Backing page: offsets 4096–8191\nrelative page 0", ink, "#f0f3f5")
    box(5.4, .85, 3.7, .75, "Backing page: offsets 8192–12287\nx at 8229; adjacent y at 8230", ink, "#edf4ee")
    ax.text(5, .48, "r = 4133 = 1 × 4096 + 37; file offset = O + r = 8229 (0x2025)",
            ha="center", fontsize=11.5, weight="bold", color=ink)
    ax.text(5, .16, "Arrows identify backing contents before private writes; page tables separately choose resident frames.",
            ha="center", fontsize=9.6, color=ink)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
