"""Schematic donor/acceptor roles for two water molecules.

Output matching PNG to CWD. Not a measured water-dimer structure.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def atom(ax, point, label):
    oxygen = label == "O"
    ax.add_patch(Circle(point, 0.17 if oxygen else 0.13,
                        facecolor="#bf4244" if oxygen else "#f3f5f7",
                        edgecolor="#9a3235" if oxygen else "#8b98a3",
                        linewidth=1.2, zorder=4))
    ax.text(*point, label, ha="center", va="center", weight="bold",
            color="white" if oxygen else "#334451", zorder=5, fontsize=12)


def main():
    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(11.4, 5.1), dpi=100, facecolor="white")
    fig.subplots_adjust(left=0.045, right=0.965, bottom=0.18, top=0.83)
    donor = np.array([0.0, 0.0])
    acceptor = np.array([2.3, 0.0])
    angle = np.deg2rad(104.5)
    donor_h = [np.array([0.9, 0]), 0.9*np.array([np.cos(angle), np.sin(angle)])]
    acceptor_h = [
        acceptor+0.9*np.array([np.cos(angle/2), np.sin(angle/2)]),
        acceptor+0.9*np.array([np.cos(angle/2), -np.sin(angle/2)]),
    ]
    for oxygen, hydrogens in [(donor, donor_h), (acceptor, acceptor_h)]:
        for hydrogen in hydrogens:
            ax.plot([oxygen[0], hydrogen[0]], [oxygen[1], hydrogen[1]],
                    color="#526472", linewidth=3, zorder=1)
        atom(ax, oxygen, "O")
        for hydrogen in hydrogens:
            atom(ax, hydrogen, "H")
    ax.plot([donor_h[0][0], acceptor[0]], [0, 0], color="#b77b2b",
            linestyle=(0, (2, 3)), linewidth=2.7, zorder=1)
    for oxygen, offsets in [
        (donor, [(-0.28, -0.23), (0.15, -0.32)]),
        (acceptor, [(-0.32, 0.28), (-0.32, -0.28)]),
    ]:
        for dx, dy in offsets:
            ax.scatter([oxygen[0]+dx-0.025, oxygen[0]+dx+0.025],
                       [oxygen[1]+dy, oxygen[1]+dy], s=15,
                       c="#536b96", zorder=6)
    ax.text(0.0, 1.32, "Donor molecule\nO–H supplies the hydrogen",
            ha="center", fontsize=12, linespacing=1.5, color="#334d70")
    ax.text(2.3, 1.32, "Acceptor molecule\nO supplies the accepting site",
            ha="center", fontsize=12, linespacing=1.5, color="#334d70")
    ax.annotate("Covalent O–H bond", xy=(0.43, 0), xytext=(0.08, -0.65),
                ha="center", color="#526472",
                arrowprops={"arrowstyle": "->", "color": "#526472"})
    ax.annotate("Hydrogen bond H···O", xy=(1.58, 0), xytext=(1.62, -0.65),
                ha="center", color="#966521",
                arrowprops={"arrowstyle": "->", "color": "#966521"})
    ax.set(xlim=(-0.75, 3.35), ylim=(-0.95, 1.7), aspect="equal")
    ax.axis("off")
    fig.suptitle("One association, two roles: hydrogen-bond donor and acceptor",
                 fontsize=16, y=0.96)
    fig.text(0.5, 0.065,
             "Schematic single pair, not a measured dimer geometry. Both molecules keep their covalent O–H bonds.\n"
             "Blue dot pairs are Lewis bookkeeping; they do not specify fixed electron positions.",
             ha="center", fontsize=11, linespacing=1.5, color="#444")
    fig.savefig(Path.cwd() / "water-hydrogen-bond-roles.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
