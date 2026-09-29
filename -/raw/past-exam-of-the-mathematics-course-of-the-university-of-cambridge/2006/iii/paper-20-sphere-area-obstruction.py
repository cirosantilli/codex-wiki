"""Render complementary sphere areas; write the PNG to the caller's directory."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba


def main():
    phi = np.linspace(0, 2 * np.pi, 121)
    theta = np.linspace(0, np.pi, 81)
    pp, tt = np.meshgrid(phi, theta)
    xx = np.sin(tt) * np.cos(pp)
    yy = np.sin(tt) * np.sin(pp)
    zz = np.cos(tt)
    upper = "#75b6db"
    lower = "#f4c38a"
    fig = plt.figure(figsize=(8, 4.2), dpi=120, facecolor="white")
    for column, (height, title, upper_area, lower_area) in enumerate(
        [
            (0, "Equator: height 0", r"$2\pi$", r"$2\pi$"),
            (0.5, "Latitude: height 1/2", r"$\pi$", r"$3\pi$"),
        ],
        start=1,
    ):
        ax = fig.add_subplot(1, 2, column, projection="3d")
        colors = np.empty(zz.shape + (4,))
        colors[:] = to_rgba(lower)
        colors[zz >= height] = to_rgba(upper)
        ax.plot_surface(
            xx, yy, zz, facecolors=colors, rstride=2, cstride=2,
            linewidth=0.15, edgecolor="#ffffff44", shade=False,
            antialiased=True,
        )
        radius = np.sqrt(1 - height**2)
        ax.plot(
            radius * np.cos(phi), radius * np.sin(phi),
            np.full_like(phi, height), color="#24344b", lw=2,
        )
        ax.view_init(elev=13, azim=-55)
        ax.set_box_aspect((1, 1, 1))
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1, 1)
        ax.set_axis_off()
        ax.set_title(title, fontsize=13, pad=2)
        ax.text2D(
            0.5, 0.90, "Upper region: " + upper_area,
            transform=ax.transAxes, ha="center", fontsize=12, color="#276287",
        )
        ax.text2D(
            0.5, 0.035, "Lower region: " + lower_area,
            transform=ax.transAxes, ha="center", fontsize=12, color="#975822",
        )
    fig.suptitle("Complementary areas on the unit sphere", fontsize=15, y=0.97)
    fig.text(
        0.5, 0.035, "Total area is 4π; a symplectomorphism preserves both region areas.",
        ha="center", fontsize=10.5, color="#354254",
    )
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.12, top=0.83, wspace=0.02)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
