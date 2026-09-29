"""Exhaustively compare C(r) and N(<r>) in S3; save a white PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Products act on the rightmost factor first. Tuples give images of 1, 2, 3.
"""

from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def compose(left, right):
    return tuple(left[i - 1] for i in right)


def inverse(p):
    return tuple(p.index(i) + 1 for i in range(1, 4))


def conjugate(g, x):
    return compose(compose(g, x), inverse(g))


def cycle_label(p):
    remaining = set(range(1, 4))
    result = []
    while remaining:
        i = min(remaining)
        cycle = []
        while i in remaining:
            remaining.remove(i)
            cycle.append(str(i))
            i = p[i - 1]
        if len(cycle) > 1:
            result.append("(" + "".join(cycle) + ")")
    return "".join(result) or "e"


def compute():
    group = tuple(permutations((1, 2, 3)))
    e, t, r = (1, 2, 3), (2, 1, 3), (2, 3, 1)
    subgroup = {e, r, compose(r, r)}
    centralizer = {g for g in group if compose(g, r) == compose(r, g)}
    normalizer = {g for g in group
                  if {conjugate(g, h) for h in subgroup} == subgroup}
    assert centralizer == subgroup
    assert normalizer == set(group)
    assert conjugate(t, r) == inverse(r) != r
    assert {conjugate(t, h) for h in subgroup} == subgroup
    k = {e, t}
    assert {g for g in group if {conjugate(g, h) for h in k} == k} == k
    order = (e, t, (3, 2, 1), (1, 3, 2), r, inverse(r))
    rows = [[cycle_label(g), cycle_label(conjugate(g, r)),
             "yes" if g in centralizer else "no", "yes" if g in normalizer else "no"]
            for g in order]
    return rows, centralizer, normalizer


def draw_cycle(ax, p, center, color, title, direction):
    # Vertices 1,2,3 are clockwise in this layout; arrows are computed from p.
    vertices = np.array([[0, 0.072], [0.083, -0.06], [-0.083, -0.06]])
    vertices += np.asarray(center)
    for i, target in enumerate(p):
        ax.add_patch(FancyArrowPatch(vertices[i], vertices[target - 1],
                                    arrowstyle="-|>", mutation_scale=15,
                                    shrinkA=13, shrinkB=13, linewidth=2, color=color))
    ax.scatter(vertices[:, 0], vertices[:, 1], s=480, facecolor="white",
               edgecolor=color, linewidth=2, zorder=3)
    for label, point in enumerate(vertices, start=1):
        ax.text(*point, str(label), ha="center", va="center", color=color,
                weight="bold", zorder=4)
    ax.text(center[0], center[1] + 0.145, title, ha="center", color=color,
            fontsize=15, weight="bold")
    ax.text(center[0], center[1] - 0.115, direction, ha="center", fontsize=12)


def main():
    rows, centralizer, normalizer = compute()
    plt.rcParams.update({"font.size": 13, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(0.5, 0.955, "Fixing a generator versus preserving its subgroup",
            ha="center", fontsize=18, weight="bold")
    ax.text(0.5, 0.885, "r = (123),   H = ⟨r⟩ = {e, (123), (132)}",
            ha="center", fontsize=15)
    table = ax.table(cellText=rows,
                     colLabels=["g", "g r g⁻¹", "Fixes r?", "Preserves H?"],
                     colWidths=[0.12, 0.15, 0.16, 0.20],
                     cellLoc="center", bbox=(0.035, 0.285, 0.59, 0.515))
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#cbd5e1")
        if row == 0:
            cell.set_facecolor("#e2e8f0")
            cell.get_text().set_weight("bold")
        else:
            fixed = rows[row - 1][2] == "yes"
            cell.set_facecolor("#eef6fc" if fixed else "#fff5ec")
            if col == 2:
                cell.get_text().set_color("#2166a5" if fixed else "#b65b13")
    draw_cycle(ax, (2, 3, 1), (0.80, 0.65), "#2166a5",
               "r = (123)", "1 → 2 → 3 → 1; clockwise")
    draw_cycle(ax, (3, 1, 2), (0.80, 0.335), "#b65b13",
               "r⁻¹ = (132)", "1 → 3 → 2 → 1; counterclockwise")
    ax.text(0.5, 0.19, "C(r) = H: 3 elements        N(H) = S₃: all 6 elements",
            ha="center", fontsize=15, weight="bold")
    ax.text(0.5, 0.105, "t = (12) exchanges r and r⁻¹, keeping H intact:  t H t⁻¹ = H",
            ha="center", fontsize=14)
    ax.text(0.5, 0.035, "Products apply the rightmost factor first. Arrows show where each label goes.",
            ha="center", fontsize=11.5, color="#475569")
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.015, top=0.99)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print({"centralizer_size": len(centralizer), "normalizer_size": len(normalizer),
           "conjugation_rows": rows})


if __name__ == "__main__":
    main()
