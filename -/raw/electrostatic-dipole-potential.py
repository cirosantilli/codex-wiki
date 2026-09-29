"""Compute dipole equipotentials and electric-field directions, without paths.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dimensionless sources are +1 at (1, 0), -1 at (-1, 0).
The output is an opaque white PNG in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import Circle
import numpy as np


def potential_and_field(x, y, mask_radius=0.22):
    """Return Phi/(kq/a) and E/(kq/a**2), masking source neighborhoods."""
    x, y = np.broadcast_arrays(np.asarray(x, dtype=float), np.asarray(y, dtype=float))
    plus_distance = np.hypot(x - 1, y)
    minus_distance = np.hypot(x + 1, y)
    mask = (plus_distance <= mask_radius) | (minus_distance <= mask_radius)
    # Replace excluded distances before dividing, so even an exact source
    # sample cannot generate infinities or floating-point warnings.
    rp = np.where(mask, 1.0, plus_distance)
    rm = np.where(mask, 1.0, minus_distance)
    potential = 1 / rp - 1 / rm
    ex = (x - 1) / rp**3 - (x + 1) / rm**3
    ey = y / rp**3 - y / rm**3
    return tuple(np.ma.array(value, mask=mask) for value in (potential, ex, ey))


def main():
    phi, ex, ey = potential_and_field([0, 2], [0, 0])
    np.testing.assert_allclose(phi, [0.0, 2.0 / 3.0])
    np.testing.assert_allclose(ex, [-2.0, 8.0 / 9.0])
    np.testing.assert_allclose(ey, [0.0, 0.0])
    grid_x, grid_y = np.meshgrid(np.linspace(-3.2, 3.2, 481), np.linspace(-2.5, 2.5, 381))
    phi, _, _ = potential_and_field(grid_x, grid_y)
    fig, ax = plt.subplots(figsize=(9.4, 6.6), dpi=120)
    norm = TwoSlopeNorm(vmin=-2.0, vcenter=0.0, vmax=2.0)
    color = ax.pcolormesh(grid_x, grid_y, phi, cmap="RdBu_r", norm=norm,
                          shading="auto", rasterized=True)
    levels = [-2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2]
    contours = ax.contour(grid_x, grid_y, phi, levels=levels,
                          colors="#48545b", linewidths=0.8,
                          linestyles="solid", corner_mask=False)
    # Place contour values deliberately in the upper half, leaving the
    # midpoint annotation and source symbols clear.
    labels = [(-1.2, 0.36), (-1.22, 0.62), (-1.30, 1.03), (-1.5, 1.65),
              (0, 2.15), (1.5, 1.65), (1.30, 1.03), (1.22, 0.62), (1.2, 0.36)]
    ax.clabel(contours, levels, manual=labels, inline=True, fmt="%g", fontsize=9)
    arrow_x, arrow_y = np.meshgrid(np.linspace(-3, 3, 19), np.linspace(-2.3, 2.3, 15))
    _, ex, ey = potential_and_field(arrow_x, arrow_y, mask_radius=0.38)
    magnitude = np.ma.sqrt(ex**2 + ey**2)
    ax.quiver(arrow_x, arrow_y, ex / magnitude, ey / magnitude,
              angles="xy", scale_units="xy", scale=5.1, pivot="mid",
              color="#183342", width=0.0032, headwidth=3.6, zorder=3)
    for x, label, charge_color in [(-1, "−q", "#216baf"), (1, "+q", "#b53d35")]:
        ax.add_patch(Circle((x, 0), 0.22, facecolor="white", edgecolor="#63717b", lw=1.1, zorder=4))
        ax.scatter([x], [0], s=360, color=charge_color, edgecolor="white", zorder=5)
        ax.text(x, 0, label, color="white", ha="center", va="center", fontsize=11, zorder=6)
    ax.scatter([0], [0], color="#183342", s=24, zorder=5)
    ax.annotate(r"Midpoint: $\Phi=0$, but $E_x/(kq/a^2)=-2$",
                xy=(0, 0), xytext=(0, -1.12), ha="center", fontsize=11,
                bbox={"facecolor": "white", "edgecolor": "#c7d1d7", "pad": 5},
                arrowprops={"arrowstyle": "->", "color": "#183342"}, zorder=7)
    ax.set(xlim=(-3.2, 3.2), ylim=(-2.5, 2.5), xlabel=r"$X=x/a$", ylabel=r"$Y=y/a$")
    ax.set_aspect("equal")
    ax.set_title("Electric dipole: equipotentials and field directions", fontsize=14, pad=13)
    bar = fig.colorbar(color, ax=ax, shrink=0.88, pad=0.035, extend="both")
    bar.set_label(r"$\Phi/C$, where $C=kq/a$", fontsize=11)
    fig.text(0.48, 0.085, "Contours: computed potential. Arrows: normalized electric-field directions.",
             ha="center", fontsize=10)
    fig.text(0.48, 0.045, "White disks mask the singular sources. Colors saturate beyond ±2; arrows are not particle paths.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.085, right=0.92, bottom=0.17, top=0.89)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
