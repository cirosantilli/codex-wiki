"""Oxford A10 (2015), Q1: meridional streamlines past a fixed sphere.

Writes 2015-sphere-streamlines.png in the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; root pyproject.toml.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    z = np.linspace(-3.3, 3.3, 480)
    s = np.linspace(-2.35, 2.35, 360)
    Z, S = np.meshgrid(z, s)
    r = np.maximum(np.hypot(Z, S), 1e-3)
    axial = 1 + 0.5 / r**3 - 1.5 * Z**2 / r**5
    transverse = -1.5 * Z * S / r**5
    mask = r <= 1.015
    axial = np.ma.masked_where(mask, axial)
    transverse = np.ma.masked_where(mask, transverse)
    fig, ax = plt.subplots(figsize=(7.3, 5.2), facecolor="white")
    starts = np.column_stack((-3.29*np.ones(25), np.linspace(-2.15, 2.15, 25)))
    ax.streamplot(z, s, axial, transverse, density=1.35, color="#176b93",
                  linewidth=0.9, arrowsize=1.0, start_points=starts,
                  integration_direction="forward", broken_streamlines=False, maxlength=8)
    ax.add_patch(plt.Circle((0, 0), 1, facecolor="#e6e9ec", edgecolor="#37474f", lw=1.7, zorder=5))
    ax.plot([1.02, 3.3], [0, 0], color="#176b93", lw=.9)
    ax.annotate("", xy=(2.1, 0), xytext=(1.8, 0),
                arrowprops={"arrowstyle": "->", "color": "#176b93", "lw": .9})
    ax.plot([-1, 1], [0, 0], "o", color="#b4591c", ms=5, zorder=6)
    ax.text(0, 0, "Fixed sphere\n$a=1$", ha="center", va="center", fontsize=12, zorder=6)
    ax.set(xlim=(-3.3, 3.3), ylim=(-2.35, 2.35), aspect="equal", xlabel="$z$",
           ylabel="Transverse meridional coordinate", title="Uniform potential flow past a sphere ($U=1$)")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig("2015-sphere-streamlines.png", dpi=160, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
