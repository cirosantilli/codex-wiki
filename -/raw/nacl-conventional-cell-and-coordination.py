"""Original NaCl cell accounting and six-neighbour geometry; no measured data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(11, 6.2), dpi=110)
    left = fig.add_subplot(121, projection="3d")
    right = fig.add_subplot(122, projection="3d")
    blue, orange = "#176baf", "#d76b13"
    # Coordinates are in units of a/2. Even parity is Cl, odd parity Na.
    sites = np.array(list(product(range(3), repeat=3)))
    chloride = sites[sites.sum(axis=1) % 2 == 0] / 2
    sodium = sites[sites.sum(axis=1) % 2 == 1] / 2
    for p in product([0, 1], repeat=3):
        p = np.array(p)
        for axis in range(3):
            if p[axis] == 0:
                q = p.copy()
                q[axis] = 1
                left.plot(*np.stack([p, q]).T, color=".6", lw=.8, zorder=0)
    left.scatter(*chloride.T, s=95, c=orange, edgecolors="white", depthshade=False,
                 label=r"$\mathrm{Cl}^-$")
    left.scatter(*sodium.T, s=65, c=blue, edgecolors="white", depthshade=False,
                 label=r"$\mathrm{Na}^+$")
    left.legend(loc="upper left", frameon=False)
    left.set_title("Conventional cubic cell, side a", pad=16, weight="bold")
    left.text(.5, -.15, -.13, "a", color=".3")
    center = np.array([0., 0., 0.])
    neighbors = np.concatenate([np.eye(3), -np.eye(3)]) / 2
    for p in neighbors:
        right.plot(*np.stack([center, p]).T, color=".65", lw=1)
    right.scatter(*neighbors.T, s=240, c=orange, edgecolors="white", depthshade=False)
    right.scatter(0, 0, 0, s=140, c=blue, edgecolors="white", depthshade=False)
    right.text(.52, 0, .03, r"$\mathrm{Cl}^-$")
    right.text(.03, .02, .08, r"$\mathrm{Na}^+$", color=blue)
    right.set_title("Six nearest unlike neighbours", pad=16, weight="bold")
    for ax in [left, right]:
        ax.set_box_aspect((1, 1, 1))
        ax.set_axis_off()
        ax.view_init(elev=20, azim=-55)
    fig.suptitle("NaCl: count shared sites and distinguish the neighbour shells", fontsize=15)
    fig.text(.27, .19, r"$\mathrm{Cl}^-:\quad8\times\frac{1}{8}+6\times\frac{1}{2}=4$",
             ha="center", fontsize=13, color=orange)
    fig.text(.27, .13, r"$\mathrm{Na}^+:\quad12\times\frac{1}{4}+1=4$",
             ha="center", fontsize=13, color=blue)
    fig.text(.76, .19, r"Unlike ions: 6 at distance $a/2$", ha="center", fontsize=12)
    fig.text(.76, .13, r"Same ions (FCC): 12 at distance $a/\sqrt{2}$", ha="center", fontsize=12)
    fig.text(.5, .035, "Ideal geometry; dot sizes are symbolic. Grey segments show distances, not discrete NaCl molecules.",
             ha="center", fontsize=10, color=".3")
    fig.subplots_adjust(left=.015, right=.985, bottom=.23, top=.86, wspace=.02)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
