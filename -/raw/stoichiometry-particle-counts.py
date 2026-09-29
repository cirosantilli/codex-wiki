"""Draw stoichiometry-particle-counts.png into the current working directory.

Schematic particles, not a reaction mechanism or a molecular geometry model.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
From _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp python3 ../stoichiometry-particle-counts.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


H_COLOR = "#246baa"
O_COLOR = "#c64b39"


def molecule(ax, center, species):
    center = np.asarray(center, dtype=float)
    if species == "H2":
        positions = center + np.array([[-0.21, 0], [0.21, 0]])
        elements = ["H", "H"]
        bonds = [(0, 1)]
    elif species == "O2":
        positions = center + np.array([[-0.27, 0], [0.27, 0]])
        elements = ["O", "O"]
        bonds = [(0, 1)]
    else:
        positions = center + np.array([[0, 0.13], [-0.35, -0.15], [0.35, -0.15]])
        elements = ["O", "H", "H"]
        bonds = [(0, 1), (0, 2)]
    for i, j in bonds:
        ax.plot(positions[[i, j], 0], positions[[i, j], 1], color="#555555", lw=3, zorder=1)
    for pos, element in zip(positions, elements):
        ax.add_patch(Circle(pos, 0.18 if element == "H" else 0.23,
                            facecolor=H_COLOR if element == "H" else O_COLOR,
                            edgecolor="white", lw=1.1, zorder=2))
        ax.text(*pos, element, color="white", fontsize=13, weight="bold",
                ha="center", va="center", zorder=3)


def main():
    # Columns: H2, O2, H2O. Rows: H atoms, O atoms.
    atoms = np.array([[2, 0, 2], [0, 2, 1]], dtype=int)
    initial = np.array([2, 1, 0])
    final = np.array([0, 0, 2])
    np.testing.assert_array_equal(atoms @ initial, atoms @ final)
    np.testing.assert_array_equal(atoms @ initial, [4, 2])
    avogadro_number = 602214076000000000000000
    assert 2 * avogadro_number == 1204428152000000000000000
    plt.rcParams.update({"font.size": 14, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10, 5.6), facecolor="white")
    ax = fig.add_axes([0.035, 0.32, 0.93, 0.50])
    ax.set(xlim=(0, 10), ylim=(-0.65, 1.95), aspect="equal")
    ax.axis("off")
    fig.suptitle("One ratio, two counting scales", fontsize=23, y=0.955)
    molecule(ax, (0.7, 0.9), "H2")
    molecule(ax, (1.95, 0.9), "H2")
    molecule(ax, (4.5, 0.9), "O2")
    molecule(ax, (7.6, 0.9), "H2O")
    molecule(ax, (9.15, 0.9), "H2O")
    ax.text(3.05, 0.9, "+", fontsize=28, ha="center", va="center")
    ax.annotate("", xy=(6.8, 0.9), xytext=(5.65, 0.9),
                arrowprops={"arrowstyle": "->", "lw": 2.5, "color": "#333333"})
    for x, label in [(1.32, "2 H₂ molecules"), (4.5, "1 O₂ molecule"), (8.38, "2 H₂O molecules")]:
        ax.text(x, 0.05, label, ha="center", fontsize=16)
    ax.text(5, -0.47, "Both sides: 4 H atoms + 2 O atoms", ha="center", fontsize=16)
    fig.text(0.5, 0.31, "Multiply every count by the same Avogadro number", ha="center", fontsize=15)
    fig.text(0.5, 0.235, "2 mol H₂   +   1 mol O₂   →   2 mol H₂O", ha="center", fontsize=21, weight="bold")
    fig.text(0.5, 0.15, "1 mol contains exactly 6.02214076 × 10²³ specified entities.", ha="center", fontsize=14)
    fig.text(0.5, 0.055, "Each top drawing is one molecule. Connections and sizes are schematic.",
             ha="center", fontsize=13, color="#555555")
    fig.savefig("stoichiometry-particle-counts.png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified 4 H and 2 O atoms on each side; exact count in two moles.")


if __name__ == "__main__":
    main()
