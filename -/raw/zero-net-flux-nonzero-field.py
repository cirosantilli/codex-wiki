#!/usr/bin/env python3
"""Original y=0 section of a 3D Coulomb dipole; run from _media.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Lengths are normalized by R; field by kq/R^2. The source singularities
are masked for plotting. No two-dimensional Gauss integral is used.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.4, 7.1), facecolor="white")
    grid = np.linspace(-1.5, 1.5, 501)
    x, z = np.meshgrid(grid, grid)
    ex, ez = np.zeros_like(x), np.zeros_like(z)
    mask = np.zeros_like(x, dtype=bool)
    for source_x, charge in ((-0.3, 1.0), (0.3, -1.0)):
        dx = x - source_x
        squared_distance = dx**2 + z**2
        mask |= squared_distance < 0.075**2
        # In the y=0 plane, the 3D inverse-square vector field has r^3
        # in its denominator, unlike a 2D logarithmic potential field.
        denominator = np.maximum(squared_distance, 1e-12)**1.5
        ex += charge * dx / denominator
        ez += charge * z / denominator
    ex, ez = np.ma.array(ex, mask=mask), np.ma.array(ez, mask=mask)
    ax.streamplot(grid, grid, ex, ez, color="#7499ac", density=1.15,
                  linewidth=0.85, arrowsize=1.0, zorder=1)
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor="#222222",
                        linewidth=2.1, linestyle="--", zorder=3))
    for source_x, color, label in ((-0.3, "#c64f24", "+q"),
                                   (0.3, "#0072b2", "−q")):
        ax.add_patch(Circle((source_x, 0), 0.085, facecolor=color,
                            edgecolor="white", zorder=5))
        ax.text(source_x, 0, label, color="white", ha="center", va="center",
                fontsize=12, weight="bold", zorder=6)
        ax.text(source_x, -0.19, f"x/R={source_x:+.1f}",
                ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.9,
                                              "edgecolor": "none"}, zorder=7)
    ax.plot(0, 1, "o", color="#111111", markersize=5, zorder=7)
    ax.annotate("", xy=(0.55, 1), xytext=(0, 1),
                arrowprops={"arrowstyle": "-|>", "color": "#0072b2", "lw": 2.8}, zorder=8)
    ax.annotate("", xy=(0, 1.43), xytext=(0, 1),
                arrowprops={"arrowstyle": "-|>", "color": "#b34b00", "lw": 2.5}, zorder=8)
    ax.text(0.10, 1.37, r"outward $\mathbf{n}$", color="#b34b00", fontsize=12)
    ax.text(0.40, 1.08, r"$\mathbf{E}(P)\ne0$", color="#0072b2", fontsize=13,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    ax.text(-0.11, 1.06, "P", fontsize=12)
    for text, xy, location in (("outward crossing", (-0.82, 0.57), (-1.47, 0.83)),
                                ("inward crossing", (0.82, 0.57), (0.75, 0.83))):
        ax.annotate(text, xy=xy, xytext=location, fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": "#222222"},
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.95},
                    zorder=9)
    ax.text(0, -1.21, r"$Q_{\mathrm{enclosed}}=q-q=0$" + "\n" +
            r"$\oint_{\mathrm{sphere}}\mathbf{E}\cdot\mathbf{n}\,dA=0$",
            ha="center", va="center", fontsize=14,
            bbox={"facecolor": "white", "edgecolor": "#dddddd", "pad": 6}, zorder=10)
    ax.set(xlim=(-1.55, 1.55), ylim=(-1.48, 1.53), aspect="equal",
           xlabel=r"$x/R$", ylabel=r"$z/R$")
    ax.set_xticks([-1, -0.3, 0, 0.3, 1])
    ax.set_yticks([-1, 0, 1])
    ax.spines[["right", "top"]].set_visible(False)
    ax.set_title("Zero net flux, nonzero electric field\n"
                 "3D dipole cross-section: y = 0, sphere radius R = 1 m",
                 fontsize=15, pad=15)
    fig.text(0.5, 0.033, "Dashed circle = sphere cross-section; flux is over the full sphere.\n"
             "Curves follow the 3D Coulomb field; arrow lengths at P are schematic.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.13, right=0.95, top=0.85, bottom=0.16)
    fig.savefig("zero-net-flux-nonzero-field.png", dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
