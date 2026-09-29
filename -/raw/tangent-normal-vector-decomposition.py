"""Orthogonal projections at (1,1) on a parabola; PNG to current directory."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    point = np.array([1., 1.])
    tangent = np.array([1., 2.]) / np.sqrt(5)
    normal = np.array([-2., 1.]) / np.sqrt(5)
    vector = np.array([3., 1.])
    along = (vector @ tangent) * tangent
    across = (vector @ normal) * normal
    assert np.allclose(along, [1, 2])
    assert np.allclose(across, [2, -1])
    assert np.allclose(along + across, vector)
    assert np.isclose(along @ across, 0)
    assert np.isclose(np.linalg.norm(vector)**2,
                      np.linalg.norm(along)**2 + np.linalg.norm(across)**2)
    fig, ax = plt.subplots(figsize=(9.2, 6.3), dpi=110)
    fig.patch.set_facecolor("white")
    x = np.linspace(-1.1, 2.3, 250)
    ax.plot(x, x*x, color="#777777", lw=2, label=r"Curve $y=x^2$")
    ax.scatter(*point, color="#343434", s=45, zorder=5)
    for displacement, color in [(vector, "#343434"),
                                (along, "#245f9b"), (across, "#c56521")]:
        ax.annotate("", point + displacement, point,
                    arrowprops=dict(arrowstyle="-|>", color=color,
                                    lw=2.5, mutation_scale=18))
    for endpoint in [point+along, point+across]:
        ax.plot([endpoint[0], (point+vector)[0]],
                [endpoint[1], (point+vector)[1]],
                color="#aaaaaa", ls="--", lw=1.3)
    ax.text(.5, .55, "P = (1, 1)", fontsize=11)
    ax.text(2.08, 3.15, "Tangent part\n(1, 2)", color="#245f9b", fontsize=12)
    ax.text(3.1, -.45, "Normal part\n(2, −1)", color="#c56521", fontsize=12)
    ax.text(4.05, 2.13, "w = (3, 1)", fontsize=12)
    ax.set_xlim(-1.3, 5.4)
    ax.set_ylim(-.9, 5.2)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("A vector splits along the local tangent and normal", fontsize=15)
    ax.grid(alpha=.16)
    ax.legend(loc="upper left", fontsize=10)
    fig.text(.5, .035,
             "Arrows share the base point P; dashed connectors show vector addition. "
             "The two components are perpendicular.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.07, right=.98, bottom=.13, top=.9)
    fig.savefig(Path.cwd() / "tangent-normal-vector-decomposition.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
