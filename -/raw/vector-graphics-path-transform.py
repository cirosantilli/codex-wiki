"""Original quadratic path and affine image; no SVG assets are written.

Run from _media with MPLBACKEND=Agg. Tested with Python 3.14,
NumPy 2.3 and Matplotlib 3.10; output goes to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path as PlotPath
import numpy as np


CONTROL = np.array([[1.0, 4.0], [3.0, 0.0], [5.0, 4.0]])
LINEAR = np.array([[1.5, 0.5], [0.0, 1.0]])
OFFSET = np.array([1.0, 1.0])


def bezier(t, points):
    t = np.asarray(t)[..., None]
    return (1 - t) ** 2 * points[0] + 2 * t * (1 - t) * points[1] + t**2 * points[2]


def transform(points):
    return np.asarray(points) @ LINEAR.T + OFFSET


def main():
    mapped = transform(CONTROL)
    np.testing.assert_allclose(mapped, [[4.5, 5], [5.5, 1], [10.5, 5]])
    np.testing.assert_allclose(bezier(0.5, CONTROL), [3, 2])
    np.testing.assert_allclose(bezier(0.5, mapped), [6.5, 3])
    samples = np.linspace(0, 1, 501)
    np.testing.assert_allclose(bezier(samples, mapped), transform(bezier(samples, CONTROL)))

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.6), dpi=110)
    fig.subplots_adjust(left=0.07, right=0.98, bottom=0.21, top=0.79, wspace=0.24)
    fig.suptitle("Stored path geometry and an affine transformation", y=0.98, fontsize=16)
    fig.text(0.5, 0.91, r"Analytical illustration • $T(x,y)=(1.5x+0.5y+1,\ y+1)$", ha="center", fontsize=12)

    configurations = [
        (CONTROL, "Original: M 1 4 Q 3 0 5 4 Z", (0, 6), (-0.8, 5.1), r"Filled area $16/3$"),
        (mapped, "Image: M 4.5 5 Q 5.5 1 10.5 5 Z", (3.5, 11.5), (-0.1, 6.1), r"Filled area $8$; area factor $|\det A|=1.5$"),
    ]
    for ax, (points, title, xlim, ylim, note) in zip(axes, configurations):
        path = PlotPath(np.vstack([points, points[0]]),
                        [PlotPath.MOVETO, PlotPath.CURVE3, PlotPath.CURVE3, PlotPath.CLOSEPOLY])
        ax.add_patch(PathPatch(path, facecolor="#cfe8f5", edgecolor="#136a9b", lw=2.3, zorder=2))
        ax.plot(points[:, 0], points[:, 1], "--", color="#7a7a7a", lw=1.4, zorder=3)
        ax.scatter(points[:, 0], points[:, 1], s=36, color="#333333", zorder=4)
        middle = bezier(0.5, points)
        ax.scatter(*middle, marker="D", s=46, color="#c35718", zorder=5)
        for index, (x, y) in enumerate(points):
            shift = (0, 13) if index == 1 else (0, -22)
            ax.annotate(f"P{index} ({x:g}, {y:g})", (x, y), xytext=shift,
                        textcoords="offset points", ha="center", fontsize=10)
        ax.annotate(f"t = 1/2\n({middle[0]:g}, {middle[1]:g})", middle,
                    xytext=(12, 12), textcoords="offset points", color="#994411", fontsize=10)
        ax.set(xlim=xlim, ylim=ylim, xlabel="x", ylabel="y (increases downward)")
        ax.invert_yaxis()
        ax.set_aspect("equal", adjustable="box")
        ax.set_title(title, fontsize=11, pad=14)
        ax.grid(color="#eeeeee", lw=0.7)
        ax.text(0.5, -0.24, note, transform=ax.transAxes, ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Blue: filled path and closing segment   •   Dashed: control polygon   •   Orange: curve midpoint",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
