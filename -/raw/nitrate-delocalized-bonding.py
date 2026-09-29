"""Draw an original symbolic nitrate bonding diagram; save basename PNG to cwd.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../nitrate-delocalized-bonding.py
Tested with Python 3.14.4, Matplotlib 3.10.7 (+dfsg1), NumPy 2.3.5.
Dashed companions symbolize delocalization; this is not a density calculation.
The fraction 4/3 is an equal-contributor Lewis count, not a universal observable.
"""
from fractions import Fraction
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BOND = "#216b97"
INK = "#222222"


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    orders = [(2, 1, 1), (1, 2, 1), (1, 1, 2)]
    averages = [sum(Fraction(row[j], 3) for row in orders) for j in range(3)]
    assert averages == [Fraction(4, 3)] * 3
    fig = plt.figure(figsize=(8.6, 5.6), dpi=120)
    ax = fig.add_axes([.065, .27, .48, .52])
    ax.set(xlim=(-2.1, 2.1), ylim=(-1.65, 2.0), aspect="equal")
    ax.axis("off")
    fig.suptitle("Nitrate: one electronic structure, three equivalent bonds", fontsize=16, y=.96)
    fig.text(.5, .895, "Isolated symmetric ion; symbolic bonding diagram", ha="center", fontsize=12)
    ax.text(0, 0, "N", ha="center", va="center", fontsize=28, color=INK)
    directions = np.array([[0., 1.], [-np.sqrt(3)/2, -.5], [np.sqrt(3)/2, -.5]])
    for i, direction in enumerate(directions):
        tangent = np.array([-direction[1], direction[0]])
        points = np.array([.28 * direction, 1.11 * direction])
        ax.plot(*points.T, lw=3, color=BOND, solid_capstyle="round")
        companion = points + .15 * tangent
        ax.plot(*companion.T, lw=2.3, color=BOND, ls=(0, (3, 3)))
        ax.text(*(1.43 * direction), rf"$\mathrm{{O}}_{i+1}$", ha="center", va="center", fontsize=26, color=INK)
        ax.text(*(.76 * direction - .30 * tangent), r"$\frac{4}{3}$", ha="center", va="center", fontsize=18,
                color=BOND, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for side in [-1, 1]:
        x = side * 1.88
        ax.plot([x, x], [-1.5, 1.85], lw=1.2, color=INK)
        ax.plot([x, x - side * .12], [1.85, 1.85], lw=1.2, color=INK)
        ax.plot([x, x - side * .12], [-1.5, -1.5], lw=1.2, color=INK)
    ax.text(1.98, 1.94, "−", fontsize=18, color=INK, ha="left", va="center", clip_on=False)
    fig.text(.59, .735, "Track any one N–O connection:", fontsize=12)
    fig.text(.59, .655, "double in one contributor\nsingle in two contributors", fontsize=12, linespacing=1.8)
    fig.text(.59, .495, r"$\overline{b} = \frac{2+1+1}{3} = \frac{4}{3}$", fontsize=21, color=BOND)
    fig.text(.59, .365, "Equal weighting within the\nthree-contributor Lewis model", fontsize=11, linespacing=1.7)
    fig.text(.5, .195, "Identical line styles indicate equivalent bonds; no bond is selected as a double bond.", ha="center", fontsize=10)
    fig.text(.5, .135, "Dashed companions are symbols, not electron density or electron paths.", ha="center", fontsize=10)
    fig.text(.5, .065, "4/3 is a model average, not a universal measured bond order of exactly 1.333…", ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False, facecolor="white")
    plt.close(fig)
    print("Independent rational averaging:", [str(x) for x in averages])


if __name__ == "__main__":
    main()
