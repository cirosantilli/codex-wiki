"""Show local Earth rotation geometry and a northward-velocity example.

Run from the desired output directory. Tested with Python 3.14,
Matplotlib 3.10.7 and NumPy 2.3.5; dependencies are in pyproject.toml.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle
import numpy as np


def arrow(ax, start, end, color, label=None, text=None):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2, "mutation_scale": 15})
    if label:
        ax.text(*text, label, fontsize=11, color=color)


def main():
    omega, speed, phi = 7.292115e-5, 20.0, np.pi / 4
    acceleration = 2 * omega * speed * np.sin(phi)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 5.7), facecolor="white")
    fig.subplots_adjust(left=0.035, right=0.98, top=0.79, bottom=0.25, wspace=0.15)
    for ax in (left, right):
        ax.set_aspect("equal")
        ax.set_facecolor("white")
        ax.axis("off")
    left.set_xlim(-1.25, 1.65)
    left.set_ylim(-1.1, 1.5)
    left.add_patch(Circle((0, 0), 0.88, facecolor="#eef6fa", edgecolor="#507080", lw=1.4))
    left.plot([-1.1, 1.1], [0, 0], color="#999999", lw=1)
    left.text(-1.14, -0.16, "equatorial plane", fontsize=10)
    arrow(left, (0, -1.0), (0, 1.37), "#555555", r"$\boldsymbol{\Omega}$", (0.08, 1.22))
    p = 0.88 * np.array([np.cos(phi), np.sin(phi)])
    left.plot([0, p[0]], [0, p[1]], color="#888888", ls="--")
    left.add_patch(Arc((0, 0), 0.70, 0.70, theta1=0, theta2=45, color="#555555"))
    left.text(0.37, 0.13, r"$\varphi=45^\circ$", fontsize=11)
    left.plot(*p, "o", color="#222222", ms=5)
    arrow(left, p, p + 0.52 * np.array([np.cos(phi), np.sin(phi)]),
          "#009e73", "up", (1.04, 1.02))
    arrow(left, p, p + 0.56 * np.array([-np.sin(phi), np.cos(phi)]),
          "#0072b2", "north", (0.11, 1.10))
    left.text(0, -1.05, "Meridian section (spherical Earth)", ha="center", fontsize=10)
    left.set_title("Latitude sets the vertical rotation component", fontsize=12, pad=16)

    right.set_xlim(-0.65, 1.65)
    right.set_ylim(-0.3, 1.7)
    arrow(right, (0, 0), (1.4, 0), "#777777", "east", (1.22, -0.17))
    arrow(right, (0, 0), (0, 1.35), "#777777", "north", (-0.18, 1.46))
    arrow(right, (0, 0), (0, 1.06), "#0072b2")
    right.text(0.08, 1.0, r"$\mathbf{v}=20\,\mathbf{e}_N\ {\rm m\,s^{-1}}$", fontsize=11, color="#0072b2")
    arrow(right, (0, 0.59), (1.12, 0.59), "#d55e00")
    right.text(0.20, 0.74, r"$\mathbf{a}_{\rm cor}=f u\,\mathbf{e}_E$", fontsize=12, color="#d55e00")
    right.text(0.35, 0.37, "eastward acceleration", fontsize=10, color="#d55e00")
    right.text(-0.49, 0.57, r"$\odot$", fontsize=24, color="#009e73", ha="center")
    right.text(-0.60, 0.24, "up\n(out of page)", fontsize=9, color="#009e73")
    right.text(0.55, -0.29, "Arrows show directions; lengths are schematic.", ha="center", fontsize=9)
    right.set_title("Local horizontal view at 45° north", fontsize=12, pad=16)
    fig.suptitle("Why a northward velocity has an eastward Coriolis acceleration", fontsize=15, y=0.98)
    fig.text(0.5, 0.875, r"$\boldsymbol{\Omega}=\Omega\cos\varphi\,\mathbf{e}_N+\Omega\sin\varphi\,\mathbf{e}_U,\qquad f=2\Omega\sin\varphi$",
             fontsize=13, ha="center")
    fig.text(0.5, 0.15, rf"$\Omega=7.292115\times10^{{-5}}\ {{\rm s^{{-1}}}},\qquad a_E={acceleration:.7f}\ {{\rm m\,s^{{-2}}}}$",
             fontsize=13, ha="center")
    fig.text(0.5, 0.085, r"At 10 s: $\Delta x_E\simeq\frac{1}{2} a_E t^2=0.1031$ m (local, short-time estimate).",
             fontsize=11, ha="center")
    fig.text(0.5, 0.025, "Initial northward motion, no other horizontal force; this is not a prediction of a wind trajectory.",
             fontsize=10, ha="center")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
