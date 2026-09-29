"""Draw T(2,3) with meridional p=2 and longitudinal q=3.

Run from the desired output directory; writes torus-trefoil-geometry.png.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


R, r, p, q = 2.0, 0.7, 2, 3


def torus(phi, theta):
    rho = R + r * np.cos(phi)
    return np.column_stack((rho * np.cos(theta), rho * np.sin(theta), r * np.sin(phi)))


def main():
    t = np.linspace(0, 2 * np.pi, 2401)
    curve = torus(p * t, q * t)
    rho = np.hypot(curve[:, 0], curve[:, 1])
    assert np.allclose((rho - R) ** 2 + curve[:, 2] ** 2, r ** 2)
    assert np.allclose(curve[0], curve[-1])
    # Unwrapped angles independently recover the signed winding counts.
    phi = np.unwrap(np.arctan2(curve[:, 2], rho - R))
    theta = np.unwrap(np.arctan2(curve[:, 1], curve[:, 0]))
    assert np.allclose([(phi[-1] - phi[0]) / (2 * np.pi), (theta[-1] - theta[0]) / (2 * np.pi)], [p, q])
    assert np.min(r ** 2 * p ** 2 + q ** 2 * rho ** 2) > 0

    # Orthographic camera: sort every short segment by depth, including guides.
    azimuth, elevation = np.deg2rad([28, 28])
    right = np.array([-np.sin(azimuth), np.cos(azimuth), 0])
    eye = np.array([np.cos(elevation) * np.cos(azimuth), np.cos(elevation) * np.sin(azimuth), np.sin(elevation)])
    up = np.cross(eye, right)
    camera = np.column_stack((right, up, eye))
    segments, colors, widths = [], [], []

    def add_line(points, color, width):
        projected = points @ camera
        segments.extend(np.stack((projected[:-1], projected[1:]), axis=1))
        colors.extend([color] * (len(points) - 1))
        widths.extend([width] * (len(points) - 1))

    guide = np.linspace(0, 2 * np.pi, 361)
    for angle in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        add_line(torus(guide, np.full_like(guide, angle)), "#d2d9df", 0.65)
    for angle in np.linspace(0, 2 * np.pi, 7, endpoint=False):
        add_line(torus(np.full_like(guide, angle), guide), "#d2d9df", 0.65)
    add_line(curve, "#176b9a", 3.6)
    segments = np.asarray(segments)
    order = np.argsort(segments[:, :, 2].mean(axis=1))

    fig, (ax, angles) = plt.subplots(1, 2, figsize=(9.8, 4.4), gridspec_kw={"width_ratios": [1.25, 1]}, layout="constrained")
    fig.patch.set_facecolor("white")
    fig.suptitle("A trefoil on a torus: meridional p = 2, longitudinal q = 3", fontsize=14)
    ax.add_collection(LineCollection(segments[order, :, :2], colors=np.asarray(colors)[order], linewidths=np.asarray(widths)[order], capstyle="round"))
    ax.set(xlim=(-3, 3), ylim=(-2.2, 2.2), aspect="equal")
    ax.axis("off")
    ax.set_title("One closed, nonintersecting loop", fontsize=11)
    ax.text(0.5, -0.01, "R = 2, r = 0.7; pale lines show the supporting torus", transform=ax.transAxes, ha="center", fontsize=9)

    fraction = t / (2 * np.pi)
    angles.plot(fraction, phi / (2 * np.pi), color="#a44883", linewidth=2.5, label="Meridional angle / 2π")
    angles.plot(fraction, theta / (2 * np.pi), color="#176b9a", linewidth=2.5, label="Longitudinal angle / 2π")
    angles.scatter([1, 1], [p, q], c=["#a44883", "#176b9a"], s=35, zorder=3)
    angles.set(xlim=(0, 1.07), ylim=(0, 3.3), xlabel="Fraction of one circuit, t / (2π)", ylabel="Accumulated turns", xticks=[0, 0.5, 1], yticks=[0, 1, 2, 3])
    angles.set_title("Winding counts from unwrapped angles", fontsize=11)
    angles.grid(alpha=0.2)
    angles.legend(loc="upper left", fontsize=9, frameon=False)
    angles.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / "torus-trefoil-geometry.png", dpi=100, facecolor="white", transparent=False)
    print("Validated closure, torus equation, nonzero speed, winding counts (2,3).")


if __name__ == "__main__":
    main()
