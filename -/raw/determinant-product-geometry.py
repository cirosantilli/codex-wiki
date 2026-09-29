"""Plot the successive area factors of B and A; save a white PNG in CWD.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(10.2, 5.9), facecolor="white")
    fig.subplots_adjust(left=0.055, right=0.97, bottom=0.17, top=0.75, wspace=0.25)
    a = np.array([[2, 1], [1, 3]])
    b = np.diag([1, 2])
    corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    blue, orange = "#2365a0", "#b64a18"
    for ax, matrix, heading, area in zip(axes, [np.eye(2), b, a @ b],
                                       ["Original square", "After B", "After A: AB"], [1, 2, 10]):
        vertices = corners @ matrix.T
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.set_xlim(-0.45, 4.65)
        ax.set_ylim(-0.45, 7.6)
        ax.set_xticks(range(5))
        ax.set_yticks(range(8))
        ax.grid(color="#e7e7e7", linewidth=0.7, zorder=0)
        ax.axhline(0, color="#999999", linewidth=0.8)
        ax.axvline(0, color="#999999", linewidth=0.8)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=9, length=0)
        ax.fill(*vertices.T, color="#bddbd2", alpha=0.7, zorder=2)
        closed = np.vstack([vertices, vertices[0]])
        ax.plot(*closed.T, color="#3e7366", linewidth=1.8, zorder=3)
        for col, color in zip(matrix.T, [blue, orange]):
            ax.annotate("", col, (0, 0), arrowprops={"arrowstyle": "->", "color": color,
                        "lw": 2.8, "mutation_scale": 15, "shrinkA": 0, "shrinkB": 0}, zorder=5)
        ax.plot(*vertices[2], "o", color="#3e7366", markersize=4, zorder=4)
        ax.set_title(heading, fontsize=13, pad=12)
        ax.text(0.5, -0.14, f"area = {area}", transform=ax.transAxes, ha="center", fontsize=12)
        ax.set_xlabel("x", fontsize=10)
        ax.set_ylabel("y", fontsize=10)
    fig.suptitle("Two maps multiply their area factors", fontsize=17, y=0.965)
    fig.text(0.5, 0.90, r"$B=\mathrm{diag}(1,2)$     $A=(\, (2,1)^T\;\; (1,3)^T\,)$", ha="center", fontsize=13)
    centers = [ax.get_position().x0 + ax.get_position().width / 2 for ax in axes]
    for left, right, label in [(centers[0], centers[1], "apply B: ×2"),
                               (centers[1], centers[2], "apply A: ×5")]:
        axes[0].annotate("", xy=(right - 0.06, 0.805), xytext=(left + 0.06, 0.805),
                         xycoords=fig.transFigure, textcoords=fig.transFigure,
                         arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.5})
        fig.text((left + right) / 2, 0.83, label, ha="center", fontsize=12)
    fig.text(0.5, 0.055, r"$1\times 2\times 5=10$     $\det(AB)=\det(A)\det(B)$     Same coordinate scale in every panel",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
