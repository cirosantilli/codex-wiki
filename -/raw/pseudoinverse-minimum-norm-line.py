"""The closest solution of x1 + 2 x2 = 3; output to the CWD."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    matrix = np.array([[1., 2.]])
    inverse = np.array([[1.], [2.]]) / 5
    closest = (inverse * 3).ravel()
    kernel = np.array([-2., 1.])
    assert np.allclose(matrix @ closest, 3)
    assert np.allclose(matrix @ kernel, 0)
    assert np.isclose(closest @ kernel, 0)
    t = np.linspace(-1.5, 1.5, 251)
    points = closest[:, None] + kernel[:, None] * t
    assert np.allclose(np.sum(points**2, axis=0), 9 / 5 + 5 * t**2)
    fig, ax = plt.subplots(figsize=(8.2, 6.6), dpi=110)
    fig.patch.set_facecolor("white")
    ax.plot(points[0], points[1], color="#245f9b", lw=2.5,
            label=r"Exact solutions: $x_1+2x_2=3$")
    ax.add_patch(Circle((0, 0), np.linalg.norm(closest), fill=False,
                        color="#8b529f", lw=1.7, linestyle="--"))
    ax.annotate("", closest, (0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#8b529f",
                                lw=2.5, mutation_scale=18))
    ax.scatter([0, closest[0]], [0, closest[1]], s=60,
               c=["#343434", "#8b529f"], zorder=5)
    ax.text(closest[0] + .22, closest[1] + .14,
            r"$x_*=(3/5,6/5)$" "\nSmallest norm", fontsize=12,
            color="#8b529f")
    for shift, offset in [(-1, (.18, .2)), (1, (-.6, -.48))]:
        point = closest + shift * kernel
        ax.plot([0, point[0]], [0, point[1]], color="#b0b0b0", lw=1)
        ax.scatter(*point, color="#245f9b", s=45, zorder=4)
        ax.text(point[0] + offset[0], point[1] + offset[1],
                f"t = {shift:g}\n({point[0]:g}, {point[1]:g})",
                color="#245f9b", fontsize=11)
    unit_kernel = kernel / np.linalg.norm(kernel)
    unit_closest = closest / np.linalg.norm(closest)
    square = np.array([closest - .18 * unit_closest,
                       closest - .18 * unit_closest + .18 * unit_kernel,
                       closest + .18 * unit_kernel])
    ax.plot(square[:, 0], square[:, 1], color="#777777", lw=1.3)
    ax.axhline(0, color="#777777", lw=.8)
    ax.axvline(0, color="#777777", lw=.8)
    ax.set_aspect("equal")
    ax.set_xlim(-3, 4)
    ax.set_ylim(-1.8, 3.6)
    ax.set_xlabel(r"$x_1$", fontsize=13)
    ax.set_ylabel(r"$x_2$", fontsize=13)
    ax.set_title("Pseudoinverse: shortest input giving the required output",
                 fontsize=14, pad=14)
    ax.grid(alpha=.18)
    ax.legend(loc="upper right", fontsize=10)
    fig.text(.5, .035,
             r"All points on the line have zero residual. "
             r"Moving by $t(-2,1)$ adds $5t^2$ to the squared norm.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.08, right=.98, bottom=.12, top=.89)
    fig.savefig(Path.cwd() / "pseudoinverse-minimum-norm-line.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
