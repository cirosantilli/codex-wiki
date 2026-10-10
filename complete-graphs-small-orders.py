"""Draw complete graphs K1 through K5, with exact edge and degree counts."""
from pathlib import Path
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np


def positions(n):
    if n == 1:
        return np.array([[0., 0.]])
    if n == 2:
        return np.array([[-.75, 0.], [.75, 0.]])
    if n == 4:
        angles = np.pi / 2 + 2 * np.pi * np.arange(3) / 3
        return np.vstack((np.column_stack((np.cos(angles), np.sin(angles))), [0., 0.]))
    angles = np.pi / 2 + 2 * np.pi * np.arange(n) / n
    return np.column_stack((np.cos(angles), np.sin(angles)))


def main():
    fig, axes = plt.subplots(1, 5, figsize=(12.4, 3.8), dpi=100, facecolor="white")
    for n, ax in enumerate(axes, 1):
        p = positions(n)
        for i, j in combinations(range(n), 2):
            ax.plot(p[[i, j], 0], p[[i, j], 1], color="#617f96", lw=1.65, zorder=1)
        ax.scatter(p[:, 0], p[:, 1], s=190, facecolor="#235e88", edgecolor="white", lw=1, zorder=3)
        for i, (x, y) in enumerate(p, 1):
            ax.text(x, y, str(i), color="white", ha="center", va="center", fontsize=10, zorder=4)
        ax.set_aspect("equal"); ax.set(xlim=(-1.2, 1.2), ylim=(-1.25, 1.25))
        ax.axis("off"); ax.set_title(rf"$K_{n}$", fontsize=18)
        ax.text(.5, -.08, f"Vertices: {n}\nEdges: {n * (n - 1) // 2}\nEach degree: {n - 1}",
                transform=ax.transAxes, ha="center", va="top", fontsize=11)
    fig.suptitle("Complete graphs: every pair of distinct vertices has an edge", fontsize=16)
    fig.text(.5, .035, "In K5, line crossings without vertex markers are not extra vertices.", ha="center", fontsize=11)
    fig.tight_layout(rect=(0, .19, 1, .89), w_pad=1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
