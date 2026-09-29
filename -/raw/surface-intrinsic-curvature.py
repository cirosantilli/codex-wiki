"""Compare plane, cylinder, and sphere; write basename.png to the cwd.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "mathtext.fontset": "dejavusans"})
    fig = plt.figure(figsize=(10.8, 4.8), facecolor="white")
    titles = ["Plane", "Circular cylinder", "Sphere"]
    colors = ["#d9e9ed", "#d9e9ed", "#f0dfc3"]
    grid_colors = ["#347c91", "#347c91", "#ac742e"]
    axes = []
    for i, title in enumerate(titles):
        ax = fig.add_axes([.015 + .33 * i, .30, .31, .53], projection="3d", computed_zorder=False)
        ax.set_proj_type("ortho")
        ax.set_facecolor("white")
        ax.set_box_aspect((1, 1, 1), zoom=1.35)
        ax.view_init(elev=24, azim=-55)
        ax.set(xlim=(-1.25, 1.25), ylim=(-1.25, 1.25), zlim=(-1.25, 1.25))
        ax.set_axis_off()
        ax.set_title(title, fontsize=15, pad=0)
        axes.append(ax)

    # Same equally spaced arc-length coordinates on the plane and cylinder.
    u, v = np.meshgrid(np.linspace(-1.1, 1.1, 81), np.linspace(-.9, .9, 61))
    plane = (u, v, np.zeros_like(u))
    cylinder = (np.sin(u), -np.cos(u), v)
    phi, theta = np.meshgrid(np.linspace(0, 2 * np.pi, 97), np.linspace(0, np.pi, 65))
    sphere = (np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta))
    for ax, coords, color in zip(axes, [plane, cylinder, sphere], colors):
        ax.plot_surface(*coords, color=color, linewidth=0, alpha=1,
                        shade=False, antialiased=False, zorder=1)

    t = np.linspace(-1.1, 1.1, 151)
    s = np.linspace(-.9, .9, 151)
    for fixed_u in np.linspace(-1.1, 1.1, 9):
        axes[0].plot(np.full_like(s, fixed_u), s, np.full_like(s, .006),
                     color=grid_colors[0], lw=1, zorder=3)
        # Tiny outward displacement keeps grid curves visible on the surface.
        axes[1].plot(np.full_like(s, 1.006 * np.sin(fixed_u)),
                     np.full_like(s, -1.006 * np.cos(fixed_u)), s,
                     color=grid_colors[1], lw=1, zorder=3)
    for fixed_v in np.linspace(-.9, .9, 7):
        axes[0].plot(t, np.full_like(t, fixed_v), np.full_like(t, .006),
                     color=grid_colors[0], lw=1, zorder=3)
        axes[1].plot(1.006 * np.sin(t), -1.006 * np.cos(t), np.full_like(t, fixed_v),
                     color=grid_colors[1], lw=1, zorder=3)

    # Only draw the front half of each spherical grid curve to avoid false
    # impressions of transparency; hidden curves are occluded by the sphere.
    camera = np.array([np.cos(np.deg2rad(24)) * np.cos(np.deg2rad(-55)),
                       np.cos(np.deg2rad(24)) * np.sin(np.deg2rad(-55)),
                       np.sin(np.deg2rad(24))])

    def front_grid(x, y, z):
        coords = 1.006 * np.array([x, y, z])
        coords[:, camera @ coords < 0] = np.nan
        axes[2].plot(*coords, color=grid_colors[2], lw=1, zorder=3)

    ph = np.linspace(0, 2 * np.pi, 361)
    th = np.linspace(0, np.pi, 181)
    for latitude in np.linspace(np.pi / 6, 5 * np.pi / 6, 5):
        front_grid(np.sin(latitude) * np.cos(ph), np.sin(latitude) * np.sin(ph),
                   np.full_like(ph, np.cos(latitude)))
    for longitude in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        front_grid(np.sin(th) * np.cos(longitude), np.sin(th) * np.sin(longitude), np.cos(th))

    metrics = [r"$I=du^2+dv^2$", r"$I=du^2+dv^2$", r"$I=R^2(d\theta^2+\sin^2\theta\,d\phi^2)$"]
    curvatures = [r"$K=0$", r"$K=0$", r"$K=1/R^2$"]
    notes = ["No bending", "Bends in one direction", "Bends in both principal directions"]
    for i in range(3):
        x = .17 + .33 * i
        fig.text(x, .255, metrics[i], ha="center", fontsize=13)
        fig.text(x, .185, curvatures[i], ha="center", fontsize=16, weight="bold")
        fig.text(x, .125, notes[i], ha="center", fontsize=11)
    fig.suptitle("Visible bending does not determine intrinsic curvature", fontsize=17, y=.97)
    fig.text(.5, .035, "Plane and cylinder grids preserve local lengths and angles. A spherical patch cannot flatten isometrically.",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
