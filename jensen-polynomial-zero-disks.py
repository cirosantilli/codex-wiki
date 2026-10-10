"""Plot Jensen zero geometry; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media; the opaque PNG is written to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    radii = (0.2, 0.4, 0.75)
    roots = np.array([0.25, -0.5])
    colors = ("#2878a6", "#c47a13", "#448655")
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.6), sharex=True, sharey=True)
    fig.suptitle(r"Zeros of $f(z)=3(z-1/4)(z+1/2)$", fontsize=15, y=0.99)
    for ax, radius, color in zip(axes, radii, colors):
        count = int(np.count_nonzero(np.abs(roots) < radius))
        ax.add_patch(Circle((0, 0), radius, edgecolor=color,
                            facecolor=color, alpha=0.12, linewidth=0))
        ax.add_patch(Circle((0, 0), radius, edgecolor=color,
                            facecolor="none", linewidth=2))
        ax.axhline(0, color="#aaaaaa", linewidth=0.8, zorder=0)
        ax.axvline(0, color="#aaaaaa", linewidth=0.8, zorder=0)
        ax.scatter(roots, np.zeros(2), marker="x", s=90,
                   color="#9c2436", linewidths=2, zorder=3)
        ax.scatter([0], [0], s=16, color="#333333", zorder=3)
        ax.annotate(r"$-1/2$", (-0.5, 0), xytext=(0, -22),
                    textcoords="offset points", ha="center", fontsize=11)
        ax.annotate(r"$1/4$", (0.25, 0), xytext=(0, 10),
                    textcoords="offset points", ha="center", fontsize=11)
        ax.set_title(f"R = {radius:g}   |   {count} interior zero"
                     + ("s" if count != 1 else ""), fontsize=11, color=color)
        ax.set_aspect("equal")
        ax.set_xlim(-0.85, 0.85)
        ax.set_ylim(-0.85, 0.85)
        ax.set_xticks([-0.5, 0, 0.5])
        ax.set_yticks([-0.5, 0, 0.5])
        ax.set_xlabel("Re z")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Im z")
    fig.text(0.5, 0.025, "Each marked zero is simple; all three boundary circles avoid the zeros.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.99, top=0.81, bottom=0.2, wspace=0.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
