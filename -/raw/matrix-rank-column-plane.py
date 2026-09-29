"""Draw original column-space geometry; tested with Python 3.14 and Matplotlib 3.10."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10, 6.4), dpi=100, facecolor="white")
    ax = fig.add_axes((0.02, 0.09, 0.69, 0.80), projection="3d")
    fig.suptitle("Three columns, two independent output directions", fontsize=19, y=0.97)
    u, v = np.meshgrid(np.linspace(-0.25, 3.35, 2), np.linspace(-0.4, 2.4, 2))
    ax.plot_surface(u, 2 * u, v, color="#85b9d6", alpha=0.24, shade=False)
    columns = np.array([[1, 2, 1], [2, 4, 1], [3, 6, 2]], dtype=float)
    colors = ["#176b9b", "#ba6e16", "#6b4196"]
    offsets = [(0.02, -0.2, 0.15), (0.08, 0.05, -0.2), (-0.04, 0.10, 0.12)]
    for index, (column, color, offset) in enumerate(zip(columns, colors, offsets), 1):
        ax.quiver(0, 0, 0, *column, color=color, linewidth=2.8, arrow_length_ratio=0.08)
        ax.text(*(column + offset), rf"$c_{index}$", color=color, fontsize=16)
    for start in columns[:2]:
        ax.plot(*np.stack([start, columns[2]]).T, color="#6b4196", linestyle="--", linewidth=1.4)
    b = np.array([1.0, 2.0, 0.0])
    impossible = np.array([1.0, 3.0, 0.0])
    foot = np.array([1.4, 2.8, 0.0])
    ax.scatter(*b, color="#238452", s=70, depthshade=False)
    ax.scatter(*impossible, color="#c53636", marker="x", linewidths=2.5, s=80, depthshade=False)
    ax.plot(*np.stack([foot, impossible]).T, color="#c53636", linestyle=":", linewidth=2)
    ax.text(0.86, 1.75, -0.23, r"$b$", color="#238452", fontsize=15)
    ax.text(0.94, 3.30, 0.0, r"$b'$", color="#c53636", fontsize=15)
    ax.scatter(0, 0, 0, color="#333333", s=18, depthshade=False)
    ax.set(xlim=(-0.4, 3.6), ylim=(-0.8, 7.2), zlim=(-0.5, 2.6))
    ax.set_xlabel(r"$b_1$", labelpad=8)
    ax.set_ylabel(r"$b_2$", labelpad=8)
    ax.set_zlabel(r"$b_3$", labelpad=7)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_yticks([0, 2, 4, 6])
    ax.set_zticks([0, 1, 2])
    ax.view_init(elev=24, azim=-54)
    ax.set_box_aspect((4, 6, 3.2))
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor("white")
    fig.text(0.73, 0.80, r"$c_1=(1,2,1)^T$", color=colors[0], fontsize=15)
    fig.text(0.73, 0.74, r"$c_2=(2,4,1)^T$", color=colors[1], fontsize=15)
    fig.text(0.73, 0.68, r"$c_3=c_1+c_2$", color=colors[2], fontsize=16)
    fig.text(0.73, 0.55, r"Image plane: $b_2=2b_1$", fontsize=14)
    fig.text(0.73, 0.48, "Rank = 2", fontsize=17)
    fig.text(0.73, 0.36, r"$b=(1,2,0)^T$", color="#238452", fontsize=15)
    fig.text(0.73, 0.31, r"$b=-c_1+c_2$", color="#238452", fontsize=14)
    fig.text(0.73, 0.20, r"$b'=(1,3,0)^T$", color="#c53636", fontsize=15)
    fig.text(0.73, 0.15, r"$3\ne 2\cdot1$: unreachable", color="#c53636", fontsize=12)
    fig.legend(handles=[Patch(facecolor="#85b9d6", alpha=0.5, label="Column space"),
                        Line2D([0], [0], color="#6b4196", linestyle="--", label="Column addition")],
               loc="lower left", bbox_to_anchor=(0.10, 0.015), frameon=False, ncol=2)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
