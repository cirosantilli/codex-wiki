"""Draw Bellman–Ford's negative-edge example; emit the PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from math import inf
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


VERTICES = ("S", "A", "B", "C", "T")
EDGES = (("S", "A", 4), ("S", "B", 5), ("A", "B", -2),
         ("B", "C", 3), ("C", "T", 2), ("A", "T", 8))
SCAN = tuple(reversed(EDGES))


def trace():
    labels = dict.fromkeys(VERTICES, inf)
    labels["S"] = 0
    rows = [labels.copy()]
    for _ in range(4):
        for u, v, weight in SCAN:
            if labels[u] != inf:
                labels[v] = min(labels[v], labels[u] + weight)
        rows.append(labels.copy())
    return rows


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(10, 7), dpi=120, facecolor="white")
    fig.suptitle("Bellman–Ford: a negative edge, no negative cycle",
                 fontsize=17, weight="bold", y=0.97)
    ax = fig.add_axes((0.05, 0.54, 0.90, 0.36))
    ax.set(xlim=(-0.7, 8.7), ylim=(-1.65, 1.65), aspect="equal")
    ax.axis("off")
    positions = {v: (2 * i, 0) for i, v in enumerate(VERTICES)}
    for u, v, weight in EDGES:
        color = "#b72532" if weight < 0 else "#226b88"
        curvature = 0.50 if (u, v) == ("A", "T") else 0
        if (u, v) == ("S", "B"):
            curvature = -0.52
        arrow = FancyArrowPatch(positions[u], positions[v],
                                connectionstyle=f"arc3,rad={curvature}",
                                arrowstyle="-|>", mutation_scale=18,
                                linewidth=2.3, color=color,
                                shrinkA=21, shrinkB=21)
        ax.add_patch(arrow)
        midpoint = ((positions[u][0] + positions[v][0]) / 2, 0.33)
        if (u, v) == ("S", "B"):
            midpoint = (2, 1.30)
        elif (u, v) == ("A", "T"):
            midpoint = (5, -1.36)
        ax.text(*midpoint, str(weight).replace("-", "−"), ha="center",
                va="center", fontsize=14, color=color,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for v, (x, y) in positions.items():
        ax.add_patch(Circle((x, y), 0.27, facecolor="white",
                            edgecolor="#263b48", linewidth=1.6, zorder=3))
        ax.text(x, y, v, ha="center", va="center", fontsize=14,
                weight="bold", zorder=4)
    fig.text(0.5, 0.53, "In-place scan: A→T, C→T, B→C, A→B, S→B, S→A",
             ha="center", fontsize=12)
    fig.text(0.5, 0.489, "Labels after each complete pass; blue cells decreased in that pass",
             ha="center", fontsize=11, color="#425665")
    table_ax = fig.add_axes((0.08, 0.12, 0.84, 0.34))
    table_ax.axis("off")
    rows = trace()
    cells = [["initial" if i == 0 else f"pass {i}"] +
             ["∞" if row[v] == inf else str(row[v]) for v in VERTICES]
             for i, row in enumerate(rows)]
    table = table_ax.table(cellText=cells, colLabels=("",) + VERTICES,
                           cellLoc="center", loc="center", bbox=(0, 0, 1, 1))
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    for (i, j), cell in table.get_celld().items():
        cell.set_edgecolor("#ccd8df")
        if i == 0:
            cell.set_facecolor("#263b48")
            cell.set_text_props(color="white", weight="bold")
        elif j == 0:
            cell.set_facecolor("#f0f3f5")
        elif i > 1 and rows[i - 1][VERTICES[j - 1]] < rows[i - 2][VERTICES[j - 1]]:
            cell.set_facecolor("#dceff8")
            cell.set_text_props(color="#125675", weight="bold")
    fig.text(0.5, 0.052, "Best route: S→A→B→C→T       cost = 4 − 2 + 3 + 2 = 7",
             ha="center", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
