"""Acceleration decomposition of r(t)=(t,t²) at t=1; PNG to CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    point = np.array([1., 1.])
    velocity = np.array([1., 2.])
    acceleration = np.array([0., 2.])
    speed = np.linalg.norm(velocity)
    tangent = velocity / speed
    normal = np.array([-2., 1.]) / speed
    tangential = (acceleration @ tangent) * tangent
    normal_part = (acceleration @ normal) * normal
    curvature = 2 / (5*np.sqrt(5))
    assert np.allclose(tangential, [4/5, 8/5])
    assert np.allclose(normal_part, [-4/5, 2/5])
    assert np.allclose(tangential + normal_part, acceleration)
    assert np.isclose(acceleration @ tangent, 4/np.sqrt(5))
    assert np.isclose(acceleration @ normal, curvature*speed**2)
    fig, ax = plt.subplots(figsize=(8.6, 6.4), dpi=110)
    fig.patch.set_facecolor("white")
    x = np.linspace(-.8, 2.2, 251)
    ax.plot(x, x*x, color="#777777", lw=2, label=r"Path $r(t)=(t,t^2)$")
    ax.scatter(*point, color="#343434", s=45, zorder=5)
    for displacement, color in [(acceleration, "#343434"),
                                (tangential, "#245f9b"), (normal_part, "#c56521")]:
        ax.annotate("", point + displacement, point,
                    arrowprops=dict(arrowstyle="-|>", color=color,
                                    lw=2.5, mutation_scale=18))
    for end in [point+tangential, point+normal_part]:
        ax.plot([end[0], (point+acceleration)[0]],
                [end[1], (point+acceleration)[1]],
                color="#aaaaaa", ls="--", lw=1.3)
    ax.text(.62, .68, "P = (1, 1)", fontsize=11)
    ax.text(1.04, 3.12, "a = (0, 2)", fontsize=12)
    ax.text(1.88, 2.38, "Tangent part\n(0.8, 1.6)", fontsize=12,
            color="#245f9b")
    ax.text(-.61, 1.53, "Normal part\n(−0.8, 0.4)", fontsize=12,
            color="#c56521")
    ax.set_xlim(-1, 3.6)
    ax.set_ylim(-.2, 4.8)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Acceleration changes both speed and direction", fontsize=15)
    ax.grid(alpha=.16)
    ax.legend(loc="upper left", fontsize=10)
    fig.text(.5, .04,
             "At t = 1: tangential acceleration increases speed; "
             "normal acceleration turns the velocity. Dimensionless model.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.07, right=.98, bottom=.14, top=.9)
    fig.savefig(Path.cwd() / "tangent-normal-acceleration-on-parabola.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
