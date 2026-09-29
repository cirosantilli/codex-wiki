"""Draw original CO2 Lewis allocations and formal-charge calculations.

Build: make _media/lewis-carbon-dioxide-formal-charge.png
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Every line is one bond pair, and every dot is one nonbonding electron.
The resonance contributors are not equally dominant or flipping molecules.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


BOND = "#216b97"
LONE = "#a44f25"


def draw_bond(axis, start, end, order):
    start, end = np.asarray(start, dtype=float), np.asarray(end, dtype=float)
    direction = (end - start) / np.linalg.norm(end - start)
    normal = np.array([-direction[1], direction[0]])
    for offset in np.arange(order) * 0.12 - (order - 1) * 0.06:
        endpoints = np.array([start + 0.28 * direction + offset * normal,
                              end - 0.28 * direction + offset * normal])
        axis.plot(*endpoints.T, color=BOND, lw=2.8, solid_capstyle="round")


def draw_pair(axis, position, vertical=False):
    centre = np.asarray(position, dtype=float)
    separation = np.array([0, 0.075] if vertical else [0.075, 0])
    dots = np.array([centre - separation, centre + separation])
    axis.scatter(*dots.T, s=34, color=LONE, zorder=3)


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 5.9), dpi=120)
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.37, top=0.78, wspace=0.22)
    fig.suptitle(r"Carbon dioxide: $4 + 2\times6 = 16$ valence electrons", fontsize=17, y=0.965)
    positions = [(-1.2, 0), (0, 0), (1.2, 0)]
    valence = np.array([6, 4, 6])  # Left O, C, right O.
    examples = [
        ("Dominant contributor", (2, 2),
         [[(-1.2, 0.48, False), (-1.2, -0.48, False)], [],
          [(1.2, 0.48, False), (1.2, -0.48, False)]],
         (0, 0, 0)),
        ("Less important, charge-separated contributor", (1, 3),
         [[(-1.2, 0.48, False), (-1.2, -0.48, False), (-1.73, 0, True)], [],
          [(1.2, 0.48, False)]],
         (-1, 0, 1)),
    ]
    for axis, (heading, orders, pairs, expected) in zip(axes, examples):
        nonbonding = 2 * np.array([len(p) for p in pairs])
        incident = 2 * np.array([orders[0], sum(orders), orders[1]])
        formal = valence - nonbonding - incident // 2
        total = int(nonbonding.sum() + incident.sum() // 2)
        np.testing.assert_array_equal(formal, expected)
        np.testing.assert_array_equal(nonbonding + incident, [8, 8, 8])
        assert total == 16 and formal.sum() == 0
        assert len(pairs[1]) == 0 and sum(map(len, pairs)) == 4
        assert sum(orders) == 4
        axis.set(xlim=(-2.0, 2.0), ylim=(-1.08, 0.85), aspect="equal")
        axis.axis("off")
        axis.set_title(heading, fontsize=11, pad=24)
        axis.text(0.5, 1.065, "4 bond pairs + 4 lone pairs = 16 electrons",
                  ha="center", transform=axis.transAxes, fontsize=10)
        for i, ((x, y), symbol) in enumerate(zip(positions, ["O", "C", "O"])):
            axis.text(x, y, symbol, ha="center", va="center", fontsize=29)
            if formal[i]:
                axis.text(x + 0.2, y + 0.21, "−" if formal[i] < 0 else "+",
                          ha="center", va="center", fontsize=17)
            for px, py, vertical in pairs[i]:
                draw_pair(axis, (px, py), vertical)
            charge = "0" if formal[i] == 0 else f"{formal[i]:+d}".replace("-", "−")
            axis.text(x, -0.85, f"FC = {charge}", ha="center", fontsize=12)
        for i, order in enumerate(orders):
            draw_bond(axis, positions[i], positions[i + 1], order)
        calculations = [f"{label}: {v} − {n} − {b}/2 = {fc:+d}".replace("+0", "0")
                        for label, v, n, b, fc in
                        zip(["Left O", "C", "Right O"], valence, nonbonding, incident, formal)]
        axis.text(0.5, -0.04, "\n".join(calculations), transform=axis.transAxes,
                  ha="center", va="top", linespacing=1.7, fontsize=11)
        print(f"CO2 orders={orders}; nonbonding={nonbonding.tolist()}; "
              f"incident bonding={incident.tolist()}; FC={formal.tolist()}; "
              f"total={total}; local counts={(nonbonding + incident).tolist()}")

    fig.text(0.5, 0.63, r"$\leftrightarrow$", fontsize=24, ha="center")
    fig.text(0.5, 0.24, "Formal charge = v − nonbonding electrons − ½ bonding electrons",
             ha="center", fontsize=12)
    fig.text(0.5, 0.19, "v = neutral atom's valence count; C has no lone pairs in either drawing.",
             ha="center", fontsize=10)
    fig.legend(handles=[Line2D([0], [0], color=BOND, lw=3, label="Line = 2 shared electrons"),
                        Line2D([0], [0], color=LONE, marker="o", ls="",
                               label="Dot = 1 nonbonding electron")],
               loc="lower center", bbox_to_anchor=(0.5, 0.105), ncol=2,
               frameon=False, fontsize=10)
    fig.text(0.5, 0.073, "Both drawings: local octets of 8 and net formal charge 0. Unequal contributions.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.03, "Formal charges are bookkeeping; resonance is not rapid flips between drawings.",
             ha="center", fontsize=10, color="#555555")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
