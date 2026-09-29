"""Draw an exact annulus deformation; write the PNG basename to cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-mpl python ../annulus-deformation-retraction.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    blue, orange, gray = "#16679c", "#b34e16", "#c7c7c7"
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.2), facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.18, top=0.77, wspace=0.2)
    fig.suptitle("The annulus shrinks to its inner circle without crossing the hole", fontsize=16)
    fig.text(0.5, 0.86, r"$H(x,t)=((1-t)+t/\|x\|)x$,     radius $(1-t)\rho+t$",
             ha="center", fontsize=13)
    theta = np.linspace(0, 2 * np.pi, 721)
    rays = np.linspace(0, 2 * np.pi, 12, endpoint=False)
    for ax, t in zip(axes, [0, 0.5, 1]):
        ax.set_aspect("equal")
        ax.set(xlim=(-2.22, 2.22), ylim=(-2.22, 2.22), title=f"t = {t:g}")
        ax.axis("off")
        ax.add_patch(Circle((0, 0), 2, facecolor="#f4f4f4", edgecolor=gray, lw=1))
        ax.add_patch(Circle((0, 0), 1, facecolor="white", edgecolor=gray, lw=1))
        outer = 2 - t
        ax.add_patch(Circle((0, 0), outer, facecolor="#dcecf7", edgecolor=blue, lw=2))
        ax.add_patch(Circle((0, 0), 1, facecolor="white", edgecolor=blue, lw=2.5))
        for angle in rays:
            ax.plot([np.cos(angle), outer * np.cos(angle)],
                    [np.sin(angle), outer * np.sin(angle)], color=blue, lw=0.7, alpha=0.4)
        radius = (1 - t) * 1.5 + t
        ax.plot(radius * np.cos(theta), radius * np.sin(theta), color=orange, lw=2.4, ls="--")
        ax.scatter([0], [outer], s=40, color=blue, zorder=5)
        ax.scatter([0], [1], s=35, color="#222222", zorder=6)
        ax.text(0.12, outer + 0.09, f"{outer:g}", color=blue, fontsize=10)
        ax.text(0, 0, "excluded\nhole", ha="center", va="center", fontsize=10, color="#555555")
        ax.text(0.5, -0.12, f"Tracked loop radius: {radius:g}", transform=ax.transAxes,
                ha="center", color=orange)
    fig.text(0.5, 0.055,
             "Gray: original domain.  Blue: current image.  Orange: tracked loop.  Inner circle fixed at every time.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
