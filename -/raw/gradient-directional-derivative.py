"""Exact directional derivatives of x^2 + 2 y^2 at (1, 1)."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    point = np.array([1.0, 1.0])
    gradient = np.array([2.0, 4.0])
    best = gradient / np.linalg.norm(gradient)
    tangent = np.array([-2.0, 1.0]) / np.sqrt(5)
    assert np.isclose(gradient @ best, 2 * np.sqrt(5))
    assert np.isclose(gradient @ tangent, 0)
    angle = np.linspace(0, 2 * np.pi, 1001)
    rates = 2 * np.cos(angle) + 4 * np.sin(angle)
    grid = np.linspace(-2, 2, 401)
    x, y = np.meshgrid(grid, grid)
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.1), dpi=120)
    fig.patch.set_facecolor("white")
    ax = axes[0]
    lines = ax.contour(x, y, x**2 + 2 * y**2,
                      levels=[0.5, 1, 2, 3, 4, 6, 8],
                      colors="#b7c2cb", linewidths=1)
    ax.clabel(lines, fontsize=9, inline=True)
    ax.contour(x, y, x**2 + 2 * y**2, levels=[3],
               colors="#333e60", linewidths=2)
    ax.scatter(*point, color="#222222", s=35, zorder=4)
    for direction, color in [(best, "#c76716"), (tangent, "#1675a9")]:
        ax.annotate("", xy=point + 0.65 * direction, xytext=point,
                    arrowprops={"arrowstyle": "-|>", "color": color,
                                "lw": 2.5, "mutation_scale": 18})
    ax.text(1.2, 1.65, "steepest", color="#c76716", fontsize=11)
    ax.text(0.22, 1.44, "tangent", color="#1675a9", fontsize=11)
    ax.text(1.1, 0.85, "(1, 1)", fontsize=10)
    ax.set_aspect("equal")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(r"Level curves of $f=x^2+2y^2$", fontsize=13)
    ax.text(0.5, -0.23, "Arrows show unit directions at the marked point.",
            transform=ax.transAxes, ha="center", fontsize=10)
    ax = axes[1]
    ax.plot(np.degrees(angle), rates, color="#333e60", lw=2)
    ax.axhline(0, color="#999999", lw=0.8)
    theta_best = np.arctan2(4, 2)
    theta_tangent = theta_best + np.pi / 2
    ax.scatter(np.degrees(theta_best), 2 * np.sqrt(5),
               color="#c76716", s=45, zorder=4)
    ax.scatter(np.degrees(theta_tangent), 0,
               color="#1675a9", s=45, zorder=4)
    ax.annotate(r"maximum $2\sqrt{5}$", xy=(np.degrees(theta_best), 2 * np.sqrt(5)),
                xytext=(115, 4.6), fontsize=11, color="#c76716",
                arrowprops={"arrowstyle": "-", "color": "#c76716"})
    ax.annotate("tangent: rate 0", xy=(np.degrees(theta_tangent), 0),
                xytext=(190, 1.5), fontsize=11, color="#1675a9",
                arrowprops={"arrowstyle": "-", "color": "#1675a9"})
    ax.set_xlim(0, 360)
    ax.set_ylim(-5.2, 5.5)
    ax.set_xticks([0, 90, 180, 270, 360])
    ax.set_xlabel("Unit direction angle (degrees)")
    ax.set_ylabel("Change per unit distance")
    ax.set_title(r"$D_{(\cos\theta,\sin\theta)}f=2\cos\theta+4\sin\theta$",
                 fontsize=12)
    fig.suptitle("One gradient predicts the rate in every direction",
                 fontsize=16, y=0.98)
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.22, top=0.82, wspace=0.35)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
