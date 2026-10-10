"""Draw the Chance–Williams apparatus and qualitative response, without traces.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle


def main():
    fig, ax = plt.subplots(figsize=(12, 6.6), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 12), ylim=(0, 7))
    ax.axis("off")
    blue, orange = "#2466a1", "#bc6220"

    def text(x, y, s, size=12, **kw):
        ax.text(x, y, s, ha="center", va="center", fontsize=size,
                color="#24313d", **kw)

    def arrow(a, b, color=blue, style="-|>"):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=15,
                                    lw=1.8, color=color))

    def box(x, y, w, h, s, color="#edf3f8", size=12):
        ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                                   boxstyle="round,pad=0.05", facecolor=color,
                                   edgecolor="#627687", lw=1.2))
        text(x, y, s, size)

    text(6, 6.63, "Respiratory control: apparatus and inference", 18, weight="bold")
    text(2.9, 6.13, "1955 experiment: vibrating platinum electrode", 12)
    # Open cuvette: intentionally no lid, oxygen-permeable film or Clark cell.
    ax.add_patch(Rectangle((1.0, 2.1), 3.9, 2.8, facecolor="#e8f3fa", edgecolor="none"))
    ax.plot([1, 1, 4.9, 4.9], [5.3, 1.95, 1.95, 5.3], color="#556b7c", lw=2)
    ax.plot([1, 4.9], [4.9, 4.9], color="#68a6c7", lw=1)
    text(2.2, 5.27, "open to air", 11)
    arrow((2.2, 5.65), (2.2, 4.96), orange, "<->")
    text(2.9, 2.56, "isolated liver mitochondria\nsubstrate + phosphate\nisotonic medium", 11)
    text(2.9, 1.63, "1 mL optical cuvette", 11)
    # Top-down cartoon places the platinum tip beside the optical beam.
    arrow((0.25, 3.9), (5.45, 3.9), "#ab841c")
    text(2.65, 4.12, "optical path", 10)
    ax.plot([4.1, 4.1], [5.6, 4.47], color="#585b67", lw=3)
    ax.plot(4.1, 4.45, "o", color="#585b67", markersize=5)
    arrow((3.75, 5.55), (4.45, 5.55), orange, "<->")
    text(4.15, 5.96, "Pt tip vibrates", 11)
    arrow((3.15, 5.75), (3.15, 4.92), orange)
    text(3.15, 5.97, "ADP", 11)
    box(4.25, 3.13, 1.03, 0.45, "Pt tip", size=10)
    arrow((4.25, 3.4), (4.1, 4.36), "#585b67")

    box(6.2, 4.47, 1.72, 1.28, "electrode current\n→ calibrated O₂\n→ recorder", size=10.5)
    arrow((4.35, 4.55), (5.29, 4.55))
    text(9.5, 6.11, "Reported response to repeated ADP additions", 12)
    stages = [(5.27, "Before ADP: slow O₂ consumption"),
              (4.27, "ADP added: faster O₂ consumption"),
              (3.27, "ADP used: slow O₂ consumption"),
              (2.27, "Another ADP addition: faster again")]
    for y, s in stages:
        box(9.6, y, 4.1, 0.67, s, size=10.5)
    for y in (4.8, 3.8, 2.8):
        arrow((9.6, y+0.04), (9.6, y-0.13))
    arrow((7.1, 4.47), (7.47, 4.47))

    box(3.3, 0.82, 5.5, 0.92,
        "Instrument check: oxygen calibration\nBiological comparison: delayed substrate addition", size=11)
    box(9.2, 0.82, 5.0, 0.92,
        "Limits: oxygen entry, dilution and sensitivity shifts\nO₂ consumption does not directly count ATP", color="#fcf2e9", size=11)
    text(6, 0.12, "Original schematic; boxes encode no measured concentrations, slopes or times.", 10)
    fig.subplots_adjust(left=0.015, right=0.985, top=0.98, bottom=0.025)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
