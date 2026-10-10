"""Original functional schematics; Python 3.14, matplotlib 3.10, numpy 2.3.

Run from _media; no historical diagram coordinates or event data are used.
"""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle
import numpy as np


def arrow(ax, start, end, color, **kw):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=14, lw=2, color=color, **kw))


def main():
    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.6), facecolor="white")
    blue, red, green = "#2266aa", "#b23b40", "#25745c"
    for ax in axes:
        ax.set(xlim=(0, 10), ylim=(0, 8))
        ax.axis("off")
    ax = axes[0]
    ax.set_title("Brookhaven: proton beam on a fixed target", weight="bold", fontsize=12)
    arrow(ax, (0.3, 4), (2.25, 4), blue)
    ax.text(0.3, 4.35, "protons", color=blue)
    ax.add_patch(Rectangle((2.25, 3.65), 0.22, 0.7, color="#777777"))
    ax.text(2.35, 3.25, "stationary Be target", ha="center")
    for sign, y, col in [("$e^+$", 6.15, red), ("$e^-$", 1.85, blue)]:
        arrow(ax, (2.5, 4), (4.4, y), col)
        ax.add_patch(Rectangle((4.45, y - 0.45), 1.3, 0.9,
                               facecolor="#eeeeee", edgecolor="#555555"))
        ax.text(5.1, y, "magnet", ha="center", va="center", fontsize=10)
        arrow(ax, (5.8, y), (7.1, y), col)
        for x in (6.2, 6.55):
            ax.plot([x, x], [y - 0.4, y + 0.4], color=green, lw=3)
        ax.add_patch(Rectangle((7.2, y - 0.5), 2.3, 1,
                               facecolor="#edf4f9", edgecolor=col))
        ax.text(8.35, y, "particle ID\ncounters", ha="center", va="center", fontsize=10)
        ax.text(3.7, y + 0.4, sign, color=col)
    ax.text(6.35, 3.9, "tracking planes", color=green, ha="center", fontsize=10)
    ax.text(5, 0.65, "Readout: daughter momenta + opening angle\nReconstruct pair invariant mass for each event",
            ha="center", va="center", weight="bold", fontsize=10)
    ax = axes[1]
    ax.set_title("SPEAR: counterrotating stored beams", weight="bold", fontsize=12)
    ax.add_patch(Ellipse((5, 4.1), 8, 4.5, fill=False, lw=2, edgecolor="#777777"))
    # Nearby parallel strokes denote the same stored orbit, not two rings.
    arrow(ax, (3.8, 6.3), (2.4, 5.8), blue)
    arrow(ax, (5.9, 6.3), (7.3, 5.8), red)
    ax.text(1.4, 6.6, "$e^-$", color=blue)
    ax.text(7.6, 6.6, "$e^+$", color=red)
    ax.text(5, 4.2, "storage ring\n(one shared orbit)", ha="center", color="#555555")
    # At the bottom interaction point, local tangents point oppositely.
    ip = (5, 1.85)
    ax.add_patch(Circle(ip, 1.0, facecolor="#eef6f0", edgecolor=green, lw=2))
    arrow(ax, (3, 1.85), (4.8, 1.85), blue)
    arrow(ax, (7, 1.85), (5.2, 1.85), red)
    ax.plot(*ip, "o", color="black", ms=5)
    for angle in (40, 110, 235, 310):
        a = np.deg2rad(angle)
        arrow(ax, ip, (5 + 0.83*np.cos(a), 1.85 + 0.83*np.sin(a)), "#777777")
    ax.text(7.2, 2.65, "magnetic\ndetector", color=green, fontsize=10)
    ax.text(5, 0.05, "Readout: selected event yield / collision exposure\nScan collision energy by changing both beam energies",
            ha="center", va="center", weight="bold", fontsize=10)
    fig.suptitle("Two independent routes to the same narrow particle state", fontsize=15, weight="bold")
    fig.text(0.5, 0.02, "Original functional diagrams; not to scale. Detector positions and outgoing tracks are schematic.",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=0.025, right=0.98, top=0.84, bottom=0.12, wspace=0.12)
    fig.savefig(Path(__file__).stem + ".png", dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
