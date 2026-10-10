"""Write chemical-formula-and-coefficient.png to the current working directory.

Connections H-O-H and H-O-O-H are schematic, not molecular geometry models.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp python3 ../chemical-formula-and-coefficient.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


COLORS = {"H": "#246baa", "O": "#c64b39"}


def molecule(ax, y, elements):
    x = np.linspace(-0.4 * (len(elements) - 1),
                     0.4 * (len(elements) - 1), len(elements))
    ax.plot(x, np.full(len(elements), y), color="#555555", lw=3, zorder=1)
    for position, element in zip(x, elements):
        ax.add_patch(Circle((position, y), 0.27, facecolor=COLORS[element],
                            edgecolor="white", lw=1.2, zorder=2))
        ax.text(position, y, element, fontsize=15, color="white", weight="bold",
                ha="center", va="center", zorder=3)


def main():
    groups = [["HOH"], ["HOH", "HOH"], ["HOOH"]]
    counts = np.array([[sum(group.count(element) for group in column)
                        for column in groups] for element in "HO"], dtype=int)
    np.testing.assert_array_equal(counts, [[2, 4, 2], [1, 2, 2]])
    plt.rcParams.update({"font.size": 14, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10, 5.7), facecolor="white")
    fig.suptitle("Coefficient and subscript do different jobs", fontsize=21, y=0.96)
    centers = [0.18, 0.50, 0.82]
    titles = ["H₂O", "2 H₂O", "H₂O₂"]
    subtitles = ["One water molecule", "Two water molecules", "One hydrogen peroxide molecule"]
    for index, (center, title, subtitle, column) in enumerate(zip(centers, titles, subtitles, groups)):
        fig.text(center, 0.80, title, ha="center", fontsize=27, weight="bold")
        fig.text(center, 0.735, subtitle, ha="center", fontsize=12)
        ax = fig.add_axes([center - 0.145, 0.365, 0.29, 0.33])
        ax.set(xlim=(-1.6, 1.6), ylim=(-1.05, 1.05), aspect="equal")
        ax.axis("off")
        for group, y in zip(column, [0] if len(column) == 1 else [0.5, -0.5]):
            molecule(ax, y, group)
        fig.text(center, 0.295, f"H atoms: {counts[0, index]}", ha="center", fontsize=17, color=COLORS["H"])
        fig.text(center, 0.23, f"O atoms: {counts[1, index]}", ha="center", fontsize=17, color=COLORS["O"])
    for x in [0.34, 0.66]:
        fig.add_artist(plt.Line2D([x, x], [0.20, 0.86], transform=fig.transFigure,
                                 color="#dddddd", lw=1))
    fig.text(0.5, 0.135, "A coefficient multiplies the whole formula. A subscript changes its composition.",
             ha="center", fontsize=13)
    fig.text(0.5, 0.055, "H–O–H and H–O–O–H connections only; lengths and angles are schematic.",
             ha="center", fontsize=12, color="#555555")
    fig.savefig("chemical-formula-and-coefficient.png", dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified columns: H atoms = [2, 4, 2]; O atoms = [1, 2, 2].")


if __name__ == "__main__":
    main()
