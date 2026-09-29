"""Original affine geometry example; write the matching opaque PNG to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def transform(points):
    return np.asarray(points) @ np.array([[2.0, 0.0], [1.0, 1.0]]) + [1.0, -2.0]


def main():
    triangle = np.array([[0., 0.], [2., 0.], [0., 2.]])
    assert np.array_equal(transform(triangle), [[1., -2.], [5., -2.], [3., 0.]])
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.3), dpi=100, facecolor="white")
    fig.suptitle(r"Affine map: $T(x,y)=(2x+y+1,\ y-2)$", fontsize=17)
    for ax, mapped in zip(axes, [False, True]):
        for level in np.arange(-1., 4.):
            for line in [np.array([[-1., level], [3., level]]), np.array([[level, -1.], [level, 3.]])]:
                points = transform(line) if mapped else line
                ax.plot(points[:, 0], points[:, 1], color="#c8d3dc", lw=1, zorder=0)
        vertices = transform(triangle) if mapped else triangle
        closed = np.vstack([vertices, vertices[0]])
        ax.fill(vertices[:, 0], vertices[:, 1], color="#d9eaf5", alpha=.8)
        ax.plot(closed[:, 0], closed[:, 1], "o-", color="#245e91", lw=2.5, markersize=6)
        for name, point, offset in zip(["A", "B", "C"], vertices, [(-8,-24),(9,-15),(-16,12)]):
            label = name + ("′" if mapped else "")
            ax.annotate(f"{label} = ({point[0]:g}, {point[1]:g})", point, xytext=offset, textcoords="offset points", fontsize=11)
        ax.axhline(0, color="#555", lw=.8, zorder=0)
        ax.axvline(0, color="#555", lw=.8, zorder=0)
        ax.set_aspect("equal", adjustable="box")
        ax.set(xlim=((-3,11) if mapped else (-1.7,3.7)), ylim=((-3.7,1.7) if mapped else (-1.7,3.7)))
        ax.set_xlabel("x′" if mapped else "x", fontsize=12)
        ax.set_ylabel("y′" if mapped else "y", fontsize=12)
        ax.set_title("After: area 4, angle at A′ = 45°" if mapped else "Before: area 2, angle at A = 90°", fontsize=12, pad=12)
        ax.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(left=.065, right=.975, bottom=.13, top=.83, wspace=.27)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
