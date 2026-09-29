"""Draw a consistently oriented Ampere loop through an ideal infinite winding.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Write the same-basename opaque PNG to CWD; use the root Make media target.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


def arrow(ax, start, end, colour, scale=15, width=2):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=scale,
                                color=colour, lw=width, zorder=5))


def main():
    # Physical coordinates: +x is page-up, +y is out of page, +z is page-right.
    # Top wire dl=+y and source-to-axis R=-x give dl cross R=+z.
    np.testing.assert_array_equal(np.cross([0, 1, 0], [-1, 0, 0]), [0, 0, 1])
    np.testing.assert_array_equal(np.cross([0, -1, 0], [1, 0, 0]), [0, 0, 1])
    wire_z = np.arange(-4.5, 5, 1.0)
    loop_left, loop_right = -3.0, 3.0
    crossings = wire_z[(wire_z > loop_left) & (wire_z < loop_right)]
    density, path_length = 1.0, loop_right - loop_left
    assert len(crossings) == density * path_length == 6
    # Interior +z followed by outward +x: oriented surface normal z cross x=+y.
    np.testing.assert_array_equal(np.cross([0, 0, 1], [1, 0, 0]), [0, 1, 0])
    print("Right-hand field and loop-normal signs verified; ns=6 upper crossings, 0 lower crossings.")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    blue, orange, grey = "#216baf", "#b55c2b", "#52616c"
    fig, ax = plt.subplots(figsize=(8, 5), dpi=120, facecolor="white")
    ax.set(xlim=(-5.8, 6.0), ylim=(-3.0, 3.6), aspect="equal")
    ax.axis("off")
    ax.add_patch(Rectangle((-5.4, -1), 10.8, 2, color="#edf3f7", zorder=0))
    for row in (-1, 1):
        ax.plot([-5.5, 5.5], [row, row], color=grey, lw=1, ls=":")
        for z in wire_z:
            ax.add_patch(Circle((z, row), 0.14, facecolor="white", edgecolor=orange, lw=1.8, zorder=3))
            if row == 1:
                ax.add_patch(Circle((z, row), 0.045, color=orange, zorder=4))
            else:
                ax.plot([z - 0.07, z + 0.07], [row - 0.07, row + 0.07], color=orange, lw=1.5, zorder=4)
                ax.plot([z - 0.07, z + 0.07], [row + 0.07, row - 0.07], color=orange, lw=1.5, zorder=4)
        ax.text(-5.75, row, "…", va="center", ha="center", color=grey)
        ax.text(5.75, row, "…", va="center", ha="center", color=grey)

    # The lower path lies inside and goes right; the exterior return goes left.
    bottom, top = 0.0, 2.1
    ax.plot([loop_left, loop_right, loop_right, loop_left, loop_left],
            [bottom, bottom, top, top, bottom], color=orange, lw=2)
    arrow(ax, (-1.7, bottom), (-0.9, bottom), orange)
    arrow(ax, (loop_right, 1.3), (loop_right, 1.9), orange)
    arrow(ax, (1.0, top), (0.2, top), orange)
    arrow(ax, (loop_left, 0.8), (loop_left, 0.2), orange)
    for x in (-0.55, 0.55):
        for z in (-4.7, -1.8, 1.2, 4.1):
            arrow(ax, (z, x), (z + 0.65, x), blue, scale=12, width=1.7)

    ax.text(0, 3.25, "An Ampère loop crosses one side of the winding", ha="center", fontsize=14)
    ax.text(0, 2.7, r"Exterior return: $\mathbf{B}=0$ in the infinite ideal model", ha="center", color=grey)
    ax.text(-2.7, 1.65, r"$ns=6$ positive current crossings", color=orange, fontsize=10)
    ax.text(3.3, 1.8, r"$\Gamma$", color=orange, fontsize=14)
    ax.text(0, -1.48, r"Inside: $\mathbf{B}=\mu_0 n I\,\hat{\mathbf{z}}$", ha="center", color=blue)
    arrow(ax, (3.9, -1.6), (5.0, -1.6), grey, scale=12, width=1.2)
    ax.text(5.12, -1.6, r"$+z$", va="center", color=grey)
    ax.annotate("", (loop_right, -1.98), (loop_left, -1.98),
                arrowprops={"arrowstyle": "<->", "color": grey, "lw": 1.1})
    ax.text(0, -2.25, r"Path length $s$: $Bs=\mu_0(ns)I$", ha="center")
    ax.text(0, -2.85, "Dot: current out of page   •   Cross: current into page   |   Winding continues at both sides",
            ha="center", fontsize=9, color=grey)
    fig.subplots_adjust(left=0.025, right=0.975, bottom=0.015, top=0.98)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
