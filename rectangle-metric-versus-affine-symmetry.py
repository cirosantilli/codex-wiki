"""Show one affine rectangle symmetry that does not preserve Euclidean length."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    points = np.array([[2., 1.], [-2., 1.], [-2., -1.], [2., -1.]])
    transform = np.array([[0., -2.], [.5, 0.]])
    image = points @ transform.T
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.3), dpi=100, layout="constrained")
    fig.set_facecolor("white")
    for ax, vertices, title, length in zip(axes, [points, image], ["Original side: length 4", "Image side: length 2"], [4, 2]):
        outline = np.vstack([points, points[0]])
        ax.plot(outline[:, 0], outline[:, 1], color="#647680", linewidth=2)
        ax.scatter(vertices[:, 0], vertices[:, 1], color="#34495e", s=47, zorder=4)
        # Track the same ordered edge, rather than coloring the whole object.
        edge = vertices[:2]
        ax.annotate("", xy=edge[1], xytext=edge[0], arrowprops={"arrowstyle": "->", "color": "#d17a22", "lw": 3})
        for label, point in zip(["A", "B", "C", "D"], vertices):
            offset = (9 if point[0] >= 0 else -19, 9 if point[1] >= 0 else -21)
            ax.annotate(label, point, xytext=offset, textcoords="offset points", fontsize=12)
        midpoint = edge.mean(axis=0)
        offset = (0, 20) if length == 4 else (40, 0)
        ax.annotate(f"Length {length}", midpoint, xytext=offset, textcoords="offset points", fontsize=11, color="#bd661b", ha="center", va="center")
        ax.set(xlim=(-2.85, 2.85), ylim=(-1.95, 1.95), xlabel="x", ylabel="y", title=title)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xticks(range(-2, 3)); ax.set_yticks(range(-1, 2)); ax.grid(alpha=.17)
        ax.axhline(0, color="#aaaaaa", linewidth=.7);ax.axvline(0, color="#aaaaaa", linewidth=.7)
    fig.suptitle("Affine symmetry T(x, y) = (−2y, x/2): same vertex set, different side length", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
