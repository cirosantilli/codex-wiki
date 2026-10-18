"""Sketch Question 3(b)(iii); write the PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure(figsize=(7.0, 5.8), facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.22, top=0.92)
    ax = fig.add_subplot(projection="3d")
    phi, rho = np.meshgrid(np.linspace(0, 2 * np.pi, 81), np.linspace(0.015, 0.995, 35))
    ax.plot_surface(rho**2, 1 + rho * np.cos(phi), rho * np.sin(phi), color="#81bbd8", alpha=0.5, edgecolor="white", linewidth=0.2)
    t = np.linspace(0.005, 0.995, 201)
    ax.plot(t**2, 1 + t, np.zeros_like(t), color="#bf5f18", linewidth=3, label=r"Generating curve: $y=1+\sqrt{x},\ z=0$")
    angle = np.linspace(0, 2 * np.pi, 301)
    ax.plot(np.ones_like(angle), 1 + np.cos(angle), np.sin(angle), "--", color="#2e6f8e", linewidth=1.8, label="Excluded rim at $x=1$")
    ax.plot([-0.15, 1.2], [1, 1], [0, 0], "--", color="#333333", linewidth=1.5, label=r"Rotation axis $L$: $y=1,\ z=0$")
    ax.scatter([0], [1], [0], s=40, facecolors="white", edgecolors="#333333", zorder=10)
    ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-0.15, 1.2), ylim=(-0.1, 2.1), zlim=(-1.1, 1.1), title=r"$(y-1)^2+z^2=x,\quad 0<x<1$")
    ax.set_box_aspect((1.5, 2, 2))
    ax.view_init(elev=23, azim=-55)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 1))
    fig.legend(loc="lower center", bbox_to_anchor=(0.5, 0.015), frameon=False, fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=115, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
