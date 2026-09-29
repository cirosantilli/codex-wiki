"""Compare full-matrix and unsorted-list queries on an original graph.

Run from _media; writes adjacency-list-matrix-query-tradeoff.png to the CWD.
Tested with Python 3.14, matplotlib 3.10.7; counts are logical entries, not bytes.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


VERTICES = tuple("ABCDEF")
EDGES = ("AB", "AC", "BC", "CD", "DE", "DF", "EF")
BLUE = "#24639b"
TEAL = "#087f83"
ORANGE = "#af5712"
INK = "#243543"


def main():
    lists = {v: [] for v in VERTICES}
    for u, v in EDGES:
        lists[u].append(v)
        lists[v].append(u)
    matrix = [[int(v in lists[u]) for v in VERTICES] for u in VERTICES]
    assert matrix[2] == [1, 1, 0, 1, 0, 0]
    assert sum(map(sum, matrix)) == 14
    plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11.2, 7.6), dpi=100, facecolor="white")
    fig.suptitle("Same graph, different questions", y=0.96, fontsize=21, color=INK)
    matrix_ax = fig.add_axes((0.065, 0.35, 0.40, 0.49))
    lists_ax = fig.add_axes((0.55, 0.35, 0.40, 0.49))
    matrix_ax.set_title("Full adjacency matrix", fontsize=16, pad=16)
    for i, u in enumerate(VERTICES):
        matrix_ax.text(-0.52, i + 0.5, u, ha="center", va="center", color=TEAL if u == "C" else INK,
                       fontsize=15, weight="bold" if u == "C" else "normal")
        matrix_ax.text(i + 0.5, -0.4, u, ha="center", va="center", color=INK, fontsize=15)
        for j, value in enumerate(matrix[i]):
            fill = "#e6f4f3" if u == "C" else "#edf3f9" if value else "white"
            matrix_ax.add_patch(Rectangle((j, i), 1, 1, facecolor=fill, edgecolor="#bac6cd", linewidth=1))
            matrix_ax.text(j + 0.5, i + 0.5, str(value), ha="center", va="center",
                           color=TEAL if u == "C" else INK, fontsize=15)
    matrix_ax.add_patch(Rectangle((0, 2), 6, 1, facecolor="none", edgecolor=TEAL, linewidth=2.2))
    matrix_ax.add_patch(Rectangle((5.06, 2.06), 0.88, 0.88, facecolor="none", edgecolor=ORANGE, linewidth=3))
    matrix_ax.set(xlim=(-0.9, 6.15), ylim=(6.15, -0.85), aspect="equal")
    matrix_ax.axis("off")
    lists_ax.set_title("Unsorted adjacency lists", fontsize=16, pad=16)
    for row, v in enumerate(VERTICES):
        y = 5 - row
        color = TEAL if v == "C" else BLUE
        lists_ax.text(-0.4, y, v + ":", ha="center", va="center", color=color, fontsize=16, weight="bold")
        for j, neighbour in enumerate(lists[v]):
            x = 0.10 + j * 0.95
            lists_ax.add_patch(Rectangle((x, y - 0.34), 0.78, 0.68,
                                         facecolor="#e6f4f3" if v == "C" else "white", edgecolor=color, linewidth=1.5))
            lists_ax.text(x + 0.39, y, neighbour, ha="center", va="center", color=INK, fontsize=16)
        if v == "C":
            lists_ax.add_patch(Rectangle((-0.08, y - 0.48), 3.08, 0.96,
                                         facecolor="none", edgecolor=ORANGE, linewidth=2, linestyle="--"))
    lists_ax.set(xlim=(-0.85, 3.25), ylim=(-0.65, 5.65))
    lists_ax.axis("off")
    fig.text(0.26, 0.307, "36 matrix entries", ha="center", color=INK, fontsize=14)
    fig.text(0.75, 0.307, "6 descriptors + 14 neighbour entries", ha="center", color=INK, fontsize=14)
    table_ax = fig.add_axes((0.045, 0.072, 0.91, 0.195))
    table_ax.axis("off")
    rows = [["List C's neighbours", "Scan 6 entries", "Read 3 entries"],
            ["Does CF exist?", "Read 1 entry: 0", "Compare F with A, B, D"],
            ["General cost (degree d ≥ 1)", "List: O(n) · test: O(1)", "List: O(d) · test: O(d)"]]
    table = table_ax.table(cellText=rows, colLabels=["Question", "Full matrix", "Unsorted lists"],
                           cellLoc="left", colLoc="left", colWidths=[0.31, 0.32, 0.37], bbox=(0, 0, 1, 1))
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#c7d3da")
        cell.set_text_props(color=INK)
        if row == 0:
            cell.set_facecolor("#edf3f9")
            cell.set_text_props(weight="bold")
        elif row == 1:
            cell.set_facecolor("#e6f4f3")
        elif row == 2:
            cell.set_facecolor("#fff4e9")
    fig.text(0.50, 0.024, "n = number of vertices. Logical counts are not byte sizes; empty lists add constant overhead.",
             ha="center", color=INK, fontsize=10.5)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
