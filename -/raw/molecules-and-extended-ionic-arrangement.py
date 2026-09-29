"""Original teaching cartoon; run from _media with Python 3.14 / matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def atom(ax, x, y, text, color, radius=0.24):
    ax.add_patch(Circle((x, y), radius, facecolor=color, edgecolor="#253348", lw=1.5, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=12, zorder=4)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), dpi=120, facecolor="white")
    for ax in axes:
        ax.set(xlim=(0, 5), ylim=(0, 4.5), aspect="equal")
        ax.axis("off")
    left, right = axes
    left.set_title("Discrete neutral molecules", fontsize=15, pad=14)
    groups = [([(0.75, 3.15, "H", "#e8edf3"), (1.4, 3.5, "O", "#f3ada9"), (2.05, 3.15, "H", "#e8edf3")], [(0, 1), (1, 2)], r"H$_2$O: 3 atoms"),
              ([(3.1, 2.65, "O", "#f3ada9"), (3.85, 2.65, "O", "#f3ada9")], [(0, 1)], r"O$_2$: 2 atoms"),
              ([(0.95, 1.25, "O", "#f3ada9"), (1.75, 1.25, "C", "#b7c9df"), (2.55, 1.25, "O", "#f3ada9")], [(0, 1), (1, 2)], r"CO$_2$: 3 atoms")]
    for pts, bonds, label in groups:
        for a, b in bonds:
            left.plot([pts[a][0], pts[b][0]], [pts[a][1], pts[b][1]], color="#465166", lw=3)
        for x, y, name, color in pts:
            atom(left, x, y, name, color)
        cx = sum(p[0] for p in pts) / len(pts)
        cy = min(p[1] for p in pts) - 0.55
        left.text(cx, cy, label, ha="center", fontsize=12)
    left.text(2.5, 0.05, "Each connected group is one molecule", ha="center", fontsize=11)
    right.set_title("Extended ionic crystal", fontsize=15, pad=14)
    positions = [(i, j) for i in range(4) for j in range(4)]
    for i, j in positions:
        x, y = 0.85 + i, 0.95 + 0.85 * j
        # Dotted neighbor guides express continuation, not localized covalent bonds.
        right.plot([x - 0.5, x + 0.5], [y, y], ":", color="#c2cad3", lw=1, zorder=1)
        right.plot([x, x], [y - 0.425, y + 0.425], ":", color="#c2cad3", lw=1, zorder=1)
        positive = (i + j) % 2 == 0
        atom(right, x, y, "Na+" if positive else "Cl−", "#f6d48f" if positive else "#afe0c6", 0.31)
    right.add_patch(FancyBboxPatch((0.47, 0.56), 1.76, 0.78, boxstyle="round,pad=0.02", fill=False, edgecolor="#8057a0", lw=2))
    right.text(2.5, 0.08, "NaCl formula unit: a 1:1 count\nBox selects a count, not an isolated molecule", ha="center", fontsize=11)
    fig.text(0.5, 0.025, "Original cartoons • positions, sizes and lines are schematic • ionic panel is a 2D patch, not full 3D geometry", ha="center", fontsize=10, color="#465166")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.85, bottom=0.15, wspace=0.09)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
