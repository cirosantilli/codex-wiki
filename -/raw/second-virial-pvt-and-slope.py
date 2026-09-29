"""Burnett principle and chosen virial polynomials; no measured data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../second-virial-pvt-and-slope.py
The PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12, "axes.labelsize": 11})
    fig, (apparatus, slopes) = plt.subplots(1, 2, figsize=(9.8, 5.4))
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=0.04, right=0.97, bottom=0.27, top=0.80, wspace=0.30)
    fig.suptitle("Second virial coefficient: a small departure from ideal-gas pressure", fontsize=14, y=0.96)
    fig.text(0.5, 0.89, "Apparatus schematic + deliberately chosen toy curves (no measured data)", ha="center", fontsize=11)

    apparatus.set(xlim=(0, 10), ylim=(0, 9))
    apparatus.axis("off")
    apparatus.set_title("A. Repeat expansions at the same temperature", pad=18)
    apparatus.add_patch(Rectangle((0.45, 2.3), 8.95, 4.9, facecolor="#f3f8fc", edgecolor="#6390ae", lw=1.5))
    apparatus.text(4.9, 6.75, "Thermostatic bath at T", ha="center", color="#245670")
    for x, label, desc in [(1.3, "$V_A$", "sample"), (6.45, "$V_B$", "expansion")]:
        apparatus.add_patch(Rectangle((x, 3.45), 2.1, 2.5, facecolor="white", edgecolor="#334452", lw=1.7))
        apparatus.text(x + 1.05, 4.9, label, ha="center", fontsize=15)
        apparatus.text(x + 1.05, 4.05, desc, ha="center", fontsize=10)
    apparatus.plot([3.4, 4.8, 6.45], [4.7, 4.7, 4.7], color="#334452", lw=1.7)
    apparatus.plot([4.55, 5.05], [4.4, 5.0], color="#334452", lw=1.7)
    apparatus.text(4.9, 3.55, "valve", ha="center")
    apparatus.plot([2.35, 2.35], [5.95, 7.7], color="#334452", lw=1.7)
    apparatus.add_patch(Circle((2.35, 8.0), 0.42, facecolor="white", edgecolor="#334452", lw=1.5))
    apparatus.text(2.35, 8.0, "p", ha="center", va="center")
    apparatus.text(3.05, 8.0, "pressure readout", va="center", fontsize=10)
    apparatus.add_patch(FancyArrowPatch((7.5, 3.4), (7.5, 2.65), arrowstyle="->", mutation_scale=12, lw=1.3))
    apparatus.text(7.5, 2.0, "evacuate while isolated", ha="center", fontsize=10)
    apparatus.text(4.9, 0.80, "Open → equilibrate → record p\nClose → evacuate expansion chamber → repeat", ha="center", va="center", fontsize=10.5)

    x = np.linspace(0, 0.14, 400)
    slopes.set_title("B. The initial slope is the coefficient", pad=18)
    slopes.axvspan(0, 0.035, color="#e9f3e5")
    for b, color, label in [(2, "#c36a20", "$b=+2$"), (-2, "#21669c", "$b=-2$")]:
        slopes.plot(x, 1 + b*x + 6*x*x, color=color, lw=2.3, label=label + ": $Z=1+bx+6x^2$")
        tangent_x = np.linspace(0, 0.09, 60)
        slopes.plot(tangent_x, 1 + b*tangent_x, "--", color=color, lw=1.4)
    slopes.axhline(1, color="#6b6b6b", lw=1)
    slopes.set(xlim=(0, 0.14), ylim=(0.77, 1.45), xlabel=r"$x=n\ell^3$ (dimensionless density)", ylabel="$Z=p/(nk_BT)$")
    slopes.set_xticks([0, 0.035, 0.07, 0.105, 0.14], ["0", ".035", ".070", ".105", ".140"])
    slopes.grid(alpha=0.18)
    slopes.text(0.005, 1.38, "narrow\nfit window", fontsize=10, color="#3f6634")
    slopes.legend(loc="lower right", fontsize=9, frameon=True, facecolor="white", framealpha=1)
    slopes.text(0.064, 1.22, "dashed: tangents at x = 0", fontsize=9, rotation=0)
    fig.text(0.5, 0.10, r"$B_2=b\ell^3$; chosen curvature $B_3=6\ell^6$.  Finite secant slope: $(Z(h)-1)/h=b+6h$.", ha="center", fontsize=11)
    fig.text(0.5, 0.045, "A low-density fit needs temperature control, calibration and a check for curvature.", ha="center", fontsize=10.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
