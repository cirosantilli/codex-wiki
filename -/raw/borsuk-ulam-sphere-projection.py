"""Original sphere projection diagram; output PNG basename to CWD.

Tested with Python 3.14.4, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media: python ../borsuk-ulam-sphere-projection.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    blue, orange, purple = "#2166ac", "#b95319", "#754399"
    fig = plt.figure(figsize=(10, 4.8), facecolor="white")
    fig.suptitle(r"Sphere example: $f(x,y,z)=(x,y)$", fontsize=15, y=0.96)
    sphere = fig.add_axes([0.015, 0.13, 0.49, 0.70], projection="3d")
    plane = fig.add_axes([0.60, 0.20, 0.34, 0.59])
    angle = np.linspace(0, 2 * np.pi, 181)
    latitude = np.linspace(-np.pi / 2, np.pi / 2, 91)
    for phi in np.linspace(-np.pi / 3, np.pi / 3, 5):
        sphere.plot(np.cos(phi) * np.cos(angle), np.cos(phi) * np.sin(angle),
                    np.full_like(angle, np.sin(phi)), color="#a6b7c7", lw=0.7)
    for azimuth in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        sphere.plot(np.cos(latitude) * np.cos(azimuth),
                    np.cos(latitude) * np.sin(azimuth), np.sin(latitude),
                    color="#a6b7c7", lw=0.7)
    sphere.plot(np.cos(angle), np.sin(angle), np.zeros_like(angle),
                color="#576875", lw=1.6)
    xx, yy = np.meshgrid([-1.1, 1.1], [-1.1, 1.1])
    sphere.plot_surface(xx, yy, np.zeros_like(xx), color="#daeaf5",
                        alpha=0.25, shade=False)
    sphere.quiver(0, 0, 1, 0, 0, -0.96, color=blue, lw=2,
                  arrow_length_ratio=0.12)
    sphere.quiver(0, 0, -1, 0, 0, 0.96, color=orange, lw=2,
                  arrow_length_ratio=0.12)
    sphere.scatter([0, 0], [0, 0], [1, -1], color=[blue, orange], s=50,
                   depthshade=False)
    sphere.scatter([0], [0], [0], color=purple, s=40, depthshade=False)
    sphere.text(0.10, 0, 1.18, r"$N=(0,0,1)$", color=blue, fontsize=10)
    sphere.text(0.10, 0, -1.28, r"$S=(0,0,-1)$", color=orange, fontsize=10)
    sphere.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2), zlim=(-1.4, 1.4))
    sphere.set_box_aspect((1, 1, 1.15), zoom=1.18)
    sphere.view_init(elev=18, azim=-58)
    sphere.set_title(r"Domain $S^2$: project to $z=0$", pad=8)
    sphere.set_axis_off()

    plane.add_patch(Circle((0, 0), 1, facecolor="#eaf3fa",
                           edgecolor="#66717b", lw=1.5))
    plane.axhline(0, color="#a5afb8", lw=1)
    plane.axvline(0, color="#a5afb8", lw=1)
    plane.scatter(0, 0, s=85, color=purple, zorder=5)
    plane.annotate(r"$f(N)=f(S)=(0,0)$", xy=(0, 0), xytext=(0.20, 0.63),
                   fontsize=11, color=purple,
                   arrowprops={"arrowstyle": "->", "color": purple, "lw": 1.5})
    plane.text(0.30, -0.67, "Image: unit disk", color="#475361", ha="center")
    plane.set(xlim=(-1.25, 1.55), ylim=(-1.25, 1.25), aspect="equal")
    plane.set_xticks([-1, 0, 1])
    plane.set_yticks([-1, 0, 1])
    plane.set(xlabel="$x$", ylabel="$y$", title=r"Output plane $\mathbb{R}^2$")
    for spine in ("top", "right"):
        plane.spines[spine].set_visible(False)
    fig.text(0.52, 0.64, r"$f$", ha="center", fontsize=15)
    plane.annotate("", xy=(0.60, 0.62), xytext=(0.46, 0.62),
                   xycoords=fig.transFigure, textcoords=fig.transFigure,
                   arrowprops={"arrowstyle": "->", "color": "#465563", "lw": 2})
    fig.text(0.50, 0.065, "The opposite poles have one common output. "
             "This example does not prove the general theorem.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
