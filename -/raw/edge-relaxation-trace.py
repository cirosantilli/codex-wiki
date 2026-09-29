"""Draw an original relaxation trace, writing this script's PNG basename to CWD.

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


def trace():
    edges = [("s", "t", 10), ("s", "a", 6), ("s", "b", 2),
             ("a", "t", 2), ("b", "a", -1), ("a", "t", 2),
             ("b", "t", 7)]
    labels = dict.fromkeys("sabt z".replace(" ", ""), float("inf"))
    labels["s"] = 0
    predecessors = dict.fromkeys(labels)
    rows = [("Start", labels.copy(), None)]
    for u, v, weight in edges:
        candidate = labels[u] + weight
        improved = candidate < labels[v]
        if improved:
            labels[v] = candidate
            predecessors[v] = u
        rows.append((f"{u} → {v}", labels.copy(), v if improved else None))
    assert [row[1]["t"] for row in rows] == [float("inf"), 10, 10, 10, 8, 8, 3, 3]
    assert predecessors == {"s": None, "a": "b", "b": "s", "t": "a", "z": None}
    return rows


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(9.0, 5.0), dpi=120, facecolor="white")
    fig.text(0.5, 0.95, "One edge at a time: discovered routes get cheaper",
             ha="center", fontsize=16, weight="bold", color=INK)
    fig.text(0.5, 0.895, "Constructed directed graph • negative edge allowed • s stays at 0",
             ha="center", fontsize=11, color=INK)
    ax = fig.add_axes((0.03, 0.23, 0.43, 0.60), facecolor="white")
    positions = {"s": (0, 1.2), "a": (2.2, 2.1), "b": (2.2, 0.1),
                 "t": (4.4, 1.2), "z": (0, -0.5)}
    # Original edge costs; blue edges are the final predecessor route.
    edges = [("s", "a", 6, (0.98, 1.85), 0),
             ("s", "b", 2, (0.96, 0.47), 0),
             ("b", "a", -1, (2.44, 1.1), 0),
             ("a", "t", 2, (3.4, 1.85), 0),
             ("b", "t", 7, (3.4, 0.47), 0),
             ("s", "t", 10, (2.2, 3.13), -0.86)]
    route_edges = {("s", "b"), ("b", "a"), ("a", "t")}
    for u, v, weight, label_pos, bend in edges:
        color = BLUE if (u, v) in route_edges else GRAY
        ax.add_patch(FancyArrowPatch(
            positions[u], positions[v], arrowstyle="-|>", mutation_scale=14,
            shrinkA=15, shrinkB=15, linewidth=2.5 if color == BLUE else 1.6,
            color=color, connectionstyle=f"arc3,rad={bend}", zorder=1))
        ax.text(*label_pos, str(weight), fontsize=13, ha="center", va="center",
                color="#b63d2c" if weight < 0 else color,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5}, zorder=3)
    for vertex, (x, y) in positions.items():
        ax.scatter(x, y, s=640, facecolors="white", edgecolors=INK, linewidths=1.6, zorder=4)
        ax.text(x, y, vertex, ha="center", va="center", fontsize=14, color=INK, zorder=5)
    ax.text(0.42, -0.5, "isolated: d(z) = ∞", fontsize=10, color=GRAY, va="center")
    ax.set(xlim=(-0.5, 4.9), ylim=(-0.9, 3.65), aspect="equal")
    ax.axis("off")
    fig.text(0.245, 0.235, "Blue: final route s → b → a → t", ha="center", color=BLUE, fontsize=11)

    table_ax = fig.add_axes((0.49, 0.22, 0.48, 0.59))
    table_ax.axis("off")
    rows = trace()
    data = [[operation] + ["∞" if label[v] == float("inf") else str(label[v])
                          for v in "abtz"] for operation, label, _ in rows]
    table = table_ax.table(cellText=data, colLabels=["Relax", "d(a)", "d(b)", "d(t)", "d(z)"],
                           colWidths=[0.29, 0.1775, 0.1775, 0.1775, 0.1775],
                           cellLoc="center", bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d7dfe5")
        cell.set_linewidth(0.6)
        cell.set_text_props(color=INK)
        if row == 0:
            cell.set_facecolor("#e9eff3")
            cell.set_text_props(weight="bold")
        else:
            cell.set_facecolor("white" if row % 2 else "#f7f9fb")
            changed = rows[row - 1][2]
            if col and "abtz"[col - 1] == changed:
                cell.set_facecolor("#dceef8")
                cell.set_text_props(color=BLUE, weight="bold")
    fig.text(0.73, 0.835, "Labels after each operation", ha="center", color=INK, fontsize=12)
    fig.text(0.5, 0.125, "After b → a: revisit a → t, since 1 + 2 < 8.",
             ha="center", fontsize=12, color=INK)
    fig.text(0.5, 0.065, "Final cost: 2 − 1 + 2 = 3    |    This is a relaxation trace, not Dijkstra's order.",
             ha="center", fontsize=11, color=INK)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)
    print("Trace: a=1, b=2, t=3, z=inf; final predecessor route s-b-a-t")


if __name__ == "__main__":
    main()
