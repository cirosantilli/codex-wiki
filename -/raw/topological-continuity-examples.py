"""Original topology examples; run from _media to write the PNG to cwd.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    blue, orange = "#186aa6", "#bd4a18"
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.2), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, top=0.91, bottom=0.09,
                        hspace=0.62, wspace=0.34)
    fig.suptitle("Topology: maps and the effect of removing a point", fontsize=17)

    ax = axes[0, 0]
    x = np.linspace(0.02, 0.98, 1000)
    ax.plot(x, np.tan(np.pi * (x - 0.5)), color=blue, lw=2.5)
    ax.scatter([0.25, 0.5, 0.75], [-1, 0, 1], color=orange, zorder=4)
    ax.axhline(0, color="#aaaaaa", lw=0.8)
    ax.axvline(0, color="#888888", ls="--", lw=1)
    ax.axvline(1, color="#888888", ls="--", lw=1)
    ax.set(xlim=(-0.03, 1.03), ylim=(-4, 4), xlabel=r"$x\in(0,1)$",
           ylabel=r"$f(x)\in\mathbb{R}$",
           title=r"Homeomorphism: $f(x)=\tan(\pi(x-1/2))$")
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1], ["0", "1/4", "1/2", "3/4", "1"])
    ax.text(0.04, 0.95, "Dashed boundaries are excluded", transform=ax.transAxes,
            va="top", fontsize=10)

    ax = axes[0, 1]
    x = np.linspace(-2.3, 2.3, 700)
    ax.axhspan(1, 4, color="#e7f1fa", zorder=0)
    ax.plot(x, x**2, color=blue, lw=2.5)
    for a, b in [(-2, -1), (1, 2)]:
        ax.plot([a, b], [0, 0], color=orange, lw=5, solid_capstyle="butt")
    ax.scatter([-2, -1, 1, 2], [0]*4, facecolors="white", edgecolors=orange,
               s=65, lw=1.8, zorder=5)
    ax.axhline(1, color=blue, lw=0.8, ls="--")
    ax.axhline(4, color=blue, lw=0.8, ls="--")
    ax.text(0, 2.5, r"target $(1,4)$", ha="center", fontsize=11)
    ax.set(xlim=(-2.4, 2.4), ylim=(-0.5, 5.4), xlabel=r"$x$", ylabel=r"$f(x)$",
           title=r"Continuity uses inverse images: $f(x)=x^2$")
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.text(0.5, -0.31, r"$f^{-1}((1,4))=(-2,-1)\cup(1,2)$",
            transform=ax.transAxes, ha="center", fontsize=12)

    ax = axes[1, 0]
    theta = np.linspace(0, 2*np.pi, 900)
    ax.plot(np.cos(theta), np.sin(theta), color=blue, lw=4)
    ax.scatter([1], [0], s=105, facecolors="white", edgecolors=orange,
               lw=2, zorder=5)
    ax.annotate("removed point", xy=(1.02, 0.03), xytext=(0.25, 1.12),
                arrowprops={"arrowstyle": "->", "color": orange}, color=orange,
                fontsize=11)
    ax.set_aspect("equal")
    ax.set(xlim=(-1.45, 1.45), ylim=(-1.25, 1.45),
           title=r"$S^1\setminus\{p\}$: one connected component")
    ax.axis("off")
    ax.text(0.5, -0.12, "This holds for every point p on the circle.",
            transform=ax.transAxes, ha="center", fontsize=11)

    ax = axes[1, 1]
    ax.plot([0, 0.5], [0, 0], color=blue, lw=5, solid_capstyle="butt")
    ax.plot([0.5, 1], [0, 0], color=orange, lw=5, solid_capstyle="butt")
    ax.scatter([0, 1], [0, 0], s=65, c=[blue, orange], zorder=4)
    ax.scatter([0.5], [0], s=115, facecolors="white", edgecolors="#333333",
               lw=2, zorder=5)
    for xpos, label in [(0, "0"), (0.5, "1/2"), (1, "1")]:
        ax.text(xpos, -0.22, label, ha="center")
    ax.text(0.25, 0.25, r"$[0,1/2)$", ha="center", color=blue, fontsize=14)
    ax.text(0.75, 0.25, r"$(1/2,1]$", ha="center", color=orange, fontsize=14)
    ax.set(xlim=(-0.1, 1.1), ylim=(-0.85, 0.85),
           title=r"$[0,1]\setminus\{1/2\}$: two connected components")
    ax.axis("off")
    ax.text(0.5, -0.12, "Choose an interior point; deleting an endpoint differs.",
            transform=ax.transAxes, ha="center", fontsize=11)

    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
