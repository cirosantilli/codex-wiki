"""Idealized four-domain frameworks for CH4, NH3 and H2O.

These ideal tetrahedral directions illustrate domain counting and molecular
shape, not measured bond angles or lone-pair shapes. Writes PNG to CWD.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    directions = np.array([[1, 1, 1], [1, -1, -1],
                           [-1, 1, -1], [-1, -1, 1]], dtype=float)/np.sqrt(3)
    # Remove selected bonded neighbours while retaining their domain directions.
    cases = [
        ("Methane  CH₄", "C", "#374653", set(), "4 bond pairs + 0 lone pairs\nTetrahedral"),
        ("Ammonia  NH₃", "N", "#386fa6", {0}, "3 bond pairs + 1 lone pair\nTrigonal pyramidal"),
        ("Water  H₂O", "O", "#bd4244", {0, 3}, "2 bond pairs + 2 lone pairs\nBent"),
    ]
    fig = plt.figure(figsize=(11.8, 6.3), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.015, right=0.985, top=0.82, bottom=0.22,
                         wspace=0.02)
    for panel, (title, centre, color, lone_pairs, description) in enumerate(cases, 1):
        ax = fig.add_subplot(1, 3, panel, projection="3d")
        for index, direction in enumerate(directions):
            lp = index in lone_pairs
            ax.plot([0, direction[0]], [0, direction[1]], [0, direction[2]],
                    color="#d2933e" if lp else "#5b6d79",
                    linestyle="--" if lp else "-", linewidth=1.7 if lp else 3)
            ax.scatter(*direction, s=700 if lp else 240,
                       c="#e3ab50" if lp else "#f0f3f5",
                       alpha=0.35 if lp else 1,
                       edgecolors="#cb9845" if lp else "#8d9aa4",
                       linewidths=1)
            ax.text(*(direction*1.16), "LP" if lp else "H",
                    color="#936119" if lp else "#334451", ha="center",
                    va="center", fontsize=12)
        ax.scatter(0, 0, 0, s=390, c=color, edgecolors="white", linewidths=1)
        ax.text(0, 0, 0, centre, color="white", ha="center",
                va="center", fontsize=11, weight="bold", zorder=10)
        ax.set(xlim=(-0.86, 0.86), ylim=(-0.86, 0.86), zlim=(-0.86, 0.86))
        ax.set_box_aspect((1, 1, 1))
        ax.view_init(elev=18, azim=-32)
        ax.set_proj_type("ortho")
        ax.set_axis_off()
        ax.set_title(title, fontsize=14, pad=5)
        ax.text2D(0.5, -0.04, description, transform=ax.transAxes,
                  ha="center", va="top", fontsize=12, linespacing=1.5)
    fig.suptitle("Same four-domain framework, different molecular shapes",
                 fontsize=16, y=0.965)
    fig.text(0.5, 0.88, "Count lone pairs as domains; count only atoms for molecular geometry.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.05,
             "Shaded LP regions stand for lone-pair domains, not additional atoms.\n"
             "Directions are idealized. Real ammonia and water bond angles differ from the tetrahedral 109.47°.",
             ha="center", fontsize=11, linespacing=1.5, color="#444")
    fig.savefig(Path.cwd() / "vsepr-four-domain-shapes.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
