"""Draw an ideal free-expansion vessel and apparatus temperature sensitivity.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media; writes free-expansion-vessel-and-thermometry.png to CWD.
All particle positions and numerical values are illustrative, not measured.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


BLUE = "#216a99"
INK = "#243445"
ORANGE = "#b35925"


def chamber(ax, x, y, width, height, filled, columns=4, rows=3):
    ax.add_patch(Rectangle((x, y), width, height, facecolor="white",
                           edgecolor=INK, linewidth=2.2))
    if filled:
        # A fixed illustrative arrangement, not a simulated particle trajectory.
        for ix in range(columns):
            for iy in range(rows):
                ax.add_patch(Circle((x + width * (ix + 0.6) / (columns + 0.2),
                                    y + height * (iy + 0.6) / (rows + 0.2)),
                                   0.014, color=BLUE))


def main():
    plt.rcParams.update({"font.size": 11, "text.color": INK,
                         "axes.labelcolor": INK, "axes.facecolor": "white",
                         "figure.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(9.4, 6.4), dpi=120)
    fig.suptitle("Free expansion: volume, temperature and the apparatus",
                 fontsize=16, y=0.97)
    left = fig.add_axes([0.04, 0.54, 0.43, 0.35])
    right = fig.add_axes([0.53, 0.54, 0.43, 0.35])
    for ax in (left, right):
        ax.set(xlim=(0, 1), ylim=(0, 1))
        ax.axis("off")
        ax.add_patch(Rectangle((0.07, 0.27), 0.86, 0.51, facecolor="white",
                               edgecolor="#758391", linewidth=5))
    left.set_title("1. Before opening", fontsize=13)
    chamber(left, 0.1, 0.3, 0.39, 0.45, True)
    chamber(left, 0.51, 0.3, 0.39, 0.45, False)
    left.text(0.705, 0.54, "Vacuum", ha="center", fontsize=14)
    left.text(0.29, 0.18, r"Gas: $V_1,\ T_1,\ p_1$", ha="center")
    left.text(0.705, 0.18, r"Empty: $V_1$", ha="center")
    left.text(0.5, 0.035, "Rigid wall; negligible wall heat capacity",
              ha="center", fontsize=10)
    right.set_title("2. After equilibration (ideal gas)", fontsize=13)
    chamber(right, 0.1, 0.3, 0.39, 0.45, True, columns=3, rows=2)
    chamber(right, 0.51, 0.3, 0.39, 0.45, True, columns=3, rows=2)
    # Open a passage through the partition, leaving the outside vessel rigid.
    right.add_patch(Rectangle((0.48, 0.47), 0.04, 0.11,
                              facecolor="white", edgecolor="none", zorder=5))
    right.text(0.5, 0.18, r"Gas: $V_2=2V_1,\ T_2=T_1,\ p_2=p_1/2$",
               ha="center")
    right.text(0.5, 0.035, r"Gas-only idealization: $Q=W=\Delta U=0$",
               ha="center", fontsize=10)
    fig.text(0.5, 0.55, "Open passage →", ha="center", fontsize=11,
             bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})

    bath = fig.add_axes([0.04, 0.11, 0.43, 0.34])
    bath.axis("off")
    bath.set(xlim=(0, 1), ylim=(0, 1))
    bath.set_title("Joule's water-bath arrangement (schematic)", fontsize=12)
    bath.add_patch(Rectangle((0.08, 0.12), 0.82, 0.61, facecolor="#e8f3f9",
                             edgecolor=INK, linewidth=2))
    chamber(bath, 0.16, 0.24, 0.24, 0.35, True)
    chamber(bath, 0.59, 0.24, 0.24, 0.35, False)
    bath.plot([0.4, 0.59], [0.42, 0.42], color=INK, lw=4)
    bath.plot([0.495, 0.495], [0.4, 0.56], color=ORANGE, lw=3)
    bath.plot([0.46, 0.53], [0.56, 0.56], color=ORANGE, lw=3)
    bath.text(0.28, 0.64, "Charged", ha="center", fontsize=10)
    bath.text(0.71, 0.64, "Evacuated", ha="center", fontsize=10)
    bath.plot([0.86, 0.86], [0.49, 0.88], color=ORANGE, lw=3)
    bath.add_patch(Circle((0.86, 0.47), 0.024, color=ORANGE))
    bath.text(0.81, 0.83, "Read stirred\nwater temperature", ha="right", fontsize=10)
    bath.text(0.49, 0.18, "Water", ha="center", color=BLUE, fontsize=10)
    bath.text(0.49, -0.05, "Insulate outside; heat can pass inside",
               ha="center", fontsize=11)

    sensitivity = fig.add_axes([0.6, 0.20, 0.34, 0.20])
    demand, gas_capacity, apparatus_capacity = 5.0, 10.0, 990.0
    drops = np.array([demand / gas_capacity,
                      demand / (gas_capacity + apparatus_capacity)])
    threshold = 0.01
    assert np.allclose(drops, [0.5, 0.005])
    sensitivity.barh([1, 0], drops, height=0.45, color=[BLUE, ORANGE])
    sensitivity.set_xscale("log")
    sensitivity.set(xlim=(0.001, 1), ylim=(-0.6, 1.6),
                    yticks=[1, 0], yticklabels=["Gas alone", "With apparatus"],
                    xlabel="Cooling magnitude |ΔT| (K)")
    sensitivity.set_title("Toy sensitivity calculation", fontsize=12, pad=22)
    sensitivity.axvline(threshold, color="#657280", linestyle="--", lw=1.5)
    sensitivity.text(threshold, 1.53, "0.01 K threshold", fontsize=9,
                     ha="center", va="bottom")
    sensitivity.text(drops[0] * 1.13, 1, "0.5 K", va="center", fontsize=10)
    sensitivity.text(np.sqrt(0.001 * drops[1]), 0, "0.005 K",
                     ha="center", va="center", fontsize=10, color="white")
    sensitivity.spines[["top", "right"]].set_visible(False)
    fig.text(0.745, 0.085, "A = 5 J; gas: 10 J/K; apparatus: 990 J/K",
             ha="center", fontsize=10)
    fig.text(0.5, 0.025, "Illustrative geometry and chosen values; no measured data",
             ha="center", fontsize=10, color="#596673")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
