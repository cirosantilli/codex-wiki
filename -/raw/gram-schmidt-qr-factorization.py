"""Show a computed Gram-Schmidt QR factorization; write a PNG to CWD.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media to create gram-schmidt-qr-factorization.png there.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import Rectangle
import numpy as np


def exact_residuals():
    """Check the residuals with rational arithmetic before drawing decimals."""
    inputs = [list(map(Fraction, v)) for v in [[1, 1, 0], [1, 0, 1], [0, 1, 1]]]
    residuals = []
    dot = lambda a, b: sum(x * y for x, y in zip(a, b))
    for v in inputs:
        remainder = v.copy()
        for u in residuals:
            coefficient = dot(v, u) / dot(u, u)
            remainder = [x - coefficient * y for x, y in zip(remainder, u)]
        residuals.append(remainder)
    assert residuals[1] == [Fraction(1, 2), Fraction(-1, 2), Fraction(1)]
    assert residuals[2] == [Fraction(-2, 3), Fraction(2, 3), Fraction(2, 3)]
    squared_lengths = [dot(u, u) for u in residuals]
    assert squared_lengths == [Fraction(2), Fraction(3, 2), Fraction(4, 3)]
    for i in range(3):
        for j in range(i):
            assert dot(residuals[i], residuals[j]) == 0
    print("Exact residuals:", residuals)
    print("Exact squared lengths:", squared_lengths)


def main():
    exact_residuals()
    a = np.array([[1., 1., 0.], [1., 0., 1.], [0., 1., 1.]])
    q = np.array([[1., 1., -1.], [1., -1., 1.], [0., 2., 1.]]) / np.sqrt([2., 6., 3.])
    r = np.array([[np.sqrt(2), 1 / np.sqrt(2), 1 / np.sqrt(2)],
                  [0, np.sqrt(3 / 2), 1 / np.sqrt(6)], [0, 0, 2 / np.sqrt(3)]])
    assert np.allclose(q.T @ q, np.eye(3), atol=1e-14, rtol=0)
    assert np.allclose(q @ r, a, atol=1e-14, rtol=0)
    assert np.allclose(q.T @ a, r, atol=1e-14, rtol=0)
    assert np.allclose(r.T @ r, a.T @ a, atol=1e-14, rtol=0)
    b = np.array([0., 0., 1.])
    q_two, a_two = q[:, :2], a[:, :2]
    projection = q_two @ (q_two.T @ b)
    x = np.linalg.solve(r[:2, :2], q_two.T @ b)
    assert np.allclose(x, [-1 / 3, 2 / 3], atol=1e-14)
    assert np.allclose(projection, [1 / 3, -1 / 3, 2 / 3], atol=1e-14)
    assert np.allclose(a_two @ x, projection, atol=1e-14)
    assert np.allclose(q_two.T @ (b - projection), 0, atol=1e-14)
    assert np.isclose(np.linalg.norm(b - projection), 1 / np.sqrt(3), atol=1e-14)

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(11, 5.2))
    positions = [0.07, 0.38, 0.69]
    axes = [fig.add_axes([left, 0.30, 0.24, 0.45]) for left in positions]
    norm = TwoSlopeNorm(vmin=-1.5, vcenter=0, vmax=1.5)
    titles = ["A: original columns", "Q: unit directions", "R: recorded coefficients"]
    column_labels = [[r"$v_1$", r"$v_2$", r"$v_3$"],
                     [r"$q_1$", r"$q_2$", r"$q_3$"],
                     [r"$v_1$", r"$v_2$", r"$v_3$"]]
    for index, (ax, matrix, title, labels) in enumerate(zip(axes, [a, q, r], titles, column_labels)):
        im = ax.imshow(matrix, cmap="RdBu_r", norm=norm, interpolation="nearest")
        ax.set_title(title, fontsize=13, pad=14)
        ax.set_xticks(range(3), labels=labels)
        ax.tick_params(length=0)
        ax.set_yticks(range(3), labels=([r"$q_1$", r"$q_2$", r"$q_3$"]
                                      if index == 2 else ["1", "2", "3"]))
        ax.set_xticks(np.arange(-0.5, 3, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 3, 1), minor=True)
        ax.grid(which="minor", color="white", linewidth=2)
        ax.tick_params(which="minor", length=0)
        for row in range(3):
            for col in range(3):
                value = matrix[row, col]
                label = str(int(value)) if index == 0 or value == 0 else f"{value:.3f}"
                ax.text(col, row, label, ha="center", va="center", fontsize=16,
                        color="white" if abs(value) > 1.05 else "#182b3b")
                if index == 2 and row == col:
                    ax.add_patch(Rectangle((col - 0.46, row - 0.46), 0.92, 0.92,
                                           fill=False, edgecolor="#f3bd49", linewidth=2.3))
    fig.text(0.345, 0.53, "=", fontsize=27, ha="center", va="center")
    fig.text(0.655, 0.53, "×", fontsize=27, ha="center", va="center")
    fig.suptitle("Gram–Schmidt records the factorization A = QR", fontsize=17, y=0.97)
    fig.text(0.5, 0.86, "Color shows signed entries on one common scale; decimals are rounded to 3 places.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.23, r"$Q^TQ=I$    ·    $QR=A$    ·    $R^TR=A^TA$", ha="center", fontsize=14)
    fig.text(0.5, 0.15, r"Highlighted diagonal: $\|u_1\|=\sqrt{2}$,  "
             r"$\|u_2\|=\sqrt{3/2}$,  $\|u_3\|=2/\sqrt{3}$", ha="center", fontsize=12)
    color_ax = fig.add_axes([0.31, 0.055, 0.38, 0.023])
    fig.colorbar(im, cax=color_ax, orientation="horizontal", ticks=[-1.5, 0, 1.5])
    color_ax.tick_params(labelsize=10, length=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("max|Q.T Q-I| =", np.max(np.abs(q.T @ q - np.eye(3))))
    print("max|QR-A| =", np.max(np.abs(q @ r - a)))
    print("Checked: Q.T A=R; R.T R=A.T A; projection and least squares x=(-1/3,2/3), distance=1/sqrt(3).")


if __name__ == "__main__":
    main()
