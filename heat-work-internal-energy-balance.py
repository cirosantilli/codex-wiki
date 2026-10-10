"""Draw energy transfers for a closed sample in a sealed piston cylinder.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes heat-work-internal-energy-balance.png to the current directory.
Stipulated transfers; bulk kinetic and potential energy remain unchanged.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


def main():
    heat, work = 20.0, 5.0  # kJ; entering heat and outgoing work are positive.
    internal_change = heat - work
    assert internal_change == 15.0
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.2, 5.0), dpi=120)
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.07, top=0.84)
    fig.suptitle("Heat and work cross the boundary; internal energy changes inside", fontsize=14)
    ax.set(xlim=(0, 10), ylim=(0, 5))
    ax.axis("off")
    blue, orange, ink = "#216a99", "#b8531c", "#343b43"
    # A horizontal sealed cylinder: fixed wall at left, moving piston at right.
    ax.add_patch(Rectangle((3.1, 1.75), 2.45, 2.15, facecolor="#e9f3f7", edgecolor="none"))
    ax.plot([5.95, 3.05, 3.05, 5.95], [3.95, 3.95, 1.7, 1.7], color=ink, lw=3)
    ax.add_patch(Rectangle((5.5, 1.7), 0.22, 2.25, facecolor="#a3adb6", edgecolor=ink, lw=2))
    ax.plot([5.72, 6.6], [2.83, 2.83], color=ink, lw=6, solid_capstyle="butt")
    ax.add_patch(Rectangle((2.9, 1.5), 2.9, 2.65, facecolor="none",
                           edgecolor=blue, ls=(0, (5, 4)), lw=1.5))
    ax.text(4.35, 4.45, "Closed system: fixed amount of matter", ha="center", fontsize=12)
    ax.text(4.3, 3.45, "Stored internal energy U", ha="center", fontsize=11)
    ax.text(4.3, 2.95, "ΔU = +15 kJ", ha="center", fontsize=15, weight="bold")
    ax.text(4.3, 2.3, "Sealed sample", ha="center", fontsize=11)
    ax.text(4.35, 1.14, "Dashed system boundary moves with the piston", ha="center", fontsize=10, color=blue)
    ax.add_patch(FancyArrowPatch((0.45, 2.83), (3.0, 2.83), arrowstyle="-|>",
                                 mutation_scale=25, lw=3, color=orange))
    ax.text(1.55, 3.28, "Heat enters\nQ = +20 kJ", ha="center", color=orange)
    ax.add_patch(FancyArrowPatch((5.8, 2.83), (9.55, 2.83), arrowstyle="-|>",
                                 mutation_scale=25, lw=3, color=blue))
    ax.text(8.0, 3.28, "Work leaves\nW = +5 kJ", ha="center", color=blue)
    ax.text(8.0, 2.05, "Piston pushes the surroundings", ha="center", fontsize=10, color=blue)
    ax.text(5, 0.56, "First law: ΔU = Q − W = 20 − 5 = 15 kJ", ha="center", fontsize=14)
    ax.text(5, 0.02, "No matter crosses the boundary; bulk kinetic and potential energy are unchanged",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Q={heat:g} kJ; W={work:g} kJ; ΔU={internal_change:g} kJ")


if __name__ == "__main__":
    main()
