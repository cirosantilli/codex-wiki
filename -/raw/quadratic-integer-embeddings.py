"""Draw the coefficient lattice and both real embeddings of Z[sqrt(2)].

PNG output goes to the current working directory.
Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    root_two = np.sqrt(2)
    transform = np.array([[1, root_two], [1, -root_two]])
    coefficients = np.array([(a, b) for a in range(-8, 9) for b in range(-8, 9)])
    images = coefficients @ transform.T
    cell = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    assert np.isclose(abs(np.linalg.det(transform)), np.sqrt(8))
    assert np.allclose(images[:, 0] * images[:, 1],
                       coefficients[:, 0]**2 - 2 * coefficients[:, 1]**2)

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.3), dpi=120)
    colors = ["#186b9c", "#a65419", "#853a96", "#16815a"]
    marked = [(1, 0), (0, 1), (1, 1), (3, 2)]
    labels = [r"$1$", r"$\sqrt{2}$", r"$1+\sqrt{2}$", r"$3+2\sqrt{2}$"]
    offsets = [[(8, -19), (-15, 12), (9, 10), (-74, 12)],
               [(-13, 14), (-35, -23), (11, -20), (-72, 30)]]
    for panel, ax in enumerate(axes):
        points = coefficients if panel == 0 else images
        ax.scatter(points[:, 0], points[:, 1], s=12, color="#b3bec8", zorder=2)
        ax.add_patch(Polygon(cell if panel == 0 else cell @ transform.T,
                             facecolor="#dbeaf7", edgecolor="#48779a", linewidth=1.6,
                             zorder=1))
        ax.axhline(0, color="#c0c7ce", lw=0.8)
        ax.axvline(0, color="#c0c7ce", lw=0.8)
        for k, (pair, label, color) in enumerate(zip(marked, labels, colors)):
            point = np.array(pair) if panel == 0 else transform @ pair
            ax.scatter(*point, s=65, color=color, zorder=4)
            ax.annotate(label, point, xytext=offsets[panel][k],
                        textcoords="offset points", color=color, fontsize=12,
                        bbox={"facecolor": "white", "edgecolor": "none", "pad": 1},
                        arrowprops={"arrowstyle": "-", "color": color} if k == 3 else None,
                        zorder=5)
        ax.set_aspect("equal")
        ax.grid(alpha=0.12)
    axes[0].set(xlim=(-3.5, 4.5), ylim=(-3.5, 4.5), xlabel=r"coefficient $a$",
                ylabel=r"coefficient $b$", title=r"$a+b\sqrt{2}$: integer coefficients")
    axes[0].set_xticks(range(-3, 5))
    axes[0].set_yticks(range(-3, 5))
    axes[1].set(xlim=(-7.5, 7.5), ylim=(-7.5, 7.5), xlabel=r"$x=a+b\sqrt{2}$",
                ylabel=r"$y=a-b\sqrt{2}$", title=r"Both embeddings: $N=xy$")
    for sign, color in [(1, "#16815a"), (-1, "#853a96")]:
        for branch in [-1, 1]:
            x = branch * np.geomspace(1 / 7.5, 7.5, 350)
            axes[1].plot(x, sign / x, color=color, lw=1, alpha=0.65, zorder=0)
    axes[1].text(-7, 6.7, r"$xy=-1$", color="#853a96", fontsize=11)
    axes[1].text(4.7, 6.7, r"$xy=1$", color="#16815a", fontsize=11)
    fig.suptitle(r"One quadratic integer, two real values", fontsize=16, y=0.97)
    fig.text(0.5, 0.035, r"Shaded basis cells: area $1$ on the left, $2\sqrt{2}$ on the right."
             "  Colored points represent the same elements.", ha="center", fontsize=11)
    fig.subplots_adjust(left=0.065, right=0.98, bottom=0.17, top=0.85, wspace=0.27)
    fig.savefig(Path.cwd() / "quadratic-integer-embeddings.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
