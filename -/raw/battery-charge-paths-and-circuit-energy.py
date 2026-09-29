"""Original battery transport/circuit/work schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; writes its matching basename PNG to the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle


def arrow(ax, start, end, color, label=None, label_xy=None):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "lw": 2, "color": color})
    if label:
        ax.text(*label_xy, label, color=color, ha="center", va="center", fontsize=11)


def box(ax, xy, width, height, text, color):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.08",
                              facecolor="white", edgecolor=color, linewidth=1.7))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=12, color=color)


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.8, 7.5), facecolor="white")
    left = fig.add_axes([0.03, 0.44, 0.46, 0.47])
    right = fig.add_axes([0.53, 0.44, 0.44, 0.47])
    bottom = fig.add_axes([0.03, 0.03, 0.94, 0.29])
    for ax in (left, right, bottom):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis("off")
    fig.suptitle("Battery discharge: charge paths and available electrical work", fontsize=16, y=0.98)

    left.set_title("Physical transport (schematic)", fontsize=13, pad=8)
    left.add_patch(Rectangle((0.6, 0.6), 8.8, 3.1, facecolor="#f3f8fb", edgecolor="#71828a"))
    left.text(5, 1.05, "Electrolyte: mobile ions", ha="center")
    for x, name in [(1.7, "− anode\noxidation"), (8.3, "+ cathode\nreduction")]:
        left.add_patch(Rectangle((x - 0.45, 1.4), 0.9, 2.65, color="#aab5be"))
        left.text(x, 0.12, name, ha="center", va="top")
    left.plot([1.7, 1.7, 4], [4.05, 6.6, 6.6], color="#333333", lw=2)
    left.plot([6, 8.3, 8.3], [6.6, 6.6, 4.05], color="#333333", lw=2)
    left.add_patch(Rectangle((4, 6.22), 2, 0.76, fill=False, edgecolor="#333333", lw=2))
    left.text(5, 6.6, "Load", ha="center", va="center")
    arrow(left, (2.5, 7.45), (7.5, 7.45), "#176da3", "Electron motion in wire", (5, 7.85))
    arrow(left, (7.5, 5.4), (2.5, 5.4), "#9a3d27", "Conventional current outside", (5, 4.85))
    arrow(left, (2.7, 2.65), (7.3, 2.65), "#38814a", "Net ionic current inside", (5, 3.28))
    left.text(5, -0.7, "Electrode reactions join the paths;\nno electron loops through the electrolyte.",
              ha="center", va="top", fontsize=10)

    right.set_title("Terminal model for a short interval", fontsize=13, pad=8)
    right.add_patch(Rectangle((0.4, 1.0), 4.9, 6.3, fill=False, edgecolor="#71828a", ls="--"))
    right.text(2.85, 0.5, "Battery boundary", ha="center", color="#536570")
    right.plot([2.8, 2.8], [1.9, 3.5], color="#333333", lw=2)
    right.add_patch(Circle((2.8, 4.2), 0.7, fill=False, edgecolor="#333333", lw=2))
    right.text(2.8, 4.2, "+\n−", ha="center", va="center", fontsize=12)
    right.text(0.9, 4.2, "$\\mathcal{E}=3$ V", ha="center")
    right.plot([2.8, 2.8], [4.9, 5.25], color="#333333", lw=2)
    right.add_patch(Rectangle((2.42, 5.25), 0.76, 1.0, fill=False, edgecolor="#333333", lw=2))
    right.text(0.95, 5.75, "$r=1$ Ω", ha="center")
    right.plot([2.8, 2.8, 7.5, 7.5], [6.25, 6.8, 6.8, 5.0], color="#333333", lw=2)
    right.add_patch(Rectangle((7.12, 3.35), 0.76, 1.65, fill=False, edgecolor="#333333", lw=2))
    right.text(8.7, 4.55, "$R=4$ Ω", ha="center")
    right.text(8.7, 3.75, "$V_L=2.4$ V", ha="center")
    right.plot([7.5, 7.5, 2.8], [3.35, 1.9, 1.9], color="#333333", lw=2)
    right.plot([5.5, 5.5], [6.8, 1.9], "o", color="#333333", ms=5)
    right.text(5.7, 6.25, "+", fontsize=13)
    right.text(5.7, 2.25, "−", fontsize=13)
    arrow(right, (5.65, 7.55), (7.35, 7.55), "#9a3d27", "$I=0.6$ A", (6.5, 7.95))
    right.text(5, -0.7, "The ideal source symbol approximates a finite\nchemical reservoir; it does not create energy.",
               ha="center", va="top", fontsize=10)

    bottom.text(5, 7.15, "Available electrical work per 1 coulomb through the load", ha="center", fontsize=13)
    box(bottom, (0.2, 2.2), 2.9, 3.2, "Chemical free-energy\ndecrease: 3.0 J\n(short-interval model)", "#176da3")
    box(bottom, (6.6, 4.0), 3.0, 2.25, "Delivered to load\n2.4 J", "#38814a")
    box(bottom, (6.6, 0.6), 3.0, 2.25, "Internal dissipation\n0.6 J", "#9a3d27")
    arrow(bottom, (3.3, 4.2), (6.4, 5.1), "#38814a")
    arrow(bottom, (3.3, 3.1), (6.4, 1.7), "#9a3d27")
    bottom.text(4.85, 6.1, "3.0 = 2.4 + 0.6 J", ha="center", fontsize=12)
    bottom.text(5, -0.25, "Stipulated values; transport arrows are not a map of energy propagation. Complete thermal budgets also include reaction entropy.",
                ha="center", va="top", fontsize=9)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
