"""Draw genus accounting for a double sphere cover; run in _media.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The drawing represents cell counts, not an immersion of the covering surface.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


def main():
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig = plt.figure(figsize=(10, 5.5), facecolor="white")
    ax = fig.add_axes((0.02, 0.06, 0.96, 0.83))
    ax.set(xlim=(0, 10), ylim=(0, 5.5))
    ax.axis("off")
    blue, red = "#226b9a", "#b74339"
    fig.suptitle("Double cover with four simple branch values: genus 1", fontsize=17, y=0.97)
    vertices = np.array([[0.65, 1.8], [3.55, 1.8], [2.1, 4.25], [2.1, 2.65]])
    for i in range(4):
        for j in range(i + 1, 4):
            ax.plot(vertices[[i, j], 0], vertices[[i, j], 1], color=blue, lw=2)
    ax.scatter(vertices[:, 0], vertices[:, 1], color=red, s=65, zorder=4)
    for (x, y), label, dx, dy in zip(vertices, [r"$b_1$", r"$b_2$", r"$b_3$", r"$b_4$"], [-0.25, 0.25, 0, 0.3], [-0.28, -0.28, 0.25, 0.07]):
        ax.text(x + dx, y + dy, label, ha="center", color=red, fontsize=14)
    ax.text(2.1, 4.95, "Target sphere Y", ha="center", fontsize=14)
    ax.text(2.1, 1.15, "Tetrahedral triangulation\n3 inner faces + the outer face", ha="center", fontsize=12)
    ax.text(2.1, 0.45, r"$\chi(Y)=4-6+4=2$", ha="center", fontsize=15)
    ax.add_patch(FancyArrowPatch((3.95, 3.7), (5.2, 3.7), arrowstyle="->", mutation_scale=18, lw=2))
    ax.text(4.58, 4.05, "Lift", ha="center")
    ax.text(7.55, 4.95, "Source X: cell counts", ha="center", fontsize=14)
    for x, label in [(5.45, "Cells"), (7.0, "Y"), (9.0, "X")]:
        ax.text(x, 4.35, label, fontsize=13, ha="left" if x == 5.45 else "center", weight="bold")
    rows = [(3.72, "Vertices", "4", "4 × 1 = 4"), (3.15, "Edges", "6", "6 × 2 = 12"), (2.58, "Faces", "4", "4 × 2 = 8")]
    for y, label, base, lift in rows:
        ax.text(5.45, y, label)
        ax.text(7.0, y, base, ha="center")
        ax.text(9.0, y, lift, ha="center", color=red if label == "Vertices" else blue)
    ax.plot([5.3, 9.9], [2.22, 2.22], color="#aaaaaa", lw=1)
    ax.text(7.55, 1.84, r"$e_p=2$ at each of four points", ha="center", color=red, fontsize=13)
    ax.text(7.55, 1.27, r"$\chi(X)=4-12+8=0$", ha="center", fontsize=15)
    ax.text(7.55, 0.7, r"$2-2g_X=0\quad\Longrightarrow\quad g_X=1$", ha="center", fontsize=15)
    fig.text(0.5, 0.02, "Cell-count schematic: the outer face closes the sphere; the source surface is not drawn as an immersion.", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
