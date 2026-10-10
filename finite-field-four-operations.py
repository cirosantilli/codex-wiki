"""Compute F4 tables using coefficient bits; write matching PNG to cwd.

Tested with Python 3.14.4 and the repository's matplotlib dependency.
Bit 0 is the constant coefficient; bit 1 is the coefficient of alpha.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


LABELS = ["0", "1", r"$\alpha$", r"$\alpha+1$"]
COLORS = ["#f0f2f4", "#cce8f6", "#f9ddb3", "#ded5ed"]


def multiply(x, y):
    """Reduce the product using alpha**2 = alpha + 1 over F2."""
    a, b = x & 1, (x >> 1) & 1
    c, d = y & 1, (y >> 1) & 1
    constant = (a * c) ^ (b * d)
    alpha = (a * d) ^ (b * c) ^ (b * d)
    return constant | (alpha << 1)


def verify():
    add = [[x ^ y for y in range(4)] for x in range(4)]
    mul = [[multiply(x, y) for y in range(4)] for x in range(4)]
    assert add == [[0, 1, 2, 3], [1, 0, 3, 2],
                   [2, 3, 0, 1], [3, 2, 1, 0]]
    assert mul == [[0, 0, 0, 0], [0, 1, 2, 3],
                   [0, 2, 3, 1], [0, 3, 1, 2]]
    for x in range(4):
        assert x ^ 0 == x and x ^ x == 0
        assert multiply(x, 1) == x and multiply(x, 0) == 0
        assert sorted(add[x]) == list(range(4))
        if x:
            assert sorted(mul[x]) == list(range(4))
            assert sum(multiply(x, y) == 1 for y in range(1, 4)) == 1
    for x, y in product(range(4), repeat=2):
        assert multiply(x, y) == multiply(y, x)
    for x, y, z in product(range(4), repeat=3):
        assert multiply(multiply(x, y), z) == multiply(x, multiply(y, z))
        assert multiply(x, y ^ z) == multiply(x, y) ^ multiply(x, z)
    assert [multiply(x, x) for x in range(4)] == [0, 1, 3, 2]
    assert multiply(2, multiply(2, 2)) == 1
    assert [((x * x) ^ x ^ 1) for x in range(2)] == [1, 1]
    print("F4 addition, labels 0, 1, alpha, alpha+1:", add)
    print("F4 multiplication:", mul)
    print("Checked all 64 associativity and distributivity triples; inverses [1, 3, 2].")
    return add, mul


def draw_table(ax, values, symbol, title):
    ax.set_xlim(-1.15, 4.05)
    ax.set_ylim(-0.15, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(1.5, 5.15, title, ha="center", fontsize=16, weight="bold")
    ax.text(-0.55, 4.45, symbol, ha="center", va="center", fontsize=20)
    for index, label in enumerate(LABELS):
        ax.text(index + 0.5, 4.45, label, ha="center", va="center", fontsize=17)
        ax.text(-0.55, 3.5 - index, label, ha="center", va="center", fontsize=17)
    for row, col in product(range(4), repeat=2):
        value = values[row][col]
        ax.add_patch(Rectangle((col, 3 - row), 1, 1,
                               facecolor=COLORS[value], edgecolor="white", lw=2))
        ax.text(col + 0.5, 3.5 - row, LABELS[value],
                ha="center", va="center", fontsize=19, color="#263746")


def main():
    add, mul = verify()
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.7), dpi=120, facecolor="white")
    draw_table(axes[0], add, "+", "Addition: coefficient XOR")
    draw_table(axes[1], mul, r"$\times$", r"Multiplication: $\alpha^2=\alpha+1$")
    fig.suptitle(r"The four-element field $\mathbb{F}_2[t]/(t^2+t+1)$",
                 fontsize=18, y=0.96)
    fig.text(0.5, 0.055,
             r"Bit labels:  $0\leftrightarrow00$     $1\leftrightarrow01$     "
             r"$\alpha\leftrightarrow10$     $\alpha+1\leftrightarrow11$",
             ha="center", fontsize=13)
    fig.subplots_adjust(left=0.045, right=0.985, top=0.87, bottom=0.14, wspace=0.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
