"""Compare active quarter-turn orders about fixed x and z axes.

Write the matching opaque PNG to CWD. Tested with Python 3.14,
matplotlib 3.10.7 and numpy 2.3.5; run from _media with MPLBACKEND=Agg.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def rotate_x(angle, vector):
    x, y, z = vector
    c, s = np.cos(angle), np.sin(angle)
    return np.array([x, c * y - s * z, s * y + c * z])


def rotate_z(angle, vector):
    x, y, z = vector
    c, s = np.cos(angle), np.sin(angle)
    return np.array([c * x - s * y, s * x + c * y, z])


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(9, 4.8), facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.21, top=0.82, wspace=0.03)
    start = np.array([1.0, 1.0, 0.0])
    colors = ["#657789", "#196ba1", "#c14b23"]
    turns = [(rotate_x, rotate_z), (rotate_z, rotate_x)]
    titles = [r"First $R_x$, then $R_z$", r"First $R_z$, then $R_x$"]
    lines = [r"$(1,1,0)\to(1,0,1)\to(0,1,1)$",
             r"$(1,1,0)\to(-1,1,0)\to(-1,0,1)$"]
    for number, (functions, title, line) in enumerate(zip(turns, titles, lines), 1):
        ax = fig.add_subplot(1, 2, number, projection="3d", facecolor="white")
        intermediate = functions[0](np.pi / 2, start)
        end = functions[1](np.pi / 2, intermediate)
        for axis, name in zip(np.eye(3), ["x", "y", "z"]):
            ax.plot(*np.stack([-1.4 * axis, 1.65 * axis], axis=1),
                    color="#c1c8cf", lw=1.2)
            ax.text(*(1.78 * axis), name, fontsize=12, color="#4d5258")
        for vector, color in zip([start, intermediate, end], colors):
            ax.quiver(0, 0, 0, *vector, color=color, linewidth=2.7,
                      arrow_length_ratio=0.13)
        for function, vector, color in zip(functions, [start, intermediate], colors[1:]):
            curve = np.stack([function(t, vector) for t in np.linspace(0, np.pi / 2, 100)])
            ax.plot(*curve.T, color=color, lw=2, linestyle="--")
            tangent = curve[-1] - curve[-8]
            ax.quiver(*curve[-8], *tangent, color=color, linewidth=2,
                      arrow_length_ratio=0.6)
        ax.set(xlim=(-1.45, 1.8), ylim=(-1.45, 1.8), zlim=(-0.5, 1.8))
        ax.set_box_aspect((1, 1, 0.85))
        ax.view_init(elev=23, azim=35)
        ax.set_axis_off()
        ax.set_title(title, fontsize=16, pad=8)
        ax.text2D(0.5, -0.055, line, transform=ax.transAxes, ha="center", fontsize=12)
    fig.suptitle("Order matters for rotations in three dimensions", fontsize=19)
    fig.text(0.5, 0.09, "Gray: initial vector   ·   Blue: after first turn   ·   Orange: final vector",
             ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Active +90° turns · right-hand rule · fixed axes · column vectors · all lengths √2",
             ha="center", fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
