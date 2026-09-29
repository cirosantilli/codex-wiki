"""Compare area-driven circulation with an angular form on a punctured plane."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 2 * np.pi, 4097)
    for radius in (1.0, 2.0):
        x, y = radius * np.cos(t), radius * np.sin(t)
        dx, dy = -radius * np.sin(t), radius * np.cos(t)
        smooth = np.trapezoid((-y * dx + x * dy) / 2, t)
        angular = np.trapezoid((-y * dx + x * dy) / radius**2, t)
        assert np.isclose(smooth, np.pi * radius**2)
        assert np.isclose(angular, 2 * np.pi)

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.4), dpi=120)
    fig.patch.set_facecolor("white")
    grid = np.linspace(-2.2, 2.2, 17)
    xg, yg = np.meshgrid(grid, grid)
    r2 = xg**2 + yg**2
    for index, ax in enumerate(axes):
        ax.set_aspect("equal")
        ax.set_xlim(-2.55, 2.55)
        ax.set_ylim(-2.55, 2.55)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_xticks([-2, 0, 2])
        ax.set_yticks([-2, 0, 2])
        if index == 0:
            u, v = -yg / 2, xg / 2
        else:
            keep = r2 > 0.30
            safe = np.where(keep, r2, 1)
            u = np.ma.masked_where(~keep, -yg / safe)
            v = np.ma.masked_where(~keep, xg / safe)
        ax.quiver(xg, yg, u, v, color="#a2adb8", angles="xy",
                  scale_units="xy", scale=4, width=0.004)
        for radius, color in ((1, "#147c67"), (2, "#3156b0")):
            ax.plot(radius * np.cos(t), radius * np.sin(t),
                    color=color, lw=2)
            start, end = 0.32, 0.52
            ax.annotate("", xy=(radius * np.cos(end), radius * np.sin(end)),
                        xytext=(radius * np.cos(start), radius * np.sin(start)),
                        arrowprops={"arrowstyle": "-|>", "color": color,
                                    "lw": 2, "mutation_scale": 15})
        if index == 0:
            ax.set_title(r"$\eta=(-y\,dx+x\,dy)/2$", fontsize=15, pad=14)
            equation = r"$d\eta=dx\wedge dy$ everywhere"
            values = (r"$R=1:\ \oint\eta=\pi$",
                      r"$R=2:\ \oint\eta=4\pi$")
        else:
            ax.set_title(r"$\omega=(-y\,dx+x\,dy)/(x^2+y^2)$",
                         fontsize=14, pad=14)
            equation = r"$d\omega=0$ for $(x,y)\ne(0,0)$"
            values = (r"$R=1:\ \oint\omega=2\pi$",
                      r"$R=2:\ \oint\omega=2\pi$")
            ax.plot(0, 0, marker="x", color="#ba2634", ms=9, mew=2)
            ax.text(0, -0.45, "excluded", color="#ba2634", fontsize=10,
                    ha="center", bbox={"facecolor": "white", "edgecolor": "none",
                                      "pad": 1})
        ax.text(0.5, -0.20, equation, transform=ax.transAxes,
                ha="center", fontsize=11)
        for j, (value, color) in enumerate(zip(values, ("#147c67", "#3156b0"))):
            ax.text(0.5, -0.29 - 0.085 * j, value, transform=ax.transAxes,
                    ha="center", color=color, fontsize=12)
    fig.suptitle("Local circulation and global winding are different", fontsize=16, y=0.98)
    fig.text(0.5, 0.02, "Arrows display one-form coefficients in Euclidean coordinates, at the same arrow scale.",
             ha="center", fontsize=10, color="#444444")
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.30, top=0.84, wspace=0.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
