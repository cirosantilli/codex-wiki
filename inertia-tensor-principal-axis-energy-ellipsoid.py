"""Constant-energy surface of the six-mass tensor.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white"})
    inertia = np.array([[6., -2., 0.], [-2., 12., 0.], [0., 0., 14.]])
    angle = 0.5 * np.arctan2(2, 3)
    c, s = np.cos(angle), np.sin(angle)
    rotation = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    moments = np.array([9 - np.sqrt(13), 9 + np.sqrt(13), 14])
    np.testing.assert_allclose(rotation.T @ inertia @ rotation, np.diag(moments), atol=1e-12)
    lengths = np.sqrt(2 / moments)
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 73), np.linspace(0, np.pi, 37))
    surface = np.stack((lengths[0] * np.cos(u) * np.sin(v),
                        lengths[1] * np.sin(u) * np.sin(v), lengths[2] * np.cos(v)))
    fig = plt.figure(figsize=(10, 5.2))
    fig.suptitle("One energy ellipsoid, two coordinate descriptions", fontsize=16, y=0.97)
    colors = ["#c66322", "#167b92", "#774fa1"]
    for panel, transform in enumerate([rotation, np.eye(3)], start=1):
        ax = fig.add_subplot(1, 2, panel, projection="3d")
        xyz = np.einsum("ij,jkl->ikl", transform, surface)
        ax.plot_surface(*xyz, color="#87b8bf", alpha=0.33, edgecolor="none", shade=False)
        ax.plot_wireframe(*xyz, rstride=6, cstride=8, color="#4a7b84", linewidth=0.6, alpha=0.65)
        for i, color in enumerate(colors):
            e = transform[:, i]
            endpoints = np.outer(e, [-lengths[i], lengths[i]])
            ax.plot(*endpoints, color=color, lw=3)
            end = e * lengths[i] * 1.15
            ax.text(*end, f"$e_{i+1}$", color=color, fontsize=12)
        ax.set(xlim=(-0.7, 0.7), ylim=(-0.7, 0.7), zlim=(-0.7, 0.7))
        ax.set_box_aspect((1, 1, 1))
        ax.view_init(elev=22, azim=-58)
        suffixes = ["x", "y", "z"] if panel == 1 else ["1", "2", "3"]
        ax.set_xlabel(r"$\omega_{" + suffixes[0] + r"}/\Omega_0$", labelpad=3)
        ax.set_ylabel(r"$\omega_{" + suffixes[1] + r"}/\Omega_0$", labelpad=3)
        ax.set_zlabel(r"$\omega_{" + suffixes[2] + r"}/\Omega_0$", labelpad=3)
        ax.set_xticks([-0.5, 0, 0.5]); ax.set_yticks([-0.5, 0, 0.5]); ax.set_zticks([-0.5, 0, 0.5])
        for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
            axis.set_pane_color((1, 1, 1, 1))
        ax.set_title("Original coordinates" if panel == 1 else "Principal coordinates", pad=-6)
    fig.subplots_adjust(left=0.015, right=0.95, bottom=0.20, top=0.88, wspace=0.05)
    fig.text(0.5, 0.10, r"$I_i/(ma^2)=(9-\sqrt{13},\ 9+\sqrt{13},\ 14)$" +
             "     " + r"$K_0=ma^2\Omega_0^2$", ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Semiaxes ≈ (0.609, 0.398, 0.378) • angular-velocity space, not the body's shape", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
