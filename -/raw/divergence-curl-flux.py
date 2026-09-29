"""Planar flux and circulation for two equal-magnitude analytic vector fields."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 2 * np.pi, 4097)
    normal = np.array([np.cos(t), np.sin(t)])
    tangent = np.array([-np.sin(t), np.cos(t)])
    for field, expected in [(normal, (2 * np.pi, 0)),
                            (tangent, (0, 2 * np.pi))]:
        flux = np.trapezoid(np.sum(field * normal, axis=0), t)
        circulation = np.trapezoid(np.sum(field * tangent, axis=0), t)
        assert np.isclose(flux, expected[0])
        assert np.isclose(circulation, expected[1])
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.2), dpi=120)
    fig.patch.set_facecolor("white")
    grid = np.linspace(-1.5, 1.5, 15)
    x, y = np.meshgrid(grid, grid)
    colors = ["#c76716", "#1675a9"]
    for ax, rotating, color in zip(axes, [False, True], colors):
        u, v = (-y, x) if rotating else (x, y)
        ax.fill(np.cos(t), np.sin(t), color="#f2f5f7", zorder=0)
        ax.quiver(x, y, u, v, color="#b1bcc5", angles="xy",
                  scale_units="xy", scale=5, width=0.004)
        ax.plot(np.cos(t), np.sin(t), color="#333e60", lw=2)
        for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
            p = np.array([np.cos(angle), np.sin(angle)])
            direction = np.array([-p[1], p[0]]) if rotating else p
            ax.annotate("", xy=p + 0.26 * direction, xytext=p,
                        arrowprops={"arrowstyle": "-|>", "color": color,
                                    "lw": 2, "mutation_scale": 13})
        ax.set_aspect("equal")
        ax.set_xlim(-1.7, 1.7)
        ax.set_ylim(-1.7, 1.7)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(r"$G=(-y,x,0)$: rigid rotation" if rotating
                     else r"$F=(x,y,0)$: radial expansion", fontsize=13)
        statements = ([r"$\mathrm{div}\,G=0,\quad\mathrm{curl}\,G=(0,0,2)$",
                       r"outward flux $=0$; circulation $=2\pi$"] if rotating
                      else [r"$\mathrm{div}\,F=2,\quad\mathrm{curl}\,F=0$",
                            r"outward flux $=2\pi$; circulation $=0$"])
        for j, line in enumerate(statements):
            ax.text(0.5, -0.22 - j * 0.085, line, transform=ax.transAxes,
                    ha="center", fontsize=11, color=color)
    fig.suptitle("Same vector lengths, different boundary measurements",
                 fontsize=16, y=0.98)
    fig.text(0.5, 0.025, "Unit-circle planar flux; counterclockwise circulation. Fields have zero z component.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.28, top=0.83, wspace=0.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
