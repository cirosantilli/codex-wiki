"""Draw original-edge flow amounts and their vertex ledger; run from _media."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.4, 5.2), dpi=100, facecolor="white")
    graph = fig.add_axes((0.035, 0.20, 0.55, 0.62))
    graph.set(xlim=(-0.5, 4.1), ylim=(-1.55, 1.55), aspect="equal")
    graph.axis("off")
    pos = {"s": (0, 0), "a": (1.8, 1.05), "b": (1.8, -1.05), "t": (3.6, 0)}
    edges = [("s", "a", 3), ("s", "b", 2), ("a", "b", 1), ("a", "t", 2), ("b", "t", 3)]
    offsets = {( "s", "a"): (-0.12, 0.22), ("s", "b"): (-0.12, -0.25),
               ("a", "b"): (0.34, 0), ("a", "t"): (0.1, 0.22),
               ("b", "t"): (0.1, -0.25)}
    for u, v, amount in edges:
        graph.add_patch(FancyArrowPatch(pos[u], pos[v], arrowstyle="-|>",
                                       mutation_scale=19, shrinkA=17, shrinkB=17,
                                       linewidth=2.4, color="#246ba8"))
        dx, dy = offsets[u, v]
        graph.text((pos[u][0] + pos[v][0]) / 2 + dx,
                   (pos[u][1] + pos[v][1]) / 2 + dy, f"{amount}/{amount}",
                   ha="center", va="center", fontsize=14,
                   bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for node, xy in pos.items():
        graph.add_patch(Circle(xy, 0.16, facecolor="white", edgecolor="#23465d", linewidth=2, zorder=5))
        graph.text(*xy, node, ha="center", va="center", fontsize=16, zorder=6)
    fig.text(0.30, 0.83, "Labels: flow / capacity", ha="center", color="#246ba8", fontsize=13)
    ledger = fig.add_axes((0.62, 0.24, 0.35, 0.52))
    ledger.axis("off")
    rows = [["s", "0", "5", "+5"], ["a", "3", "1 + 2", "0"],
            ["b", "2 + 1", "3", "0"], ["t", "5", "0", "−5"]]
    table = ledger.table(cellText=rows, colLabels=["Vertex", "In", "Out", "Out − In"],
                         cellLoc="center", loc="center", colWidths=[0.21, 0.23, 0.23, 0.33])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2.2)
    for (row, _), cell in table.get_celld().items():
        cell.set_edgecolor("#d0dce4")
        cell.set_facecolor("#e9f2f9" if row == 0 else "#f3f8f4" if row in (2, 3) else "white")
    fig.text(0.79, 0.80, "Vertex ledger", ha="center", fontsize=15, weight="bold")
    fig.text(0.5, 0.94, "Feasible flow: delivery rate 5", ha="center", fontsize=20, weight="bold")
    fig.text(0.5, 0.135, "At a: 3 = 1 + 2      At b: 2 + 1 = 3", ha="center", fontsize=14)
    fig.text(0.5, 0.065, "Sum of edge amounts = 11       Net delivery = 5", ha="center", fontsize=14,
             bbox={"facecolor": "#eef5fa", "edgecolor": "none", "pad": 8})
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
