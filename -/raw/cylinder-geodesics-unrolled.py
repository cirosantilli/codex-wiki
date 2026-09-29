"""Compare winding classes using the Euclidean covering plane; PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(12, 6), layout="constrained")
    ax = fig.add_subplot(121, projection="3d")
    flat = fig.add_subplot(122)
    p = np.array([1., 0., 0.])
    q = np.array([0., 1., 3.])
    t = np.linspace(0, 1, 2001)
    phi, height = np.meshgrid(np.linspace(0, 2 * np.pi, 65), np.linspace(0, 3, 33))
    ax.plot_wireframe(np.cos(phi), np.sin(phi), height, rstride=6, cstride=8,
                      color="#aabfc7", lw=.7, alpha=.65)
    azimuth = -60
    colors = ["#087e8b", "#c85b28"]
    for k, color in zip([0, -1], colors):
        end_x = np.pi / 2 + 2 * np.pi * k
        length = np.hypot(end_x, 3)
        curve = np.array([np.cos(end_x * t), np.sin(end_x * t), 3 * t])
        assert np.allclose(curve[:, 0], p)
        assert np.allclose(curve[:, -1], q)
        polygon_length = np.linalg.norm(np.diff(curve, axis=1), axis=0).sum()
        assert np.isclose(polygon_length, length, rtol=1e-6)
        visible = np.cos(end_x * t - np.deg2rad(azimuth)) >= 0
        for mask, style, alpha in [(visible, "-", 1), (~visible, "--", .65)]:
            part = curve.copy()
            part[:, ~mask] = np.nan
            ax.plot(*part, color=color, lw=3, linestyle=style, alpha=alpha)
        flat.plot(end_x * t, 3 * t, color=color, lw=3,
                  label=f"k = {k}: length {length:.3f}")
        flat.scatter(end_x, 3, color=color, s=40)
        flat.annotate(rf"$q_{{{k}}}$", (end_x, 3), xytext=(5, 7),
                      textcoords="offset points", fontsize=14)
    candidates = np.hypot(np.pi / 2 + 2 * np.pi * np.arange(-8, 9), 3)
    assert np.argmin(candidates) == 8  # k = 0 minimizes among every nearby winding.
    for point, label in [(p, "p"), (q, "q")]:
        ax.scatter(*point, color="#25313b", s=35, depthshade=False)
        ax.text(*(point + np.array([.08, .08, .10])), label, fontsize=14)
    ax.view_init(elev=23, azim=azimuth)
    ax.set_box_aspect((2, 2, 3))
    ax.set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), zlim=(-.1, 3.2))
    ax.set_axis_off()
    ax.set_title("Same endpoints; different winding", pad=15)
    flat.scatter(0, 0, color="#25313b", s=40, zorder=5)
    flat.annotate("p", (0, 0), xytext=(6, -18), textcoords="offset points", fontsize=14)
    flat.plot([-3 * np.pi / 2, np.pi / 2], [3, 3], ":", color="#8796a3", lw=1.4)
    flat.text(-np.pi / 2, 3.38, r"Equivalent lifts are $2\pi$ apart",
              ha="center", fontsize=11)
    flat.set(xlim=(-5.2, 2.2), ylim=(-.5, 3.9), xlabel=r"Unrolled coordinate $x=\theta$",
             ylabel="Height z")
    flat.set_aspect("equal")
    flat.set_xticks([-3 * np.pi / 2, 0, np.pi / 2], [r"$-3\pi/2$", "0", r"$\pi/2$"])
    flat.set_yticks([0, 1, 2, 3])
    flat.grid(alpha=.18)
    flat.spines[["top", "right"]].set_visible(False)
    flat.set_title("Straight segments on the covering plane", pad=16)
    flat.legend(loc="upper center", bbox_to_anchor=(.5, -.14), frameon=False, fontsize=11)
    fig.suptitle("Cylinder distance: choose the shortest lifted segment", fontsize=17)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
