"""Show induced boundary orientation and cut cancellation on an annulus.

Run from _media; requires Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Wedge
import numpy as np


OUTER = "#175a9e"
INNER = "#bb4e12"


def arrow(ax, start, end, color):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", color=color,
                                mutation_scale=17, linewidth=2.2, zorder=5))


def boundary(ax):
    for radius, direction, color in [(2, 1, OUTER), (1, -1, INNER)]:
        ax.add_patch(Circle((0, 0), radius, fill=False, edgecolor=color, lw=2.2))
        for t in [0.6, 2.2, 3.8, 5.4]:
            ts = np.linspace(t, t+direction*0.45, 30)
            ax.plot(radius*np.cos(ts), radius*np.sin(ts), color=color, lw=2.3)
            arrow(ax, (radius*np.cos(ts[-2]), radius*np.sin(ts[-2])),
                  (radius*np.cos(ts[-1]), radius*np.sin(ts[-1])), color)
    ax.plot(0, 0, "x", color="#a52727", ms=8, mew=2)
    ax.text(0, -0.27, "origin excluded", ha="center", color="#a52727", fontsize=11)
    ax.set(aspect="equal", xlim=(-2.65, 2.65), ylim=(-2.6, 2.6))
    ax.axis("off")


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.1), dpi=120)
    fig.suptitle(r"$G=(-y,x)/(x^2+y^2)$: zero curl throughout the annulus", fontsize=17)
    ax = axes[0]
    ax.add_patch(Wedge((0, 0), 2, 0, 360, width=1, facecolor="#e9f3fb"))
    gx, gy = np.meshgrid(np.linspace(-1.8, 1.8, 11), np.linspace(-1.8, 1.8, 11))
    r2 = gx*gx+gy*gy
    mask = (r2 > 1.15) & (r2 < 3.7)
    ax.quiver(gx[mask], gy[mask], -gy[mask]/r2[mask], gx[mask]/r2[mask],
              color="#768477", angles="xy", scale_units="xy", scale=2.7, width=0.006)
    boundary(ax)
    ax.set_title("Keep the annulus on the left", fontsize=14)
    ax.text(0.5, -0.04, r"Outer CCW: $+2\pi$     Inner CW: $-2\pi$",
            ha="center", transform=ax.transAxes, fontsize=12)
    ax.text(0.5, -0.14, r"Complete boundary: $2\pi-2\pi=0$",
            ha="center", transform=ax.transAxes, fontsize=13)

    ax = axes[1]
    ax.add_patch(Wedge((0, 0), 2, 0, 180, width=1, facecolor="#e9f3fb"))
    ax.add_patch(Wedge((0, 0), 2, 180, 360, width=1, facecolor="#fff0df"))
    boundary(ax)
    for sign in [-1, 1]:
        ax.plot([sign, 2*sign], [0, 0], color="#666666", lw=1, ls="--")
    # The upper piece goes right on its right cut and left on its left cut;
    # the lower piece goes in the opposite direction on each shared cut.
    for a, b, y in [(1.1, 1.9, 0.06), (1.9, 1.1, -0.06),
                     (-1.1, -1.9, 0.06), (-1.9, -1.1, -0.06)]:
        arrow(ax, (a, y), (b, y), "#333333")
    ax.text(0, 1.48, "upper piece", ha="center", fontsize=11)
    ax.text(0, -1.48, "lower piece", ha="center", fontsize=11)
    ax.set_title("Two cuts give two simple boundaries", fontsize=14)
    ax.text(0.5, -0.04, "Opposite directions on each shared cut",
            ha="center", transform=ax.transAxes, fontsize=12)
    ax.text(0.5, -0.14, "Cut integrals cancel when the pieces are added",
            ha="center", transform=ax.transAxes, fontsize=12)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.8, bottom=0.2, wspace=0.08)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
