"""Illustrate original integer matrix powers reduced by Cayley–Hamilton; emit to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.array([[2, 1], [1, 1]], dtype=object)
    identity = np.eye(2, dtype=object)
    assert np.array_equal(a @ a - 3 * a + identity, np.zeros((2, 2), dtype=object))
    rows = []
    coefficient, constant = 0, 1
    for n in range(8):
        assert np.array_equal(np.linalg.matrix_power(a, n), coefficient * a + constant * identity)
        rows.append([n, coefficient, constant])
        coefficient, constant = 3 * coefficient + constant, -coefficient
    fig = plt.figure(figsize=(10, 6), dpi=120, facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 3, height_ratios=[1.4, 1])
    ax = fig.add_subplot(grid[0, :2])
    ax.axis("off")
    table = ax.table(cellText=rows, colLabels=["n", "Coefficient of A", "Coefficient of I"], cellLoc="center", bbox=[0.15, 0, 0.7, 0.9])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for j in range(3):
        table[(0, j)].set_facecolor("#dce9f4")
        table[(6, j)].set_facecolor("#e5f2e5")
    ax.set_title(r"Every power is $A^n=a_n A+b_n I$", fontsize=14)
    ax = fig.add_subplot(grid[0, 2])
    ax.axis("off")
    for y, text in [(0.91, "A = [[2, 1], [1, 1]]"), (0.68, r"$A^2=3A-I$"), (0.43, r"$a_{n+1}=3a_n+b_n$"), (0.24, r"$b_{n+1}=-a_n$")]:
        ax.text(0.5, y, text, ha="center", va="center", fontsize=13)
    matrices = [55 * a, -21 * identity, np.linalg.matrix_power(a, 5)]
    for j, (matrix, title) in enumerate(zip(matrices, [r"$55A$", r"$-21I$", r"$A^5=55A-21I$"])):
        ax = fig.add_subplot(grid[1, j])
        values = np.asarray(matrix, dtype=float)
        ax.imshow(values, cmap="RdBu", vmin=-110, vmax=110)
        for (i, k), value in np.ndenumerate(matrix):
            ax.text(k, i, str(value), ha="center", va="center", fontsize=17, color="white" if abs(value) > 70 else "black")
        ax.set(xticks=[], yticks=[], title=title)
    fig.suptitle("Two scalar coefficients replace repeated matrix multiplication", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
