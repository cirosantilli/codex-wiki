"""Draw metric-unit-ball-comparison.png in the current directory.

Uses the repository's NumPy/Matplotlib environment; tested with Python 3.14.4.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 15})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.6), facecolor="white")
    colors = ["#17678b", "#b3571b", "#5752a1"]
    shapes = [
        Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)], closed=True),
        Circle((0, 0), 1),
        Rectangle((-1, -1), 2, 2),
    ]
    titles = ["Manhattan / L1", "Euclidean / L2", "Chebyshev / L∞"]
    formulas = [
        r"$|x|+|y|\leq 1$",
        r"$x^2+y^2\leq 1$",
        r"$\max\{|x|,|y|\}\leq 1$",
    ]
    point = np.array([0.8, 0.8])
    distances = [np.linalg.norm(point, 1), np.linalg.norm(point, 2), np.linalg.norm(point, np.inf)]
    assert np.allclose(distances, [1.6, np.sqrt(1.28), 0.8])
    for ax, shape, color, title, formula, distance in zip(
        axes, shapes, colors, titles, formulas, distances
    ):
        ax.set_facecolor("white")
        shape.set_facecolor(color)
        shape.set_alpha(0.16)
        ax.add_patch(shape)
        # Draw the included boundary separately so its opacity stays high.
        if isinstance(shape, Circle):
            outline = Circle((0, 0), 1, fill=False)
        elif isinstance(shape, Rectangle):
            outline = Rectangle((-1, -1), 2, 2, fill=False)
        else:
            outline = Polygon(shape.get_xy(), closed=True, fill=False)
        outline.set_edgecolor(color)
        outline.set_linewidth(2.5)
        ax.add_patch(outline)
        ax.axhline(0, color="#8a9196", lw=0.8, zorder=0)
        ax.axvline(0, color="#8a9196", lw=0.8, zorder=0)
        ax.scatter([0], [0], s=18, color="#263238", zorder=4)
        ax.scatter(*point, s=50, color="#20272d", zorder=5)
        ax.annotate("(0.8, 0.8)", point, xytext=(0, 20), textcoords="offset points", ha="center", fontsize=11)
        ax.set(xlim=(-1.35, 1.35), ylim=(-1.35, 1.35), xticks=[-1, 0, 1], yticks=[-1, 0, 1])
        ax.set_aspect("equal")
        ax.set_xlabel("x", labelpad=0)
        ax.set_ylabel("y", rotation=0, labelpad=8)
        ax.set_title(title + "\n" + formula, pad=12)
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#b7bec3")
        value = f"{distance:.3f}" if title.startswith("Euclidean") else f"{distance:.1f}"
        status = "inside" if distance < 1 else "outside"
        ax.text(0.5, -0.27, f"Marked point: distance {value} — {status}", transform=ax.transAxes, ha="center", fontsize=11)
    fig.suptitle("Closed unit balls: same radius, different shapes", fontsize=18, y=0.98)
    fig.text(0.5, 0.03, "Solid outlines are included. Open unit balls omit the outlines.", ha="center", fontsize=12)
    fig.subplots_adjust(left=0.055, right=0.985, bottom=0.23, top=0.72, wspace=0.30)
    fig.savefig("metric-unit-ball-comparison.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
