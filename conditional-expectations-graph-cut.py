"""Original Max-Cut comparison; Python 3.14, matplotlib 3.10.7, no graph library."""

from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle


VERTICES = "ABCDE"
EDGES = ("AB", "BC", "CD", "DE", "EA", "AC", "BD")
POSITIONS = {"A": (-0.9, 0.8), "B": (0.9, 0.8), "C": (1.25, -0.45),
             "D": (0.0, -1.15), "E": (-1.25, -0.45)}
INK = "#213547"
TEAL = "#167486"
FILLS = ("#dcecf8", "#ffe6b5")


def cut_size(labels):
    return sum(labels[u] != labels[v] for u, v in EDGES)


def main():
    # Use neighbour counts here, independently of the expectation ledger script.
    chosen = {}
    for v in VERTICES:
        neighbours = [e[1] if e[0] == v else e[0] for e in EDGES if v in e]
        d0 = sum(chosen.get(u) == 0 for u in neighbours)
        d1 = sum(chosen.get(u) == 1 for u in neighbours)
        chosen[v] = int(d0 > d1)
    all_labels = [dict(zip(VERTICES, bits)) for bits in product((0, 1), repeat=5)]
    optimum = max(map(cut_size, all_labels))
    best = next(labels for labels in all_labels if cut_size(labels) == optimum)
    assert tuple(chosen.values()) == (0, 1, 0, 0, 1)
    assert cut_size(chosen) == 5 and optimum == 6

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.35), dpi=125, facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.965, top=0.77, bottom=0.20, wspace=0.12)
    fig.suptitle("A guaranteed cut can miss the maximum", fontsize=20, color=INK,
                 weight="bold", y=0.96)
    fig.text(0.5, 0.875, "Same original graph: AB, BC, CD, DE, EA, AC, BD",
             ha="center", color=INK)
    for ax, labels, title in zip(axes, (chosen, best),
                                  ("Conditional expectations: 5 edges", "Maximum cut: 6 edges")):
        ax.set(xlim=(-1.65, 1.65), ylim=(-1.5, 1.2), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=13, weight="bold", color=INK, pad=8)
        for u, v in EDGES:
            crossing = labels[u] != labels[v]
            ax.plot((POSITIONS[u][0], POSITIONS[v][0]),
                    (POSITIONS[u][1], POSITIONS[v][1]),
                    color=TEAL if crossing else "#8b9298", lw=3 if crossing else 1.9,
                    ls="-" if crossing else (0, (4, 3)), zorder=1)
        for v, (x, y) in POSITIONS.items():
            ax.add_patch(Circle((x, y), 0.20, facecolor=FILLS[labels[v]],
                                edgecolor=INK, lw=1.3, zorder=2))
            ax.text(x, y, f"{v}\n{labels[v]}", ha="center", va="center", color=INK,
                    fontsize=12, weight="bold", linespacing=1.05, zorder=3)
    handles = [Line2D([], [], color=TEAL, lw=3, label="Crossing edge"),
               Line2D([], [], color="#8b9298", lw=1.9, ls="--", label="Noncrossing edge"),
               Line2D([], [], marker="o", ls="", markerfacecolor=FILLS[0],
                      markeredgecolor=INK, markersize=11, label="Side 0"),
               Line2D([], [], marker="o", ls="", markerfacecolor=FILLS[1],
                      markeredgecolor=INK, markersize=11, label="Side 1")]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.09),
               ncol=4, frameon=False, fontsize=11)
    fig.text(0.5, 0.045, "Node labels give the chosen bits. Crossings of lines are not vertices.",
             ha="center", color=INK, fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
