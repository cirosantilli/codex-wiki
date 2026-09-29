"""Show three radius-one power series with different boundary convergence.

Green means absolute convergence, orange conditional convergence, and red
divergence. The classifications follow the term, Dirichlet, and p-series
tests, not a finite numerical sample.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

GREEN = "#27835f"
ORANGE = "#d68a20"
RED = "#b83a3a"


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 5.2), dpi=100)
    titles = [r"$\sum_{n=0}^{\infty} z^n$",
              r"$\sum_{n=1}^{\infty} z^n/n$",
              r"$\sum_{n=1}^{\infty} z^n/n^2$"]
    labels = ["Boundary: all divergent",
              "Boundary: conditional,\nexcept divergence at z = 1",
              "Boundary: all absolutely\nconvergent"]
    for ax, title, label, boundary_color in zip(
        axes, titles, labels, [RED, ORANGE, GREEN], strict=True
    ):
        ax.add_patch(Circle((0, 0), 1, facecolor="#e6f2eb", edgecolor=boundary_color,
                            linewidth=4, zorder=2))
        ax.axhline(0, color="#888888", linewidth=0.8, zorder=1)
        ax.axvline(0, color="#888888", linewidth=0.8, zorder=1)
        ax.scatter([1], [0], color=RED if boundary_color != GREEN else GREEN,
                    s=65, edgecolors="white", linewidths=1, zorder=3)
        ax.text(0, 0.15, "Interior:\nabsolute convergence", ha="center",
                va="center", fontsize=10.5, color=GREEN)
        ax.text(1.02, -0.19, "1", ha="center", fontsize=10)
        ax.set_title(title, pad=10)
        ax.text(0.5, -0.23, label, transform=ax.transAxes, ha="center",
                va="top", fontsize=10.5, color=boundary_color)
        ax.set_xlim(-1.24, 1.24)
        ax.set_ylim(-1.24, 1.24)
        ax.set_aspect("equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.set_xlabel("Re z")
    axes[0].set_ylabel("Im z")
    fig.suptitle("The same radius R = 1 does not decide boundary convergence",
                 fontsize=15, y=0.97)
    fig.text(0.5, 0.045,
             "Green: absolute convergence     "
             "Orange: conditional convergence     Red: divergence",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.055, right=0.98, top=0.77, bottom=0.28, wspace=0.23)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
