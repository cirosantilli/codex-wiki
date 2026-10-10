"""Plot a quadratic bowl and its levels; run from _media with Python 3.14.

Uses matplotlib 3.10.7 and numpy 2.3.5, as specified in pyproject.toml.
Writes an opaque white PNG with this script's basename to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10.2, 4.6), layout="constrained")
    fig.suptitle(r"Positive quadratic energy: $q(x,y)=3x^2+2xy+3y^2$", fontsize=15)
    ax = fig.add_subplot(121, projection="3d")
    grid = np.linspace(-1.4, 1.4, 91)
    x, y = np.meshgrid(grid, grid)
    q = 3 * x**2 + 2 * x * y + 3 * y**2
    ax.plot_surface(x, y, q, cmap="viridis", alpha=0.9, linewidth=0)
    ax.contour(x, y, q, levels=[1, 2, 4, 8], zdir="z", offset=0,
               colors=["#414487", "#2a788e", "#22a884", "#b3b624"])
    ax.scatter([0], [0], [0], color="black", s=25)
    ax.set(xlabel="$x$", ylabel="$y$", zlabel="$q$", zlim=(0, 16))
    ax.set_title("Every nonzero displacement costs energy", fontsize=11)
    ax.view_init(elev=27, azim=-55)
    ax.set_box_aspect((1, 1, 0.8))

    ax = fig.add_subplot(122)
    theta = np.linspace(0, 2 * np.pi, 600)
    eplus = np.array([1.0, 1.0]) / np.sqrt(2)
    eminus = np.array([1.0, -1.0]) / np.sqrt(2)
    for level, color in zip([1, 2, 4, 8],
                            ["#414487", "#2a788e", "#22a884", "#a0a317"]):
        points = (np.sqrt(level / 4) * np.cos(theta)[:, None] * eplus
                  + np.sqrt(level / 2) * np.sin(theta)[:, None] * eminus)
        ax.plot(points[:, 0], points[:, 1], color=color, lw=2,
                label=f"$q={level}$")
    for direction, color in [(eplus, "#ab3f26"), (eminus, "#285494")]:
        ax.plot([-2.1 * direction[0], 2.1 * direction[0]],
                [-2.1 * direction[1], 2.1 * direction[1]],
                "--", color=color, lw=1.2)
    ax.text(0.6, 1.3, r"$e_+,\ \lambda=4$", color="#ab3f26")
    ax.text(0.4, -1.8, r"$e_-,\ \lambda=2$", color="#285494")
    ax.scatter([0], [0], color="black", s=20, zorder=5)
    ax.set(xlabel="$x$", ylabel="$y$", xlim=(-2.1, 2.1), ylim=(-2.1, 2.1))
    ax.set_aspect("equal")
    ax.set_title("Smaller eigenvalue means a longer semi-axis", fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
