"""Draw left multiplication in C4 and S3; write the matching PNG to CWD.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np


def compose(p, q):
    """Apply q first, then p."""
    return tuple(p[q[i]] for i in range(len(p)))


def cycles(permutation):
    remaining = set(range(len(permutation)))
    result = []
    while remaining:
        first = min(remaining)
        cycle, current = [], first
        while current in remaining:
            cycle.append(current)
            remaining.remove(current)
            current = permutation[current]
        result.append(cycle)
    return result


def draw(ax, permutation, labels, title, notation, color):
    parts = cycles(permutation)
    positions = {}
    for j, part in enumerate(parts):
        center = (j - (len(parts) - 1) / 2) * 2.35
        if len(part) == 2:
            points = [(center, .65), (center, -.65)]
        else:
            angles = np.pi / 2 - np.arange(len(part)) * 2 * np.pi / len(part)
            points = [(center + .78 * np.cos(a), .78 * np.sin(a)) for a in angles]
        positions.update(zip(part, points))
    for start, end in enumerate(permutation):
        ax.add_patch(FancyArrowPatch(
            positions[start], positions[end], arrowstyle="-|>",
            connectionstyle="arc3,rad=.22", shrinkA=22, shrinkB=22,
            mutation_scale=15, lw=2, color=color, zorder=1))
    for i, position in positions.items():
        ax.scatter(*position, s=1300, facecolor="white", edgecolor=color, lw=2, zorder=2)
        ax.text(*position, labels[i], ha="center", va="center", fontsize=14, zorder=3)
    extent = max(1.4, (len(parts) - 1) * 2.35 / 2 + 1.2)
    ax.set(xlim=(-extent, extent), ylim=(-1.25, 1.3), aspect="equal")
    ax.set_title(title, fontsize=15, pad=8)
    ax.text(.5, -.10, notation, ha="center", va="top", transform=ax.transAxes, fontsize=13)
    ax.axis("off")


def main():
    e, r, s = (0, 1, 2), (1, 2, 0), (1, 0, 2)
    r2 = compose(r, r)
    elements = [e, r, r2, s, compose(r, s), compose(r2, s)]
    assert len(set(elements)) == 6
    translations = [tuple(elements.index(compose(g, x)) for x in elements) for g in elements]
    for i, g in enumerate(elements):
        for j, h in enumerate(elements):
            assert compose(translations[i], translations[j]) == translations[elements.index(compose(g, h))]
    assert translations[1] == (1, 2, 0, 4, 5, 3)
    assert translations[3] == (3, 5, 4, 0, 2, 1)
    assert compose(translations[1], translations[3])[0] == 4
    assert compose(translations[3], translations[1])[0] == 5

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.3), facecolor="white")
    fig.suptitle("Cayley's model: each group element permutes all the labels", fontsize=18, y=.98)
    c4labels = [str(i) for i in range(4)]
    draw(axes[0, 0], (1, 2, 3, 0), c4labels, r"$C_4$: add 1", r"$L_1=(0\ 1\ 2\ 3)$", "#2369a0")
    draw(axes[0, 1], (2, 3, 0, 1), c4labels, r"$C_4$: add 2", r"$L_2=(0\ 2)(1\ 3)$", "#2369a0")
    labels = [r"$e$", r"$r$", r"$r^2$", r"$s$", r"$rs$", r"$r^2s$"]
    draw(axes[1, 0], translations[1], labels, r"$S_3$: multiply on the left by $r=(123)$",
         r"$L_r=(e\ r\ r^2)(s\ rs\ r^2s)$", "#ad4b24")
    draw(axes[1, 1], translations[3], labels, r"$S_3$: multiply on the left by $s=(12)$",
         r"$L_s=(e\ s)(r\ r^2s)(r^2\ rs)$", "#ad4b24")
    fig.subplots_adjust(left=.04, right=.98, top=.89, bottom=.12, hspace=.55, wspace=.25)
    fig.text(.5, .025, r"An arrow means $x\mapsto gx$.  Products act rightmost first: $L_gL_h=L_{gh}$.",
             ha="center", fontsize=13)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
