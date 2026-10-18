"""Plot Oxford Prelims Mathematics IV (2021), Question 3(b)(iii).

Run from the desired output directory. Dependencies are declared in the
repository pyproject.toml; tested with Python 3.14.4, NumPy 2.3.5 and
Matplotlib 3.10.7. The original plot is saved on an opaque white background.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(0, 1, 160)
    theta = np.linspace(0, 2 * np.pi, 90)
    rho = np.sqrt(25 + 62 * t + 82 * t**2)
    z = 1 + 6 * t
    fig = plt.figure(figsize=(10.4, 4.4), facecolor="white", layout="constrained")
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    ax.plot_surface(
        rho[:, None] * np.cos(theta),
        rho[:, None] * np.sin(theta),
        np.broadcast_to(z[:, None], (len(t), len(theta))),
        color="#6baed6", alpha=0.5, linewidth=0, antialiased=True,
    )
    ax.plot(3 + 9 * t, 4 + t, z, color="#b0292d", lw=3,
            label="Original straight segment")
    ax.scatter([3, 12], [4, 5], [1, 7], color="#b0292d", s=24)
    ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$",
           title="Actual surface swept about the vertical axis")
    ax.set_box_aspect((1, 1, 0.65))
    ax.view_init(elev=23, azim=128)
    ax.legend(loc="upper left", fontsize=8)
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.plot(rho, z, color="#226eaa", lw=2.8, label="Actual radial profile")
    ax2.plot(5 + 8 * t, z, "--", color="#d88428", lw=2,
             label="Frustum joining endpoint radii")
    ax2.scatter([5, 13], [1, 7], color="#222222", zorder=4)
    ax2.annotate("$(5,1)$", (5, 1), xytext=(7, -2),
                 textcoords="offset points", fontsize=9)
    ax2.annotate("$(13,7)$", (13, 7), xytext=(-50, 7),
                 textcoords="offset points", fontsize=9)
    ax2.set(xlabel=r"Radius $\rho=\sqrt{x^2+y^2}$", ylabel="Height $z$",
            title="The radial profile is curved",
            xlim=(4.3, 14), ylim=(0.5, 7.8))
    ax2.text(0.04, 0.96,
             r"Actual area $\approx 561.8721$" + "\n" +
             r"Frustum area $180\pi\approx 565.4867$",
             transform=ax2.transAxes, va="top", fontsize=10,
             bbox={"facecolor": "white", "edgecolor": "#dddddd", "alpha": 0.95})
    ax2.grid(alpha=0.22)
    ax2.legend(loc="lower right", fontsize=8)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", dpi=130,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
