"""Draw schematic DMA payload and control paths; no real hardware operations.

Tested with Python 3.14.4, Matplotlib 3.10.7.
Run from _media; the opaque matching PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=110, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 8))
    ax.axis("off")
    ink, blue, orange = "#203040", "#155d8a", "#a84b12"

    def text(x, y, label, size=12, color=ink, weight="normal", background=False):
        ax.text(x, y, label, ha="center", va="center", fontsize=size,
                color=color, weight=weight, linespacing=1.4, zorder=6,
                bbox=dict(facecolor="white", edgecolor="none", pad=2)
                if background else None)

    def box(x, y, w, h, label, color=blue):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                                   facecolor="#f5f8fb", edgecolor=color, linewidth=1.7))
        text(x + w / 2, y + h / 2, label, 13, color)

    def arrow(start, end, control=False, curve=0):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                   mutation_scale=19, linewidth=1.9 if control else 3.3,
                                   linestyle="--" if control else "-",
                                   color=orange if control else blue,
                                   connectionstyle=f"arc3,rad={curve}"))

    text(6, 7.65, "DMA: separate data movement from CPU control", 18, weight="bold")
    text(6, 7.15, "Toy receive operation: four bytes A, B, C, D", 12)
    box(4.3, 5.6, 3.4, 1.0, "CPU running driver code", orange)
    box(0.65, 2.9, 2.8, 1.0, "Device with\nDMA engine")
    box(4.55, 2.9, 2.9, 1.0, "Optional IOMMU\ntranslation / protection")
    box(8.55, 2.9, 2.8, 1.0, "Memory buffer\n[A] [B] [C] [D]")

    arrow((4.28, 6.05), (1.35, 3.98), True, 0.18)
    text(1.7, 5.9, "1. Setup:\naddress, length, direction", 11, orange, background=True)
    arrow((3.0, 3.98), (5.25, 5.55), True, 0.08)
    text(5.9, 4.7, "3. Completion\nnotification", 11, orange, background=True)
    arrow((7.72, 6.02), (10.5, 3.98), True, -0.12)
    text(10.4, 6.15, "CPU still coordinates\nbuffer ownership,\ncaches and mappings", 11, orange, background=True)

    arrow((3.55, 3.4), (4.45, 3.4))
    arrow((7.55, 3.4), (8.45, 3.4))
    text(6, 2.35, "2. Payload data: device → memory", 14, blue, "bold")
    text(6, 1.9, "No per-item CPU copy on this path; interconnect details omitted.", 11)
    text(6, 1.45, "Dashed orange = CPU setup / completion / coordination", 11, orange)
    text(6, 1.05, "Solid blue = payload transfer", 11, blue)
    text(6, 0.55, "Completion may use an interrupt or be polled. DMA is not an interrupt.", 11)
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
