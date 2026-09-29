"""Draw a lattice point in two unimodularly related bases."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.9), dpi=100, layout="constrained")
    fig.set_facecolor("white")
    grid = np.array([(x, y) for x in range(-1, 6) for y in range(-1, 5)])
    bases = (np.eye(2, dtype=int), np.array([[1, 1], [0, 1]]))
    point = np.array([3, 2])
    for ax, basis, label in zip(axes, bases, ("Standard basis: coordinates (3, 2)", "Sheared basis: coordinates (1, 2)")):
        ax.scatter(grid[:, 0], grid[:, 1], color="#59666d", s=22)
        b1, b2 = basis[:, 0], basis[:, 1]
        vertices = np.array([[0, 0], b1, b1 + b2, b2])
        ax.add_patch(Polygon(vertices, facecolor="#87b7d4", edgecolor="#216893", alpha=0.34, linewidth=2))
        for vector, color, text in [(b1, "#1f77b4", "b₁"), (b2, "#d17a22", "b₂")]:
            ax.annotate("", xy=vector, xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": color, "lw": 2.5})
            ax.text(vector[0] + 0.07, vector[1] + 0.13, text, color=color, fontsize=12)
        coefficient = (3, 2) if np.array_equal(basis, np.eye(2)) else (1, 2)
        first = coefficient[0] * b1
        ax.plot([0, first[0], point[0]], [0, first[1], point[1]], linestyle="--", color="#b22a40", linewidth=1.7)
        ax.scatter([point[0]], [point[1]], color="#b22a40", s=72, zorder=5)
        ax.annotate("Same point (3, 2)", point, xytext=(10, 10), textcoords="offset points", color="#b22a40", fontsize=11)
        ax.text(-0.65, 3.55, "Fundamental cell area = 1", fontsize=11)
        ax.set(xlim=(-.9, 4.65), ylim=(-.7, 4.05), xlabel="x", ylabel="y", title=label)
        ax.set_xticks(range(0, 5)); ax.set_yticks(range(0, 5))
        ax.set_aspect("equal", adjustable="box"); ax.grid(alpha=.15)
    fig.suptitle("Unimodular basis change: the integer lattice stays the same", fontsize=15)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
