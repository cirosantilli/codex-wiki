"""Compute and visualize two orders of matrix action; PNG goes to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def matrix(ax, entries, center, label, color):
    x, y = center
    for i in range(2):
        for j in range(2):
            ax.text(x + (j - 0.5) * 0.24, y + (0.5 - i) * 0.26, str(entries[i, j]),
                    ha="center", va="center", fontsize=15, color=color)
    for side in (-1, 1):
        edge = x + side * 0.28
        ax.plot([edge - side * 0.07, edge, edge, edge - side * 0.07],
                [y + 0.29, y + 0.29, y - 0.29, y - 0.29], color=color, linewidth=1.5)
    ax.text(x - 0.37, y, label + " =", ha="right", va="center", fontsize=15, color=color)


def main():
    a = np.array([[1, 0], [0, 0]], dtype=int)
    b = np.array([[0, 1], [1, 0]], dtype=int)
    v = np.array([1, 0], dtype=int)
    ab, ba = a @ b, b @ a
    assert ab.tolist() == [[0, 1], [0, 0]]
    assert ba.tolist() == [[0, 0], [1, 0]]
    assert not np.array_equal(ab, ba)
    assert (ab @ v).tolist() == [0, 0]
    assert (ba @ v).tolist() == [0, 1]
    assert np.array_equal(ab @ v, a @ (b @ v))
    assert np.array_equal(ba @ v, b @ (a @ v))

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.6), dpi=120)
    for ax, first, second, product, label, color in [
        (axes[0], b, a, ab, "AB", "#176997"),
        (axes[1], a, b, ba, "BA", "#b95f22"),
    ]:
        ax.set_xlim(-0.5, 2.5)
        ax.set_ylim(-1.1, 1.6)
        ax.axis("off")
        values = [v, first @ v, second @ (first @ v)]
        for x, value in enumerate(values):
            ax.text(x, 0.8, f"({value[0]}, {value[1]})", ha="center", va="center",
                    fontsize=15, color=color,
                    bbox={"boxstyle": "round,pad=0.35", "fc": "#f2f5f8", "ec": color})
        actions = ["B: swap", "A: keep first"] if label == "AB" else ["A: keep first", "B: swap"]
        for x, action in enumerate(actions):
            ax.annotate("", xy=(x + 0.73, 0.8), xytext=(x + 0.27, 0.8),
                        arrowprops={"arrowstyle": "-|>", "lw": 2, "color": color,
                                    "mutation_scale": 14})
            ax.text(x + 0.5, 1.22, action, ha="center", fontsize=11, color=color)
        ax.set_title(f"{label}: apply the right factor first", fontsize=13, pad=16, color=color)
        matrix(ax, product, (1.12, -0.3), label, color)
        ax.text(1, -0.95, f"{label}(1, 0) = ({values[-1][0]}, {values[-1][1]})",
                ha="center", fontsize=12, color=color)
    fig.suptitle("Swapping and discarding a coordinate depend on order", fontsize=15, y=0.98)
    fig.text(0.5, 0.86, "A(x, y) = (x, 0)     B(x, y) = (y, x)     All pairs are column vectors",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.70, bottom=0.06, wspace=0.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
