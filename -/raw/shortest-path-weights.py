"""Draw the weighted route example; write shortest-path-weights.png to cwd.

Tested with Python 3.14 and the repository's matplotlib/numpy dependencies.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    positions = {"A": (0, 0), "B": (2, 1.8), "C": (2, 0), "D": (4, 0)}
    weights = {"AB": 4, "AC": 1, "CB": 2, "BD": 1, "CD": 5, "AD": 10}
    route = ["A", "C", "B", "D"]
    total = sum(weights.get(u + v, weights.get(v + u))
                for u, v in zip(route, route[1:]))
    assert total == 4
    fig, ax = plt.subplots(figsize=(7.4, 4.3), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    teal, gray = "#087e83", "#9ca3af"
    for edge, weight in weights.items():
        start, end = (positions[v] for v in edge)
        selected = edge in {"AC", "CB", "BD"}
        color = teal if selected else gray
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-", shrinkA=17, shrinkB=17,
            connectionstyle="arc3,rad=0.50" if edge == "AD" else "arc3",
            linewidth=3.5 if selected else 1.8, color=color, zorder=1))
        x, y = ((start[i] + end[i]) / 2 for i in range(2))
        if edge == "AD":
            y = -1.0
        elif edge == "CB":
            x -= 0.18
        ax.text(x, y, str(weight), fontsize=14, ha="center", va="center",
                color=color, zorder=3,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for label, (x, y) in positions.items():
        ax.scatter([x], [y], s=740, facecolor="white", edgecolor="#253746",
                   linewidth=1.7, zorder=4)
        ax.text(x, y, label, ha="center", va="center", fontsize=14, zorder=5)
    ax.set_title("Cheapest route: A → C → B → D", fontsize=15, pad=14)
    ax.text(2, -1.49, "3 edges, cost 1 + 2 + 1 = 4     |     Direct edge, cost 10",
            ha="center", fontsize=11, color="#253746")
    ax.set(xlim=(-0.4, 4.4), ylim=(-1.7, 2.2), aspect="equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path.cwd() / "shortest-path-weights.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print("Shortest highlighted route A-C-B-D: cost 4")


if __name__ == "__main__":
    main()
