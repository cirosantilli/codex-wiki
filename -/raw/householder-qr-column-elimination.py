"""Reflecting two columns into a signed upper-triangular factor; output to CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    matrix = np.array([[3., 1.], [4., 2.]])
    reflection = np.array([[-3., -4.], [-4., 3.]]) / 5
    triangular = reflection @ matrix
    assert np.allclose(triangular, [[-5, -11/5], [0, 2/5]])
    assert np.allclose(reflection @ triangular, matrix)
    assert np.allclose(matrix.T @ matrix, triangular.T @ triangular)
    sign = np.diag([-1., 1.])
    q = reflection @ sign
    positive = sign @ triangular
    assert np.allclose(q @ positive, matrix)
    assert np.allclose(q.T @ q, np.eye(2))
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.4), dpi=110)
    fig.patch.set_facecolor("white")
    datasets = [(matrix, "Original columns", ["(3, 4)", "(1, 2)"]),
                (triangular, "After the same reflection", ["(−5, 0)", "(−2.2, 0.4)"])]
    for i, (ax, (columns, title, labels)) in enumerate(zip(axes, datasets)):
        for j, color in enumerate(["#245f9b", "#c56521"]):
            end = columns[:, j]
            ax.annotate("", end, (0, 0),
                        arrowprops=dict(arrowstyle="-|>", color=color,
                                        lw=2.5, mutation_scale=18))
            ax.scatter(*end, color=color, s=45, zorder=4)
            offset = (.15, .2) if i == 0 else (-.6, -.6) if j == 0 else (-.45, .3)
            ax.text(end[0]+offset[0], end[1]+offset[1], labels[j],
                    color=color, fontsize=12)
        ax.axhline(0, color="#777777", lw=.8)
        ax.axvline(0, color="#777777", lw=.8)
        ax.set_xlim(-6.3, 4.3)
        ax.set_ylim(-1.2, 5)
        ax.set_aspect("equal")
        ax.set_xlabel("First component")
        ax.set_ylabel("Second component")
        ax.set_title(title, fontsize=13)
        ax.grid(alpha=.16)
    fig.suptitle("Householder elimination: the first column lands on an axis", fontsize=15)
    fig.text(.5, .07,
             "Column lengths and their inner product are unchanged. "
             "The first column's second component becomes zero.",
             ha="center", fontsize=10.5)
    fig.text(.5, .025,
             "This is the intermediate signed R; flipping the first row yields "
             "the positive-diagonal convention.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.07, right=.98, bottom=.17, top=.86, wspace=.22)
    fig.savefig(Path.cwd() / "householder-qr-column-elimination.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
