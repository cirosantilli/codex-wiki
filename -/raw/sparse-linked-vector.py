"""Draw an original circular sparse-vector example; output to the current directory."""
from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path as DrawPath


def main():
    figure = Figure(figsize=(9.6, 3.8), dpi=100, facecolor="white")
    FigureCanvasAgg(figure)
    ax = figure.add_axes((0.025, 0.18, 0.95, 0.67))
    positions = (0.0, 2.45, 4.9, 7.35)
    labels = ("HEADER\ndimension: 9", "index: 1\nvalue: 3", "index: 4\nvalue: −2", "index: 7\nvalue: 5")
    forward, backward = "#245e9c", "#a85b16"
    width, bottom, height = 1.8, 0.7, 0.8
    for i, (x, label) in enumerate(zip(positions, labels)):
        ax.add_patch(FancyBboxPatch((x, bottom), width, height,
                     boxstyle="round,pad=0.03", edgecolor="#3c5366",
                     facecolor="#e6eef6" if i == 0 else "#f4f6f8", linewidth=1.4))
        ax.text(x + width / 2, bottom + height / 2, label,
                ha="center", va="center", fontsize=12, linespacing=1.45)
    for left, right in zip(positions, positions[1:]):
        for start, end, y, color in ((left + width, right, 1.28, forward),
                                      (right, left + width, 0.92, backward)):
            ax.add_patch(FancyArrowPatch((start, y), (end, y),
                         arrowstyle="-|>", mutation_scale=15, linewidth=1.8,
                         color=color, shrinkA=4, shrinkB=4))
    wraps = (
        ([(9.18, 1.28), (9.55, 1.28), (9.55, 2.04), (-0.4, 2.04),
          (-0.4, 1.28), (-0.03, 1.28)], forward),
        ([(-0.03, 0.92), (-0.4, 0.92), (-0.4, 0.15), (9.55, 0.15),
          (9.55, 0.92), (9.18, 0.92)], backward),
    )
    for vertices, color in wraps:
        path = DrawPath(vertices, [DrawPath.MOVETO] + [DrawPath.LINETO] * 5)
        ax.add_patch(FancyArrowPatch(path=path, arrowstyle="-|>",
                     mutation_scale=15, linewidth=1.8, color=color))
    ax.text(4.55, 2.17, "next →", color=forward, fontsize=12, ha="center")
    ax.text(4.55, -0.12, "← prev", color=backward, fontsize=12, ha="center")
    ax.set(xlim=(-0.65, 9.8), ylim=(-0.36, 2.44))
    ax.axis("off")
    figure.text(0.5, 0.95, "Store three coordinates, represent a nine-dimensional vector",
                ha="center", fontsize=15)
    figure.text(0.5, 0.075, "(0, 3, 0, 0, −2, 0, 0, 5, 0)\nThe header is metadata; every omitted coordinate is zero.",
                ha="center", va="center", fontsize=12, linespacing=1.5)
    figure.savefig(Path.cwd() / "sparse-linked-vector.png",
                   dpi=100, facecolor="white", transparent=False)


if __name__ == "__main__":
    main()
