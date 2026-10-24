"""Original DFS counterexample; write the matching PNG to the current directory."""
from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    figure = Figure(figsize=(4.8, 3.9), dpi=110, facecolor="white")
    FigureCanvasAgg(figure)
    ax = figure.add_axes((0.03, 0.14, 0.94, 0.72))
    points = {"r": (0, 1.6), "u": (-1, 0), "v": (1, 0)}
    for start, end, color, curve in (
        ("r", "u", "#516777", 0.16),
        ("u", "r", "#b6403a", 0.16),
        ("r", "v", "#516777", 0),
    ):
        ax.add_patch(FancyArrowPatch(points[start], points[end],
                     arrowstyle="-|>", mutation_scale=16, linewidth=1.8,
                     color=color, shrinkA=21, shrinkB=21,
                     connectionstyle=f"arc3,rad={curve}"))
    for name, (x, y) in points.items():
        ax.add_patch(Circle((x, y), 0.23, facecolor="#e7eef5",
                            edgecolor="#405974", linewidth=1.4, zorder=3))
        ax.text(x, y, name, ha="center", va="center", fontsize=17, zorder=4)
    for name, text in (("r", "d = 1, f = 6"), ("u", "d = 2, f = 3"), ("v", "d = 4, f = 5")):
        x, y = points[name]
        if name == "r":
            ax.text(x + 0.68, y, text, ha="left", va="center", fontsize=10)
        else:
            ax.text(x, y - 0.40, text, ha="center", va="center", fontsize=10)
    ax.text(-1.45, 1.05, "back edge", color="#b6403a", fontsize=10)
    ax.set(xlim=(-1.7, 1.7), ylim=(-0.7, 2.0), aspect="equal")
    ax.axis("off")
    figure.text(0.5, 0.965, "A directed path can leave a DFS subtree",
                ha="center", va="top", fontsize=13)
    figure.text(0.5, 0.08, "The path u → r → v exists.\nu finishes before v is discovered.",
                ha="center", va="center", fontsize=10, color="#414141")
    figure.savefig(Path.cwd() / "functional-programming-design-and-analysis-of-algorithms-dfs-branch.png",
                   dpi=110, facecolor="white", transparent=False)


if __name__ == "__main__":
    main()
