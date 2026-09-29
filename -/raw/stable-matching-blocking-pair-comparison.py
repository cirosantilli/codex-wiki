"""Compare a blocking pair and two stable outcomes; Python 3.14/matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg python ../stable-matching-blocking-pair-comparison.py
"""
from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

LEFT = {"A": "XYZ", "B": "XYZ", "C": "YZX"}
RIGHT = {"X": "CAB", "Y": "ABC", "Z": "ABC"}


def blocking_pairs(partners):
    """Check all unused pairs directly, independently of a proposal algorithm."""
    assigned = dict(zip(LEFT, partners))
    inverse = {r: l for l, r in assigned.items()}
    return [(l, r) for l in LEFT for r in RIGHT
            if assigned[l] != r
            and LEFT[l].index(r) < LEFT[l].index(assigned[l])
            and RIGHT[r].index(l) < RIGHT[r].index(inverse[r])]


def draw_matching(ax, partners, title, stable):
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(.5, .98, title, ha="center", va="top", fontsize=16, weight="bold", color="#172f44")
    ax.text(.5, .89, "STABLE" if stable else "UNSTABLE", ha="center", fontsize=12,
            color="#166952" if stable else "#b23c33", weight="bold")
    coords = {name: (x, y) for names, x in ((LEFT, .18), (RIGHT, .82))
              for name, y in zip(names, (.74, .50, .26))}
    for left, right in zip(LEFT, partners):
        a, b = coords[left], coords[right]
        ax.plot((a[0], b[0]), (a[1], b[1]), color="#2475ac", lw=3, zorder=1)
    if not stable:
        ax.add_patch(FancyArrowPatch(coords["B"], coords["Y"], arrowstyle="<->", mutation_scale=17,
                                     lw=2.5, linestyle="--", color="#c23a31", zorder=2,
                                     shrinkA=19, shrinkB=19))
        ax.text(.5, .55, "blocking pair", color="#b23c33", ha="center", fontsize=12,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for name, (x, y) in coords.items():
        ax.add_patch(Circle((x, y), .045, fc="white", ec="#172f44", lw=1.5, zorder=3))
        ax.text(x, y, name, ha="center", va="center", weight="bold", fontsize=14, zorder=4)
    left_ranks = ", ".join(str(LEFT[l].index(r) + 1) for l, r in zip(LEFT, partners))
    inverse = {r: l for l, r in zip(LEFT, partners)}
    right_ranks = ", ".join(str(RIGHT[r].index(inverse[r]) + 1) for r in RIGHT)
    ax.text(.5, .10, f"Left partner ranks: {left_ranks}", ha="center", fontsize=11)
    ax.text(.5, .035, f"Right partner ranks: {right_ranks}", ha="center", fontsize=11)


def main():
    all_pairs = {"".join(p): blocking_pairs(p) for p in permutations(RIGHT)}
    assert all_pairs == {"XYZ": [], "XZY": [("B", "Y")], "YXZ": [("A", "X")],
                         "YZX": [], "ZXY": [("A", "X"), ("A", "Y")], "ZYX": [("A", "Y")]}
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(11.7, 6.7), dpi=120, facecolor="white")
    fig.text(.035, .96, "The same preferences: one blocking pair, two stable outcomes", fontsize=18,
             weight="bold", va="top", color="#172f44")
    fig.text(.035, .88, "Left:   A: X > Y > Z     B: X > Y > Z     C: Y > Z > X", fontsize=12)
    fig.text(.035, .83, "Right: X: C > A > B     Y: A > B > C     Z: A > B > C", fontsize=12)
    for i, (partners, title, stable) in enumerate([
            ("XZY", "N: a perfect matching", False),
            ("XYZ", "Mₗ: left proposes", True),
            ("YZX", "Mᵣ: right proposes", True)]):
        ax = fig.add_axes((.025 + i * .325, .205, .305, .565))
        draw_matching(ax, partners, title, stable)
    fig.text(.035, .13, "In N: B prefers Y to Z, and Y prefers B to C. Both would change partners.",
             fontsize=12, color="#b23c33")
    fig.text(.035, .082, "Every left vertex prefers Mₗ; every right vertex prefers Mᵣ. Both have no blocking pair.", fontsize=12)
    fig.text(.035, .035, "Blue lines = matched pairs. Red dashed arrow = unused blocking pair. Crossings are not vertices. Rank 1 is best.", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
