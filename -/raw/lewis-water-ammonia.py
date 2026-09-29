"""Draw original Lewis electron counts; write the matching PNG to cwd.

Build: make _media/lewis-water-ammonia.png
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Layouts show allocations, not molecular geometries or electron trajectories.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


BOND = "#216b97"
LONE = "#a44f25"


def draw_bond(axis, start, end):
    start, end = np.asarray(start, dtype=float), np.asarray(end, dtype=float)
    direction = (end - start) / np.linalg.norm(end - start)
    endpoints = np.array([start + 0.25 * direction, end - 0.25 * direction])
    axis.plot(*endpoints.T, color=BOND, lw=3.2, solid_capstyle="round")


def draw_pair(axis, position):
    x, y = position
    axis.scatter([x - 0.07, x + 0.07], [y, y], s=36, color=LONE, zorder=3)


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 5.4), dpi=120)
    fig.subplots_adjust(left=0.055, right=0.945, bottom=0.32, top=0.75, wspace=0.3)
    fig.suptitle("Same electron budget, different pair allocations", fontsize=17, y=0.96)
    examples = [
        ("Water", r"$\mathrm{H_2O}$", "O", 6,
         [(-1.05, 0), (1.05, 0)], [(0, 0.48), (0, -0.48)]),
        ("Ammonia", r"$\mathrm{NH_3}$", "N", 5,
         [(-1.05, 0), (1.05, 0), (0, -0.95)], [(0, 0.48)]),
    ]
    for axis, (name, formula, centre, valence, hydrogens, pairs) in zip(axes, examples):
        shared = len(hydrogens)
        nonbonding = len(pairs)
        total = valence + shared  # Each neutral hydrogen supplies one electron.
        assert total == 8 == 2 * shared + 2 * nonbonding
        assert 2 * (shared + nonbonding) == 8  # Central atom's local octet.
        assert valence - 2 * nonbonding - shared == 0  # Central formal charge.
        assert 1 - 0 - 2 / 2 == 0  # Each hydrogen's formal charge.
        axis.set(xlim=(-1.5, 1.5), ylim=(-1.25, 0.85), aspect="equal")
        axis.axis("off")
        axis.set_title(f"{name}: {formula}", fontsize=15, pad=29)
        axis.text(0.5, 1.05, f"{valence} + {shared} × 1 = {total} valence electrons",
                  ha="center", transform=axis.transAxes)
        axis.text(0, 0, centre, ha="center", va="center", fontsize=30)
        for position in hydrogens:
            axis.text(*position, "H", ha="center", va="center", fontsize=28)
            draw_bond(axis, (0, 0), position)
        for position in pairs:
            draw_pair(axis, position)
        pair_word = "pairs" if nonbonding > 1 else "pair"
        axis.text(0.5, -0.02, f"{shared} bond pairs + {nonbonding} lone {pair_word}\n"
                  f"{2 * shared} shared + {2 * nonbonding} nonbonding = 8 electrons",
                  transform=axis.transAxes, ha="center", va="top", linespacing=1.6)
        print(f"{formula}: total={total}; bond pairs={shared}; lone pairs={nonbonding}; "
              "central local count=8; each H local count=2; all formal charges=0")

    fig.text(0.5, 0.195, "Local counts: O and N each count 8 electrons; each H counts 2.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.145, "Count each shared pair once in the molecule's budget.",
             ha="center", fontsize=11)
    fig.legend(handles=[Line2D([0], [0], color=BOND, lw=3, label="Line = 2 shared electrons"),
                        Line2D([0], [0], marker="o", color=LONE, ls="",
                               label="Dot = 1 nonbonding electron")],
               loc="lower center", bbox_to_anchor=(0.5, 0.072), ncol=2,
               frameon=False, fontsize=10)
    fig.text(0.5, 0.035, "Schematic Lewis layouts: no shape, angle, or electron path is implied.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
