"""Draw the final insertion tree; write the PNG to the current directory.

Tested with the Python, NumPy and Matplotlib versions in the root pyproject.toml.
This is an original diagram, not an image extracted from the examination paper.
"""

from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import Circle


def main():
    figure = Figure(figsize=(6.4, 4.2), dpi=110, facecolor="white")
    FigureCanvasAgg(figure)
    ax = figure.add_axes((0.02, 0.08, 0.96, 0.80))
    positions = {
        34: (0.40, 3.0),
        21: (0.12, 2.0),
        45: (0.69, 2.0),
        40: (0.52, 1.0),
        55: (0.88, 1.0),
        37: (0.37, 0.0),
    }
    edges = ((34, 21), (34, 45), (45, 40), (45, 55), (40, 37))
    red = {45, 37}
    # Draw in data coordinates with a matching aspect ratio, keeping nodes round.
    for parent, child in edges:
        x1, y1 = positions[parent]
        x2, y2 = positions[child]
        ax.plot((4 * x1, 4 * x2), (y1, y2), color="#737373", lw=1.7)
    for key, (x, y) in positions.items():
        is_red = key in red
        ax.add_patch(Circle((4 * x, y), 0.24,
                            facecolor="#f8b8b8" if is_red else "#252b33",
                            edgecolor="#a01818" if is_red else "#252b33",
                            linewidth=1.5, zorder=3))
        ax.text(4 * x, y + 0.045, str(key), ha="center", va="center",
                color="#501010" if is_red else "white", fontsize=13, zorder=4)
        ax.text(4 * x, y - 0.125, "R" if is_red else "B",
                ha="center", va="center",
                color="#501010" if is_red else "white", fontsize=9, zorder=4)
    ax.set(xlim=(-0.05, 4.05), ylim=(-0.40, 3.40), aspect="equal")
    ax.axis("off")
    figure.text(0.5, 0.955, "Red-black tree after the six insertions",
                ha="center", va="top", fontsize=14, color="#202832")
    figure.text(0.5, 0.035, "B = black, R = red. Absent children are black sentinels.",
                ha="center", fontsize=10, color="#414141")
    figure.savefig(Path.cwd() / "algorithms-red-black-insertion.png",
                   dpi=110, facecolor="white", transparent=False)


if __name__ == "__main__":
    main()
