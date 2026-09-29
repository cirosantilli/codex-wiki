"""Show heat and transport data geometry; output basename.png to cwd.

Heat contours use the exact solution x + exp(-pi**2*t)*sin(pi*x).
Transport characteristics have speed one; no numerical PDE solver is used.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def heat(x, t):
    return x + np.exp(-np.pi**2 * t) * np.sin(np.pi * x)


def characteristic_foot(x, t):
    """Return the initial or inflow intersection when tracing backwards."""
    return (x - t, 0) if x >= t else (0, t - x)


def main():
    plt.rcParams.update({"font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.5), facecolor="white")
    blue, orange, green, gray = "#1266a0", "#bd5017", "#23765a", "#888888"
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="Position x", ylabel="Time t",
               xticks=[0, 0.5, 1], yticks=[0, 0.5, 1], aspect="equal")
        ax.tick_params(axis="both", length=3)
        ax.yaxis.labelpad = 34
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.plot([0, 1], [1, 1], color=gray, ls="--", lw=1.2, clip_on=False)
        ax.plot([0, 1], [0, 0], color=blue, lw=4, clip_on=False, zorder=4)
        ax.plot([0, 0], [0, 1], color=orange, lw=4, clip_on=False, zorder=4)
    ax = axes[0]
    ax.set_title(r"Heat: $u_t=u_{xx}$", fontsize=14, pad=28)
    ax.plot([1, 1], [0, 1], color=orange, lw=4, clip_on=False, zorder=4)
    x, t = np.meshgrid(np.linspace(0, 1, 301), np.linspace(0, 1, 301))
    contours = ax.contour(x, t, heat(x, t), levels=[0.25, 0.5, 0.75, 1.1],
                          colors="#bbc2c8", linewidths=1)
    ax.clabel(contours, inline=True, fontsize=8, fmt="u=%.2g")
    ax.text(-0.12, 0.52, "a(t) = 0", rotation=90, ha="center", va="center",
            transform=ax.transAxes, color=orange)
    ax.text(1.1, 0.52, "b(t) = 1", rotation=90, ha="center", va="center",
            transform=ax.transAxes, color=orange)
    ax.text(0.5, -0.2, r"$g(x)=x+\sin(\pi x)$", transform=ax.transAxes,
            ha="center", color=blue)
    ax.text(0.5, 1.035, "Future values are determined", transform=ax.transAxes,
            ha="center", fontsize=9, color=gray)

    ax = axes[1]
    ax.set_title(r"Transport: $u_t+u_x=0$", fontsize=14, pad=28)
    ax.plot([1, 1], [0, 1], color=gray, lw=1.2, ls="--", clip_on=False)
    for offset in np.linspace(-0.8, 0.8, 9):
        start_t, end_t = max(0, -offset), min(1, 1 - offset)
        ray_t = np.linspace(start_t, end_t, 20)
        ax.plot(ray_t + offset, ray_t, color="#d7dee3", lw=1)
    ax.plot([0, 1], [0, 1], color=gray, ls=":", lw=1.3)
    for point, label, shift in [
        ((0.75, 0.6), "From g(0.15)", (-0.13, -0.25)),
        ((0.35, 0.65), "From a(0.30)", (-0.23, 0.09)),
    ]:
        foot = characteristic_foot(*point)
        ax.annotate("", xy=point, xytext=foot,
                    arrowprops={"arrowstyle": "->", "color": green, "lw": 2.3})
        ax.plot(*point, "o", color=green, ms=5)
        ax.text(point[0] + shift[0], point[1] + shift[1], label,
                fontsize=9, color=green,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    ax.text(-0.12, 0.52, "Inflow a(t)", rotation=90, ha="center", va="center",
            transform=ax.transAxes, color=orange)
    ax.text(1.1, 0.52, "Outflow determined", rotation=90, ha="center", va="center",
            transform=ax.transAxes, color=gray)
    ax.text(0.5, -0.2, "Initial profile g(x)", transform=ax.transAxes,
            ha="center", color=blue)
    ax.text(0.5, 1.035, "Future values are determined", transform=ax.transAxes,
            ha="center", fontsize=9, color=gray)
    fig.suptitle("The equation decides where to prescribe data", fontsize=16, y=0.975)
    fig.text(0.5, 0.07, "Blue: initial data     Orange: boundary data     Dashed: determined values",
             ha="center", fontsize=11)
    fig.text(0.5, 0.02, "Left: contours of an exact heat solution.   Right: straight characteristics, speed = 1.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.09, right=0.93, bottom=0.26, top=0.77, wspace=0.42)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=125, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
