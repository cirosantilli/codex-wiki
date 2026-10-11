"""Original Q12 contour plot; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    grid = np.linspace(0, 2, 601)
    x, y = np.meshgrid(grid, grid)
    g = 4*x*x+4*y*y+x**4-6*x*x*y*y+y**4
    fig, ax = plt.subplots(figsize=(5.9, 5.2), layout="constrained")
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    contours = ax.contour(x, y, g, levels=[-24, -8, 0, 1, 2, 3, 6, 12, 24], cmap="viridis", linewidths=1.2)
    ax.clabel(contours, fmt="%g", fontsize=9)
    critical = ax.contour(x, y, g, levels=[4], colors=["#b34332"], linewidths=2)
    ax.clabel(critical, fmt="%g", fontsize=10)
    ax.scatter(1, 1, marker="x", color="#b34332", s=70, linewidth=2.2, zorder=5)
    ax.scatter(0, 0, color="#24764f", s=45, clip_on=False, zorder=5)
    ax.annotate("Saddle (1, 1)", (1, 1), xytext=(1.22, 0.72), arrowprops={"arrowstyle": "->", "color": "#b34332"}, fontsize=9, color="#9c3324")
    ax.text(0.07, 0.08, "Minimum", fontsize=9, color="#24764f")
    ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="$x$", ylabel="$y$", title=r"$g=4x^2+4y^2+x^4-6x^2y^2+y^4$")
    ax.set_aspect("equal")
    ax.grid(alpha=0.12)
    fig.savefig(Path("paper-1-quartic-contours.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
