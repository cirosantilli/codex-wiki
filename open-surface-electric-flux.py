#!/usr/bin/env python3
"""Original oriented-plane diagram; run from _media to save the PNG there.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Arrow lengths are schematic; patches share one area and the field is constant.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(11.8, 4.7), facecolor="white")
    field_color, normal_color = "#0072b2", "#b34b00"
    for index, degrees in enumerate((0, 60, 120), start=1):
        ax = fig.add_subplot(1, 3, index, projection="3d")
        theta = np.deg2rad(degrees)
        normal = np.array([np.cos(theta), 0.0, np.sin(theta)])
        tangent = np.array([-np.sin(theta), 0.0, np.cos(theta)])
        side = np.array([0.0, 1.0, 0.0])
        corners = [0.68 * (u * tangent + v * side)
                   for u, v in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        ax.add_collection3d(Poly3DCollection(
            [corners], facecolors="#a9cdda", edgecolors="#447280",
            linewidths=1.2, alpha=0.48))
        # Parallel equal arrows illustrate a single constant 3D field.
        for offset in (-0.46, 0.46):
            start = offset * side - 0.84 * np.array([1.0, 0.0, 0.0])
            ax.quiver(*start, 1.65, 0, 0, color=field_color,
                      linewidth=1.6, arrow_length_ratio=0.12)
        # Both reference arrows start at the same point on the patch.
        origin = -0.12 * side
        ax.quiver(*origin, 1.08, 0, 0, color=field_color,
                  linewidth=2.5, arrow_length_ratio=0.15)
        ax.quiver(*origin, *(0.96 * normal), color=normal_color,
                  linewidth=2.7, arrow_length_ratio=0.18)
        ax.text(*(origin + 1.24 * np.array([1.0, 0.0, 0.0])),
                r"$\mathbf{E}$", color=field_color, fontsize=14)
        label = origin + 1.1 * normal + 0.32 * side + 0.12 * tangent
        ax.text(*label, r"$\mathbf{n}$", color=normal_color, fontsize=14)
        if degrees:
            angles = np.linspace(0, theta, 80)
            arc = origin[:, None] + 0.38 * np.vstack(
                (np.cos(angles), np.zeros_like(angles), np.sin(angles)))
            ax.plot(*arc, color="#333333", linewidth=1.4)
            mid = origin + 0.55 * np.array([np.cos(theta / 2), 0,
                                           np.sin(theta / 2)])
            ax.text(*mid, rf"${degrees}^\circ$", fontsize=11)
        else:
            ax.text2D(0.06, 0.80, "E and n point\nthe same way", transform=ax.transAxes,
                      fontsize=10, color="#444444")
        value = int(round(100 * 0.02 * np.dot(normal, [1, 0, 0])))
        ax.set_title(rf"$\theta={degrees}^\circ$" + "\n" +
                     rf"$\Phi_E={value}\ \mathrm{{N\,m^2/C}}$", pad=9)
        ax.text2D(0.29, 0.04, r"open patch: $A=0.02\ \mathrm{m^2}$",
                  transform=ax.transAxes, fontsize=10, ha="center")
        ax.set(xlim=(-1.25, 1.4), ylim=(-1, 1), zlim=(-1, 1.4))
        ax.set_box_aspect((2.65, 2, 2.4))
        ax.view_init(elev=40, azim=-55)
        ax.set_axis_off()
        ax.set_facecolor("white")
    fig.suptitle("Electric flux through an oriented open plane", fontsize=18, y=0.97)
    fig.text(0.5, 0.025,
             r"Constant $E=100\ \mathrm{N/C}$    |    $\Phi_E=EA\cos\theta$    |    "
             r"$\theta$ is the angle to the chosen normal (orange)",
             ha="center", fontsize=12)
    fig.subplots_adjust(left=0.015, right=0.98, bottom=0.12, top=0.76, wspace=0.08)
    fig.savefig("open-surface-electric-flux.png", dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
