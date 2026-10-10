"""Original bivector and its three signed coordinate-plane projections.

Inputs u=(1,2,0), v=(0,1,3); coefficients (1,3,6) in e12,e13,e23.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Write basename.png to the current working directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 14})
    u = np.array([1., 2., 0.])
    v = np.array([0., 1., 3.])
    points = np.array([[0., 0., 0.], u, u+v, v])
    fig = plt.figure(figsize=(9.6, 6.7), dpi=120, facecolor="white")
    space = fig.add_subplot(2, 2, 1, projection="3d")
    space.add_collection3d(Poly3DCollection([points], facecolors="#c7e9c0",
                                          edgecolors="#238b45", alpha=0.7, linewidths=1.7))
    space.quiver(0, 0, 0, *u, color="#2166ac", linewidth=2.5, arrow_length_ratio=0.12)
    space.quiver(0, 0, 0, *v, color="#c65102", linewidth=2.5, arrow_length_ratio=0.12)
    space.text(*u, "u", color="#2166ac", fontsize=14)
    space.text(*v, "v", color="#c65102", fontsize=14)
    space.set(xlabel="x", ylabel="y", zlabel="z", xlim=(0, 1.3), ylim=(0, 3.5),
              zlim=(0, 3.5), title="Full area = √46")
    space.set_box_aspect((1.3, 3.5, 3.5))
    space.view_init(elev=24, azim=-48)
    space.set_xticks([0, 1])
    space.set_yticks([0, 1, 2, 3])
    space.set_zticks([0, 1, 2, 3])

    for position, pair, labels, area in [
        (2, (0, 1), ("x", "y"), 1),
        (3, (0, 2), ("x", "z"), 3),
        (4, (1, 2), ("y", "z"), 6)
    ]:
        ax = fig.add_subplot(2, 2, position)
        projected = points[:, pair]
        ax.add_patch(Polygon(projected, closed=True, facecolor="#c7e9c0",
                             edgecolor="#238b45", linewidth=2))
        for vector, color in [(u[list(pair)], "#2166ac"), (v[list(pair)], "#c65102")]:
            if np.linalg.norm(vector):
                ax.annotate("", vector, xytext=(0, 0),
                            arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.5})
        center = projected.mean(axis=0)
        ax.text(*center, f"+{area}", ha="center", va="center", fontsize=18,
                color="#145a26",
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85})
        ax.set(xlabel=labels[0], ylabel=labels[1],
               title=f"{''.join(labels)} projection: signed area {area}",
               xlim=(-0.2, float(projected[:, 0].max())+0.35),
               ylim=(-0.2, float(projected[:, 1].max())+0.35))
        ax.set_aspect("equal")
        ax.grid(alpha=0.22)
    fig.suptitle(r"$u\wedge v=e_1\wedge e_2+3e_1\wedge e_3+6e_2\wedge e_3$",
                 fontsize=17, y=0.975)
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.08, top=0.88,
                        wspace=0.24, hspace=0.44)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
