"""An exterior, a sphere cap and a reciprocal disc; existing plotting dependencies."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np


def plane_axes(ax, limit, real, imag):
    for end in [(limit, 0), (0, limit)]:
        ax.annotate("", xy=end, xytext=(-end[0], -end[1]),
                    arrowprops={"arrowstyle": "->", "color": "#637380", "lw": 1})
    ax.text(limit * .55, -limit * .12, real, fontsize=10)
    ax.text(limit * .05, limit * .89, imag, fontsize=10)
    ax.set(xlim=(-limit, limit), ylim=(-limit, limit), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (zax, sax, wax) = plt.subplots(1, 3, figsize=(11.2, 4.7))
    blue, orange = "#2367b1", "#bd581b"
    zax.set_facecolor("#e6f0fc")
    zax.add_patch(Polygon([(-3.1, -3.1), (3.1, -3.1), (3.1, 3.1), (-3.1, 3.1)],
                          facecolor="#e6f0fc", edgecolor="none", zorder=0))
    zax.add_patch(Circle((0, 0), 2, facecolor="white", edgecolor=blue, linestyle="--", lw=1.8))
    plane_axes(zax, 3.1, r"Re$(z)$", r"Im$(z)$")
    zax.scatter([2], [1], color=orange, s=45, zorder=5)
    zax.annotate("$2+i$", (2, 1), xytext=(5, 9), textcoords="offset points", color=orange)
    zax.text(-.36, -.49, "$0$")
    zax.text(-2.83, -2.7, "Exterior continues outward", fontsize=10, color=blue)
    zax.set_title("$z$ chart: $|z|>2$", pad=18)

    theta = np.linspace(0, 2 * np.pi, 500)
    sax.fill(np.cos(theta), np.sin(theta), color="#f3f6fa")
    cap_theta = np.linspace(np.arcsin(.6), np.pi - np.arcsin(.6), 200)
    sax.fill(np.cos(cap_theta), np.sin(cap_theta), color="#e6f0fc")
    sax.plot(np.cos(theta), np.sin(theta), color="#65788c", lw=1.5)
    sax.plot([-.8, .8], [.6, .6], color=blue, linestyle="--", lw=1.8)
    sax.axhline(0, color="#a5b0ba", lw=.8)
    sax.scatter([0], [1], s=40, color=blue, zorder=5)
    sax.text(-.37, 1.1, r"$N=\infty$")
    sax.annotate("$Z=3/5$", (.8, .6), xytext=(.64, .21),
                 arrowprops={"arrowstyle": "-", "color": blue}, color=blue)
    sax.text(-.61, -.15, "equatorial plane", fontsize=10)
    sax.text(-.62, -.85, "$S$ ($z=0$)", fontsize=11)
    sax.text(-.74, -1.31, "Meridian section of the cap", fontsize=10)
    sax.set(xlim=(-1.25, 1.25), ylim=(-1.45, 1.38), aspect="equal")
    sax.set_title("Sphere: $Z>3/5$", pad=18)
    sax.axis("off")

    wax.add_patch(Circle((0, 0), .5, facecolor="#e6f0fc", edgecolor=blue, linestyle="--", lw=1.8))
    plane_axes(wax, .72, r"Re$(w)$", r"Im$(w)$")
    wax.scatter([0], [0], s=40, color=blue, zorder=5)
    wax.text(-.28, .08, "$w=0$\n(infinity)", fontsize=10, color=blue)
    wax.scatter([.4], [-.2], color=orange, s=45, zorder=5)
    wax.annotate("$(2-i)/5$", (.4, -.2), xytext=(.1, -.63),
                 arrowprops={"arrowstyle": "-", "color": orange}, color=orange)
    wax.set_title("$w=1/z$ chart: $|w|<1/2$", pad=18)
    fig.suptitle("One neighbourhood of infinity, three geometric views", fontsize=16, y=.98)
    fig.text(.5, .065, "Blue shading is included. Dashed boundaries are excluded.   Positive Im(z) becomes negative Im(w).",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.035, right=.98, top=.81, bottom=.16, wspace=.24)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
