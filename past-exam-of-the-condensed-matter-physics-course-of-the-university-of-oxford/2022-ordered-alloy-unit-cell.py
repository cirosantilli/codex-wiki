"""Draw the ordered Cu3Au cell; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def main():
    fig = plt.figure(figsize=(7.2, 5.8), dpi=140, facecolor="white")
    ax = fig.add_subplot(111, projection="3d", facecolor="white")
    corners = np.array(list(product((0, 1), repeat=3)))
    faces = np.array([(0, .5, .5), (1, .5, .5), (.5, 0, .5),
                      (.5, 1, .5), (.5, .5, 0), (.5, .5, 1)])
    for p in corners:
        for axis in range(3):
            if p[axis] == 0:
                q = p.copy()
                q[axis] = 1
                ax.plot(*np.array([p, q]).T, color="#777777", lw=1.3)
    ax.scatter(*corners.T, s=170, c="#e3ad24", edgecolors="#6e5210",
               depthshade=False, zorder=3)
    ax.scatter(*faces.T, s=130, c="#cf7251", edgecolors="#713522",
               depthshade=False, zorder=4)
    ax.set(xlabel="x / a", ylabel="y / a", zlabel="z / a",
           xticks=[0, .5, 1], yticks=[0, .5, 1], zticks=[0, .5, 1])
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=21, azim=32)
    ax.grid(False)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.fill = False
    ax.set_title("Ordered Cu₃Au: chemically distinct corner and face sites", pad=18)
    handles = [Line2D([], [], marker="o", ls="", color="#e3ad24", markersize=10,
                      label="Au: 8 corners × 1/8 = 1 atom"),
               Line2D([], [], marker="o", ls="", color="#cf7251", markersize=10,
                      label="Cu: 6 faces × 1/2 = 3 atoms")]
    fig.legend(handles=handles, loc="lower center", frameon=False, ncol=1)
    fig.subplots_adjust(top=.89, bottom=.16, left=.02, right=.95)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
