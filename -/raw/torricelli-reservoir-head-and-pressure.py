"""Original Torricelli schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; emit the matching PNG into the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.4, 6.5), dpi=100, facecolor="white")
    fig.suptitle("Torricelli outflow: height becomes kinetic energy", fontsize=19, y=0.96)
    ax = fig.add_axes([0.05, 0.19, 0.55, 0.65])
    ax.set(xlim=(-0.25, 5.5), ylim=(-0.5, 4.15))
    ax.axis("off")
    water = "#d7ebfa"
    ink = "#18374d"
    ax.add_patch(Rectangle((0.6, 0.15), 3.0, 3.05, facecolor=water, edgecolor="none"))
    ax.plot([0.6, 0.6, 3.6], [3.85, 0.15, 0.15], color=ink, lw=3)
    ax.plot([3.6, 3.6], [0.15, 0.60], color=ink, lw=3)
    ax.plot([3.6, 3.6], [0.80, 3.85], color=ink, lw=3)
    ax.plot([0.6, 3.6], [3.2, 3.2], color="#167cb4", lw=2.2)
    ax.plot([0.35, 5.0], [0.7, 0.7], color="#939da5", lw=1, ls="--")
    x = np.linspace(3.6, 5.0, 100)
    centre = 0.7 - 0.25 * (x - 3.6) ** 2
    ax.add_patch(Polygon(np.column_stack((np.r_[x, x[::-1]],
                                         np.r_[centre + 0.065, (centre - 0.065)[::-1]])),
                         closed=True, facecolor="#61b0df", edgecolor="none"))
    ax.annotate("", xy=(3.10, 3.2), xytext=(3.10, 0.7),
                arrowprops={"arrowstyle": "<->", "lw": 1.8, "color": ink})
    ax.text(2.91, 1.95, r"$h=z_s-z_o$", ha="right", va="center", fontsize=15,
            bbox={"facecolor": water, "edgecolor": "none", "pad": 3})
    ax.text(1.95, 3.47, r"Free surface: $p=p_{\rm ambient}$", ha="center")
    ax.text(1.1, 2.6, r"Tank area $A$", color=ink)
    ax.text(1.1, 2.23, r"Surface speed $Q/A\approx0$", color=ink)
    ax.annotate(r"Orifice area $a$", xy=(3.60, 0.70), xytext=(2.65, -0.30),
                ha="center", arrowprops={"arrowstyle": "->", "color": ink})
    ax.text(4.55, 1.36, r"Jet: $p\approx p_{\rm ambient}$", ha="center", fontsize=11)
    ax.annotate("", xy=(4.75, 0.88), xytext=(3.87, 0.88),
                arrowprops={"arrowstyle": "->", "color": ink, "lw": 1.8})
    ax.text(4.27, 1.02, r"$v$", ha="center", fontsize=15)
    ax.text(0.2, 3.2, r"$z_s$", ha="center", va="center")
    ax.text(0.2, 0.7, r"$z_o$", ha="center", va="center")
    note = fig.add_axes([0.65, 0.20, 0.31, 0.63])
    note.axis("off")
    note.text(0, 0.96, "Equal boundary pressures", fontsize=14, weight="bold")
    note.text(0, 0.80, r"$gz_s=\frac{v^2}{2}+gz_o$", fontsize=20)
    note.text(0, 0.65, r"$v=\sqrt{2gh}$", fontsize=24, color="#167cb4")
    note.text(0, 0.44, "Bulk pressure at outlet level", fontsize=14, weight="bold")
    note.text(0, 0.33, r"$p_{\rm bulk}\approx p_{\rm ambient}+\rho gh$", fontsize=14)
    note.text(0, 0.16, "The bulk pressure is not\nthe emerging jet pressure.", linespacing=1.5)
    fig.text(0.5, 0.085, "Ideal, incompressible, lossless, quasi-steady flow; negligible surface tension.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, "Original explanatory schematic — not to scale or experimental data.",
             ha="center", fontsize=11, color="#576570")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
