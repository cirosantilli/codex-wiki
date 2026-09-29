"""Generate stellar-distance-and-flux.png in the current working directory.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp python3 ../stellar-distance-and-flux.py
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All sources are isotropic, unattenuated, and steady in Euclidean space.
The right panel is schematic, not to scale; star sizes do not encode luminosity.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 13, "savefig.facecolor": "white"})
    fig, (curve, cases) = plt.subplots(1, 2, figsize=(11, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.18, top=0.78, wspace=0.30)
    fig.suptitle("Distance dims light; luminosity can compensate", fontsize=21, y=0.97)
    fig.text(0.5, 0.89, r"Isotropic, steady source; transparent space: $F=L/(4\pi d^2)$",
             ha="center", fontsize=14)
    distance = np.linspace(1, 3.4, 250)
    curve.plot(distance, distance ** -2, color="#2368ac", lw=3)
    curve.scatter([1, 2, 3], [1, 1/4, 1/9], color="#2368ac", s=65, zorder=4)
    for x, y, label, offset in ((1, 1, r"$F_0$", (12, -7)),
                                 (2, 1/4, r"$F_0/4$", (8, 12)),
                                 (3, 1/9, r"$F_0/9$", (0, 14))):
        curve.annotate(label, (x, y), xytext=offset, textcoords="offset points", fontsize=15)
    curve.set(xlim=(0.8, 3.5), ylim=(0, 1.17), xticks=[1, 2, 3],
              yticks=[0, 0.25, 0.5, 0.75, 1], xlabel=r"Distance $d/d_0$",
              ylabel=r"Received flux $F/F_0$")
    curve.set_title(r"Fixed luminosity $L_0$", fontsize=16, pad=15)
    curve.spines[["top", "right"]].set_visible(False)
    curve.grid(alpha=0.20)

    for y, source_x, lum, separation, flux, color in (
        (0.84, 0.46, r"$L_0$", r"$d_0$", r"$F_0$", "#2368ac"),
        (0.50, 0.04, r"$L_0$", r"$2d_0$", r"$F_0/4$", "#cf6519"),
        (0.16, 0.04, r"$4L_0$", r"$2d_0$", r"$F_0$", "#453778"),
    ):
        cases.scatter([source_x], [y], marker="*", s=190, color=color, zorder=5)
        cases.text(source_x, y + 0.10, lum, ha="center", color=color, fontsize=16)
        cases.add_patch(Rectangle((0.88, y - 0.045), 0.035, 0.09,
                                 facecolor="white", edgecolor=color, lw=2))
        cases.annotate("", xy=(0.865, y), xytext=(source_x + 0.04, y),
                       arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        cases.text((source_x + 0.88) / 2, y - 0.085, separation, ha="center", fontsize=15)
        cases.text(0.965, y, flux, va="center", fontsize=16, color=color)
    cases.text(0.90, 1.04, "Detector", ha="center", fontsize=12)
    cases.set(xlim=(-0.07, 1.27), ylim=(-0.10, 1.13))
    cases.axis("off")
    cases.set_title("Three configurations", fontsize=16, pad=15)
    fig.text(0.30, 0.045, "Twice the distance gives one quarter of the flux", ha="center", fontsize=11)
    fig.text(0.75, 0.045, "Top and bottom: same flux\nSchematic, not to scale", ha="center", fontsize=11)
    fig.savefig("stellar-distance-and-flux.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print("Wrote stellar-distance-and-flux.png (1100 × 570); ratios 1, 1/4, 1/9.")


if __name__ == "__main__":
    main()
