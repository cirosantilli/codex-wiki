"""Illustrate coefficient-dependent homology and coefficient-independent Euler characteristic."""
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    fig = plt.figure(figsize=(10, 5.4), dpi=120, facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.1, 1])
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(-0.4, 4.4), ylim=(-0.4, 2.7))
    ax.axis("off")
    for x, label in zip([0, 2, 4], [r"$C_2$", r"$C_1$", r"$C_0$"]):
        ax.text(x, 2.35, label, ha="center", fontsize=14)
    for y, field, maps in [(1.5, r"$\mathbb{Q}$", ["×2", "0"]), (0.25, r"$\mathbb{F}_2$", ["0", "0"])]:
        for x in [0, 2, 4]:
            ax.text(x, y, field, ha="center", va="center", fontsize=17, bbox={"boxstyle": "round,pad=0.35", "facecolor": "#e6eef6", "edgecolor": "#3679b3"})
        for a, b, label in zip([0.3, 2.3], [1.7, 3.7], maps):
            ax.annotate("", xy=(b, y), xytext=(a, y), arrowprops={"arrowstyle": "->", "lw": 1.7})
            ax.text((a + b) / 2, y + 0.2, label, ha="center", fontsize=13)
    for col, (field, betti) in enumerate([(r"$\mathbb{Q}$", [1, 0, 0]), (r"$\mathbb{F}_2$", [1, 1, 1])]):
        assert betti[0] - betti[1] + betti[2] == 1
        ax = fig.add_subplot(grid[1, col])
        ax.bar(range(3), betti, color=["#3679b3", "#b95745", "#3679b3"], width=0.55)
        ax.set(xticks=range(3), xticklabels=[r"$b_0$ (+)", r"$b_1$ (−)", r"$b_2$ (+)"], ylim=(0, 1.4), yticks=[0, 1], ylabel="Homology dimension")
        for i, b in enumerate(betti):
            ax.text(i, b + 0.05, str(b), ha="center", fontsize=12)
        ax.set_title(field + (r": $\chi=1-0+0=1$" if col == 0 else r": $\chi=1-1+1=1$"), fontsize=13)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(r"$\mathbb{RP}^{2}$: the boundary map changes, the alternating sum does not", fontsize=14)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
