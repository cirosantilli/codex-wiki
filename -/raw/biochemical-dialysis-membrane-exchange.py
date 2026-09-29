"""Original dialysis schematic; run from _media (Python 3.14, matplotlib 3.10)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle


def ion(ax, x, y, sign):
    color = "#137caf" if sign == "+" else "#c45b19"
    ax.add_patch(Circle((x, y), 0.105, facecolor=color, edgecolor="white", lw=0.7))
    ax.text(x, y, sign, ha="center", va="center", color="white", fontsize=11, weight="bold")


def protein(ax, x, y, radius=0.29):
    ax.add_patch(Circle((x, y), radius, facecolor="#7852a5", edgecolor="#4f3275", lw=1.2))
    ax.text(x, y, "P", ha="center", va="center", color="white", fontsize=15, weight="bold")


def arrow(ax, start, end, color="#334c62", style="->", lw=1.7):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=13, lw=lw, color=color))


def main():
    fig, ax = plt.subplots(figsize=(10.4, 5.7), dpi=120, facecolor="white")
    ax.set(xlim=(0, 12), ylim=(0, 6.5))
    ax.set_axis_off()
    ax.text(6, 6.18, "Dialysis: change the solution around a retained protein", ha="center", fontsize=17, weight="bold")
    ax.add_patch(Rectangle((0.45, 1.4), 4.8, 3.9, facecolor="#eaf5fa", edgecolor="#59758a", lw=1.4))
    ax.text(2.85, 5.0, "External bath (dialysate)", ha="center", fontsize=12)
    bag = FancyBboxPatch((1.35, 2.02), 2.0, 2.27, boxstyle="round,pad=0.05,rounding_size=0.28", facecolor="white", edgecolor="#52656e", lw=3)
    ax.add_patch(bag)
    ax.text(2.35, 3.95, "Sample", ha="center", fontsize=12)
    protein(ax, 1.86, 3.08)
    protein(ax, 2.7, 2.7)
    for x, y, sign in [(2.55, 3.48, "+"), (2.95, 3.1, "−"), (1.7, 2.47, "+"), (2.2, 2.65, "−"), (2.97, 3.62, "+"), (2.17, 3.54, "−"), (4.3, 3.6, "+"), (4.45, 2.35, "−")]:
        ion(ax, x, y, sign)
    arrow(ax, (3.48, 3.15), (4.1, 3.15))
    ax.text(4.22, 2.95, "Net salt\nmovement", fontsize=10, ha="center", va="top")
    ax.text(2.85, 1.73, "Bag wall = semipermeable membrane", ha="center", fontsize=10)
    ax.text(2.85, 0.83, "Fresh bath removes escaped salt\nand renews the concentration difference", ha="center", fontsize=11)
    arrow(ax, (3.4, 4.15), (6.08, 5.35), color="#8a979f", lw=1.1)
    arrow(ax, (3.4, 2.18), (6.08, 1.75), color="#8a979f", lw=1.1)
    ax.text(6.9, 5.65, "Enlarged wall", ha="center", fontsize=12, weight="bold")
    ax.text(5.85, 4.77, "Sample side", ha="center", fontsize=11)
    ax.text(8.02, 5.08, "Bath side", ha="left", fontsize=11)
    # Openings represent passage schematically, not measured pore geometry.
    for low, high in [(1.7, 2.78), (3.2, 3.9), (4.32, 4.92)]:
        ax.add_patch(Rectangle((6.5, low), 0.75, high - low, facecolor="#cbd4d9", edgecolor="#52656e", lw=1))
    ion(ax, 5.9, 4.1, "+")
    ion(ax, 7.82, 2.97, "−")
    arrow(ax, (6.08, 4.1), (7.72, 4.1), color="#137caf")
    arrow(ax, (7.62, 2.99), (5.96, 2.99), color="#c45b19")
    protein(ax, 5.85, 2.12, radius=0.34)
    arrow(ax, (6.23, 2.12), (6.43, 2.12), color="#7852a5")
    ax.plot([6.45, 6.45], [1.94, 2.30], color="#7852a5", lw=2.5)
    ax.text(8.12, 4.09, "Small salt ions cross\nin both directions", fontsize=12, va="center")
    ax.text(8.12, 2.22, "Large protein\nis retained", fontsize=12, va="center", color="#624089")
    ax.text(8.3, 0.8, "Schematic only: symbols and gaps are not to scale.\nMWCO is a retention rating, not a sharp pore diameter.", ha="center", fontsize=10, color="#46535d")
    fig.subplots_adjust(left=0.015, right=0.99, bottom=0.015, top=0.99)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
