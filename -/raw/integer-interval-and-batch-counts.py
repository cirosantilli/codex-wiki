"""Exact integer counts, contrasted with ceiling capacity requirements."""
from pathlib import Path
import math

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, (interval, batch) = plt.subplots(1, 2, figsize=(11.6, 5.8),
                                         layout="constrained")
    cases = [(-2.7, 1.1), (-2, 2), (.2, 4.7), (.2, .8)]
    lattice = np.arange(-3, 6)
    for row, (a, b) in enumerate(cases):
        y = 3 - row
        selected = lattice[(lattice >= a) & (lattice <= b)]
        count = max(0, math.floor(b) - math.ceil(a) + 1)
        assert len(selected) == count
        interval.plot(lattice, np.full_like(lattice, y), color="#d4dde1", lw=.8)
        interval.plot([a, b], [y, y], color="#c26030", lw=4,
                      solid_capstyle="butt", alpha=.7)
        interval.scatter(lattice, np.full_like(lattice, y), color="#b6c2c9",
                         s=30, zorder=3)
        interval.scatter(selected, np.full_like(selected, y), color="#167e8d",
                         s=48, zorder=4)
        endpoint_colors = ["#167e8d" if float(value).is_integer() else "#c26030"
                           for value in (a, b)]
        interval.scatter([a, b], [y, y], facecolors=endpoint_colors,
                         edgecolors="#c26030", s=43, linewidths=1.3, zorder=5)
        interval.text(-3.35, y + .30, f"[{a:g}, {b:g}]: {count} integer points",
                      fontsize=11)
    interval.set(title="Real endpoints choose the allowed integers",
                  xlabel="Real number line", xlim=(-3.5, 5.3), ylim=(-.5, 3.75),
                  xticks=lattice, yticks=[])
    interval.spines[["top", "right", "left"]].set_visible(False)
    interval.text(-3.35, -.33, "Blue points are counted; orange bars show closed intervals.",
                  fontsize=9)
    items, capacity = 102, 20
    batches = math.ceil(items / capacity)
    assert batches == 6 and (batches - 1) * capacity < items <= batches * capacity
    for index in range(batches):
        x, y = index % 3 * 1.42, 1 - index // 3 * 1.18
        used = min(capacity, max(0, items - index * capacity))
        batch.add_patch(Rectangle((x - .08, y - .08), 1.12, .92,
                                   facecolor="white", edgecolor="#8396a2", lw=1.2))
        for place in range(capacity):
            px, py = place % 5, place // 5
            batch.add_patch(Rectangle((x + .2 * px, y + .2 * py), .16, .16,
                                       facecolor="#167e8d" if place < used else "#e4ebee",
                                       edgecolor="white", lw=.4))
        batch.text(x + .46, y - .27, f"Batch {index + 1}: {used}/20",
                    ha="center", fontsize=10)
    batch.text(1.85, 2.02, r"$\lceil102/20\rceil=6$", ha="center", fontsize=17)
    batch.text(1.85, -.93, "5 full batches + 1 with two items\n18 unused places",
                ha="center", fontsize=12, linespacing=1.5)
    batch.set(title="A partly filled batch still counts as one",
               xlim=(-.26, 4.2), ylim=(-1.27, 2.35))
    batch.set_aspect("equal")
    batch.set_axis_off()
    fig.suptitle("Floor and ceiling turn boundaries into exact discrete counts", fontsize=17)
    fig.get_layout_engine().set(rect=(0, .065, 1, .90))
    fig.text(.5, .017, "Interval length differs from its integer-point count; complete groups differ from sufficient capacity.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
