"""Functional thermionic-emission schematic; Python 3.14, matplotlib 3.10.7.

Run from _media. No historical dimensions or instrument performance implied.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10, 6.1), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.1), aspect="equal")
    ax.axis("off")
    blue, orange, gray = "#165e99", "#d35416", "#4d5966"
    ax.text(5, 5.86, "Thermionic emission: supply, collection, and readout",
            ha="center", fontsize=16, weight="bold")
    ax.add_patch(FancyBboxPatch((0.5, 1.75), 6.3, 3.45,
                               boxstyle="round,pad=0.02,rounding_size=0.25",
                               facecolor="white", edgecolor=gray, linewidth=1.7))
    ax.text(0.85, 4.86, "Evacuated vessel", color=gray)
    # Longitudinal section through a cylindrical collector: two walls.
    ax.plot([1.65, 5.8], [4.35, 4.35], color=blue, lw=7, solid_capstyle="butt")
    ax.plot([1.65, 5.8], [2.6, 2.6], color=blue, lw=7, solid_capstyle="butt")
    ax.text(3.7, 4.55, "Surrounding metal collector", ha="center", color=blue)
    ax.plot([0.13, 1.5], [3.5, 3.5], color=orange, lw=2)
    ax.plot([1.5, 5.65], [3.5, 3.5], color=orange, lw=5)
    ax.plot([5.65, 6.15, 6.15, 7.25], [3.5, 3.5, 2.05, 2.05], color=orange, lw=2)
    ax.text(3.6, 3.66, "Heated wire", ha="center", color=orange)
    for x in [2.0, 3.1, 4.2, 5.3]:
        for y in [2.76, 4.18]:
            ax.add_patch(FancyArrowPatch((x, 3.42 if y < 3.5 else 3.56), (x, y),
                         arrowstyle="-|>", mutation_scale=14, color=blue, lw=1.5))
    ax.plot([5.8, 7.7, 7.7], [4.35, 4.35, 4.0], color=blue, lw=1.8)
    ax.add_patch(Circle((7.7, 3.7), 0.3, facecolor="white", edgecolor=blue, lw=1.8))
    ax.text(7.7, 3.7, "G", ha="center", va="center", color=blue)
    ax.plot([7.7, 7.7], [3.4, 2.9], color=blue, lw=1.8)
    for y, w in [(2.9, .34), (2.81, .24), (2.72, .13)]:
        ax.plot([7.7-w/2, 7.7+w/2], [y, y], color=blue, lw=1.8)
    ax.text(8.15, 3.86, "Collector current", va="center", fontsize=11)
    ax.text(8.15, 3.56, "readout", va="center", fontsize=11)
    ax.text(8.15, 3.16, "G: galvanometer", fontsize=10)
    ax.annotate("To pump", xy=(0.57, 2.2), xytext=(0.05, 1.25), color=gray,
                arrowprops={"arrowstyle": "->", "color": gray}, fontsize=11)
    ax.annotate("Heating supply and\nwire-resistance readout", xy=(6.65, 2.05),
                xytext=(7.35, 1.86), color=orange, fontsize=11,
                arrowprops={"arrowstyle": "->", "color": orange})
    ax.text(3.8, 2.24, "Wire biased negative relative to collector", ha="center", fontsize=11)
    ax.text(.65, .77, "Arrows: outgoing electrons. Vary collecting bias to test complete collection.",
            fontsize=12)
    ax.text(.65, .34, "Functional schematic; layout simplified and not to scale.",
            fontsize=11, color=gray)
    fig.subplots_adjust(left=.015, right=.985, bottom=.025, top=.985)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
