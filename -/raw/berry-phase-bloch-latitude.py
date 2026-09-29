"""Draw an original Bloch-sphere latitude and its north polar cap.

Write the opaque basename PNG to CWD. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7. The model follows the positive-spin
eigenstate of n dot sigma, with H = -Delta n dot sigma / 2, Delta > 0.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    theta = np.pi / 3
    phi = np.linspace(0, 2 * np.pi, 161)
    polar = np.linspace(0, np.pi, 81)
    p, t = np.meshgrid(phi, polar)
    fig = plt.figure(figsize=(10, 5.5), dpi=110, facecolor="white")
    ax = fig.add_axes((0.015, 0.08, 0.57, 0.78), projection="3d", computed_zorder=False)
    ax.plot_surface(np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t),
                    color="#b9cbd5", alpha=0.13, edgecolor="none", shade=False, zorder=0)
    for angle in (0, np.pi / 2):
        ax.plot(np.sin(polar) * np.cos(angle), np.sin(polar) * np.sin(angle),
                np.cos(polar), color="#a2b0bb", lw=0.8, alpha=0.6)
        ax.plot(-np.sin(polar) * np.cos(angle), -np.sin(polar) * np.sin(angle),
                np.cos(polar), color="#a2b0bb", lw=0.8, alpha=0.6)
    ax.plot(np.cos(phi), np.sin(phi), np.zeros_like(phi), color="#a2b0bb", lw=0.8)
    cap_p, cap_t = np.meshgrid(phi, np.linspace(0, theta, 31))
    ax.plot_surface(np.sin(cap_t) * np.cos(cap_p), np.sin(cap_t) * np.sin(cap_p),
                    np.cos(cap_t), color="#e6a044", alpha=0.78, shade=False,
                    linewidth=0, antialiased=True, zorder=1)
    ax.plot(np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi),
            np.full_like(phi, np.cos(theta)), color="#2163a6", lw=3.0)
    start = -np.pi / 2
    xyz = np.array([np.sin(theta) * np.cos(start), np.sin(theta) * np.sin(start), np.cos(theta)])
    tangent = np.array([-np.sin(start), np.cos(start), 0])
    ax.quiver(*xyz, *tangent, length=0.27, color="#2163a6", lw=2.5,
              arrow_length_ratio=0.5, normalize=True)
    for direction, label in (([1.15, 0, 0], "$x$"), ([0, 1.15, 0], "$y$"), ([0, 0, 1.25], "$z$")):
        ax.plot([0, direction[0]], [0, direction[1]], [0, direction[2]], color="#596571", lw=1)
        ax.text(*direction, label, fontsize=12)
    direction_phi = -0.7
    n = np.array([np.sin(theta) * np.cos(direction_phi), np.sin(theta) * np.sin(direction_phi), np.cos(theta)])
    ax.quiver(0, 0, 0, *n, color="#323b46", length=1, lw=1.8, arrow_length_ratio=0.08)
    arc = np.linspace(0, theta, 80)
    ax.plot(0.44 * np.sin(arc) * np.cos(direction_phi),
            0.44 * np.sin(arc) * np.sin(direction_phi), 0.44 * np.cos(arc), color="#323b46", lw=1.6)
    ax.text(0.12, -0.3, 0.44, r"$\theta$", fontsize=14, zorder=4)
    ax.text(*(1.08 * n), r"$\mathbf{n}$", fontsize=14, zorder=4)
    ax.text(0, 0, -1.16, r"$|1\rangle$", ha="center", fontsize=12)
    ax.text(-0.1, 0, 1.03, r"$|0\rangle$", ha="right", fontsize=12)
    ax.set(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2), zlim=(-1.2, 1.3))
    ax.set_box_aspect((1, 1, 1), zoom=1.4)
    ax.set_proj_type("ortho")
    ax.view_init(elev=23, azim=-62)
    ax.set_axis_off()
    fig.suptitle("Berry phase: a loop remembers enclosed geometry", fontsize=17, weight="bold", y=0.96)
    fig.text(0.61, 0.76, r"Latitude loop: $\theta=60^\circ$", fontsize=15, weight="bold")
    fig.text(0.61, 0.66, "Blue loop: increasing azimuth\n" + r"$\phi:0\longrightarrow 2\pi$", color="#2163a6", linespacing=1.7)
    fig.text(0.61, 0.49, "Orange north polar cap\n" + r"$\Omega=2\pi(1-\cos\theta)=\pi$", color="#99580f", linespacing=1.7)
    fig.text(0.61, 0.33, r"$\gamma=-\Omega/2=-\pi/2$", fontsize=17)
    fig.text(0.61, 0.18, "Positive-spin eigenstate convention\nNonzero gap; ideal adiabatic cycle", fontsize=11, color="#454b53", linespacing=1.6)
    fig.text(0.5, 0.045, "Unit Bloch sphere of internal states, not a spatial trajectory. Phase is defined modulo 2π.",
             ha="center", fontsize=10.5)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
