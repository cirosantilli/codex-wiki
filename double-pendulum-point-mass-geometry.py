"""Draw the equal-point-mass double pendulum; emit a PNG in the current directory."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(8, 5.12), dpi=125)
    ax = fig.add_axes((0.06, 0.13, 0.51, 0.76))
    theta = np.deg2rad([28, -22])
    rods = np.column_stack((np.sin(theta), -np.cos(theta)))
    points = np.vstack(([0, 0], np.cumsum(rods, axis=0)))
    colors = ["#246ba0", "#bd5127"]
    ax.plot([-0.28, 0.28], [0.08, 0.08], color="#444444", lw=5)
    for i, color in enumerate(colors):
        start, end = points[i:i + 2]
        ax.plot(*np.stack((start, end)).T, color=color, lw=4, zorder=3)
        ax.plot([start[0], start[0]], [start[1], start[1] - 0.65],
                "--", color="#aaaaaa", lw=1.4)
        mid = (start + end) / 2
        ax.text(mid[0] + (0.08 if i == 0 else 0.16), mid[1],
                r"$\ell$", color=color, fontsize=17)
        angles = sorted([-90, -90 + np.rad2deg(theta[i])])
        ax.add_patch(Arc(start, 0.68, 0.68, theta1=angles[0],
                         theta2=angles[1], color=color, lw=2))
        ax.text(start[0] + (0.11 if i == 0 else -0.21),
                start[1] - 0.48, rf"$\theta_{i + 1}$", color=color)
        ax.scatter(*end, s=270, color=color, edgecolor="white", lw=1.5, zorder=4)
        ax.text(end[0] + 0.14, end[1] - 0.05, r"$m$", fontsize=17, color=color)
    ax.scatter(0, 0, s=50, color="#333333", zorder=5)
    ax.text(-0.09, 0.17, "fixed pivot", ha="center")
    ax.annotate("", (0.97, -0.8), (0.97, -0.23),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#555555"})
    ax.text(1.02, -0.52, r"$g$", va="center", fontsize=17)
    origin = np.array([-0.52, -1.6])
    for delta, label in [(np.array([0.3, 0]), "$x$"), (np.array([0, 0.3]), "$y$")]:
        ax.annotate("", origin + delta, origin,
                    arrowprops={"arrowstyle": "->", "lw": 1.3, "color": "#555555"})
        ax.text(*(origin + delta + [0.02, 0.02]), label, fontsize=13)
    ax.set(xlim=(-0.72, 1.27), ylim=(-2.13, 0.32), aspect="equal")
    ax.axis("off")
    fig.suptitle("Double pendulum: geometry before dynamics", y=0.96, fontsize=18)
    fig.text(0.60, 0.77, "Two equal point masses\nTwo massless rigid rods", linespacing=1.6)
    fig.text(0.60, 0.57, r"$x_1=\ell\sin\theta_1$" + "\n" + r"$y_1=-\ell\cos\theta_1$",
             linespacing=1.8, color=colors[0])
    fig.text(0.60, 0.34, r"$x_2=\ell(\sin\theta_1+\sin\theta_2)$" + "\n" +
             r"$y_2=-\ell(\cos\theta_1+\cos\theta_2)$", linespacing=1.8,
             color=colors[1], fontsize=11)
    fig.text(0.5, 0.05, "Each angle uses its own downward vertical; the rod bend is a difference.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
