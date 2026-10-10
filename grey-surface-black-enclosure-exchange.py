"""Draw black-enclosure exchange and an emissivity comparison.

Run from _media; writes grey-surface-black-enclosure-exchange.png to CWD.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Original ideal-model schematic; arrows are not drawn to power scale.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


SIGMA = 5.670374419e-8
AREA, BODY_T, WALL_T = 0.01, 500.0, 300.0


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.8, 5.4),
                                gridspec_kw={"width_ratios": [1.4, 1]})
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.19, top=0.84, wspace=0.28)
    fig.suptitle("A low-emissivity surface both emits less and absorbs less", fontsize=15, y=0.97)
    ax.set(xlim=(0, 10), ylim=(0, 8), aspect="equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0.35, 0.35), 9.3, 7.15, fill=False, ec="#222222", lw=5))
    ax.text(5, 6.85, "Black isothermal walls: Tₛ = 300 K", ha="center", fontsize=12)
    ax.add_patch(Circle((4.9, 3.8), 1.03, fc="#ededed", ec="#555555", lw=2))
    ax.text(4.9, 3.8, "T = 500 K\nε = 0.8", ha="center", va="center", fontsize=11)
    ax.text(5, 1.20, "Convex body: Fbody→walls = 1\nTotal emitting area A = 0.01 m²", ha="center", fontsize=11)
    arrow = {"arrowstyle": "-|>", "mutation_scale": 17, "lw": 2.2}
    ax.add_patch(FancyArrowPatch((5.55, 4.62), (8.95, 5.7), color="#b35415", **arrow))
    ax.text(7.8, 6.13, "Emitted\n28.35 W", ha="center", color="#b35415", fontsize=11)
    ax.add_patch(FancyArrowPatch((1.0, 5.5), (4.05, 4.40), color="#24689d", **arrow))
    ax.text(2.35, 6.05, "Incident 4.59 W", ha="center", color="#24689d", fontsize=11)
    ax.text(2.0, 3.55, "Absorbed\n3.67 W", ha="center", color="#24689d", fontsize=11)
    ax.add_patch(FancyArrowPatch((3.25, 4.05), (4.05, 4.20), color="#24689d", **arrow))
    ax.add_patch(FancyArrowPatch((4.05, 4.40), (1.05, 2.5), color="#888888", **arrow))
    ax.text(2.25, 1.9, "Reflected\n0.92 W", ha="center", color="#666666", fontsize=11)
    epsilon = np.linspace(0, 1, 101)
    net_black = AREA * SIGMA * (BODY_T**4 - WALL_T**4)
    bx.plot(epsilon, epsilon * net_black, color="#6c4292", lw=2.5)
    for e, labelpos in [(0.2, (0.32, 4.0)), (0.8, (0.30, 27.0))]:
        power = e * net_black
        bx.scatter(e, power, s=40, color="#6c4292", zorder=4)
        bx.annotate(f"ε = {e}: {power:.2f} W", xy=(e, power), xytext=labelpos,
                    arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    bx.set(xlim=(0, 1.02), ylim=(0, 34), xlabel="Emissivity ε",
           ylabel="Net outward radiative power (W)", title="Same area and temperatures")
    bx.grid(alpha=0.18)
    bx.text(0.04, 0.94, "Net = εσA(T⁴ − Tₛ⁴)", transform=bx.transAxes, va="top", fontsize=11)
    fig.text(0.5, 0.055, "Ideal grey, diffuse, opaque surface • Transparent intervening medium\n"
             "Enclosure schematic is not to scale; arrows indicate directions, not relative power",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
