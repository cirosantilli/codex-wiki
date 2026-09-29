"""Draw midpoint rectangles and trapezoids for x² on [0, 1].

Run from _media. Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
import numpy as np


def main():
    n = 4
    nodes = np.linspace(0, 1, n + 1)
    midpoints = (nodes[:-1] + nodes[1:]) / 2
    h = 1 / n
    midpoint = h * np.sum(midpoints**2)
    trapezoid = h * (np.sum(nodes[1:-1]**2) + nodes[-1]**2 / 2)
    assert midpoint == 21 / 64
    assert trapezoid == 11 / 32
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.6), layout="constrained")
    fig.set_facecolor("white")
    curve = np.linspace(0, 1, 401)
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(0, 1), ylim=(0, 1.08), xlabel="$x$", ylabel="Height")
        ax.set_xticks(nodes)
        ax.spines[["top", "right"]].set_visible(False)
        ax.plot(curve, curve**2, color="#20252c", lw=2.3, label="$f(x)=x^2$", zorder=4)
        ax.grid(axis="y", color="#e4e7eb", zorder=0)
    for left, center in zip(nodes[:-1], midpoints):
        axes[0].add_patch(Rectangle((left, 0), h, center**2, facecolor="#d6eafa", edgecolor="#236aa0", lw=1.5, zorder=2))
    axes[0].scatter(midpoints, midpoints**2, color="#236aa0", s=35, zorder=5, label="Midpoint samples")
    for left, right in zip(nodes[:-1], nodes[1:]):
        axes[1].add_patch(Polygon([(left, 0), (left, left**2), (right, right**2), (right, 0)], facecolor="#fce4c9", edgecolor="#b75a16", lw=1.5, zorder=2))
    axes[1].scatter(nodes, nodes**2, color="#b75a16", s=35, zorder=5, label="Endpoint samples")
    axes[0].set_title("Midpoint rectangles: four panels\n$M_4=21/64$,  $M_4-I=-1/192$", fontsize=12)
    axes[1].set_title("Trapezoids: four panels\n$T_4=11/32$,  $T_4-I=+1/96$", fontsize=12)
    for ax in axes:
        ax.legend(loc="upper left", frameon=True, facecolor="white", framealpha=1)
    fig.suptitle(r"Approximating the exact area $I=\int_0^1 x^2\,dx=1/3$", fontsize=15)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
