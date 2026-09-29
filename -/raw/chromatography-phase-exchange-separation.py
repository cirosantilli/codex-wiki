"""Original partition/transport model; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes a matching opaque PNG in the working directory.
"""

from math import comb
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


def band(steps, mobile_fraction):
    """Exact binomial populations after repeated equilibrium and one-cell shifts."""
    return np.array([
        comb(steps, j) * mobile_fraction**j * (1 - mobile_fraction)**(steps - j)
        for j in range(steps + 1)
    ])


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    teal, orange, ink = "#087e8b", "#bd5519", "#26384b"
    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 5.6),
                                     gridspec_kw={"width_ratios": [1, 1.18]})
    fig.subplots_adjust(left=.04, right=.975, bottom=.20, top=.82, wspace=.25)
    fig.suptitle("Chromatography: exchange creates differential migration",
                 fontsize=16, y=.965, color=ink)
    fig.text(.5, .895, "Original ideal model • equal accessible phase volumes • no experimental data",
             ha="center", fontsize=11, color="#536170")
    left.set(xlim=(0, 10), ylim=(0, 10))
    left.axis("off")
    left.set_title("1. Local storage and transport", loc="left", pad=15, fontsize=12)
    for y, face in [(6.2, "#e4f1f4"), (2.2, "#f4ede4")]:
        left.add_patch(Rectangle((.2, y), 9.4, 2.2, facecolor=face,
                                 edgecolor="#a0acb4", linewidth=1.2))
    left.text(4.9, 7.8, "Mobile liquid: moves onward", ha="center", color=ink)
    left.text(4.9, 3.8, "Stationary liquid: stays in the cell", ha="center", color=ink)
    left.text(.6, 6.65, r"$c_m,\ V_m$", fontsize=13, color=ink)
    left.text(.6, 2.65, r"$c_s,\ V_s$", fontsize=13, color=ink)
    left.add_patch(FancyArrowPatch((4.8, 4.5), (4.8, 6.1), arrowstyle="<->",
                                   mutation_scale=17, color=ink, linewidth=1.6))
    left.text(5.2, 5.3, "reversible\nexchange", va="center", color=ink)
    left.add_patch(FancyArrowPatch((6.4, 6.85), (9.2, 6.85), arrowstyle="->",
                                   mutation_scale=19, color=ink, linewidth=2))
    for x, y, color in [(3.0, 6.8, teal), (3.5, 6.8, teal), (4.0, 6.8, teal),
                         (3.0, 2.8, teal), (7.1, 6.8, orange), (7.1, 2.8, orange),
                         (7.6, 2.8, orange), (8.1, 2.8, orange)]:
        left.plot(x, y, "o", color=color, markersize=9)
    left.text(4.9, 1.15, r"$K=c_s/c_m$     $f_m=V_m/(V_m+KV_s)$",
              ha="center", fontsize=12, color=ink)
    left.text(4.9, .2, "Dots illustrate fractions, not individual trajectories.",
              ha="center", fontsize=9, color="#536170")
    steps = 12
    x = np.arange(steps + 1)
    for fraction, color, label, offset in [
        (.75, teal, r"A: $K=1/3$, mobile fraction $3/4$", .13),
        (.25, orange, r"B: $K=3$, mobile fraction $1/4$", -.13),
    ]:
        values = band(steps, fraction)
        right.bar(x + offset, values, width=.25, color=color, alpha=.85, label=label)
        right.axvline(steps * fraction, color=color, linestyle="--", linewidth=1.4)
        right.text(steps * fraction, .327, f"mean {steps * fraction:g}",
                   ha="center", color=color, fontsize=10)
    right.set(title="2. Bands after 12 transport cycles", xlabel="Cell position (cell units)",
              ylabel="Fraction of each component in cell", xlim=(-.65, 12.65), ylim=(0, .36))
    right.set_xticks(np.arange(0, 13, 3))
    right.set_yticks([0, .1, .2, .3])
    right.grid(axis="y", alpha=.18)
    handles, labels = right.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower right", bbox_to_anchor=(.985, .015),
               frameon=False, fontsize=10)
    fig.text(.25, .075, "Equilibrate → move only mobile fraction → repeat",
             ha="center", fontsize=10, color=ink)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
