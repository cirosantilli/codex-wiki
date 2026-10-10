"""Plot a computed linear combination and its coordinate grid; PNG goes to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run: make _media/linear-combination-coordinates.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def arrow(ax, start, end, color, width=2.6, style="-", zorder=4):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color=color, lw=width,
                                linestyle=style, shrinkA=0, shrinkB=0,
                                mutation_scale=17), zorder=zorder)


def main():
    v1, v2 = np.array([1., 1.]), np.array([1., -1.])
    basis = np.column_stack((v1, v2))
    target = np.array([3., 1.])
    coefficients = np.array([2., 1.])
    assert np.allclose(basis @ coefficients, target)
    assert np.allclose(np.linalg.solve(basis, target), coefficients)
    assert np.isclose(np.linalg.det(basis), -2.)
    # Check the general formula on a two-dimensional grid, including negatives.
    x, y = np.meshgrid(np.linspace(-4, 4, 17), np.linspace(-3, 3, 13))
    points = np.vstack((x.ravel(), y.ravel()))
    coords = np.vstack(((points[0] + points[1]) / 2,
                        (points[0] - points[1]) / 2))
    assert np.allclose(basis @ coords, points)
    assert np.allclose(basis @ [1, -1], [0, 2])

    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(7.4, 6.3), facecolor="white")
    fig.subplots_adjust(left=.10, right=.96, bottom=.22, top=.83)
    blue, orange, green = "#2466a3", "#c15a16", "#217346"
    ax.set_facecolor("white")
    ax.set_aspect("equal")
    ax.set_xlim(-1.4, 4.2)
    ax.set_ylim(-1.7, 3.0)
    ax.set_xticks(range(-1, 5))
    ax.set_yticks(range(-1, 4))
    ax.set_xlabel("x")
    ax.set_ylabel("y", rotation=0, labelpad=10)
    ax.axhline(0, color="#888888", lw=.8)
    ax.axvline(0, color="#888888", lw=.8)
    parameter = np.array([-8., 8.])
    for k in range(-5, 6):
        first_fixed = k * v1[:, None] + v2[:, None] * parameter
        second_fixed = v1[:, None] * parameter + k * v2[:, None]
        ax.plot(*first_fixed, color="#dddddd", lw=.8, zorder=0)
        ax.plot(*second_fixed, color="#dddddd", lw=.8, zorder=0)
    corners = np.array([[0, 0], 2*v1, target, v2])
    ax.fill(*corners.T, color="#eef3dc", zorder=1)
    arrow(ax, [0, 0], 2*v1, blue, width=3)
    arrow(ax, 2*v1, target, orange, width=3)
    arrow(ax, [0, 0], v2, orange)
    arrow(ax, v2, target, blue, style="--", width=2)
    arrow(ax, [0, 0], target, green, width=3.2)
    ax.plot(*target, "o", color=green, ms=6, zorder=5)
    ax.text(3.08, 1.18, r"$w=(3,1)$", color=green)
    ax.text(.05, 1.55, r"$2v_1=(2,2)$", color=blue,
            bbox=dict(facecolor="white", edgecolor="none", alpha=.9, pad=2))
    ax.text(2.70, 1.78, r"$+v_2$", color=orange)
    ax.text(.8, -1.3, r"$v_2=(1,-1)$", color=orange)
    ax.text(2.35, -.30, r"$+2v_1$", color=blue)
    ax.text(-.08, -.16, "O", ha="right", va="top")
    fig.suptitle("Two coefficients choose one arrow", fontsize=18, y=.96)
    fig.text(.5, .885, r"$v_1=(1,1),\quad v_2=(1,-1),\quad w=2v_1+v_2$",
             ha="center", fontsize=13)
    fig.text(.5, .10, "Diagonal grid: keep one coefficient fixed, vary the other.",
             ha="center", fontsize=11)
    fig.text(.5, .04, r"$(x,y)=\frac{x+y}{2}v_1+\frac{x-y}{2}v_2$",
             ha="center", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                dpi=140, facecolor="white", transparent=False)
    plt.close(fig)
    print("Verified target, unique coefficients, and formula at 221 points.")


if __name__ == "__main__":
    main()
