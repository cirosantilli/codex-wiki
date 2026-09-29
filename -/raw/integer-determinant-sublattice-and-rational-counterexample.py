"""Contrast an index-two integer image with an area-one rational lattice."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.3), dpi=100, layout="constrained")
    fig.set_facecolor("white")
    reference = np.array([(x, y) for x in range(-3, 6) for y in range(-2, 4)])
    pairs = (np.diag([2., 1.]), np.diag([2., .5]))
    titles = ("Integer matrix diag(2, 1): index 2", "Rational matrix diag(2, ½): area 1")
    for ax, matrix, title in zip(axes, pairs, titles):
        ax.scatter(reference[:, 0], reference[:, 1], s=75, facecolors="none", edgecolors="#b6bdc0", linewidths=1.0, label="Reference integer points")
        raw = np.array([(a, b) for a in range(-3, 4) for b in range(-5, 8)])
        image = raw @ matrix.T
        ax.scatter(image[:, 0], image[:, 1], s=22, color="#1f77b4", label="Image of integer points")
        b1, b2 = matrix[:, 0], matrix[:, 1]
        ax.add_patch(Polygon([[0, 0], b1, b1+b2, b2], facecolor="#7caed0", edgecolor="#13547c", linewidth=2, alpha=.32))
        for vector in [b1, b2]:ax.annotate("", xy=vector, xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": "#13547c", "lw": 2.2})
        ax.set(xlim=(-2.55, 4.55), ylim=(-1.55, 3.35), xlabel="x", ylabel="y", title=title)
        ax.set_xticks(range(-2, 5)); ax.set_yticks(np.arange(-1, 3.5, .5) if matrix[1,1] == .5 else range(-1,4))
        ax.set_aspect("equal", adjustable="box");ax.grid(alpha=.15);ax.legend(loc="upper right", fontsize=10)
    axes[0].annotate("Odd x is missing", (1,1), xytext=(.3,2.45), arrowprops={"arrowstyle":"->","color":"#a94729"}, color="#a94729",fontsize=11)
    axes[1].annotate("(0, 1) maps to (0, ½)", (0,.5), xytext=(.65,-1.0), arrowprops={"arrowstyle":"->","color":"#a94729"}, color="#a94729",fontsize=11)
    fig.suptitle("Determinant ±1 needs integer entries to preserve integer coordinates",fontsize=15)
    fig.savefig(Path(__file__).with_suffix(".png").name,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
