"""Original comparison of three ordered domains. Output PNG goes to CWD.

Tested with Python 3.14 and matplotlib 3.10; dependencies are in root pyproject.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def interval(ax, left, right, y, color):
    ax.plot([left, right], [y, y], color=color, linewidth=7,
            solid_capstyle="butt")
    ax.scatter([left, right], [y, y], s=62, color=color, zorder=3)


def main():
    fig, ax = plt.subplots(figsize=(8, 3.7), dpi=100, facecolor="white")
    ax.set(xlim=(-1.1, 5.7), ylim=(-0.55, 3.25))
    ax.axis("off")
    blue, orange = "#276586", "#c55c13"
    ax.text(2.1, 3.05, "An endpoint and an order jump are different properties",
            ha="center", fontsize=13, weight="bold", color="#18364c")
    interval(ax, 0, 1, 2.35, blue)
    ax.scatter([0.35, 0.5, 0.65], [2.35] * 3, color="#9bc6dc", s=18, zorder=4)
    ax.text(-1.03, 2.35, r"$[0,1]$", va="center", fontsize=13)
    ax.text(3.35, 2.35, "Minimum: yes\nAdjacent pair: no", va="center", fontsize=11)
    interval(ax, 0, 1, 1.2, blue)
    interval(ax, 2, 3, 1.2, blue)
    ax.scatter([1, 2], [1.2, 1.2], s=75, color=orange, zorder=4)
    ax.annotate("", xy=(1.98, 1.55), xytext=(1.02, 1.55),
                arrowprops={"arrowstyle": "<->", "linestyle": ":", "color": orange,
                            "linewidth": 2})
    ax.text(1.5, 1.76, "No domain points here", ha="center", fontsize=10, color=orange)
    ax.text(-1.03, 1.2, r"$[0,1]\cup[2,3]$", va="center", fontsize=11)
    ax.text(3.35, 1.2, "Minimum: yes\nAdjacent pair: yes", va="center", fontsize=11)
    xs = [-0.4, 0.4, 1.2, 2.0, 2.8]
    ax.plot([-0.8, 3.2], [0, 0], color="#9eb0bb", linewidth=1.3)
    ax.scatter(xs, [0] * len(xs), color=blue, s=48, zorder=3)
    ax.text(-0.89, 0, "…", ha="center", va="center", fontsize=16)
    ax.text(3.27, 0, "…", ha="center", va="center", fontsize=16)
    ax.text(-1.03, 0.36, r"$\mathbb{Z}$", fontsize=13)
    for x, label in zip(xs, ["−2", "−1", "0", "1", "2"]):
        ax.text(x, -0.28, label, ha="center", fontsize=10)
    ax.text(3.65, 0, "Minimum: no\nAdjacent pair: yes", va="center", fontsize=11)
    for x, label in [(0, "0"), (1, "1")]:
        ax.text(x, 2.10, label, ha="center", fontsize=10)
    for x, label in [(0, "0"), (1, "1"), (2, "2"), (3, "3")]:
        ax.text(x, 0.94, label, ha="center", fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.99, bottom=0.05, top=0.98)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white",
                transparent=False, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
