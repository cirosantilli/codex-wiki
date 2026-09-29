"""Draw a matching/cover optimality certificate in K2,3; write PNG to CWD.

Tested with Python 3.14.4 and Matplotlib 3.10.7, as in pyproject.toml.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3 ../bipartite-matching-cover-certificate.py
"""
from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


def main():
    left, right = {"a", "b"}, {"x", "y", "z"}
    edges = list(product(sorted(left), sorted(right)))
    matching = {("a", "x"), ("b", "y")}
    assert matching <= set(edges)
    assert len({v for e in matching for v in e}) == 2 * len(matching)
    assert all(u in left or v in left for u, v in edges)
    positions = {"a": (-1.2, 0.8), "b": (-1.2, -0.8),
                 "x": (1.2, 1.15), "y": (1.2, 0), "z": (1.2, -1.15)}
    orange, blue, gray = "#a95012", "#176db1", "#afb7c1"
    fig, ax = plt.subplots(figsize=(8.6, 4.6), dpi=100, facecolor="white")
    for u, v in edges:
        ax.plot([positions[u][0], positions[v][0]],
                [positions[u][1], positions[v][1]], color=gray, lw=1.7, zorder=1)
    for u, v in sorted(matching):
        ax.plot([positions[u][0], positions[v][0]],
                [positions[u][1], positions[v][1]], color=blue, lw=4, zorder=2)
    for v, pos in positions.items():
        covered = v in left
        ax.add_patch(Circle(pos, 0.16, facecolor=orange if covered else "white",
                            edgecolor=orange if covered else "#536170", lw=2, zorder=3))
        ax.text(*pos, v, ha="center", va="center", fontsize=15, weight="bold",
                color="white" if covered else "#253342", zorder=4)
    ax.text(-1.2, 1.55, r"$L=\{a,b\}$", ha="center", fontsize=14)
    ax.text(1.2, 1.55, r"$R=\{x,y,z\}$", ha="center", fontsize=14)
    ax.text(2.1, 1.15, "A certificate of optimality", fontsize=13, weight="bold")
    ax.text(2.1, 0.67, r"$C=\{a,b\},\quad |C|=2$", fontsize=14)
    ax.text(2.1, 0.17, r"$M=\{ax,by\},\quad |M|=2$", fontsize=14)
    ax.text(2.1, -0.38, r"$2=|M|\leq\tau(G)\leq |C|=2$", fontsize=14)
    ax.text(2.1, -0.97, r"$\nu(K_{2,3})=\tau(K_{2,3})=2$", fontsize=15, weight="bold")
    ax.set(xlim=(-1.65, 5.7), ylim=(-1.5, 1.85), aspect="equal")
    ax.axis("off")
    ax.legend(handles=[Line2D([0], [0], marker="o", markersize=12, linestyle="none",
                             color=orange, label="Selected cover vertices"),
                       Line2D([0], [0], color=blue, lw=4, label="Disjoint matching edges")],
              loc="lower center", bbox_to_anchor=(0.5, -0.17), ncol=2, frameon=False, fontsize=11)
    fig.suptitle(r"$K_{2,3}$: a two-vertex cover meets the matching lower bound", fontsize=15, y=0.96)
    fig.text(0.5, 0.03, "All six edges touch a selected left vertex. Edge crossings are not vertices.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.025, right=0.98, top=0.85, bottom=0.22)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
