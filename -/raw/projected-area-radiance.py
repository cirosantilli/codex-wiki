"""Generate projected-area-radiance.png in CWD; tested with Python 3.14.4.

Requires the repository's matplotlib and numpy environment. The two geometric
panels are cross-sections of a rectangle with unchanged depth into the page.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    radiance, area = 10.0, 0.020
    angles = np.deg2rad([0, 60])
    intensities = radiance * area * np.cos(angles)
    assert np.allclose(intensities, [0.20, 0.10], atol=1e-15, rtol=0)
    fig = plt.figure(figsize=(11.2, 4.7), dpi=100)
    grid = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.35],
                           left=0.03, right=0.98, bottom=0.23, top=0.78, wspace=0.29)
    patch_color, projection_color, ray_color = "#2166ac", "#d87911", "#8c2341"
    for column, theta in enumerate(angles):
        ax = fig.add_subplot(grid[0, column])
        direction = np.array([np.sin(theta), np.cos(theta)])
        endpoints = np.array([[-1.0, 0.0], [1.0, 0.0]])
        height = 1.5
        projected = endpoints + (height - endpoints @ direction)[:, None] * direction
        assert np.isclose(np.linalg.norm(projected[1] - projected[0]), 2 * np.cos(theta))
        ax.plot(endpoints[:, 0], endpoints[:, 1], lw=5, color=patch_color,
                solid_capstyle="butt")
        ax.plot(projected[:, 0], projected[:, 1], lw=5, color=projection_color,
                solid_capstyle="butt")
        for point, shadow in zip(endpoints, projected):
            ax.plot([point[0], shadow[0]], [point[1], shadow[1]], "--",
                    color="0.55", lw=1.2)
        ax.annotate("", xy=(0, 1.0), xytext=(0, 0),
                    arrowprops={"arrowstyle": "->", "color": "0.3", "lw": 1.7})
        ax.text(-0.12, 1.01, "normal", ha="right", color="0.3", fontsize=10)
        if column:
            ax.annotate("", xy=1.35 * direction, xytext=(0, 0),
                        arrowprops={"arrowstyle": "->", "color": ray_color, "lw": 2})
            ax.add_patch(Arc((0, 0), 0.88, 0.88, theta1=30, theta2=90,
                             color=ray_color, lw=1.3))
            ax.text(0.27, 0.53, r"$60^\circ$", color=ray_color)
            ax.text(1.78, 1.26, "view", ha="center", color=ray_color)
            ax.text(1.65, 0.31, r"$A_\perp=A/2$", ha="left", color=projection_color)
        else:
            ax.text(0.18, 0.66, "view along normal", color=ray_color, fontsize=10)
            ax.text(0, 1.67, r"$A_\perp=A$", ha="center", color=projection_color)
        ax.text(0, -0.31, "same physical patch, area A", ha="center",
                color=patch_color, fontsize=10)
        ax.set(xlim=(-1.5, 2.75), ylim=(-0.6, 2.0), aspect="equal")
        ax.set_title(rf"View at ${round(np.rad2deg(theta))}^\circ$", pad=15, fontsize=12)
        ax.axis("off")
    ax = fig.add_subplot(grid[0, 2])
    degrees = np.linspace(0, 90, 361)
    ax.plot(degrees, radiance * area * np.cos(np.deg2rad(degrees)),
            color=patch_color, lw=2.5)
    ax.scatter([0, 60], intensities, color=projection_color, zorder=4, s=50)
    ax.plot([60, 60, 0], [0, 0.1, 0.1], "--", color="0.6", lw=1)
    ax.annotate("0.20 W/sr", xy=(0, .20), xytext=(12, .209), fontsize=10)
    ax.annotate("0.10 W/sr", xy=(60, .10), xytext=(29, .065), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "0.35"})
    ax.set(xlim=(-3, 93), ylim=(0, .23), xticks=[0, 30, 60, 90],
           yticks=[0, .05, .1, .15, .2], xlabel=r"View angle $\theta$ (degrees)",
           ylabel=r"Radiant intensity $I$ (W/sr)")
    ax.set_title(r"$I(\theta)=LA\cos\theta$", fontsize=13, pad=15)
    ax.grid(alpha=.2)
    fig.suptitle("Projected area changes; radiance stays the same", fontsize=16, y=.97)
    fig.text(.5, .88, r"Uniform outgoing $L=10$ W/(m$^2$ sr), physical $A=0.020$ m$^2$",
             ha="center", fontsize=12)
    fig.text(.5, .07, "Parallel projection onto a plane perpendicular to the view.\n"
             "The rectangle's depth into the page stays fixed; only its apparent width contracts.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.savefig("projected-area-radiance.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
