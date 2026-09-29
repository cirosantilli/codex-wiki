"""Draw a computed toy DAG and enumerate its topological orders.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
The output basename is derived from this script and saved in the CWD.
"""

from itertools import permutations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

VERTICES = tuple("ABCDE")
EDGES = (("A", "C"), ("A", "D"), ("B", "D"), ("C", "E"), ("D", "E"))
TASKS = {"A": "Draft text", "B": "Draw figure", "C": "Review text", "D": "Lay out page", "E": "Publish"}
COLORS = {"A": "#d6eaff", "B": "#ffe6bf", "C": "#d9efd9", "D": "#eeddf5", "E": "#d6eeef"}


def all_orders():
    return [p for p in permutations(VERTICES) if all(p.index(u) < p.index(v) for u, v in EDGES)]


def main():
    orders = all_orders()
    assert ["".join(p) for p in orders] == ["ABCDE", "ABDCE", "ACBDE", "BACDE", "BADCE"]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig = plt.figure(figsize=(9, 6.5), dpi=120, facecolor="white")
    fig.text(0.5, 0.96, "Local prerequisites allow several complete orders", ha="center", fontsize=17, weight="bold")
    fig.text(0.5, 0.915, "Toy publishing workflow: an arrow means finish the source first", ha="center", color="#425466")
    ax = fig.add_axes((0.06, 0.52, 0.88, 0.36))
    ax.set(xlim=(-0.6, 4.6), ylim=(-1.4, 1.4), aspect="equal")
    ax.axis("off")
    positions = {"A": (0, 0.85), "B": (0, -0.85), "C": (2, 0.85), "D": (2, -0.85), "E": (4, 0)}
    for u, v in EDGES:
        ax.add_patch(FancyArrowPatch(positions[u], positions[v], arrowstyle="-|>", mutation_scale=17, linewidth=2, color="#425466", shrinkA=22, shrinkB=22))
    for v, (x, y) in positions.items():
        ax.add_patch(Circle((x, y), 0.28, facecolor=COLORS[v], edgecolor="#425466", linewidth=1.5))
        ax.text(x, y, v, ha="center", va="center", fontsize=16, weight="bold")
        ax.text(x, y - 0.48, TASKS[v], ha="center", va="center", fontsize=11)

    ax = fig.add_axes((0.09, 0.055, 0.82, 0.40))
    ax.set(xlim=(0, 6), ylim=(-0.7, 5.0))
    ax.axis("off")
    ax.text(3, 4.7, f"All {len(orders)} valid orders (checked among 120 permutations)", ha="center", fontsize=13, weight="bold")
    for row, order in enumerate(orders):
        y = 3.8 - row * 0.85
        ax.text(0.12, y, f"{row + 1}.", va="center", color="#425466")
        for col, v in enumerate(order):
            x = 1 + col
            ax.add_patch(FancyBboxPatch((x - 0.31, y - 0.29), 0.62, 0.58, boxstyle="round,pad=0.025", facecolor=COLORS[v], edgecolor="#425466"))
            ax.text(x, y, v, ha="center", va="center", weight="bold")
    ax.text(3, -0.60, "Every dependency points forward in every row.", ha="center", color="#425466", fontsize=11)
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print({"orders": ["".join(p) for p in orders], "permutations_checked": 120, "output": str(output)})


if __name__ == "__main__":
    main()
