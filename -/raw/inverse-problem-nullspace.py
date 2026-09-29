"""Write inverse-problem-nullspace.png into cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; only NumPy, Matplotlib and the standard library are used.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    weak = np.array([[0.55, 0.45], [0.45, 0.55]])
    lost = np.full((2, 2), 0.5)
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    t = np.linspace(0, 1, 5)
    samples = np.column_stack([t, 1 - t])
    np.testing.assert_allclose(samples @ lost.T, 0.5)
    np.testing.assert_allclose(weak @ [1, -1], [0.1, -0.1])
    np.testing.assert_allclose(lost @ [1, -1], [0, 0])
    colors = ["#1765a8", "#257e65", "#94640a", "#bf5b16", "#793a95"]
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.6), facecolor="white")
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.22, top=0.74, wspace=0.33)
    fig.suptitle("Weak information is different from lost information", y=0.98, fontsize=16)
    fig.text(0.5, 0.875, "The same unit square and five inputs with x₁ + x₂ = 1 are mapped in each panel.", ha="center")
    matrices = [np.eye(2), weak, lost]
    titles = ["Input pixels", "Weak difference mode", "Lost difference mode"]
    subtitles = ["x = (t, 1 − t)", "A = [[0.55, 0.45], [0.45, 0.55]]", "B = [[0.5, 0.5], [0.5, 0.5]]"]
    for i, (ax, matrix, title, subtitle) in enumerate(zip(axes, matrices, titles, subtitles)):
        boundary = square @ matrix.T
        points = samples @ matrix.T
        ax.fill(boundary[:, 0], boundary[:, 1], color="#edf1f5")
        ax.plot(boundary[:, 0], boundary[:, 1], color="#717d89", lw=1.5)
        if i < 2:
            ax.plot(points[:, 0], points[:, 1], color="#555555", lw=1, ls="--")
            ax.scatter(points[:, 0], points[:, 1], s=65, c=colors, edgecolors="white", linewidths=0.8, zorder=4)
        else:
            ax.scatter([0.5], [0.5], s=110, facecolor="white", edgecolor="#793a95", linewidth=2, zorder=4)
            ax.annotate("All five inputs\ngive (0.5, 0.5)", (0.5, 0.5), xytext=(0.08, 0.83), arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
        if i == 1:
            ax.annotate("(0.55, 0.45)", (0.55, 0.45), xytext=(0.42, 0.12), arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
            ax.annotate("(0.45, 0.55)", (0.45, 0.55), xytext=(0.03, 0.85), arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
        ax.set_title(title, pad=28)
        ax.text(0.5, 1.045, subtitle, transform=ax.transAxes, ha="center", fontsize=9)
        ax.set_xlim(-0.08, 1.08)
        ax.set_ylim(-0.08, 1.08)
        ax.set_aspect("equal")
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 0.5, 1])
        ax.set_xlabel("x₁" if i == 0 else "y₁")
        ax.set_ylabel("x₂" if i == 0 else "y₂")
        ax.set_facecolor("white")
        ax.grid(color="#e3e7eb", lw=0.6)
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.055, "Difference (1, −1):    A scales it by 0.1; B sends it to zero.    Both preserve the mean mode (1, 1).", ha="center")
    fig.savefig(Path.cwd() / "inverse-problem-nullspace.png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
