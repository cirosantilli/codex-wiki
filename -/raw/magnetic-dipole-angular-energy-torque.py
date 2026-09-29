"""Draw an imposed field, signed torque, and angular orientation energy.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.2, 4.8), facecolor="white")
    grid = fig.add_gridspec(1, 2, width_ratios=[1, 1.75], wspace=0.31)
    geometry, curves = fig.add_subplot(grid[0]), fig.add_subplot(grid[1])
    blue, orange = "#1965a6", "#a84c16"
    theta = np.pi / 3
    geometry.set_aspect("equal")
    geometry.set_xlim(-0.65, 1.65)
    geometry.set_ylim(-0.82, 1.55)
    geometry.axis("off")
    for end, color in [((1.45, 0), blue), ((1.20 * np.cos(theta), 1.20 * np.sin(theta)), orange)]:
        geometry.add_patch(FancyArrowPatch((0, 0), end, arrowstyle="-|>",
                                          mutation_scale=22, lw=2.6, color=color))
    geometry.text(1.43, -0.22, r"$\mathbf{B}_{\rm ext}$", color=blue, ha="center", fontsize=16)
    geometry.text(0.67, 1.06, r"$\mathbf{m}$", color=orange, fontsize=18)
    geometry.add_patch(Arc((0, 0), 0.75, 0.75, theta1=0, theta2=60, lw=1.4))
    geometry.text(0.40, 0.25, r"$\theta>0$", fontsize=14)
    angles = np.linspace(np.deg2rad(135), np.deg2rad(25), 80)
    geometry.plot(0.78 * np.cos(angles), 0.78 * np.sin(angles), color="#494949", lw=1.6)
    geometry.add_patch(FancyArrowPatch((0.78 * np.cos(angles[-3]), 0.78 * np.sin(angles[-3])),
                                      (0.78 * np.cos(angles[-1]), 0.78 * np.sin(angles[-1])),
                                      arrowstyle="-|>", mutation_scale=16, color="#494949"))
    geometry.text(0.48, 1.42, "Torque turns clockwise", ha="center", fontsize=12)
    geometry.text(0.45, -0.50, r"$\tau_z=-mB\sin\theta<0$", ha="center", fontsize=13)
    geometry.text(0.45, -0.74, "+z points out of the page", ha="center", fontsize=10)
    angle = np.linspace(0, 2 * np.pi, 801)
    curves.plot(angle, -np.cos(angle), color=blue, lw=2.5, label=r"$U/(mB)=-\cos\theta$")
    curves.plot(angle, -np.sin(angle), color=orange, lw=2.5, label=r"$\tau_z/(mB)=-\sin\theta$")
    curves.axhline(0, color="#666666", lw=0.8)
    curves.set_xlim(0, 2 * np.pi)
    curves.set_ylim(-1.43, 1.65)
    curves.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
                     ["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
    curves.set_yticks([-1, 0, 1])
    curves.set_xlabel(r"Angle $\theta$ from the external field (radians)")
    curves.set_ylabel("Normalized energy / signed torque")
    curves.grid(alpha=0.18)
    curves.spines[["top", "right"]].set_visible(False)
    curves.legend(loc="upper right", frameon=False, fontsize=11)
    curves.scatter([0, np.pi, 2 * np.pi], [-1, 1, -1], color=blue, zorder=5, s=25)
    curves.annotate("stable", xy=(0, -1), xytext=(0.43, -1.29), fontsize=11,
                    arrowprops={"arrowstyle": "-", "color": "#444444"})
    curves.annotate("unstable", xy=(np.pi, 1), xytext=(2.02, 1.29), fontsize=11,
                    arrowprops={"arrowstyle": "-", "color": "#444444"})
    fig.suptitle("Magnetic dipole: orientation energy and restoring torque", fontsize=16, weight="bold")
    fig.text(0.5, 0.025, r"Fixed $m$ and $B$  •  $\tau_z=-dU/d\theta$  •  $mB$: joules for energy, newton metres for torque",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.035, right=0.975, top=0.84, bottom=0.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=110,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
