"""Original surface patches; run from _media to write the matching PNG.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
All plotted coordinates use one length unit. Convention: S = -dN.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(9.6, 8.2), layout="constrained")
    fig.suptitle("Gaussian curvature: four local surface patches", fontsize=17)
    red, blue = "#ae283b", "#125da3"
    t = np.linspace(-0.66, 0.66, 151)
    q = np.linspace(-0.66, 0.66, 37)
    u, v = np.meshgrid(q, q)
    zero = np.zeros_like(t)
    titles = [
        "Plane · upward normal\n" + r"$k_1=k_2=0,\quad K=0$",
        "Cylinder · outward normal · R = 1\n" + r"$k_{\rm circ}=-1,\quad k_{\rm axial}=0,\quad K=0$",
        "Sphere · outward normal · R = 1\n" + r"$k_1=k_2=-1,\quad K=1$",
        "Saddle · upward normal · at the origin\n" + r"$k_x=1,\quad k_y=-1,\quad K=-1$",
    ]
    colors = ["#a7cfca", "#ecc283", "#acd0e8", "#c6b5d8"]
    surfaces = [
        (u, v, np.zeros_like(u)),
        (np.sin(u), v, np.cos(u)),
        (u, v, np.sqrt(1 - u**2 - v**2)),
        (u, v, (u**2 - v**2) / 2),
    ]
    curves = [
        ((t, zero, zero), (zero, t, zero)),
        ((np.sin(t), zero, np.cos(t)), (zero, t, np.ones_like(t))),
        ((t, zero, np.sqrt(1 - t**2)), (zero, t, np.sqrt(1 - t**2))),
        ((t, zero, t**2 / 2), (zero, t, -t**2 / 2)),
    ]
    for i, (surface, pair) in enumerate(zip(surfaces, curves)):
        ax = fig.add_subplot(2, 2, i + 1, projection="3d", computed_zorder=False)
        ax.plot_surface(*surface, color=colors[i], alpha=0.84,
                        edgecolor="#ffffff", linewidth=0.3, rstride=2, cstride=2, zorder=1)
        for curve, color in zip(pair, (red, blue)):
            ax.plot(*curve, color=color, lw=3.0, zorder=5)
        z0 = 1.0 if i in (1, 2) else 0.0
        ax.scatter([0], [0], [z0], color="#20252b", s=30, depthshade=False, zorder=10)
        ax.quiver(0, 0, z0, 0, 0, 0.5, color="#20252b",
                  arrow_length_ratio=0.22, linewidth=2, zorder=11)
        ax.text(0.03, 0, z0 + 0.54, "N", fontsize=12, weight="bold")
        ax.set(xlim=(-0.85, 0.85), ylim=(-0.85, 0.85),
               zlim=(z0 - 0.8, z0 + 0.8))
        ax.set_box_aspect((1, 1, 0.85))
        ax.view_init(elev=27, azim=-53)
        ax.set_title(titles[i], fontsize=11.5, pad=8)
        ax.set_xlabel("x", labelpad=-3)
        ax.set_ylabel("y (axial)" if i == 1 else "y", labelpad=-3)
        ax.set_zlabel("z", labelpad=-3)
        ax.set_xticks([-0.5, 0, 0.5])
        ax.set_yticks([-0.5, 0, 0.5])
        ax.set_zticks([z0 - 0.5, z0, z0 + 0.5])
        ax.tick_params(labelsize=8, pad=0)
        for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
            axis.pane.set_facecolor("white")
            axis.pane.set_edgecolor("#d4d9de")
    handles = [Line2D([0], [0], color=red, lw=3, label="First principal direction at the point"),
               Line2D([0], [0], color=blue, lw=3, label="Second principal direction at the point")]
    fig.legend(handles=handles, loc="outside lower center", ncol=2,
               frameon=False, fontsize=10)
    output = Path(__file__).with_suffix(".png").name
    fig.savefig(output, dpi=125, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
