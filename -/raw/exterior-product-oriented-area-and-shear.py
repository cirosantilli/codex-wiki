"""Original oriented-area comparison: u wedge v = u wedge (v + u).

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Write basename.png to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    u = np.array([3.0, 1.0])
    v = np.array([1.0, 2.0])
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.5), dpi=120)
    fig.patch.set_facecolor("white")
    for ax, other, label, title in zip(
        axes, [v, v+u], ["v = (1, 2)", "v + u = (4, 3)"],
        ["Original pair", "Sheared pair, same area"]
    ):
        points = np.array([[0., 0.], u, u+other, other])
        ax.add_patch(Polygon(points, closed=True, facecolor="#c7e9c0",
                             edgecolor="#238b45", linewidth=2))
        for vector, color in [(u, "#2166ac"), (other, "#c65102")]:
            ax.annotate("", vector, xytext=(0, 0),
                        arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.6})
        ax.annotate("u = (3, 1)", u, xytext=(9, -13), textcoords="offset points",
                    color="#2166ac", fontsize=11)
        ax.annotate(label, other, xytext=(-3, 12), textcoords="offset points",
                    color="#c65102", fontsize=11)
        center = points.mean(axis=0)
        ax.text(center[0], center[1], "Area = +5", ha="center", va="center",
                fontsize=12, color="#145a26",
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85})
        ax.scatter(points[:, 0], points[:, 1], color="#333333", s=15)
        ax.set(xlim=(-0.5, 7.8), ylim=(-0.4, 4.8), xlabel="x", ylabel="y",
               title=title, xticks=[0, 2, 4, 6], yticks=[0, 2, 4])
        ax.set_aspect("equal")
        ax.grid(alpha=0.22)
        ax.text(0.02, 0.97, "Reverse the order: area = −5",
                transform=ax.transAxes, va="top", fontsize=10)
    fig.suptitle(r"$u\wedge v = u\wedge(v+u) = 5e_1\wedge e_2$", fontsize=18)
    fig.subplots_adjust(left=0.05, right=0.985, bottom=0.15, top=0.80, wspace=0.20)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
