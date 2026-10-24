"""Oxford 2015 graphics Q1: nearest pixels and an exact midpoint tie.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run in the desired output directory; writes graphics-2015-midpoint-line.png.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    xs = np.arange(1, 10)
    ys = 1 + (6 * (xs - 1) + 8) // 16
    fig, ax = plt.subplots(figsize=(8.4, 4.2), dpi=130, facecolor="white")
    ax.set_facecolor("white")
    for x, y in zip(xs, ys):
        ax.add_patch(Rectangle((x - .5, y - .5), 1, 1,
                               facecolor="#d8eafa", edgecolor="#94b6d5", lw=.8))
    ax.plot([1, 9], [1, 4], color="#185783", lw=2, label="Exact line: y = 1 + 3(x − 1)/8")
    ax.scatter(xs, ys, s=38, color="#185783", zorder=4, label="Chosen pixel centres")
    ax.scatter([5], [2], s=50, facecolors="white", edgecolors="#b24d24", zorder=5)
    ax.scatter([5], [2.5], s=60, marker="x", color="#b24d24", zorder=5)
    ax.annotate("Midpoint tie at (5, 2.5)\nChoose upper pixel (5, 3)",
                xy=(5, 2.5), xytext=(5.75, 1.15), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#b24d24"}, color="#8b3514")
    ax.set(xlim=(.4, 9.6), ylim=(.4, 4.65), xlabel="x (pixel column)",
           ylabel="y (pixel row)", title="Integer decisions reproduce nearest pixels, including ties")
    ax.set_xticks(range(1, 10))
    ax.set_yticks(range(1, 5))
    ax.set_aspect("equal")
    ax.grid(alpha=.2)
    ax.legend(loc="upper left", fontsize=9, framealpha=1)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "graphics-2015-midpoint-line.png", facecolor="white",
                metadata={"Software": "Oxford 2015 graphics figure generator"})
    plt.close(fig)


if __name__ == "__main__":
    main()
