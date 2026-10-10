"""Draw an original all-to-one certificate; output this script's PNG basename to CWD.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Weights are constructed exact costs, not measured data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


INK = "#253746"
BLUE = "#196b9b"
GRAY = "#84919c"
EDGES = [("a", "b", 2), ("a", "r", 7), ("b", "r", 3),
         ("b", "c", -2), ("c", "r", 4)]
DISTANCE = {"a": 4, "b": 2, "c": 4, "r": 0}
LOWER = {"a": 3, "b": 1, "c": 3, "r": 0}
UPPER = {"a": 7, "b": 3, "c": 4, "r": 0}


def main():
    for u, v, cost in EDGES:
        assert LOWER[u] <= cost + LOWER[v]
        assert DISTANCE[u] <= cost + DISTANCE[v]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(9.0, 4.6), dpi=120, facecolor="white")
    fig.text(0.5, 0.94, "Local inequalities + a realizing route = an exact distance",
             ha="center", fontsize=15, weight="bold", color=INK)
    fig.text(0.5, 0.875, "All-to-one: follow original arrows to r • constructed costs, not measured data",
             ha="center", fontsize=11, color=INK)
    ax = fig.add_axes((0.025, 0.22, 0.575, 0.61), facecolor="white")
    pos = {"a": (0, 1.5), "b": (2.0, 1.5), "c": (4.0, 1.5), "r": (4.0, -0.4)}
    label_pos = {("a", "b"): (1.0, 1.76), ("a", "r"): (1.57, -0.27),
                 ("b", "r"): (2.90, 0.38), ("b", "c"): (3.0, 1.76),
                 ("c", "r"): (4.84, 0.58)}
    for u, v, cost in EDGES:
        slack = cost + DISTANCE[v] - DISTANCE[u]
        color = BLUE if slack == 0 else GRAY
        bend = 0.42 if (u, v) == ("a", "r") else 0
        ax.add_patch(FancyArrowPatch(
            pos[u], pos[v], arrowstyle="-|>", mutation_scale=14,
            shrinkA=15, shrinkB=15, color=color, linewidth=2.5 if slack == 0 else 1.6,
            connectionstyle=f"arc3,rad={bend}", zorder=1))
        x, y = label_pos[u, v]
        ax.text(x, y, f"{cost}", fontsize=13, color="#b63d2c" if cost < 0 else color,
                ha="center", va="center", zorder=3,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.3})
        ax.text(x, y - 0.28, f"slack {slack}", fontsize=9, color=color,
                ha="center", va="center", zorder=3,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.7})
    for vertex, (x, y) in pos.items():
        ax.scatter(x, y, s=600, facecolors="white", edgecolors=INK, linewidths=1.6, zorder=4)
        ax.text(x, y, vertex, ha="center", va="center", fontsize=14, color=INK, zorder=5)
        label_y = y - 0.55 if vertex == "r" else y + 0.53
        ax.text(x, label_y, f"d = {DISTANCE[vertex]}", ha="center", fontsize=11, color=BLUE)
    ax.set(xlim=(-0.5, 5.5), ylim=(-1.1, 2.45), aspect="equal")
    ax.axis("off")

    table_ax = fig.add_axes((0.63, 0.36, 0.34, 0.38))
    table_ax.axis("off")
    data = [[v, str(LOWER[v]), str(DISTANCE[v]), str(UPPER[v])] for v in "abcr"]
    table = table_ax.table(cellText=data, colLabels=["Vertex", "L", "δ(·, r)", "U"],
                           colWidths=[0.28, 0.23, 0.26, 0.23], cellLoc="center", bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d7dfe5")
        cell.set_linewidth(0.6)
        cell.set_text_props(color=INK)
        cell.set_facecolor("#e9eff3" if row == 0 else "white")
        if row == 0:
            cell.set_text_props(weight="bold")
        elif col == 2:
            cell.set_facecolor("#dceef8")
            cell.set_text_props(color=BLUE, weight="bold")
    fig.text(0.80, 0.79, "Lower ≤ exact ≤ upper", ha="center", fontsize=12, color=INK)
    fig.text(0.80, 0.315, "L: feasible labels\nU: direct routes to r", ha="center", va="top",
             fontsize=11, color=INK, linespacing=1.5)
    fig.text(0.5, 0.17, "Every slack = cost + d(head) − d(tail) ≥ 0.",
             ha="center", fontsize=12, color=INK)
    fig.text(0.5, 0.09, "Blue route a → b → c → r has zero slacks and cost 2 − 2 + 4 = 4.",
             ha="center", fontsize=11, color=BLUE)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)
    print("Certificate: a=4, b=2, c=4, r=0; edge slacks [0, 3, 1, 0, 0]")


if __name__ == "__main__":
    main()
