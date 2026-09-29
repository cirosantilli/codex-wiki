"""Illustrate a fixed cylinder and moving unit sequences (Python 3.14)."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    plt.rcParams.update({"font.size": 12})
    fig = plt.figure(figsize=(11.2, 6.6), facecolor="white")
    ax = fig.add_axes((0.08, 0.30, 0.72, 0.47))
    ax.set(xlim=(0.5, 9.4), ylim=(8.5, 0.05))
    ax.set_xticks(range(1, 9), [str(j) for j in range(1, 9)])
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position("top")
    ax.set_xlabel("Coordinate j", labelpad=8)
    ax.set_yticks(range(1, 9), [rf"$e_{n}$" for n in range(1, 9)])
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for j in (1, 3):
        ax.add_patch(Rectangle((j - 0.48, 0.55), 0.96, 7.9,
                               facecolor="#e4f0f8", edgecolor="#2878a3", lw=1.2))
    for n in range(1, 9):
        for j in range(1, 9):
            if j == n:
                ax.scatter([j], [n], s=390, color="#c36d24", zorder=2)
            ax.text(j, n, str(int(j == n)), ha="center", va="center",
                    color="white" if j == n else "#46515b", zorder=3)
        ax.text(8.8, n, "…", ha="center", va="center")
        ax.text(9.45, n, "outside B" if n in (1, 3) else "inside B",
                color="#b25328" if n in (1, 3) else "#237153", va="center")
    fig.suptitle("A fixed finite observation misses a sufficiently late unit entry", y=0.97)
    fig.text(0.5, 0.885,
             r"$B=\{x\in\mathbb{R}^{\mathbb{N}}: |x_1|<1/2,\ |x_3|<1/2\}$",
             ha="center", fontsize=14)
    fig.text(0.5, 0.23, "Blue columns: tested. All other coordinates: unrestricted, including the entire tail.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.17, r"This cylinder contains every $e_n$ for $n>3$ (and also $e_2$).",
             ha="center", fontsize=12)
    fig.text(0.5, 0.105, r"Every finite $F$: $n>\max(F\cup\{0\})$ puts $e_n$ in each cylinder about zero testing $F$.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.045, r"Yet $\|e_n\|_\infty=1$, and the box $\prod_{j\geq1}(-1/2,1/2)$ excludes every $e_n$.",
             ha="center", fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
