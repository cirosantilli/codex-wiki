#!/usr/bin/env python3
"""Plot the analytic hemisphere field; write the PNG basename to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1).
Dependencies are already listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np


def fields(x, z):
    radius = np.sqrt(x*x+z*z)
    safe = np.maximum(radius, 1.)
    potential = z*(1-safe**-3)
    ex = -3*x*z/safe**5
    ez = -1+safe**-3-3*z*z/safe**5
    mask = radius <= 1.005
    return (np.ma.masked_where(mask, potential),
            np.ma.masked_where(mask, ex), np.ma.masked_where(mask, ez))


def main():
    xs = np.linspace(-3.2, 3.2, 300)
    zs = np.linspace(0, 3.5, 230)
    x, z = np.meshgrid(xs, zs)
    potential, ex, ez = fields(x, z)
    fig, ax = plt.subplots(figsize=(7.3, 4.5), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    levels = [.2, .4, .7, 1., 1.5, 2., 2.7]
    contours = ax.contour(x, z, potential, levels=levels, colors="#d55e00",
                          linewidths=.9, linestyles="--")
    ax.clabel(contours, levels=[.4, 1., 2.], inline=True, fontsize=8, fmt="%g")
    starts = np.column_stack((np.linspace(-3., 3., 19), np.full(19, 3.42)))
    ax.streamplot(xs, zs, ex, ez, start_points=starts, integration_direction="forward",
                   color="#0072b2", linewidth=1.0, arrowsize=.85,
                   density=1.1, broken_streamlines=False)
    ax.add_patch(Wedge((0, 0), 1, 0, 180, facecolor=".83", edgecolor=".2", lw=1.6, zorder=5))
    ax.plot([-3.2, -1], [0, 0], color=".2", lw=2)
    ax.plot([1, 3.2], [0, 0], color=".2", lw=2)
    ax.text(0, .26, r"Grounded boss, $r=a$", ha="center", fontsize=10, zorder=6)
    ax.text(-3.1, 3.23, "Field enters from the distant +V plate", fontsize=9,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    ax.set(xlim=(-3.2, 3.2), ylim=(-.1, 3.5), aspect="equal",
           xlabel=r"Horizontal position $x/a$", ylabel=r"Height $z/a$",
           title="Local capacitor field: blue field lines and orange equipotentials")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
