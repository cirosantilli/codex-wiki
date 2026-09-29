"""C_n simple-root diagram; Python 3.14 and the root Matplotlib dependency.

Write an opaque basename PNG into CWD; the caller sets MPLCONFIGDIR.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def main():
    fig, ax = plt.subplots(figsize=(8, 2.35), dpi=100, facecolor="white")
    nodes = [0, 1.4, 4.4, 6.2]
    ax.plot([0, 1.4], [0, 0], color="#252525", linewidth=2)
    ax.plot([1.4, 2.45], [0, 0], color="#252525", linewidth=2)
    ax.plot([3.35, 4.4], [0, 0], color="#252525", linewidth=2)
    ax.text(2.9, 0, r"$\cdots$", ha="center", va="center", fontsize=21)
    for y in [-0.085, 0.085]:
        ax.plot([4.4, 6.2], [y, y], color="#252525", linewidth=2)
    ax.add_patch(Polygon([[5.02, 0], [5.31, 0.20], [5.31, -0.20]],
                         closed=True, facecolor="#176a9a", edgecolor="#176a9a"))
    ax.scatter(nodes, [0] * 4, s=290, facecolors="white", edgecolors="#252525",
               linewidths=2, zorder=5)
    for x, label in zip(nodes, [r"$\alpha_1$", r"$\alpha_2$", r"$\alpha_{n-1}$", r"$\alpha_n$"]):
        ax.text(x, -0.33, label, ha="center", va="center", fontsize=17)
    ax.text(4.4, -0.69, "short", ha="center", fontsize=12, color="#176a9a")
    ax.text(6.2, -0.69, "long", ha="center", fontsize=12, color="#176a9a")
    ax.set_title(r"$C_n$: the double-bond arrow points toward the short root", fontsize=14, pad=14)
    ax.set_xlim(-0.55, 6.75)
    ax.set_ylim(-0.9, 0.5)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
