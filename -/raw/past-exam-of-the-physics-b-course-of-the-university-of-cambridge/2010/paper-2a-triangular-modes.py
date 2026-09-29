"""Original equilateral-molecule mode sketch.

Python 3.14; numpy 2.3.5; matplotlib 3.10.7 (root pyproject.toml).
Writes paper-2a-triangular-modes.png to the current working directory.
Only displacement directions are illustrated; no frequencies are assigned.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
    vertices = np.array([[0.0, 1.0], [-np.sqrt(3) / 2, -0.5], [np.sqrt(3) / 2, -0.5]])
    transforms = [np.eye(2), np.diag([1.0, -1.0]), np.array([[0.0, 1.0], [1.0, 0.0]])]
    titles = ["Symmetric breathing", "Degenerate pair: basis 1", "Degenerate pair: basis 2"]
    formulas = [
        r"$\mathbf{u}_j=\mathbf{r}_j$",
        r"$\mathbf{u}_j=(x_j,-y_j)$",
        r"$\mathbf{u}_j=(y_j,x_j)$",
    ]
    colors = ["#176493", "#a44720", "#a44720"]
    fig, axes = plt.subplots(1, 3, figsize=(8.6, 3.75))
    fig.subplots_adjust(left=0.025, right=0.985, top=0.77, bottom=0.24, wspace=0.12)
    fig.suptitle(r"H$_3^+$: three in-plane vibrational modes", y=0.965, fontsize=13)
    closed = np.vstack([vertices, vertices[0]])
    for ax, transform, title, formula, color in zip(axes, transforms, titles, formulas, colors):
        vectors = vertices @ transform.T
        ax.plot(closed[:, 0], closed[:, 1], "--", color="0.62", lw=1.2)
        ax.scatter(vertices[:, 0], vertices[:, 1], s=150, color="#f1f1f1", edgecolor="0.35", zorder=4)
        ax.plot(0, 0, "+", color="0.55", ms=6)
        for vertex, vector in zip(vertices, vectors):
            ax.add_patch(
                FancyArrowPatch(vertex, vertex + 0.43 * vector, arrowstyle="-|>",
                                mutation_scale=15, lw=2.2, color=color, zorder=5)
            )
        ax.set_title(title, fontsize=10, pad=12)
        ax.text(0.5, -0.12, formula, transform=ax.transAxes, ha="center", fontsize=11)
        ax.set(xlim=(-1.45, 1.45), ylim=(-1.04, 1.57), aspect="equal")
        ax.axis("off")
    fig.text(0.5, 0.135, r"$\mathbf{r}_j=(x_j,y_j)$ is measured from the centre (+); dashed bonds mark equilibrium.",
             ha="center", fontsize=9)
    fig.text(0.5, 0.075, "Arrows show one phase; reversing all arrows gives the opposite phase.", ha="center", fontsize=9)
    fig.text(0.5, 0.02, "The two distortions span a symmetry-degenerate subspace; no measured frequencies are implied.",
             ha="center", fontsize=9)
    fig.savefig("paper-2a-triangular-modes.png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
