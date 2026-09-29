"""Compute and illustrate the subgroup preserving each vertex coloring."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def square_actions():
    r = np.array([[0, -1], [1, 0]])
    s = np.diag([1, -1])
    return [np.linalg.matrix_power(r, k) for k in range(4)] + [np.linalg.matrix_power(r, k) @ s for k in range(4)]


def preserving(points, colors, matrix):
    lookup = {tuple(point): color for point, color in zip(points, colors)}
    return all(lookup[tuple(matrix @ point)] == color for point, color in zip(points, colors))


def main():
    points = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]])
    actions = square_actions()
    patterns = [([0, 0, 0, 0], "One uniform color"), ([0, 0, 1, 1], "Two adjacent red vertices"), ([0, 1, 0, 1], "Two opposite red vertices"), ([0, 1, 2, 3], "Four distinct colors")]
    palette = ["#c64b42", "#367caf", "#279879", "#d89126"]
    fig, axes = plt.subplots(2, 2, figsize=(11.6, 7.3), dpi=100, layout="constrained")
    fig.set_facecolor("white")
    for ax, (colors, title) in zip(axes.flat, patterns):
        admitted = [matrix for matrix in actions if preserving(points, colors, matrix)]
        rotations = sum(round(np.linalg.det(matrix)) == 1 for matrix in admitted)
        reflections = len(admitted) - rotations
        outline = np.vstack([points, points[0]])
        ax.plot(outline[:, 0], outline[:, 1], color="#59666d", linewidth=2)
        # Reflection axes are the +1 eigenspaces; for symmetric orthogonal
        # reflection matrices an eigenvector is a directly checkable axis.
        for matrix in admitted:
            if round(np.linalg.det(matrix)) == -1:
                values, vectors = np.linalg.eigh(matrix)
                direction = vectors[:, np.argmax(values)]
                ends = np.array([-1.3*direction, 1.3*direction])
                ax.plot(ends[:, 0], ends[:, 1], color="#89909a", linestyle="--", linewidth=1.3)
        ax.scatter(points[:, 0], points[:, 1], c=[palette[c] for c in colors], s=140, edgecolors="white", linewidths=1.2, zorder=4)
        ax.text(0, -.05, f"{len(admitted)} preserving {'map' if len(admitted)==1 else 'maps'}", ha="center", va="center", fontsize=12, bbox={"facecolor":"white","edgecolor":"none","alpha":.93,"pad":2.0})
        ax.text(0, -1.48, f"{rotations} {'rotation' if rotations==1 else 'rotations'} + {reflections} {'reflection' if reflections==1 else 'reflections'}", ha="center", fontsize=11)
        ax.set(title=title, xlim=(-1.6,1.6), ylim=(-1.65,1.45))
        ax.set_aspect("equal", adjustable="box"); ax.axis("off")
    fig.suptitle("The square stays the same; fixed color data change its symmetry group", fontsize=15)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
