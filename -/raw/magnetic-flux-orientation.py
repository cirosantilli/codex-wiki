"""Signed magnetic flux versus surface orientation.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Write PNG to cwd for Make.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def main():
    magnetic_field, area = 2.0, 3.0
    angles = np.array([0, np.pi/3, np.pi/2, np.pi])
    fluxes = magnetic_field * area * np.cos(angles)
    np.testing.assert_allclose(fluxes, [6, 3, 0, -6], atol=1e-14)
    normals = np.column_stack((np.cos(angles), np.sin(angles)))
    np.testing.assert_allclose(normals @ np.array([magnetic_field, 0]) * area, fluxes)
    np.testing.assert_allclose((-normals) @ np.array([magnetic_field, 0]) * area, -fluxes)

    blue, orange, grey = "#176997", "#b55d20", "#637783"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig = plt.figure(figsize=(10.5, 6.1), dpi=120, facecolor="white")
    grid = fig.add_gridspec(3, 2, width_ratios=(1.05, 1.5), hspace=0.35, wspace=0.32)
    for row, (theta, label, result) in enumerate(zip(angles[:3], ["0", "π/3", "π/2"], ["6", "3", "0"])):
        ax = fig.add_subplot(grid[row, 0])
        normal = np.array([np.cos(theta), np.sin(theta)])
        edge = np.array([-np.sin(theta), np.cos(theta)])
        ax.plot([-edge[0], edge[0]], [-edge[1], edge[1]], color=blue, lw=5, solid_capstyle="round")
        ax.plot([0, 1.2], [0, 0], ls=":", color="#c1cbd1", lw=1)
        ax.annotate("", normal * 1.2, (0, 0), arrowprops={"arrowstyle": "->", "lw": 2, "color": orange})
        label_position = normal * 0.95 + np.array([0.4, 0.05])
        ax.text(*label_position, r"$\widehat{\mathbf{n}}$", ha="center", va="center", fontsize=13, color=orange)
        if theta > 0:
            ax.add_patch(Arc((0, 0), 0.85, 0.85, theta1=0, theta2=np.degrees(theta), color=orange, lw=1.2))
        ax.annotate("", (1.55, -1.25), (-1.55, -1.25), arrowprops={"arrowstyle": "->", "color": grey, "lw": 1.5})
        ax.text(1.63, -1.25, r"$\mathbf{B}$", va="center", color=grey, fontsize=12)
        ax.text(-2.00, 1.30, f"θ = {label}    →    Φ = {result} Wb", va="bottom", fontsize=11)
        ax.set(xlim=(-2.1, 2.15), ylim=(-1.5, 1.65), aspect="equal")
        ax.axis("off")

    ax = fig.add_subplot(grid[:, 1])
    theta = np.linspace(0, np.pi, 501)
    ax.plot(theta, magnetic_field * area * np.cos(theta), color=blue, lw=2.8)
    ax.axhline(0, color="#9aaab4", lw=1)
    ax.scatter(angles, fluxes, color=orange, s=38, zorder=5)
    for angle, flux, label, offset in zip(angles, fluxes, ["6 Wb", "3 Wb", "0 Wb", "−6 Wb"],
                                           [(10, -21), (12, 8), (13, 10), (-56, 14)]):
        ax.annotate(label, (angle, flux), xytext=offset, textcoords="offset points", color=orange, fontsize=11)
    ax.text(0.55, -4.4, "Reverse the normal:\nreverse the flux sign", fontsize=11, color=grey)
    ax.set(xlim=(-0.12, np.pi + 0.12), ylim=(-7.1, 7.1), xlabel="Angle θ between field and normal", ylabel="Signed magnetic flux Φ (Wb)")
    ax.set_xticks(angles, ["0", "π/3", "π/2", "π"])
    ax.set_yticks([-6, -3, 0, 3, 6])
    ax.grid(alpha=0.15)
    ax.set_title(r"$\Phi_B=BA\cos\theta=6\cos\theta\;\mathrm{Wb}$", fontsize=13, pad=15)

    fig.suptitle("Magnetic flux depends on the surface normal", fontsize=15, y=0.97)
    fig.text(0.5, 0.905, "Stipulated uniform field B = 2 T; flat surface area A = 3 m²", ha="center", fontsize=11)
    fig.text(0.24, 0.825, "Surface shown edge-on (blue)", ha="center", fontsize=11, color=blue)
    fig.text(0.5, 0.03, "Orange: chosen unit normal. Grey: fixed field direction. Rotating the surface changes flux, even at constant B.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.065, right=0.97, bottom=0.15, top=0.77)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
