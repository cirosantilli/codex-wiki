"""Draw C5 -> mu(C5); Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; saves the matching PNG to the current working directory.
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


PALETTE = ["#79b7e8", "#f2ae60", "#87cf9d", "#d5a0df"]
ORIGINAL_EDGES = [(i, (i + 1) % 5) for i in range(5)]
EDGES = ORIGINAL_EDGES + [(5 + i, j) for i in range(5) for j in ((i - 1) % 5, (i + 1) % 5)] + [(10, 5 + i) for i in range(5)]
COLOURS = [1, 2, 1, 2, 3] * 2 + [4]


def count_colourings(k):
    """Exact backtracking in fixed labelled vertex order; no symmetry quotient."""
    previous = [[] for _ in range(11)]
    for a, b in EDGES:
        a, b = sorted((a, b))
        previous[b].append(a)
    assignment = [-1] * 11

    def visit(i):
        if i == 11:
            return 1
        total = 0
        forbidden = {assignment[j] for j in previous[i]}
        for c in range(k):
            if c not in forbidden:
                assignment[i] = c
                total += visit(i + 1)
        return total

    return visit(0)


def verify():
    edge_set = {frozenset(e) for e in EDGES}
    triangles = sum(
        all(frozenset(e) in edge_set for e in combinations(t, 2))
        for t in combinations(range(11), 3)
    )
    counts = {k: count_colourings(k) for k in (3, 4)}
    assert len(edge_set) == 20 and triangles == 0
    assert counts[3] == 0 and counts[4] > 0
    assert all(COLOURS[a] != COLOURS[b] for a, b in EDGES)
    return {"vertices": 11, "edges": 20, "triangles": triangles, "colouring_counts": counts}


def draw(ax, constructed):
    angles = np.pi / 2 - np.arange(5) * 2 * np.pi / 5
    positions = {i: np.array((2 * np.cos(t), 2 * np.sin(t))) for i, t in enumerate(angles)}
    if constructed:
        positions.update({5 + i: np.array((np.cos(t), np.sin(t))) for i, t in enumerate(angles)})
        positions[10] = np.zeros(2)
    for a, b in EDGES if constructed else ORIGINAL_EDGES:
        if 10 in (a, b):
            colour, style, width = "#886196", ":", 2.4
        elif a >= 5 or b >= 5:
            colour, style, width = "#8a919a", "--", 1.8
        else:
            colour, style, width = "#283544", "-", 2.5
        ax.plot(*zip(positions[a], positions[b]), color=colour, ls=style, lw=width, zorder=1)
    for i, p in positions.items():
        ax.scatter(*p, s=750, color=PALETTE[COLOURS[i] - 1], edgecolor="#283544", lw=1.4, zorder=3)
        ax.text(*p, str(COLOURS[i]), ha="center", va="center", fontsize=13, weight="bold", zorder=4)
        if i == 10:
            label, offset = "$w$", np.array((0.45, -0.29))
        elif i < 5:
            label, offset = "$v_" + str(i + 1) + "$", p / 2 * 0.48
        else:
            label = "$u_" + str(i - 4) + "$"
            # Tangential labels leave radial apex spokes unobstructed.
            offset = np.array((-p[1], p[0])) * 0.48
        ax.text(*(p + offset), label, ha="center", va="center", fontsize=14,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.4}, zorder=5)
    ax.set(xlim=(-2.65, 2.65), ylim=(-2.65, 2.65), aspect="equal")
    ax.axis("off")


def main():
    print(verify())
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 5.3), facecolor="white")
    draw(axes[0], False)
    draw(axes[1], True)
    axes[0].set_title(r"$C_5$: three colours", fontsize=15, pad=12)
    axes[1].set_title("Grötzsch graph: four colours", fontsize=15, pad=12)
    fig.text(0.50, 0.54, r"$\mu$" + "\n" + r"$\longrightarrow$", ha="center", fontsize=21)
    legend = [Line2D([0], [0], color=c, ls=s, lw=w, label=l) for c, s, w, l in (
        ("#283544", "-", 2.5, "5 original edges"),
        ("#8a919a", "--", 1.8, "10 shadow–original edges"),
        ("#886196", ":", 2.4, "5 apex–shadow edges"),
    )]
    fig.legend(handles=legend, loc="lower center", ncol=3, frameon=False, fontsize=10)
    fig.text(0.5, 0.09, "Inner shadows have no edges to each other. Crossings without dots are not vertices.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.17, wspace=0.25)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
