"""Draw equation cancellation and an independent calorimetry model.

Tested with Python 3.14 and matplotlib 3.10. Run from _media to emit the PNG.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 5.7), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.975, bottom=0.11, top=0.81, wspace=0.17)
    fig.suptitle("Two kinds of bookkeeping", fontsize=20, y=0.97)
    fig.text(0.5, 0.89, "Constructed examples: the panels use independent chosen numbers",
             ha="center", fontsize=12, color="#475569")
    blue, orange, green = "#2463A6", "#C36B13", "#16805D"
    for ax in (left, right):
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
    left.set_title("Scale, reverse, then cancel", fontsize=16, pad=16)
    left.text(0.02, 0.91, r"$R_1:\ 2A\to2B$", fontsize=15)
    left.text(0.71, 0.91, "+36 kJ", color=blue, fontsize=15)
    left.text(0.02, 0.79, r"$R_2:\ C\to B$", fontsize=15)
    left.text(0.71, 0.79, "+25 kJ", color=orange, fontsize=15)
    left.text(0.02, 0.62, r"$\frac{1}{2} R_1:$", color=blue, fontsize=17)
    left.text(0.33, 0.62, r"$A\to B$", color=blue, fontsize=19)
    left.text(0.71, 0.62, "+18 kJ", color=blue, fontsize=15)
    left.text(0.02, 0.47, r"$-R_2:$", color=orange, fontsize=17)
    left.text(0.33, 0.47, r"$B\to C$", color=orange, fontsize=19)
    left.text(0.71, 0.47, "−25 kJ", color=orange, fontsize=15)
    left.plot([0.02, 0.97], [0.40, 0.40], color="#94A3B8", lw=1)
    left.text(0.02, 0.28, "Sum:", fontsize=15)
    left.text(0.33, 0.28, r"$A\to C$", color=green, fontsize=19)
    left.text(0.71, 0.28, "−7 kJ", color=green, fontsize=15)
    left.text(0.5, 0.10, "B is made, then consumed in equal amount.", ha="center", fontsize=11)
    left.text(0.5, 0.015, "Each unit coefficient represents one mole.", ha="center", fontsize=11, color="#475569")
    right.set_title("Warming fixes the reaction sign", fontsize=16, pad=16)
    for y, color, text in [(0.63, orange, "Reaction\n−360 J"),
                           (0.22, blue, "Solution + hardware\n+360 J")]:
        right.add_patch(FancyBboxPatch((0.15, y), 0.70, 0.22,
                                      boxstyle="round,pad=0.015", facecolor="white",
                                      edgecolor=color, linewidth=2))
        right.text(0.5, y + 0.11, text, ha="center", va="center", color=color, fontsize=16)
    right.annotate("", xy=(0.5, 0.47), xytext=(0.5, 0.60),
                   arrowprops={"arrowstyle": "-|>", "lw": 3, "color": green})
    right.text(0.57, 0.52, "360 J transferred", va="center", color=green, fontsize=11)
    right.text(0.5, 0.125, r"$C_{\rm tot}\Delta T=(120\ \mathrm{J/K})(3\ \mathrm{K})$",
               ha="center", fontsize=13)
    right.text(0.5, 0.015, r"$\xi=0.020\ \mathrm{mol}\quad\Rightarrow\quad\Delta H/\xi=-18\ \mathrm{kJ/mol}$",
               ha="center", fontsize=13)
    fig.text(0.5, 0.027, "Right panel: constant pressure, no outward heat loss, other corrections neglected.",
             ha="center", color="#475569", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
