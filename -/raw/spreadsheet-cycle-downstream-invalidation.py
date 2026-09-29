"""Original affected-subgraph and cyclic-reference illustrations.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The PNG is written to the current directory with this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def diagram(ax, cyclic):
    ax.set(xlim=(-0.8, 7.1), ylim=(-0.65, 4.7))
    ax.axis("off")
    pos = {"A1": (0, 3.7), "A2": (0, 0.8), "B1": (2.1, 3.7),
           "B2": (2.1, 1.6), "C1": (4.3, 3.0), "D1": (6.3, 3.0),
           "E1": (2.1, -0.05)}
    edges = [("A1", "B1"), ("A2", "B1"), ("A1", "B2"),
             ("B1", "C1"), ("B2", "C1"), ("C1", "D1"), ("A2", "E1")]
    if cyclic:
        edges.append(("C1", "B1"))
    boxes = {}
    old = {"A1": "3 → 5", "A2": "4", "B1": "7 → 9", "B2": "6 → 10",
           "C1": "13 → 19", "D1": "6.5 → 9.5", "E1": "16"}
    for cell, (x, y) in pos.items():
        if cyclic:
            fill = "#ffdfe1" if cell in {"B1", "C1"} else "#ffe9d3" if cell == "D1" else "#e8f2fb"
            label = "cyclic" if cell in {"B1", "C1"} else "blocked" if cell == "D1" else {"A1": "3", "A2": "4", "B2": "6", "E1": "16"}[cell]
        else:
            fill = "#ffc777" if cell == "A1" else "#fff0d6" if cell in {"B1", "B2", "C1", "D1"} else "#e8f2fb"
            label = old[cell]
        boxes[cell] = FancyBboxPatch((x-0.60, y-0.39), 1.2, 0.78,
                                    boxstyle="round,pad=0.02", facecolor=fill,
                                    edgecolor="#4b5c6c", zorder=2)
        ax.add_patch(boxes[cell])
        ax.text(x, y+0.12, cell, ha="center", va="center", weight="bold", fontsize=11, zorder=3)
        ax.text(x, y-0.18, label, ha="center", va="center", fontsize=10, zorder=3)
    for u, v in edges:
        cycle_edge = cyclic and {u, v} == {"B1", "C1"}
        ax.add_patch(FancyArrowPatch(pos[u], pos[v], arrowstyle="-|>",
                                    connectionstyle="arc3,rad=-0.33" if cycle_edge else "arc3,rad=0",
                                    patchA=boxes[u], patchB=boxes[v],
                                    mutation_scale=15, shrinkA=3, shrinkB=3,
                                    color="#b42b32" if cycle_edge else "#657589",
                                    linewidth=2.2 if cycle_edge else 1.4, zorder=1))


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(12, 6.6), facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.28, top=0.82, wspace=0.10)
    fig.suptitle("Two separate edits: invalidation versus a circular reference", y=0.97, fontsize=16)
    fig.text(0.5, 0.91, "Every arrow points from prerequisite to consumer", ha="center")
    axes[0].set_title("Input edit: A1 becomes 5", fontsize=13, pad=10)
    axes[1].set_title("Formula edit: B1 = A1 + A2 + C1", fontsize=13, pad=10)
    diagram(axes[0], False)
    diagram(axes[1], True)
    fig.text(0.26, 0.225, "Orange: changed input and downstream consumers\nBlue: valid cached values retained",
             ha="center", va="top", linespacing=1.6)
    fig.text(0.75, 0.225, "Restore inputs A1 = 3, A2 = 4 first\nRed: B1 ↔ C1; D1 depends on the cycle",
             ha="center", va="top", linespacing=1.6)
    fig.text(0.5, 0.08, "Cycle trace on demand: D1 → C1 → B1 → C1 (already ACTIVE)\n"
             "This trace follows references backwards; independent B2 and E1 still evaluate.",
             ha="center", va="center", linespacing=1.6, fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
