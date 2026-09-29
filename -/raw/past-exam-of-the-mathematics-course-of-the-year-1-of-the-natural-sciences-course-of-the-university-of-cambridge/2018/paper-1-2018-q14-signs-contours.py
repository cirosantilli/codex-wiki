"""Original sign-region and contour plots; Python 3.14, root NumPy/Matplotlib.

Write the PNG basename in cwd for mirrored _media rendering.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    a = np.sqrt(3)/2
    grid = np.unique(np.r_[np.linspace(-2.4, 2.4, 801), -a, -0.5, 0, 0.5, a])
    x, y = np.meshgrid(grid, grid)
    f = (1-4*x*y)*np.exp(-x*x-y*y)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.2), layout="constrained")
    fig.set_facecolor("white")
    axes[0].contourf(x, y, f, levels=[-1, 0, 2], colors=["#fae3dc", "#e4eff4"])
    axes[0].contour(x, y, f, levels=[0], colors=["#222222"], linewidths=1.7)
    axes[0].text(1.48, 1.7, "$f<0$", color="#9c3a28", fontsize=12)
    axes[0].text(-2.03, -1.85, "$f<0$", color="#9c3a28", fontsize=12)
    axes[0].text(1.35, -1.55, "$f>0$", color="#176b9b", fontsize=12)
    axes[0].text(-2.0, 1.55, "$f>0$", color="#176b9b", fontsize=12)
    axes[0].set_title("Signs separated by $xy=1/4$")
    levels = [-0.40, -0.25, -0.08, 0, 0.08, 0.35, 0.7, 1.0, 1.1, 1.2]
    colors = ["#a13d32"]*3+["#222222"]+["#176b9b"]*3+["#70468f"]*3
    cs = axes[1].contour(x, y, f, levels=levels, colors=colors, linewidths=1.0)
    axes[1].clabel(cs, fmt=lambda v: f"{v:g}", fontsize=8)
    axes[1].set_title("Completed level sets; saddle height $f=1$")
    for ax in axes:
        ax.axhline(0, color="0.6", lw=0.65, zorder=0)
        ax.axvline(0, color="0.6", lw=0.65, zorder=0)
        ax.scatter([-a, a], [-a, a], color="#176b9b", s=35, label="minima", zorder=6)
        ax.scatter([-0.5, 0.5], [0.5, -0.5], color="#b83c32", s=35, label="maxima", zorder=6)
        ax.scatter([0], [0], color="#333333", marker="D", s=30, label="saddle", zorder=6)
        ax.set(xlim=(-2.4, 2.4), ylim=(-2.4, 2.4), aspect="equal", xlabel="$x$", ylabel="$y$")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(loc="upper center", ncol=3, fontsize=9, framealpha=0.97)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
