"""Original extended-flow diagram; writes a PNG to the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7+dfsg1.
Uses only the dependency families documented in the root pyproject.toml.
"""
from pathlib import Path
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    fig = Figure(figsize=(8.4, 4.5), dpi=120, facecolor="white")
    FigureCanvasAgg(fig)
    ax = fig.add_axes((0.025, 0.13, 0.95, 0.70))
    pos = {"s": (-1.7, 0), "A": (0, 0), "B": (1.9, 1.3),
           "C": (1.9, -1.3), "D": (3.8, 0), "t": (5.5, 0)}
    edges = [("s", "A", "6 / 6", (-0.85, .22), True),
             ("A", "B", "4 / 5", (.78, .85), False),
             ("A", "C", "2 / 2", (.78, -.85), False),
             ("B", "C", "0 / 5", (2.18, 0), False),
             ("B", "D", "3 / 3", (2.92, .75), False),
             ("C", "D", "2 / 5", (2.92, -.75), False),
             ("B", "t", "1 / 1", (4.1, 1.05), True),
             ("D", "t", "5 / 5", (4.65, -.24), True)]
    for u, v, label, label_pos, auxiliary in edges:
        color = "#1767a5" if auxiliary else "#323b45"
        ax.add_patch(FancyArrowPatch(pos[u], pos[v], arrowstyle="-|>",
                     mutation_scale=15, shrinkA=17, shrinkB=17,
                     linewidth=1.8, color=color))
        ax.text(*label_pos, label, ha="center", va="center", fontsize=12,
                color=color, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.8})
    for name, point in pos.items():
        aux = name in ("s", "t")
        ax.add_patch(Circle(point, .22, facecolor="#e3f1fa" if aux else "#f4f5f6",
                            edgecolor="#1767a5" if aux else "#323b45", linewidth=1.5, zorder=3))
        ax.text(*point, name, ha="center", va="center", fontsize=14, zorder=4)
    ax.set(xlim=(-2.12, 5.92), ylim=(-1.75, 1.8), aspect="equal")
    ax.axis("off")
    fig.text(.5, .95, "Extended network: a maximum flow of value 6", ha="center", fontsize=16)
    fig.text(.5, .06, "Labels: flow / capacity. Blue arcs encode adjusted supplies and demands.",
             ha="center", fontsize=11, color="#323b45")
    fig.savefig(Path.cwd() / "advanced-data-structures-2015-extended-flow.png",
                facecolor="white", transparent=False, dpi=120)


if __name__ == "__main__":
    main()
