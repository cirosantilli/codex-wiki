"""Q6 quadric sketches; Python 3.14.4, root pyproject.toml dependencies.

Write the opaque PNG to cwd. Run in the matching _media course directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.linspace(0, 2 * np.pi, 100)
    fig = plt.figure(figsize=(11.4, 4.8), facecolor="white")
    titles = [r"$\Sigma_1$: two sheets", r"$\Sigma_0$: elliptic cone", r"$\Sigma_{-1}$: one sheet"]
    for index, level in enumerate([1, 0, -1], 1):
        ax = fig.add_subplot(1, 3, index, projection="3d")
        if level == 1:
            radial, angle = np.meshgrid(np.linspace(0, 1.55, 40), theta)
            for sign in [-1, 1]:
                u = sign * np.sqrt(1 + radial**2) / np.sqrt(6)
                v = radial * np.cos(angle) / np.sqrt(3)
                w = radial * np.sin(angle) / 2
                ax.plot_surface(u, v, w, color="#3d87b3", alpha=0.61, linewidth=0, antialiased=True)
            ax.scatter([-1 / np.sqrt(6), 1 / np.sqrt(6)], [0, 0], [0, 0], c="#a23c29", s=22, depthshade=False)
        else:
            u, angle = np.meshgrid(np.linspace(-0.85, 0.85, 65), theta)
            radial = np.sqrt(6 * u**2 - level)
            v = radial * np.cos(angle) / np.sqrt(3)
            w = radial * np.sin(angle) / 2
            ax.plot_surface(u, v, w, color="#3d87b3", alpha=0.61, linewidth=0, antialiased=True)
            if level == 0:
                ax.scatter([0], [0], [0], c="#a23c29", s=22, depthshade=False)
            else:
                ax.plot(np.zeros_like(theta), np.cos(theta) / np.sqrt(3), np.sin(theta) / 2, color="#a23c29", lw=2.1)
        for coordinate in range(3):
            axis = [np.zeros(2), np.zeros(2), np.zeros(2)]
            axis[coordinate] = np.array([-1.35, 1.35])
            ax.plot(*axis, color="#555555", lw=0.65)
        ax.set(xlabel=r"$u$", ylabel=r"$v$", zlabel=r"$w$", xlim=(-1.05, 1.05), ylim=(-1.35, 1.35), zlim=(-1.35, 1.35), title=titles[index - 1])
        ax.set_box_aspect((1.1, 1.35, 1.35))
        ax.view_init(elev=23, azim=-57)
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.set_zticks([-1, 0, 1])
        ax.tick_params(labelsize=8, pad=0)
        ax.grid(alpha=0.2)
    fig.suptitle(r"$6u^2-3v^2-4w^2=\alpha$", fontsize=15, y=0.98)
    fig.subplots_adjust(left=0.005, right=0.96, bottom=0.15, top=0.83, wspace=0.09)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
