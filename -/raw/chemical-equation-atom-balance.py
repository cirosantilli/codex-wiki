"""Write chemical-equation-atom-balance.png to the current working directory.

Invented atom-token schematic, not a geometry model or a reaction mechanism.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp python3 ../chemical-equation-atom-balance.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


COLORS = {"H": "#246baa", "O": "#c64b39"}


def tokens(ax, center, elements):
    offsets = np.linspace(-0.40 * (len(elements) - 1),
                          0.40 * (len(elements) - 1), len(elements))
    points = np.column_stack((center[0] + offsets,
                              np.full(len(elements), center[1])))
    ax.plot(points[:, 0], points[:, 1], color="#555555", lw=3, zorder=1)
    for (x, y), element in zip(points, elements):
        ax.add_patch(Circle((x, y), 0.27, facecolor=COLORS[element],
                            edgecolor="white", lw=1.2, zorder=2))
        ax.text(x, y, element, color="white", fontsize=15, weight="bold",
                ha="center", va="center", zorder=3)


def main():
    # H and O rows; H2, O2, H2O columns. Exact integer bookkeeping.
    composition = np.array([[2, 0, 2], [0, 2, 1]], dtype=int)
    left = composition @ np.array([2, 1, 0])
    right = composition @ np.array([0, 0, 2])
    np.testing.assert_array_equal(left, [4, 2])
    np.testing.assert_array_equal(left, right)
    plt.rcParams.update({"font.size": 13, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10, 6.2), facecolor="white")
    fig.suptitle("A balanced equation keeps the atom inventory", fontsize=20, y=0.97)
    fig.text(0.5, 0.855, "2 H₂  +  1 O₂  →  2 H₂O", ha="center", fontsize=23)
    ax = fig.add_axes([0.035, 0.49, 0.93, 0.29])
    ax.set(xlim=(0, 12), ylim=(-0.9, 1.1), aspect="equal")
    ax.axis("off")
    tokens(ax, (0.7, 0.2), "HH")
    tokens(ax, (2.3, 0.2), "HH")
    tokens(ax, (4.5, 0.2), "OO")
    tokens(ax, (8.4, 0.2), "HOH")
    tokens(ax, (10.6, 0.2), "HOH")
    ax.text(3.25, 0.2, "+", fontsize=25, ha="center", va="center")
    ax.annotate("", xy=(7, 0.2), xytext=(5.7, 0.2),
                arrowprops={"arrowstyle": "->", "lw": 2.3})
    ax.text(2.6, -0.7, "Reactants: three molecules", ha="center", fontsize=13)
    ax.text(9.5, -0.7, "Products: two molecules", ha="center", fontsize=13)
    bars = fig.add_axes([0.13, 0.16, 0.74, 0.27])
    x = np.arange(2)
    bars.bar(x - 0.18, left, 0.36, color="#246baa", label="Before")
    bars.bar(x + 0.18, right, 0.36, color="#ed9c49", label="After")
    bars.set(xticks=x, xticklabels=["H atoms", "O atoms"], ylim=(0, 5.5),
             yticks=[0, 1, 2, 3, 4], ylabel="Atom count")
    bars.spines[["top", "right"]].set_visible(False)
    bars.legend(loc="upper right", frameon=False, ncol=2)
    for offset, values in [(-0.18, left), (0.18, right)]:
        for i, count in enumerate(values):
            bars.text(i + offset, count + 0.08, str(count), ha="center", fontsize=13)
    fig.text(0.5, 0.045, "Invented schematic: lines show connections, not real lengths or angles.",
             ha="center", fontsize=12, color="#555555")
    fig.savefig("chemical-equation-atom-balance.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Exact atom counts before/after: H = 4/4, O = 2/2.")


if __name__ == "__main__":
    main()
