"""Plot determinant area, orientation, and collapse; save a white PNG in CWD.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 4, figsize=(10.8, 5.9), facecolor="white")
    fig.subplots_adjust(left=0.045, right=0.985, bottom=0.17, top=0.78, wspace=0.28)
    a = np.array([[2, 1], [1, 3]])
    cases = [
        (np.eye(2), "Unit square", r"$\det I=1$", "area = 1"),
        (a, "Apply A", r"$\det A=5$", "area = 5"),
        (a[:, ::-1], "Swap columns", r"$\det A_{\rm swap}=-5$", "area = 5"),
        (np.array([[1, 2], [2, 4]]), "Dependent columns", r"$\det C=0$", "area = 0"),
    ]
    corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    blue, orange = "#2365a0", "#b64a18"
    for ax, (matrix, heading, det_label, area_label) in zip(axes, cases):
        vertices = corners @ matrix.T
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-0.45, 3.7)
        ax.set_ylim(-0.45, 6.6)
        ax.set_xticks(range(4))
        ax.set_yticks(range(7))
        ax.grid(color="#e7e7e7", linewidth=0.7, zorder=0)
        ax.axhline(0, color="#999999", linewidth=0.8)
        ax.axvline(0, color="#999999", linewidth=0.8)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=9, length=0)
        ax.fill(*vertices.T, color="#bddbd2", alpha=0.7, zorder=2)
        closed = np.vstack([vertices, vertices[0]])
        ax.plot(*closed.T, color="#3e7366", linewidth=1.8, zorder=3)
        for col, color in zip(matrix.T, [blue, orange]):
            # Mark both column endpoints even when their arrows overlap.
            ax.annotate("", col, (0, 0), arrowprops={"arrowstyle": "->", "color": color,
                        "lw": 2.8, "mutation_scale": 15, "shrinkA": 0, "shrinkB": 0}, zorder=5)
            ax.plot(*col, "o", color=color, markersize=5, zorder=6)
        ax.plot(*vertices[2], "o", color="#3e7366", markersize=4, zorder=4)
        ax.set_title(heading + "\n" + det_label, fontsize=12, pad=12)
        ax.text(0.5, -0.14, area_label, transform=ax.transAxes, ha="center", fontsize=12)
        ax.set_xlabel("x", fontsize=10)
        ax.set_ylabel("y", fontsize=10)
    fig.suptitle("A determinant measures signed area", fontsize=17, y=0.96)
    fig.text(0.5, 0.87, "Blue = first column     Orange = second column     Same coordinate scale in every panel",
             ha="center", fontsize=11)
    fig.text(0.5, 0.055, "Swapping columns reverses orientation; dependent columns collapse the square to a segment.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
