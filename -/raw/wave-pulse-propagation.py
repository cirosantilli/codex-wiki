"""Plot a smooth wave pulse and its causal interval; save PNG in the cwd.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def bump(z):
    """Smooth compact bump, with support [-1, 1] and peak one."""
    z = np.asarray(z, dtype=float)
    out = np.zeros_like(z)
    inside = np.abs(z) < 1
    out[inside] = np.exp(1 - 1 / (1 - z[inside] ** 2))
    return out


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    left_color, right_color, total_color = "#c75a11", "#176ca4", "#252525"
    fig = plt.figure(figsize=(10, 6.3), layout="constrained")
    grid = fig.add_gridspec(3, 2, width_ratios=(1.25, 1), wspace=0.16)
    fig.suptitle("A pulse released from rest: splitting and finite-speed causality",
                 fontsize=15)
    x = np.linspace(-3, 3, 1501)
    for row, t in enumerate((0.0, 0.5, 1.5)):
        ax = fig.add_subplot(grid[row, 0])
        left, right = 0.5 * bump(x + t), 0.5 * bump(x - t)
        ax.plot(x, left + right, color=total_color, lw=2.7, label="total")
        ax.plot(x, left, color=left_color, lw=2, ls="--", label="left-moving half")
        ax.plot(x, right, color=right_color, lw=2, ls=":", label="right-moving half")
        ax.set(xlim=(-3, 3), ylim=(-0.07, 1.12), ylabel=r"$u/A$")
        ax.text(0.025, 0.86, rf"$ct/a={t:g}$", transform=ax.transAxes)
        ax.set_yticks((0, 0.5, 1))
        ax.grid(alpha=0.18)
        if row == 0:
            ax.set_title(r"$f(x)=A\,b(x/a),\quad g(x)=0$", fontsize=12)
            ax.legend(loc="upper right", fontsize=8.5, framealpha=1)
        if row == 2:
            ax.set_xlabel(r"Position $x/a$")
            for center, direction, color in ((-t, -1, left_color), (t, 1, right_color)):
                ax.annotate("", xy=(center + direction * 0.7, 0.83),
                            xytext=(center, 0.83),
                            arrowprops={"arrowstyle": "->", "color": color, "lw": 2})
        else:
            ax.tick_params(labelbottom=False)

    ax = fig.add_subplot(grid[:, 1])
    x_star, t_star = 0.5, 1.5
    ax.fill((-1, 2, x_star), (0, 0, t_star), color="#e4edf4", zorder=0)
    ax.plot((-1, x_star), (0, t_star), color=left_color, lw=2)
    ax.plot((2, x_star), (0, t_star), color=right_color, lw=2)
    ax.plot((-1, 2), (0, 0), color="#252525", lw=5, solid_capstyle="butt")
    ax.scatter((x_star,), (t_star,), color="#252525", zorder=4)
    ax.text(x_star, t_star + 0.06, r"$(x_*,t_*)=(0.5,1.5)$", ha="center", fontsize=11)
    ax.text(x_star, 0.30, "Only initial data in\nthis interval can matter",
            ha="center", fontsize=11)
    ax.text(-0.42, 0.94, r"$x-t=-1$", rotation=55, color=left_color)
    ax.text(1.37, 0.88, r"$x+t=2$", rotation=-55, color=right_color)
    ax.annotate("initial interval [-1, 2]", xy=(0.5, 0), xytext=(0.5, -0.27),
                ha="center", arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.set(xlim=(-1.55, 2.55), ylim=(-0.34, 1.91), xlabel="Position x", ylabel="Time t")
    ax.set_title("Backward characteristics\n(normalized speed c = 1)", fontsize=12)
    ax.set_xticks((-1, 0, 0.5, 2))
    ax.set_yticks((0, 0.5, 1, 1.5))
    ax.grid(alpha=0.18)
    fig.savefig(Path.cwd() / "wave-pulse-propagation.png", dpi=140, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
