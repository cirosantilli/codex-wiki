"""Oxford A1 (2021), Q3(a)(iii): run from the desired PNG output directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-1.95, 1.95, 330)
    z = np.linspace(-1.9, 1.9, 320)
    xx, zz = np.meshgrid(x, z)
    fig, ax = plt.subplots(figsize=(6.4, 5.4), layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    ax.streamplot(x, z, zz, xx**3 - xx, color="#9da9b1", density=1.15,
                  linewidth=0.7, arrowsize=0.9)
    energy = zz**2 / 2 + xx**2 / 2 - xx**4 / 4
    central = np.ma.masked_where(np.abs(xx) >= 1, energy)
    ax.contour(xx, zz, central, levels=[0.035, 0.09, 0.16, 0.22],
               colors=["#215a86"], linewidths=1.2)
    for sign in (-1, 1):
        ax.plot(x, sign * (x**2 - 1) / np.sqrt(2), color="#c94a30", lw=2,
                label="Saddle level: h = 1/4" if sign == 1 else None)
    ax.axhline(0, color="#595959", ls="--", lw=0.9, label="Nullclines")
    for a in (-1, 0, 1):
        ax.axvline(a, color="#595959", ls="--", lw=0.9)
    ax.scatter([-1, 1], [0, 0], marker="x", color="#8e2112", s=65, lw=2, zorder=5)
    ax.scatter([0], [0], color="#215a86", s=35, zorder=5)
    ax.annotate("Centre", (0, 0), (0.1, 0.16), fontsize=9)
    ax.annotate("Saddle", (-1, 0), (-1.63, -0.24), fontsize=9)
    ax.annotate("Saddle", (1, 0), (1.18, 0.18), fontsize=9)
    for x0, x1, sign in [(-0.42, -0.23, 1), (0.42, 0.23, -1)]:
        ax.annotate("", (x1, sign * (1 - x1**2) / np.sqrt(2)),
                    (x0, sign * (1 - x0**2) / np.sqrt(2)),
                    arrowprops={"arrowstyle": "->", "color": "#c94a30", "lw": 2})
    ax.set(xlim=(-1.95, 1.95), ylim=(-1.9, 1.9), xlabel=r"$x$", ylabel=r"$z=y-\beta$",
           title="Clockwise centre between two saddles", aspect="equal")
    ax.legend(loc="lower left", fontsize=8.5, framealpha=1)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
