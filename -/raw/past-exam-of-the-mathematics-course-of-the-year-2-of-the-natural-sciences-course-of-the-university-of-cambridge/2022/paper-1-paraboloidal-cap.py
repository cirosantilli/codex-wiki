"""Q1 paraboloidal cap; Python 3.14.4, root pyproject.toml dependencies.

Write the opaque PNG to cwd. Run in the matching _media course directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    radius, angle = np.meshgrid(np.linspace(0, 1, 55), np.linspace(0, 2 * np.pi, 100))
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    z = (radius**2 - 1) / 2
    fig = plt.figure(figsize=(8.6, 4.2), facecolor="white")
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ax.plot_surface(x, y, z, color="#347da9", alpha=0.57, linewidth=0, antialiased=True)
    ax.plot_surface(x, y, np.zeros_like(z), color="#c3d8e4", alpha=0.24, linewidth=0)
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(theta), np.sin(theta), np.zeros_like(theta), color="#174d70", lw=1.8)
    ax.scatter([0], [0], [-0.5], color="#a34b27", s=28, depthshade=False)
    ax.set(xlabel=r"$x$", ylabel=r"$y$", zlabel=r"$z$", title="Curved base and top disk", zlim=(-0.58, 0.1))
    ax.set_box_aspect((1, 1, 0.65))
    ax.view_init(elev=23, azim=-58)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-0.5, 0])
    ax.tick_params(labelsize=8, pad=0)

    section = fig.add_subplot(1, 2, 2)
    horizontal = np.linspace(-1, 1, 400)
    bottom = (horizontal**2 - 1) / 2
    section.fill_between(horizontal, bottom, 0, color="#d2e3ed")
    section.plot(horizontal, bottom, color="#175e90", lw=2)
    section.plot([-1, 1], [0, 0], color="#175e90", lw=2)
    section.axvline(0, color="#999999", lw=0.7, ls="--")
    section.scatter([0], [-0.5], color="#a34b27", s=28, zorder=4)
    section.annotate(r"Vertex $(0,-1/2)$", (0, -0.5), xytext=(0.14, -0.65), fontsize=9, arrowprops={"arrowstyle": "->", "color": "#777777"})
    section.text(0, -0.22, "Solid interior", ha="center", fontsize=10)
    section.text(0, 0.09, "Top disk: z = 0", ha="center", fontsize=10)
    section.set(xlabel=r"$x$ (section $y=0$)", ylabel=r"$z$", title="Meridian cross-section", xlim=(-1.15, 1.15), ylim=(-0.74, 0.19), aspect="equal")
    section.spines[["top", "right"]].set_visible(False)
    section.set_xticks([-1, 0, 1])
    section.set_yticks([-0.5, 0])
    section.grid(alpha=0.12)
    fig.suptitle(r"$(x^2+y^2-1)/2\leq z\leq0$", fontsize=14, y=0.98)
    fig.subplots_adjust(left=0.01, right=0.985, bottom=0.15, top=0.82, wspace=0.30)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
