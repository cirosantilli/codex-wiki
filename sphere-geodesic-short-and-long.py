"""Compare two affinely parametrized great-circle arcs; emit PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(11, 5.4), layout="constrained")
    ax = fig.add_subplot(121, projection="3d")
    flat = fig.add_subplot(122)
    short_color, long_color = "#087e8b", "#c85b28"
    t = np.linspace(0, 1, 2001)
    theta_short, theta_long = np.pi * t / 3, -5 * np.pi * t / 3
    p = np.array([1., 0., 0.])
    q = np.array([.5, np.sqrt(3) / 2, 0.])
    assert np.allclose([np.cos(theta_long[-1]), np.sin(theta_long[-1]), 0], q)
    assert np.isclose(np.linalg.norm(p - q), 1)
    for theta, length in [(theta_short, np.pi / 3), (theta_long, 5 * np.pi / 3)]:
        chord_sum = np.hypot(np.diff(np.cos(theta)), np.diff(np.sin(theta))).sum()
        assert np.isclose(chord_sum, length, rtol=1e-6)
    phi, latitude = np.meshgrid(np.linspace(0, 2 * np.pi, 61), np.linspace(-np.pi / 2, np.pi / 2, 31))
    ax.plot_wireframe(np.cos(latitude) * np.cos(phi), np.cos(latitude) * np.sin(phi),
                      np.sin(latitude), rstride=5, cstride=8, color="#bdc9d2", lw=.65, alpha=.65)
    azimuth = -65
    for theta, color in [(theta_long, long_color), (theta_short, short_color)]:
        curve = np.array([np.cos(theta), np.sin(theta), np.zeros_like(theta)])
        visible = np.cos(theta - np.deg2rad(azimuth)) >= 0
        for mask, style, alpha in [(visible, "-", 1), (~visible, "--", .7)]:
            part = curve.copy()
            part[:, ~mask] = np.nan
            ax.plot(*part, color=color, lw=3, linestyle=style, alpha=alpha)
    for point, label in [(p, "p"), (q, "q")]:
        ax.scatter(*point, color="#25313b", s=30, depthshade=False)
        ax.text(*(point + np.array([.06, .06, .07])), label, fontsize=14)
    ax.view_init(elev=26, azim=azimuth)
    ax.set_box_aspect((1, 1, 1), zoom=1.35)
    ax.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), zlim=(-1.15, 1.15))
    ax.set_axis_off()
    ax.set_title("Both arcs lie on the unit sphere", pad=12)
    for theta, color, label in [
        (theta_short, short_color, r"Short arc: $\pi/3 \approx 1.047$"),
        (theta_long, long_color, r"Long arc: $5\pi/3 \approx 5.236$"),
    ]:
        flat.plot(np.cos(theta), np.sin(theta), color=color, lw=3.5, label=label)
        n = len(theta) // 2
        flat.annotate("", xy=(np.cos(theta[n + 60]), np.sin(theta[n + 60])),
                      xytext=(np.cos(theta[n]), np.sin(theta[n])),
                      arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
    flat.plot([p[0], q[0]], [p[1], q[1]], "--", color="#85909a", lw=1.5,
              label="Chord: 1 (leaves the surface)")
    for point, label in [(p, "p"), (q, "q")]:
        flat.scatter(*point[:2], color="#25313b", s=30, zorder=5)
        flat.annotate(label, point[:2], xytext=(8, 5), textcoords="offset points", fontsize=14)
    flat.set_aspect("equal")
    flat.set(xlim=(-1.25, 1.28), ylim=(-1.24, 1.24))
    flat.set_axis_off()
    flat.set_title("The equatorial plane shows the two routes")
    flat.legend(loc="upper center", bbox_to_anchor=(.5, -.02), frameon=False, fontsize=11)
    fig.suptitle("A geodesic need not be the globally shortest route", fontsize=17)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
