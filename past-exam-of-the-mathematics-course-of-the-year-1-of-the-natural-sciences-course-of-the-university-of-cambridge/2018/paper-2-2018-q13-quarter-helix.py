"""Original helix sketch; Python 3.14 with root NumPy/Matplotlib deps.

Write the PNG basename in cwd for mirrored _media rendering.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, np.pi/12, 500)
    x, y, z = np.cos(6*t), np.sin(6*t), 8*t
    fig = plt.figure(figsize=(6.8, 6.0), facecolor="white")
    ax = fig.add_subplot(projection="3d")
    fig.subplots_adjust(left=0.01, right=0.87, bottom=0.14, top=0.92)
    ax.plot(x, y, z, color="#176b9b", lw=2.6)
    ax.plot(x, y, np.zeros_like(z), "--", color="0.6", lw=1.0)
    ax.plot([0, 0], [1, 1], [0, 2*np.pi/3], ":", color="0.6", lw=1.0)
    ax.scatter([1, 0], [0, 1], [0, 2*np.pi/3], color="#b83c32", s=30, depthshade=False)
    ax.text(1, 0, -0.15, "start $(1,0,0)$", fontsize=9)
    ax.text(0.04, 1.03, 2*np.pi/3, "end $(0,1,2\\pi/3)$", fontsize=9)
    ta = np.pi/24
    pos = np.array([np.cos(6*ta), np.sin(6*ta), 8*ta])
    tangent = np.array([-6*np.sin(6*ta), 6*np.cos(6*ta), 8])/10
    ax.quiver(*pos, *tangent, length=0.28, color="#176b9b", linewidth=2, arrow_length_ratio=0.4)
    ax.set(xlim=(-0.1, 1.25), ylim=(-0.1, 1.25), zlim=(-0.15, 2.4), xlabel="$x$", ylabel="$y$",
           zlabel="$z$", title="Rising quarter-turn helix")
    ax.set_box_aspect((1.35, 1.35, 2.55))
    ax.view_init(elev=22, azim=-54)
    for coord in [ax.xaxis, ax.yaxis, ax.zaxis]:
        coord.pane.set_facecolor("white")
        coord.pane.set_alpha(1.0)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)


if __name__ == "__main__":
    main()
