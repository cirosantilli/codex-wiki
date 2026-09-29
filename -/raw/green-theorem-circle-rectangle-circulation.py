"""Compare Green's theorem on two boundaries for F=(-2y, 3x).

Run from _media; requires Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np


BLUE = "#175a9e"
FIELD = "#718477"


def arrow(ax, start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                mutation_scale=17, linewidth=2.3, color=BLUE))


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), dpi=120)
    fig.suptitle(r"Green's theorem: $F=(-2y,3x)$, scalar curl $=5$", fontsize=17)
    for ax in axes:
        ax.set_aspect("equal")
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xlabel("x")
        ax.set_ylabel("y", rotation=0, labelpad=10)
        ax.grid(alpha=0.15)

    ax = axes[0]
    ax.add_patch(Circle((0, 0), 2, facecolor="#e9f3fb", edgecolor=BLUE, lw=2))
    x, y = np.meshgrid(np.linspace(-1.8, 1.8, 9), np.linspace(-1.8, 1.8, 9))
    mask = (x*x+y*y < 3.7) & (x*x+y*y > 0.1)
    ax.quiver(x[mask], y[mask], -2*y[mask], 3*x[mask], color=FIELD,
              angles="xy", scale_units="xy", scale=14, width=0.005)
    for t in [0.1, 1.7, 3.3, 4.9]:
        ts = np.linspace(t, t+0.4, 30)
        ax.plot(2*np.cos(ts), 2*np.sin(ts), color=BLUE, lw=2.5)
        arrow(ax, (2*np.cos(ts[-2]), 2*np.sin(ts[-2])),
              (2*np.cos(ts[-1]), 2*np.sin(ts[-1])))
    ax.set(xlim=(-2.55, 2.55), ylim=(-2.55, 2.55), xticks=[-2, 0, 2], yticks=[-2, 0, 2])
    ax.set_title(r"Radius 2: area $4\pi$", pad=13)
    ax.text(0.5, -0.22, r"Counterclockwise integral $=20\pi$",
            transform=ax.transAxes, ha="center", color=BLUE, fontsize=13)

    ax = axes[1]
    ax.add_patch(Rectangle((0, 0), 3, 2, facecolor="#e9f3fb", edgecolor=BLUE, lw=2))
    x, y = np.meshgrid(np.linspace(0.25, 2.75, 8), np.linspace(0.25, 1.75, 5))
    ax.quiver(x, y, -2*y, 3*x, color=FIELD, angles="xy",
              scale_units="xy", scale=21, width=0.005)
    for a, b in [((1.1, 0), (1.9, 0)), ((3, 0.65), (3, 1.35)),
                 ((1.9, 2), (1.1, 2)), ((0, 1.35), (0, 0.65))]:
        arrow(ax, a, b)
    for x0, y0, label in [(1.5, -0.28, "bottom: 0"), (3.23, 1, "right: 18"),
                          (1.5, 2.28, "top: 12"), (-0.24, 1, "left: 0")]:
        ax.text(x0, y0, label, ha="center" if y0 != 1 else ("left" if x0 > 3 else "right"),
                va="center", fontsize=11, color=BLUE)
    ax.set(xlim=(-1.05, 4.05), ylim=(-1.4, 3.7), xticks=[0, 1, 2, 3], yticks=[0, 1, 2])
    ax.set_title(r"$[0,3]\times[0,2]$: area $6$", pad=13)
    ax.text(0.5, -0.22, r"$0+18+12+0=30=5\times6$",
            transform=ax.transAxes, ha="center", color=BLUE, fontsize=13)
    fig.subplots_adjust(left=0.07, right=0.96, bottom=0.23, top=0.8, wspace=0.28)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
