"""Sketch Question 2(a); write the PNG in the current working directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10.8, 7.7))
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.08, top=0.93, wspace=0.14, hspace=0.43)
    axes = [fig.add_subplot(2, 3, i + 1, projection="3d") for i in range(5)]
    for ax in axes:
        ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$")
        ax.set_box_aspect((1, 1, 1))
        ax.view_init(elev=22, azim=-55)
        ax.xaxis.set_pane_color((1, 1, 1, 1))
        ax.yaxis.set_pane_color((1, 1, 1, 1))
        ax.zaxis.set_pane_color((1, 1, 1, 1))
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
        ax.set_zticks([-1, 0, 1])

    azimuth, polar = np.meshgrid(np.linspace(0, 2 * np.pi, 65), np.linspace(0, np.pi, 35))
    axes[0].plot_surface(np.sin(polar) * np.cos(azimuth), np.sin(polar) * np.sin(azimuth), np.cos(polar), color="#72b4dc", alpha=0.8, linewidth=0.2, edgecolor="white")
    axes[0].set_title("Unit sphere\n$x^2+y^2+z^2=1$")

    angle, radius = np.meshgrid(np.linspace(0, 2 * np.pi, 65), np.linspace(0, 1.1, 30))
    axes[1].plot_surface(radius * np.cos(angle), radius * np.sin(angle), radius**2, color="#75bf95", alpha=0.85, linewidth=0.2, edgecolor="white")
    axes[1].set_title("Circular paraboloid\n$z=x^2+y^2$")

    z = np.linspace(-1.2, 1.2, 50)
    axes[2].plot(np.zeros_like(z), np.zeros_like(z), z, color="#2669ad", linewidth=3)
    axes[2].set(xlim=(-1, 1), ylim=(-1, 1), zlim=(-1.2, 1.2))
    axes[2].set_title("$a>0$: the $z$ axis\n$ax^2+y^2=0$")

    x, z = np.meshgrid(np.linspace(-1.1, 1.1, 15), np.linspace(-1.2, 1.2, 15))
    axes[3].plot_surface(x, np.zeros_like(x), z, color="#b296cf", alpha=0.75, linewidth=0.3, edgecolor="white")
    axes[3].set(ylim=(-1.1, 1.1))
    axes[3].set_title("$a=0$: one plane\n$y^2=0$, hence $y=0$")

    axes[4].plot_surface(x, x, z, color="#e49c67", alpha=0.6, linewidth=0.3, edgecolor="white")
    axes[4].plot_surface(x, -x, z, color="#72b4dc", alpha=0.6, linewidth=0.3, edgecolor="white")
    axes[4].plot(np.zeros(50), np.zeros(50), np.linspace(-1.2, 1.2, 50), color="#333333", linewidth=2)
    axes[4].set_title("$a<0$: two intersecting planes\n" + r"$y=\pm\sqrt{-a}\,x$ ($a=-1$ drawn)")

    note = fig.add_subplot(2, 3, 6)
    note.axis("off")
    note.text(0.05, 0.73, "$ax^2+y^2=0$\n\nThe coordinate $z$ is unrestricted.\n\nA line, a repeated plane, or two planes\ncan therefore occur.\n\nInfinite sets are shown in finite windows.", va="top", linespacing=1.5)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
