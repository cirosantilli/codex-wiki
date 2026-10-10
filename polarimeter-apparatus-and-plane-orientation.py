"""Original polarimeter schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes this script's basename.png to the working directory.
All numerical material properties are stipulated, not measured.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11, 6.4), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.10, top=0.84)
    ax.set(xlim=(0, 11), ylim=(0, 5), aspect="equal")
    ax.axis("off")
    blue, orange, gray = "#2463A6", "#C45B15", "#475569"
    fig.suptitle("Optical activity: the field direction turns", fontsize=20, y=0.965)
    fig.text(0.5, 0.905, "Original ideal schematic · horizontal layout for clarity · not to scale",
             ha="center", color=gray)

    stages = [(0.75, 1.15, "Light source", "589 nm"),
              (2.75, 0.50, "Fixed polarizer", "pass axis: 0°"),
              (5.10, 2.15, "Sample tube", "path: 1 dm"),
              (7.70, 0.50, "Analyzer", "rotatable axis: θ"),
              (9.75, 1.10, "Detector", "intensity readout")]
    y = 3.65
    for x, width, title, subtitle in stages:
        ax.add_patch(FancyBboxPatch((x-width/2, y-0.36), width, 0.72,
                                   boxstyle="round,pad=0.04", facecolor="#F1F5F9",
                                   edgecolor=gray, linewidth=1.4))
        ax.text(x, y+0.57, title, ha="center", weight="bold")
        ax.text(x, y-0.68, subtitle, ha="center", fontsize=10.5, color=gray)
    for left, right in [(1.37, 2.45), (3.05, 3.95), (6.25, 7.40), (8.0, 9.15)]:
        ax.annotate("", xy=(right, y), xytext=(left, y),
                    arrowprops={"arrowstyle": "-|>", "color": blue, "lw": 2})
    ax.text(5.10, y, "solution", ha="center", color=blue)
    ax.text(5.5, 4.75, "Light travels from source to detector  →", ha="center", color=blue)
    for x, angle in [(2.75, 0), (7.70, 8)]:
        phi = np.deg2rad(angle)
        ax.plot([x-0.27*np.sin(phi), x+0.27*np.sin(phi)],
                [y-0.27*np.cos(phi), y+0.27*np.cos(phi)], color=orange, lw=3)

    cx, cy, radius = 2.15, 1.35, 0.95
    ax.add_patch(Circle((cx, cy), radius, fill=False, edgecolor="#CBD5E1", lw=1.5))
    ax.plot([cx, cx], [cy-radius, cy+radius], color=blue, lw=2, ls="--")
    alpha = np.deg2rad(8)
    ax.plot([cx-radius*np.sin(alpha), cx+radius*np.sin(alpha)],
            [cy-radius*np.cos(alpha), cy+radius*np.cos(alpha)], color=orange, lw=3)
    ax.add_patch(Circle((cx, cy), 0.09, facecolor="white", edgecolor=gray))
    ax.plot(cx, cy, ".", color=gray, ms=4)
    ax.text(cx-0.12, cy+radius+0.13, "0°", color=blue, ha="right")
    ax.annotate("+8°", xy=(cx+radius*np.sin(alpha), cy+radius*np.cos(alpha)),
                xytext=(cx+0.68, cy+0.90), color=orange, fontsize=13,
                arrowprops={"arrowstyle": "-", "color": orange})
    arc = np.linspace(-45, -100, 35)
    arc_x = cx+1.13*np.cos(np.deg2rad(arc))
    arc_y = cy+1.13*np.sin(np.deg2rad(arc))
    ax.plot(arc_x, arc_y, color=gray, lw=1.4)
    ax.add_patch(FancyArrowPatch((arc_x[-2], arc_y[-2]), (arc_x[-1], arc_y[-1]),
                                arrowstyle="-|>", mutation_scale=12, color=gray))
    ax.text(cx, 0.02, "End view: light comes toward you (⊙)", ha="center", fontsize=10)
    ax.text(4.25, 2.25, "View from the detector toward the source", weight="bold", fontsize=13)
    ax.text(4.25, 1.78, "Positive angles turn clockwise in this view.", color=gray)
    ax.plot([4.25, 4.80], [1.27, 1.27], color=blue, lw=2, ls="--")
    ax.text(4.98, 1.27, "Blank / incident field direction", va="center", color=blue)
    ax.plot([4.25, 4.80], [0.82, 0.82], color=orange, lw=3)
    ax.text(4.98, 0.82, "Emergent field direction: α = +8°", va="center", color=orange)
    ax.text(4.25, 0.30, "Lines show electric-field oscillations, not molecular motion.",
            fontsize=10.5, color=gray)
    fig.text(0.5, 0.045, "Chosen model: [α] = +40 deg mL/(g dm),  c = 0.200 g/mL,  T = 20°C",
             ha="center", fontsize=11, color=gray)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
