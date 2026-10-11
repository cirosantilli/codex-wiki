"""Q1 prolate spheroid; Python 3.14.4, root pyproject.toml dependencies.

Write the opaque PNG to cwd. Run in the matching _media course directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a, c = np.sinh(1.0), np.cosh(1.0)
    theta, phi = np.meshgrid(np.linspace(0, np.pi, 70), np.linspace(0, 2 * np.pi, 90))
    x = a * np.sin(theta) * np.cos(phi)
    y = a * np.sin(theta) * np.sin(phi)
    z = c * np.cos(theta)
    fig = plt.figure(figsize=(8.5, 4.4), facecolor="white")
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ax.plot_surface(x, y, z, color="#3f8db6", alpha=0.48, linewidth=0, antialiased=True)
    ax.plot([0, 0], [0, 0], [-c, c], color="#444444", lw=1)
    ax.scatter([0, 0], [0, 0], [-1, 1], color="#aa4a29", s=26, depthshade=False)
    ax.set(xlabel=r"$x$", ylabel=r"$y$", zlabel=r"$z$", title=r"Surface $\xi=1$")
    ax.set_box_aspect((a, a, c))
    ax.view_init(elev=20, azim=-56)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-1, 0, 1])
    ax.tick_params(labelsize=8, pad=0)

    meridian = fig.add_subplot(1, 2, 2)
    angle = np.linspace(0, 2 * np.pi, 400)
    meridian.plot(a * np.sin(angle), c * np.cos(angle), color="#175e90", lw=2)
    meridian.axhline(0, color="#aaaaaa", lw=0.8)
    meridian.axvline(0, color="#aaaaaa", lw=0.8)
    meridian.scatter([0, 0], [-1, 1], color="#aa4a29", s=25, zorder=4)
    meridian.plot([0, a], [0, 0], color="#175e90", lw=2.4)
    meridian.plot([0, 0], [0, c], color="#4a7e39", lw=2.4)
    meridian.annotate(r"$a=\sinh 1$", (a / 2, 0), xytext=(0.21, -0.32), fontsize=10)
    meridian.annotate(r"$c=\cosh 1$", (0, c / 2), xytext=(0.22, 0.7), fontsize=10)
    meridian.annotate("Foci", (0, -1), xytext=(0.28, -1.28), fontsize=10, color="#aa4a29", arrowprops={"arrowstyle": "->", "color": "#aa4a29"})
    meridian.set(aspect="equal", xlim=(-1.48, 1.6), ylim=(-1.85, 1.85), xlabel=r"$x$ (section $y=0$)", ylabel=r"$z$", title="Meridian ellipse")
    meridian.spines[["top", "right"]].set_visible(False)
    meridian.grid(alpha=0.12)
    fig.suptitle(r"$\dfrac{x^2+y^2}{\sinh^2 1}+\dfrac{z^2}{\cosh^2 1}=1$", fontsize=13, y=0.98)
    fig.subplots_adjust(left=0.01, right=0.98, bottom=0.15, top=0.81, wspace=0.28)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=115, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
