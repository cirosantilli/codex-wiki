"""Draw three original nitrate Lewis contributors; save basename PNG to cwd.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../nitrate-resonance-contributors.py
Tested with Python 3.14.4, Matplotlib 3.10.7 (+dfsg1), NumPy 2.3.5.
Every panel contains 4 bond pairs and 8 lone pairs: 24 valence electrons.
The diagrams are bookkeeping, not electron positions or time snapshots.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

BOND = "#216b97"
LONE = "#a44f25"
INK = "#222222"
DIRECTIONS = np.array([[0., 1.], [-np.sqrt(3)/2, -.5], [np.sqrt(3)/2, -.5]])


def bond(ax, direction, order):
    tangent = np.array([-direction[1], direction[0]])
    offsets = [0.] if order == 1 else [-.06, .06]
    for offset in offsets:
        points = np.array([.28 * direction, 1.13 * direction]) + offset * tangent
        ax.plot(*points.T, color=BOND, lw=2.9, solid_capstyle="round")


def lone_pair(ax, centre, tangent):
    dots = np.array([centre - .065 * tangent, centre + .065 * tangent])
    ax.scatter(*dots.T, s=21, color=LONE, zorder=3)


def contributor(ax, double_index):
    orders = np.ones(3, dtype=int)
    orders[double_index] = 2
    lone_counts = 4 - orders
    charges = 6 - 2 * lone_counts - orders
    nitrogen_charge = 5 - orders.sum()
    assert orders.sum() == 4 and lone_counts.sum() == 8
    assert 2 * (orders.sum() + lone_counts.sum()) == 24
    assert nitrogen_charge == 1 and charges.sum() + nitrogen_charge == -1
    assert 2 * orders.sum() == 8
    assert np.all(2 * lone_counts + 2 * orders == 8)
    ax.set(xlim=(-2.0, 2.0), ylim=(-1.55, 2.2), aspect="equal")
    ax.axis("off")
    ax.text(0, 0, r"$\mathrm{N}^{+}$", fontsize=25, ha="center", va="center", color=INK)
    for i, (direction, order, pairs) in enumerate(zip(DIRECTIONS, orders, lone_counts)):
        position = 1.45 * direction
        tangent = np.array([-direction[1], direction[0]])
        bond(ax, direction, order)
        # Charge is given separately, away from dots, and zero is explicit.
        ax.text(*position, rf"$\mathrm{{O}}_{i+1}$", fontsize=24,
                ha="center", va="center", color=INK)
        for sign in [-1, 1]:
            lone_pair(ax, position + sign * .37 * tangent, direction)
        if pairs == 3:
            lone_pair(ax, position + .37 * direction, tangent)
        charge_position = position + (.73 * direction if i == 0 else np.array([0., -.58]))
        ax.text(*charge_position, "0" if order == 2 else "−1",
                fontsize=12, color=INK, ha="center", va="center",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": .4}, clip_on=False)
    for side in [-1, 1]:
        x = side * 1.92
        ax.plot([x, x], [-1.47, 2.08], color=INK, lw=1.2)
        ax.plot([x, x - side * .12], [2.08, 2.08], color=INK, lw=1.2)
        ax.plot([x, x - side * .12], [-1.47, -1.47], color=INK, lw=1.2)
    ax.text(2.02, 2.14, "−", fontsize=17, color=INK, ha="left", va="center", clip_on=False)
    ax.set_title(f"Contributor {double_index + 1}", fontsize=14, pad=12)
    ax.text(.5, -.12, "4 bond pairs + 8 lone pairs\n8 + 16 = 24 electrons", ha="center",
            va="top", transform=ax.transAxes, fontsize=11, linespacing=1.5)
    return {"orders": orders.tolist(), "lone_pairs": lone_counts.tolist(),
            "oxygen_formal_charges": charges.tolist(), "nitrogen_formal_charge": int(nitrogen_charge)}


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 6.0), dpi=120)
    fig.subplots_adjust(left=.035, right=.955, bottom=.31, top=.78, wspace=.23)
    fig.suptitle(r"Nitrate: three equivalent Lewis contributors, $\mathrm{NO}_3^-$", fontsize=17, y=.965)
    fig.text(.5, .90, "Same atom positions and labels; different electron allocations", ha="center", fontsize=12)
    for i, ax in enumerate(axes):
        print(f"Contributor {i + 1}: {contributor(ax, i)}; valence electrons=24; all local counts=8")
    for left, right in zip(axes[:-1], axes[1:]):
        midpoint = (left.get_position().x1 + right.get_position().x0) / 2
        fig.text(midpoint, .555, "↔", fontsize=25, ha="center", va="center", color=INK)
    fig.text(.5, .175, "N: +1     single-bonded O: −1     double-bonded O: 0     total: −1", ha="center", fontsize=11)
    fig.legend(handles=[Line2D([0], [0], color=BOND, lw=3, label="Each line = 2 electrons"),
                        Line2D([0], [0], marker="o", color=LONE, ls="", label="Each dot = 1 electron")],
               loc="lower center", bbox_to_anchor=(.5, .09), ncol=2, frameon=False, fontsize=11)
    fig.text(.5, .075, "Atom charges are formal charges; brackets give the net ion charge.", ha="center", fontsize=10)
    fig.text(.5, .035, "The resonance arrow does not mean a reaction, equilibrium, or switching in time.", ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
