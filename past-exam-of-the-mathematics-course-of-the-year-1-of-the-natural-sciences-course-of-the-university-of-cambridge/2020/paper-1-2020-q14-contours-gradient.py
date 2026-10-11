"""Original contour and gradient construction for Q14.

Python 3.14; NumPy and Matplotlib versions are in root pyproject.toml.
The PNG basename is written in cwd, allowing a mirrored _media output.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def function(x, y):
    return (1-x*x-y*y)**2 + 3.5*np.log(3+y*y)


def gradient(x, y):
    s = x*x+y*y
    return 4*x*(s-1), y*(4*(s-1)+7/(3+y*y))


def main():
    a = 1/np.sqrt(2)
    h = 0.25+3.5*np.log(3.5)
    grid = np.unique(np.r_[np.linspace(-1.7, 1.7, 751), -1, 0, 1, -a, a])
    x, y = np.meshgrid(grid, grid)
    z = function(x, y)
    levels = [4.0, 4.35, h, 4.75, 5.0, 5.8, 7.5]
    colors = ["#176b9b", "#268c96", "#bd6a23", "#8e4f91", "#68705b", "#516b91", "#818181"]
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 6.0), layout="constrained")
    fig.set_facecolor("white")
    for ax in axes:
        cs = ax.contour(x, y, z, levels=levels, colors=colors, linewidths=1.2)
        ax.clabel(cs, fmt=lambda v: "saddle" if abs(v-h)<1e-8 else f"{v:.2f}", fontsize=8)
        ax.axhline(0, color="0.65", lw=0.65, zorder=0)
        ax.axvline(0, color="0.65", lw=0.65, zorder=0)
        ax.scatter([-1, 1], [0, 0], s=42, color="#176b9b", label="minima", zorder=6)
        ax.scatter([0], [0], marker="s", s=38, color="#a32e35", label="maximum", zorder=6)
        ax.scatter([0, 0], [-a, a], marker="D", s=36, color="#bd6a23", label="saddles", zorder=6)
        ax.set(xlim=(-1.7, 1.7), ylim=(-1.7, 1.7), aspect="equal", xlabel="$x$", ylabel="$y$")
    axes[0].set_title("Level sets and stationary points")
    axes[0].legend(loc="lower center", ncol=3, fontsize=9, framealpha=0.95)
    axes[1].set_title("Arrows point towards increasing $f$")
    samples = [(v, 0) for v in [-1.42, -0.72, -0.34, 0.34, 0.72, 1.42]]
    samples += [(0, v) for v in [-1.38, -0.98, -0.42, 0.42, 0.98, 1.38]]
    for cx, cy in [(-1, 0), (1, 0), (0, 0), (0, -a), (0, a)]:
        samples += [(cx+dx, cy+dy) for dx, dy in [(-0.16, -0.14), (0.16, -0.14),
                                                           (-0.16, 0.14), (0.16, 0.14)]]
    sx, sy = np.array(samples).T
    gx, gy = gradient(sx, sy)
    size = np.hypot(gx, gy)
    axes[1].quiver(sx, sy, gx/size, gy/size, angles="xy", scale_units="xy", scale=7.5,
                   color="#222222", width=0.004, headwidth=4, headlength=5, pivot="mid", zorder=7)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
