"""Unroll a one-turn helical geodesic; write basename.png to the cwd.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig = plt.figure(figsize=(10.2, 5.3), facecolor="white")
    ax = fig.add_axes([.015, .20, .42, .64], projection="3d", computed_zorder=False)
    ax.set_facecolor("white")
    ax.set_proj_type("ortho")
    ax.set_box_aspect((2, 2, 2.3), zoom=1.15)
    azimuth = -55
    ax.view_init(elev=20, azim=azimuth)
    ax.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2), zlim=(-.15, 2.2))
    ax.set_axis_off()
    ax.set_title("On the cylinder (R = 1)", fontsize=15, pad=10)

    phi, z = np.meshgrid(np.linspace(0, 2 * np.pi, 81), np.linspace(0, 2, 31))
    ax.plot_wireframe(np.cos(phi), np.sin(phi), z, rstride=6, cstride=10,
                      color="#a7bec6", lw=.75, alpha=.65, zorder=1)
    t = np.linspace(0, 1, 1001)
    theta = 2 * np.pi * t
    curve = np.array([np.cos(theta), np.sin(theta), 2 * t])
    visible = np.cos(theta - np.deg2rad(azimuth)) >= 0
    for mask, style, opacity in [(visible, "-", 1), (~visible, "--", .65)]:
        segment = curve.copy()
        segment[:, ~mask] = np.nan
        ax.plot(*segment, color="#b54d21", lw=3, linestyle=style, alpha=opacity, zorder=4)
    ax.plot(np.ones_like(t), np.zeros_like(t), 2 * t,
             color="#19788a", lw=2.5, zorder=3)
    for point, label in [(curve[:, 0], "A"), (curve[:, -1], "B")]:
        ax.scatter(*point, color="#262d35", s=24, depthshade=False, zorder=5)
        ax.text(point[0] + .10, point[1], point[2] + .08, label, fontsize=13, zorder=6)

    flat = fig.add_axes([.52, .38, .445, .36])
    flat.set_facecolor("white")
    flat.set_title("On the unrolled sheet", fontsize=15, pad=14)
    flat.set_aspect("equal")
    flat.set(xlim=(-.2, 2 * np.pi + .2), ylim=(-.18, 2.18))
    flat.set_xticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
    flat.set_yticks([0, 1, 2])
    flat.set_xlabel(r"Circumferential arc length $u=\theta$", labelpad=10)
    flat.set_ylabel("Height z")
    flat.grid(color="#dce3e6", lw=.8)
    flat.plot(2 * np.pi * t, 2 * t, color="#b54d21", lw=3)
    flat.plot([0, 0], [0, 2], color="#19788a", lw=2.5)
    flat.plot([2 * np.pi, 2 * np.pi], [0, 2], color="#19788a", lw=1.7, linestyle=":")
    flat.scatter([0, 0, 2 * np.pi], [0, 2, 2], color="#262d35", s=24, zorder=5)
    flat.annotate("A", (0, 0), xytext=(9, 7), textcoords="offset points")
    flat.annotate(r"$B_0$", (0, 2), xytext=(9, -16), textcoords="offset points")
    flat.annotate(r"$B_1$", (2 * np.pi, 2), xytext=(-27, -19), textcoords="offset points")
    flat.text(np.pi, .27, r"$I=du^2+dz^2$", fontsize=14, ha="center",
              bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})

    fig.suptitle("A helical geodesic is a straight line after unrolling", fontsize=17, y=.96)
    fig.text(.73, .24, r"$B_0$ and $B_1$ are the same point on the cylinder.", ha="center", fontsize=11)
    fig.text(.5, .14, r"One-turn helix: $L=\sqrt{4\pi^2+4}\approx6.59$", ha="center", color="#b54d21", fontsize=14)
    fig.text(.5, .075, "Vertical generator: L = 2. The helix minimizes within its winding class, but is longer overall.",
             ha="center", color="#19788a", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
