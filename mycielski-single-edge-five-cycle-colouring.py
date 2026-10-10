"""Draw K2 -> mu(K2)=C5; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; saves the matching PNG to the current working directory.
"""

from itertools import combinations, product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


PALETTE = ["#79b7e8", "#f2ae60", "#87cf9d"]
VERTICES = ["v1", "v2", "u1", "w", "u2"]
EDGES = [("v1", "v2"), ("v2", "u1"), ("u1", "w"), ("w", "u2"), ("u2", "v1")]
COLOURS = {"v1": 1, "v2": 2, "u1": 1, "u2": 2, "w": 3}


def verify():
    """Enumerate all labelled two- and three-colour assignments."""
    counts = {}
    for k in (2, 3):
        counts[k] = sum(
            all(c[VERTICES.index(a)] != c[VERTICES.index(b)] for a, b in EDGES)
            for c in product(range(k), repeat=5)
        )
    edge_set = {frozenset(e) for e in EDGES}
    triangles = sum(
        all(frozenset(e) in edge_set for e in combinations(t, 2))
        for t in combinations(VERTICES, 3)
    )
    assert counts == {2: 0, 3: 30}
    assert triangles == 0 and len(edge_set) == 5
    assert all(COLOURS[a] != COLOURS[b] for a, b in EDGES)
    return {"vertices": 5, "edges": 5, "triangles": triangles, "colouring_counts": counts}


def edge_style(a, b):
    if "w" in (a, b):
        return "#3c7b51", ":", 2.5
    if a.startswith("u") or b.startswith("u"):
        return "#68717d", "--", 2.2
    return "#283544", "-", 2.8


def draw(ax, positions, edges, colours):
    for a, b in edges:
        colour, style, width = edge_style(a, b)
        ax.plot(*zip(positions[a], positions[b]), color=colour, ls=style, lw=width, zorder=1)
    for name, p in positions.items():
        ax.scatter(*p, s=1050, color=PALETTE[colours[name] - 1], edgecolor="#283544", lw=1.5, zorder=3)
        ax.text(*p, str(colours[name]), ha="center", va="center", fontsize=14, weight="bold", zorder=4)
        offset = np.asarray(p) / (np.linalg.norm(p) or 1) * 0.44
        label = "$w$" if name == "w" else "$" + name[0] + "_" + name[1] + "$"
        ax.text(*(np.asarray(p) + offset), label, ha="center", va="center", fontsize=15)
    ax.set(xlim=(-1.55, 1.55), ylim=(-1.6, 1.6), aspect="equal")
    ax.axis("off")


def main():
    print(verify())
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.5), facecolor="white")
    draw(axes[0], {"v1": (-0.7, 0), "v2": (0.7, 0)}, [("v1", "v2")], COLOURS)
    axes[0].set_title(r"$K_2$: two colours", fontsize=15, pad=12)
    angles = np.pi / 2 - np.arange(5) * 2 * np.pi / 5
    positions = {v: (np.cos(t), np.sin(t)) for v, t in zip(VERTICES, angles)}
    draw(axes[1], positions, EDGES, COLOURS)
    axes[1].set_title(r"$\mu(K_2)=C_5$: three colours", fontsize=15, pad=12)
    fig.text(0.50, 0.54, r"$\mu$" + "\n" + r"$\longrightarrow$", ha="center", fontsize=21)
    legend = [Line2D([0], [0], color=c, ls=s, lw=w, label=l) for c, s, w, l in (
        ("#283544", "-", 2.8, "Original edge"),
        ("#68717d", "--", 2.2, "Shadow to original"),
        ("#3c7b51", ":", 2.5, "Apex to shadow"),
    )]
    fig.legend(handles=legend, loc="lower center", ncol=3, frameon=False, fontsize=11)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.86, bottom=0.16, wspace=0.28)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
