"""Original functional interface schematic; tested with Python 3.14/matplotlib 3.10.

Run from _media; writes this script's basename with a .png suffix to the CWD.
Positions and profiles are explanatory choices, not historical apparatus data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig = plt.figure(figsize=(11, 5.6), facecolor="white")
    left = fig.add_axes((0.035, 0.18, 0.53, 0.66))
    right = fig.add_axes((0.66, 0.23, 0.30, 0.53))
    fig.suptitle("Heat flow across a temperature jump", fontsize=17, y=0.96)
    fig.text(0.30, 0.865, "Functional measurement schematic", ha="center", fontsize=12)
    left.set(xlim=(0, 10), ylim=(0, 7))
    left.axis("off")
    left.add_patch(Rectangle((0.4, 2.2), 3.6, 3.6, fc="#f5dcc8", ec="#8b5537", lw=1.5))
    left.add_patch(Rectangle((4.0, 2.2), 5.5, 3.6, fc="#dff1fa", ec="#3c7a9a", lw=1.5))
    left.plot([4, 4], [2.2, 5.8], color="#df9a15", lw=5)
    left.text(2.1, 5.25, "Solid", ha="center", weight="bold")
    left.text(6.8, 5.25, "Liquid helium", ha="center", weight="bold")
    left.text(1.5, 3.85, "Heater\n" + r"$P$", ha="center", va="center",
              bbox={"boxstyle": "round,pad=0.35", "fc": "#ffe3de", "ec": "#a63e30"})
    left.annotate("", (6.8, 3.85), (2.35, 3.85),
                  arrowprops={"arrowstyle": "->", "lw": 2.8, "color": "#b54b2d"})
    left.text(4.5, 4.25, r"$\dot Q=Aq$", ha="center", color="#9b3527", fontsize=13)
    left.text(4, 6.15, "Interface of area " + r"$A$", ha="center", color="#86550b")
    for x, label, color in [(3.25, r"$T_s$", "#9b3527"), (4.9, r"$T_l$", "#246783")]:
        left.plot(x, 2.85, "o", color=color, ms=7)
        left.text(x, 3.13, label, ha="center", color=color, fontsize=14)
        left.annotate("", (5.0, 1.15), (x, 2.65),
                      arrowprops={"arrowstyle": "->", "lw": 1.2, "color": color})
    left.text(5, 0.9, r"Readout: $T_s-T_l$", ha="center", fontsize=13,
              bbox={"boxstyle": "round,pad=0.3", "fc": "white", "ec": "#666666"})
    left.text(8.05, 2.9, "Bath\nreference", ha="center", va="center", color="#246783")
    right.plot([0, 0.5], [1.55, 1.30], lw=3, color="#9b3527")
    right.plot([0.5, 1], [1.10, 1.0], lw=3, color="#246783")
    right.axvline(0.5, color="#df9a15", lw=1.4, ls="--")
    right.plot([0.5, 0.5], [1.30, 1.10], "o", ms=6, color="#3c3c3c")
    right.annotate("", (0.59, 1.30), (0.59, 1.10),
                   arrowprops={"arrowstyle": "<->", "color": "#3c3c3c", "lw": 1.5})
    right.text(0.64, 1.20, r"$T_s-T_l$", va="center", fontsize=12)
    right.text(0.49, 1.37, r"$T_s$", ha="right", color="#9b3527", fontsize=13)
    right.text(0.45, 1.065, r"$T_l$", ha="right", color="#246783", fontsize=13)
    right.set(xlim=(-0.04, 1.06), ylim=(0.94, 1.62), xticks=[0.15, 0.5, 0.85],
              xticklabels=["Solid", "Interface", "Liquid"], yticks=[],
              ylabel="Temperature (schematic)", title="Bulk slopes and interface jump")
    right.text(0.5, -0.25, "Position along the heat path", ha="center", transform=right.transAxes)
    fig.text(0.5, 0.065, "Surface readings require calibration and correction for bulk temperature drops.",
             ha="center", color="#444444")
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
