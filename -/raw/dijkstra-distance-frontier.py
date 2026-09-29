"""Compute and plot Dijkstra labels; write dijkstra-distance-frontier.png to cwd.

Tested with Python 3.14 and the repository's matplotlib/numpy dependencies.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def compute_labels():
    vertices = "ABCD"
    adjacency = {v: [] for v in vertices}
    for u, v, weight in [("A", "B", 4), ("A", "C", 1), ("C", "B", 2),
                         ("B", "D", 1), ("C", "D", 5), ("A", "D", 10)]:
        adjacency[u].append((v, weight))
        adjacency[v].append((u, weight))
    distances = dict.fromkeys(vertices, float("inf"))
    predecessors = dict.fromkeys(vertices)
    distances["A"] = 0
    settled, snapshots = [], []
    while len(settled) < len(vertices):
        u = min((v for v in vertices if v not in settled), key=distances.get)
        settled.append(u)
        for v, weight in adjacency[u]:
            if v not in settled and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
        snapshots.append(distances.copy())
    assert settled == ["A", "C", "B", "D"]
    assert distances == {"A": 0, "B": 3, "C": 1, "D": 4}
    assert predecessors == {"A": None, "B": "C", "C": "A", "D": "B"}
    assert [row["B"] for row in snapshots] == [4, 3, 3, 3]
    assert [row["D"] for row in snapshots] == [10, 6, 4, 4]
    return settled, snapshots


def main():
    settled, snapshots = compute_labels()
    fig, ax = plt.subplots(figsize=(8.0, 4.4), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    colors = {"A": "#616b75", "C": "#087e83", "B": "#3562a6", "D": "#b95f22"}
    for vertex in settled:
        final_step = settled.index(vertex)
        steps = list(range(final_step + 1))
        values = [snapshots[i][vertex] for i in steps]
        color = colors[vertex]
        ax.plot(steps, values, color=color, linewidth=2.2, zorder=2)
        ax.scatter(steps, values, facecolors="white", edgecolors=color,
                   s=90, linewidths=2, zorder=3)
        ax.scatter([final_step], [values[-1]], facecolors=color,
                   edgecolors=color, s=90, zorder=4)
        for step, value in zip(steps, values):
            offset = (-22, -2) if vertex == "A" else (0, 10)
            if vertex == "B" and step == final_step:
                offset = (0, -20)
            ax.annotate(f"{vertex}: {value}", (step, value), xytext=offset,
                        textcoords="offset points",
                        ha="right" if vertex == "A" else "center", fontsize=11,
                        color=color)
    ax.set_title("Tentative distances improve; permanent distances stay fixed",
                 fontsize=13, pad=15)
    ax.set_xticks(range(4), ["After A (0)", "After C (1)", "After B (3)", "After D (4)"])
    ax.set_xlabel("Finalize this vertex, then relax its incident edges", labelpad=10)
    ax.set_ylabel("Recorded cost from A")
    ax.set(xlim=(-0.35, 3.35), ylim=(-0.7, 11.25), yticks=range(0, 11, 2))
    ax.grid(axis="y", color="#e3e7eb", linewidth=0.7)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.025, "Hollow marker: tentative     •     Filled marker: permanent",
             ha="center", fontsize=10, color="#253746")
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(Path.cwd() / "dijkstra-distance-frontier.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print("Finalization A0 C1 B3 D4; tentative B4→3, D10→6→4")


if __name__ == "__main__":
    main()
