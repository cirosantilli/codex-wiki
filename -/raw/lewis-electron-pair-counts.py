"""Draw original Lewis bookkeeping diagrams; write the PNG to cwd.

Build: make _media/lewis-electron-pair-counts.png
Tested with Python 3.14.4, Matplotlib 3.10.7 (system +dfsg1).
Layouts are schematic, not molecular geometries or electron trajectories.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


BOND_COLOR = "#216b97"
LONE_COLOR = "#a44f25"


def atom(axis, symbol, x, y):
    axis.text(x, y, symbol, ha="center", va="center", fontsize=25)


def bond(axis, start, end, pairs=1):
    x1, y1 = start
    x2, y2 = end
    dx, dy = x2 - x1, y2 - y1
    length = (dx * dx + dy * dy) ** 0.5
    trim = 0.23 / length
    for offset in ([0] if pairs == 1 else [-0.055, 0.055]):
        ox, oy = -dy / length * offset, dx / length * offset
        axis.plot([x1 + trim * dx + ox, x2 - trim * dx + ox],
                  [y1 + trim * dy + oy, y2 - trim * dy + oy],
                  color=BOND_COLOR, lw=3, solid_capstyle="round")


def lone_pair(axis, x, y, vertical=False):
    gap = 0.065
    xs = [x, x] if vertical else [x - gap, x + gap]
    ys = [y - gap, y + gap] if vertical else [y, y]
    axis.scatter(xs, ys, s=27, color=LONE_COLOR, zorder=3)


def main():
    # (formula, valence total, shared pairs, nonbonding pairs)
    counts = [("H2", 2, 1, 0), ("H2O", 8, 2, 2),
              ("NH3", 8, 3, 1), ("O2", 12, 2, 4)]
    for formula, total, shared, nonbonding in counts:
        assert total == 2 * (shared + nonbonding), formula

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axes = plt.subplots(1, 4, figsize=(10, 4.3), dpi=120)
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.26, top=0.78, wspace=0.16)
    fig.suptitle("Lewis bookkeeping: count each electron once", fontsize=16, y=0.96)
    headings = [r"Hydrogen: $\mathrm{H}_2$", r"Water: $\mathrm{H}_2\mathrm{O}$",
                r"Ammonia: $\mathrm{NH}_3$", r"Oxygen: $\mathrm{O}_2$"]
    budgets = ["1 + 1 = 2 electrons", "6 + 2 = 8 electrons",
               "5 + 3 = 8 electrons", "6 + 6 = 12 electrons"]
    for axis, heading, budget, (_, total, shared, nonbonding) in zip(
            axes, headings, budgets, counts):
        axis.set(xlim=(-1.25, 1.25), ylim=(-1.15, 1.05), aspect="equal")
        axis.axis("off")
        axis.set_title(heading, fontsize=12, pad=25)
        axis.text(0.5, 1.015, budget, ha="center", transform=axis.transAxes, fontsize=10)
        axis.text(0.5, -0.08, f"{shared} bond pair{'s' if shared != 1 else ''}\n"
                  f"{nonbonding} lone pair{'s' if nonbonding != 1 else ''}",
                  ha="center", va="top", transform=axis.transAxes, linespacing=1.5)

    axis = axes[0]
    atom(axis, "H", -0.65, 0)
    atom(axis, "H", 0.65, 0)
    bond(axis, (-0.65, 0), (0.65, 0))

    axis = axes[1]
    atom(axis, "O", 0, 0)
    for x in [-0.95, 0.95]:
        atom(axis, "H", x, 0)
        bond(axis, (0, 0), (x, 0))
    lone_pair(axis, 0, 0.45)
    lone_pair(axis, 0, -0.45)

    axis = axes[2]
    atom(axis, "N", 0, 0)
    for x, y in [(-0.95, 0), (0.95, 0), (0, -0.85)]:
        atom(axis, "H", x, y)
        bond(axis, (0, 0), (x, y))
    lone_pair(axis, 0, 0.45)

    axis = axes[3]
    for x in [-0.6, 0.6]:
        atom(axis, "O", x, 0)
        lone_pair(axis, x, 0.45)
        lone_pair(axis, x, -0.45)
    bond(axis, (-0.6, 0), (0.6, 0), pairs=2)
    axis.text(0.5, -0.44, "Paired drawing does not explain\nO2 paramagnetism", color="#555555",
              ha="center", transform=axis.transAxes, fontsize=9)

    fig.legend(handles=[Line2D([0], [0], color=BOND_COLOR, lw=3, label="Line = two shared electrons"),
                        Line2D([0], [0], color=LONE_COLOR, marker="o", ls="",
                               label="Two dots = one lone pair")],
               loc="lower center", bbox_to_anchor=(0.5, 0.015), ncol=2, frameon=False, fontsize=10)
    fig.text(0.5, 0.125, "Valence electrons only; schematic layouts, not shapes or trajectories.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "lewis-electron-pair-counts.png", transparent=False)
    plt.close(fig)
    print("Valence totals verified: H2=2 (1+0 pairs); H2O=8 (2+2); "
          "NH3=8 (3+1); O2=12 (2+4).")


if __name__ == "__main__":
    main()
