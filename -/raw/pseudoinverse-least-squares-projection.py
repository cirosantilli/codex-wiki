"""Orthogonal slice of a three-dimensional least-squares example; output to CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    matrix = np.array([[1., 0.], [0., 1.], [1., 1.]])
    data = np.array([1., 2., 6.])
    inverse = np.array([[2., -1., 1.], [-1., 2., 1.]]) / 3
    solution = inverse @ data
    fitted = matrix @ solution
    residual = data - fitted
    assert np.allclose(solution, [2, 3])
    assert np.allclose(fitted, [2, 3, 5])
    assert np.allclose(residual, [-1, -1, 1])
    assert np.allclose(matrix.T @ residual, 0)
    tangent = fitted / np.linalg.norm(fitted)
    normal = residual / np.linalg.norm(residual)
    assert np.isclose(tangent @ normal, 0)
    fitted_x = fitted @ tangent
    data_y = data @ normal
    assert np.isclose(fitted_x, np.sqrt(38))
    assert np.isclose(data_y, np.sqrt(3))

    fig, ax = plt.subplots(figsize=(10.5, 5.3), dpi=110)
    fig.patch.set_facecolor("white")
    ax.axhline(0, color="#245f9b", lw=3, zorder=1)
    ax.axvline(0, color="#b0b0b0", lw=1, zorder=1)
    arrow = dict(arrowstyle="-|>", mutation_scale=20, lw=2.5)
    ax.annotate("", (fitted_x, 0), (0, 0),
                arrowprops=dict(arrow, color="#245f9b"))
    ax.annotate("", (fitted_x, data_y), (0, 0),
                arrowprops=dict(arrow, color="#343434"))
    ax.annotate("", (fitted_x, data_y), (fitted_x, 0),
                arrowprops=dict(arrow, color="#c56521"))
    ax.plot([fitted_x - .23, fitted_x - .23, fitted_x],
            [0, .23, .23], color="#777777", lw=1.4)
    ax.scatter([0, fitted_x, fitted_x], [0, 0, data_y],
               c=["#343434", "#245f9b", "#343434"], s=55, zorder=5)
    ax.text(-.1, -.28, "Origin", ha="right", fontsize=11)
    ax.text(fitted_x, -.18, "Fitted output\np = (2, 3, 5)", ha="center",
            color="#245f9b", fontsize=12, va="top")
    ax.text(fitted_x + .18, data_y + .13, "Data\nb = (1, 2, 6)",
            fontsize=12)
    ax.text(fitted_x + .35, data_y / 2, "Residual\nr = (−1, −1, 1)\n"
            r"$\|r\|=\sqrt{3}$", va="center", color="#c56521", fontsize=11)
    ax.text(2.7, -.22, "Attainable outputs in this slice",
            color="#245f9b", fontsize=11, ha="center", va="top")
    ax.set_xlim(-.6, 9.2)
    ax.set_ylim(-.8, 2.45)
    ax.set_aspect("equal")
    ax.set_xlabel("Coordinate along the unit vector p / ‖p‖", fontsize=11)
    ax.set_ylabel("Coordinate along the unit vector r / ‖r‖", fontsize=11)
    ax.set_title("Pseudoinverse: closest attainable output", fontsize=16, pad=15)
    ax.grid(alpha=.15)
    fig.text(.5, .045,
             "An orthonormal two-dimensional slice of output space ℝ³: "
             "the column space intersects this slice in the blue line.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.08, right=.98, bottom=.15, top=.89)
    fig.savefig(Path.cwd() / "pseudoinverse-least-squares-projection.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
