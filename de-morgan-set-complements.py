"""Generate de-morgan-set-complements.png in the current directory.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Both sides of each identity shade the same membership regions in U.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np


A = {1, 2, 3}
B = {3, 4}
U = set(range(1, 7))
POSITIONS = {1: (-1.2, .35), 2: (-1.2, -.35), 3: (0, 0),
             4: (1.5, 0), 5: (-2.1, -1.25), 6: (2.1, -1.25)}
RADIUS = 1.25
BOUNDS = (-2.65, 2.65, -1.65, 1.65)


def draw_panel(ax, region, selected, title, answer):
    x = np.linspace(BOUNDS[0], BOUNDS[1], 801)
    y = np.linspace(BOUNDS[2], BOUNDS[3], 501)
    xx, yy = np.meshgrid(x, y)
    in_a = (xx + .8) ** 2 + yy ** 2 <= RADIUS ** 2
    in_b = (xx - .8) ** 2 + yy ** 2 <= RADIUS ** 2
    ax.contourf(xx, yy, region(in_a, in_b).astype(int),
                levels=[-.5, .5, 1.5], colors=["white", "#b9e0d4"])
    ax.add_patch(Rectangle((BOUNDS[0], BOUNDS[2]), BOUNDS[1] - BOUNDS[0],
                           BOUNDS[3] - BOUNDS[2], fill=False, lw=1.3,
                           edgecolor="#68777e", clip_on=False))
    for cx in [-.8, .8]:
        ax.add_patch(Circle((cx, 0), RADIUS, fill=False, lw=1.7,
                            edgecolor="#263c48"))
    ax.text(-1.05, 1.03, "$A$", ha="center", fontsize=13)
    ax.text(1.05, 1.03, "$B$", ha="center", fontsize=13)
    ax.text(-2.45, 1.32, "$U$", fontsize=13)
    for n, (px, py) in POSITIONS.items():
        assert (((px + .8) ** 2 + py ** 2 <= RADIUS ** 2) == (n in A))
        assert (((px - .8) ** 2 + py ** 2 <= RADIUS ** 2) == (n in B))
        assert bool(region(n in A, n in B)) == (n in selected)
        ax.text(px, py, str(n), ha="center", va="center", fontsize=14,
                color="#123e32" if n in selected else "#6a747a",
                fontweight="bold" if n in selected else "normal",
                bbox={"boxstyle": "circle,pad=.17", "facecolor": "white",
                      "edgecolor": "#28735d" if n in selected else "#c6cdd1"})
    ax.set(xlim=(BOUNDS[0] - .08, BOUNDS[1] + .08),
           ylim=(BOUNDS[2] - .08, BOUNDS[3] + .08), aspect="equal")
    ax.set_title(title, fontsize=14, pad=12)
    ax.text(.5, -.08, answer, transform=ax.transAxes, ha="center", fontsize=12)
    ax.axis("off")


def main():
    complement_union = U - (A | B)
    complement_intersection = U - (A & B)
    assert complement_union == (U - A) & (U - B) == {5, 6}
    assert complement_intersection == (U - A) | (U - B) == {1, 2, 4, 5, 6}
    fig, axes = plt.subplots(2, 2, figsize=(8.8, 6.9), dpi=120,
                             facecolor="white")
    panels = [
        (lambda a, b: ~(np.asarray(a) | b), complement_union,
         r"$U\setminus(A\cup B)$", r"$\{5,6\}$: fail both tests"),
        (lambda a, b: ~np.asarray(a) & ~np.asarray(b), (U - A) & (U - B),
         r"$(U\setminus A)\cap(U\setminus B)$", r"$\{5,6\}$: fail both tests"),
        (lambda a, b: ~(np.asarray(a) & b), complement_intersection,
         r"$U\setminus(A\cap B)$", r"$\{1,2,4,5,6\}$: fail at least one"),
        (lambda a, b: ~np.asarray(a) | ~np.asarray(b), (U - A) | (U - B),
         r"$(U\setminus A)\cup(U\setminus B)$", r"$\{1,2,4,5,6\}$: fail at least one"),
    ]
    for ax, panel in zip(axes.flat, panels):
        draw_panel(ax, *panel)
    fig.suptitle("De Morgan's laws: matching regions in each row", fontsize=16, y=.97)
    fig.text(.5, .914, r"$A=\{1,2,3\},\quad B=\{3,4\},\quad U=\{1,2,3,4,5,6\}$",
             ha="center", fontsize=12)
    fig.text(.5, .025, "Green regions are selected. Every complement is taken within U.\n"
             "Circle areas do not represent the number of elements.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.045, right=.955, top=.84, bottom=.14,
                        hspace=.48, wspace=.13)
    fig.savefig(Path.cwd() / "de-morgan-set-complements.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
