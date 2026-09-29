"""Compute a FIFO Kahn trace and a cyclic residual, then draw both.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
The output basename is derived from this script and saved in the CWD.
"""

from collections import deque
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

VERTICES = tuple("ABCDE")
EDGES = (("A", "C"), ("A", "D"), ("B", "D"), ("C", "E"), ("D", "E"))


def trace(edges):
    outgoing = {v: [] for v in VERTICES}
    indegree = dict.fromkeys(VERTICES, 0)
    for u, v in edges:
        outgoing[u].append(v)
        indegree[v] += 1
    ready = deque(v for v in VERTICES if indegree[v] == 0)
    emitted = []
    rows = []

    def snapshot():
        rows.append(("".join(emitted), tuple(ready), tuple(None if v in emitted else indegree[v] for v in VERTICES)))

    snapshot()
    while ready:
        u = ready.popleft()
        emitted.append(u)
        for v in outgoing[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                ready.append(v)
        snapshot()
    return rows


def main():
    rows = trace(EDGES)
    blocked = trace(EDGES + (("E", "C"),))
    assert rows[-1][0] == "ABCDE"
    assert blocked[-1] == ("ABD", (), (None, None, 1, None, 1))
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(10, 5.8), dpi=120, facecolor="white")
    fig.text(0.5, 0.95, "Kahn's algorithm: ready tasks and a cycle obstruction", ha="center", fontsize=17, weight="bold")
    fig.text(0.5, 0.90, "Computed toy example; counts refer to unfinished incoming edges", ha="center", color="#425466")
    ax = fig.add_axes((0.045, 0.21, 0.58, 0.61))
    ax.axis("off")
    cells = []
    for prefix, ready, counts in rows:
        cells.append([prefix or "empty", ", ".join(ready) or "empty"] + ["–" if n is None else str(n) for n in counts])
    table = ax.table(cellText=cells, colLabels=["Emitted", "Ready FIFO", "A", "B", "C", "D", "E"], colWidths=[0.24, 0.26, 0.10, 0.10, 0.10, 0.10, 0.10], loc="center", cellLoc="center", bbox=(0, 0, 1, 1))
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#c6d0da")
        cell.set_linewidth(0.8)
        if row == 0:
            cell.set_facecolor("#e7eef5")
            cell.set_text_props(weight="bold")
        elif col >= 2:
            text = cell.get_text().get_text()
            cell.set_facecolor("#d9efd9" if text == "0" else "#f3f5f7" if text == "–" else "white")
    fig.text(0.335, 0.15, "Green 0 = ready; dash = already emitted", ha="center", fontsize=11, color="#425466")
    fig.text(0.335, 0.105, "Each edge causes one decrement; E needs both C and D.", ha="center", fontsize=11, color="#425466")

    ax = fig.add_axes((0.66, 0.25, 0.31, 0.53))
    ax.set(xlim=(-0.8, 2.8), ylim=(-1.2, 1.3), aspect="equal")
    ax.axis("off")
    ax.text(1, 1.12, "Add E → C", ha="center", color="#b52c35", fontsize=14, weight="bold")
    positions = {"C": (0, 0.15), "E": (2, 0.15)}
    ax.add_patch(FancyArrowPatch(positions["C"], positions["E"], arrowstyle="-|>", connectionstyle="arc3,rad=-0.3", shrinkA=25, shrinkB=25, mutation_scale=18, linewidth=2, color="#425466"))
    ax.add_patch(FancyArrowPatch(positions["E"], positions["C"], arrowstyle="-|>", connectionstyle="arc3,rad=-0.3", shrinkA=25, shrinkB=25, mutation_scale=18, linewidth=2.5, color="#b52c35"))
    for v, (x, y) in positions.items():
        ax.add_patch(Circle((x, y), 0.31, facecolor="#ffe3e3", edgecolor="#b52c35", linewidth=1.5))
        ax.text(x, y, v, ha="center", va="center", fontsize=16, weight="bold")
        count = blocked[-1][2][VERTICES.index(v)]
        ax.text(x, y - 0.62, f"indegree {count}", ha="center", fontsize=11)
    fig.text(0.815, 0.25, f"Emitted: {', '.join(blocked[-1][0])}\nReady queue: empty\nUnfinished: C, E", ha="center", va="top", linespacing=1.7, fontsize=12)
    fig.text(0.815, 0.075, "Neither task can become ready.", ha="center", color="#b52c35", fontsize=11)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print({"dag_trace": rows, "cyclic_trace": blocked, "output": str(output)})


if __name__ == "__main__":
    main()
