"""Original schematic of a proposed pressure/balance comparison, with no data.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes only the matching PNG basename to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle
import numpy as np


def box(ax, x, y, width, height, text, color):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
                               boxstyle="round,pad=0.08", edgecolor=color,
                               facecolor="white", linewidth=1.5))
    ax.text(x+width/2, y+height/2, text, ha="center", va="center", fontsize=11)


def arrow(ax, start, end, color="#333333", dashed=False):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 1.6,
                            "linestyle": "--" if dashed else "-"})


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(10.8, 5.6), dpi=100)
    fig.patch.set_facecolor("white")
    blue, orange = "#1969aa", "#b96722"
    ax.plot([.3, 10.4], [4.0, 4.0], color="#8a939b", linewidth=2)
    ax.plot([.3, 10.4], [2.3, 2.3], color="#8a939b", linewidth=2)
    ax.text(5.6, 4.23, "Test section: flow direction and uniformity checked", ha="center")
    for y in [2.65, 3.10, 3.55]:
        arrow(ax, (.35, y), (1.5, y))
    ax.text(.53, 3.80, r"$U_\infty$", fontsize=14)
    ax.add_patch(Polygon([[3.1, 3.32], [3.55, 3.42], [5.5, 2.93],
                         [3.55, 3.03]], closed=True, facecolor="#edf1f5",
                        edgecolor="#263746", linewidth=1.6))
    ax.plot([3.1, 5.5], [3.32, 2.93], linestyle="--", color="#7c858e", linewidth=1)
    ax.text(4.5, 3.73, "rotatable airfoil", ha="center")
    taps = [(3.55, 3.42), (4.0, 3.31), (4.7, 3.13),
            (3.55, 3.03), (4.25, 2.995), (4.9, 2.96)]
    for x, y in taps:
        ax.plot(x, y, "o", color=blue, markersize=4)
    ax.plot([4.0, 4.0, 6.9, 6.9], [3.31, 3.60, 3.60, 1.98],
            color=blue, linewidth=1.5)
    ax.text(5.9, 3.77, "tap tubing (schematic)", fontsize=10, color=blue)
    ax.plot([4.1, 4.1], [3.04, 2.02], color=orange, linewidth=4)
    ax.text(4.37, 2.55, "mount", color=orange, fontsize=10)
    # Far-field probe is separate from the model/tap measurements.
    ax.plot([2.0, 2.35, 2.35], [3.57, 3.57, 2.06], color="#546675", linewidth=2)
    ax.text(2.56, 2.63, "total / static\nprobe", fontsize=10, ha="left")
    box(ax, .6, 1.18, 2.1, .75, "q = total − static\nρ from p and T", "#546675")
    box(ax, 3.25, 1.18, 1.85, .75, "force balance\nwind-off tare", orange)
    box(ax, 5.8, 1.18, 2.3, .75, "pressure sensors\nreference: p∞", blue)
    box(ax, 8.6, 1.18, 1.65, .75, "record α, q,\nforces, taps", "#777777")
    ax.plot([4.2, 4.2, 9.4], [1.99, 2.13, 2.13], color=orange, linewidth=1.5)
    arrow(ax, (9.4, 2.13), (9.4, 1.99), orange)
    arrow(ax, (8.19, 1.56), (8.49, 1.56), blue)
    ax.text(4.15, .62, "known loads ±mg\ncheck cross coupling", ha="center", color=orange, fontsize=10)
    ax.text(6.94, .62, "known Δp\nzero, range, drift", ha="center", color=blue, fontsize=10)
    arrow(ax, (4.15, .94), (4.15, 1.10), orange)
    arrow(ax, (6.94, .94), (6.94, 1.10), blue)
    ax.add_patch(Rectangle((.5, -.29), 9.8, .57, facecolor="#f3f5f7", edgecolor="none"))
    ax.text(5.4, -.01, "Compare balance L′ with −q Σ C̄p (n · eL) Δs\nPressure taps reconstruct pressure force; balance also senses shear and support loads.",
            ha="center", va="center", fontsize=11)
    ax.set(xlim=(0, 10.8), ylim=(-.48, 4.65))
    ax.axis("off")
    fig.suptitle("Two measurement routes to the same lift component", fontsize=16, y=.96)
    fig.text(.5, .026, "Proposed apparatus schematic • not to scale • no measured results",
             ha="center", fontsize=10, color="#555555")
    fig.subplots_adjust(left=.025, right=.975, top=.87, bottom=.095)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
