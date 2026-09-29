"""Draw Q6(d)'s crescent and sector images with NumPy and Matplotlib.

Tested with Python 3.14, NumPy 2.3, Matplotlib 3.10. Output goes to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.7), layout="constrained")
    fig.patch.set_facecolor("white")
    color, fill = "#175b9e", "#d7e8f7"
    for ax in axes:
        ax.set_facecolor("white")
        ax.set_aspect("equal")
        ax.axhline(0, color="0.8", lw=.7)
        ax.axvline(0, color="0.8", lw=.7)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
    x = np.linspace(-1.6, 1.6, 600)
    y = np.linspace(-.6, 2.6, 600)
    xx, yy = np.meshgrid(x, y)
    mask = ((xx**2 + (yy + 1)**2 > 2) & (xx**2 + (yy - 1)**2 < 2))
    axes[0].contourf(xx, yy, mask.astype(float), levels=[.5, 1.5], colors=[fill])
    theta = np.linspace(0, 2*np.pi, 800)
    for center in (-1, 1):
        axes[0].plot(np.sqrt(2)*np.cos(theta), center + np.sqrt(2)*np.sin(theta),
                     color=color, lw=1.4)
    axes[0].scatter([-1, 1], [0, 0], facecolor="white", edgecolor=color, zorder=5)
    axes[0].text(-1.25, -.25, "$-1$", fontsize=10)
    axes[0].text(1.06, -.25, "$1$", fontsize=10)
    axes[0].text(.15, 1.35, "$B$", fontsize=15, color=color)
    axes[0].set_xlim(-1.7, 1.7)
    axes[0].set_ylim(-.6, 2.65)
    axes[0].set_title("1. The circular crescent", fontsize=12)
    axes[0].set_xlabel("Boundary intersections at $z=\\pm1$", fontsize=10)
    def sector(ax, low, high, limit):
        angles = np.linspace(low, high, 150)
        ax.fill(np.r_[0, limit*np.cos(angles), 0],
                np.r_[0, limit*np.sin(angles), 0], color=fill, zorder=1)
        for ang in (low, high):
            ax.plot([0, limit*np.cos(ang)], [0, limit*np.sin(ang)], color=color, lw=1.6)
        radius = .65
        ax.plot(radius*np.cos(angles), radius*np.sin(angles), color="#a65c28", lw=1.2)
        ax.scatter([0], [0], facecolor="white", edgecolor=color, zorder=5)
    sector(axes[1], np.pi/4, 3*np.pi/4, 7)
    axes[1].text(-.6, 1.0, r"$\pi/2$", color="#a65c28", fontsize=12)
    axes[1].set_xlim(-2.05, 2.05)
    axes[1].set_ylim(-.25, 3.3)
    axes[1].set_title(r"2. $w=(z-1)/(z+1)$", fontsize=12)
    axes[1].set_xlabel(r"$\pi/4<\arg w<3\pi/4$", fontsize=11)
    sector(axes[2], 0, np.pi/3, 7)
    axes[2].text(.78, .35, r"$\pi/3$", color="#a65c28", fontsize=12)
    axes[2].text(1.6, 1.0, "$C$", fontsize=15, color=color)
    axes[2].set_xlim(-.25, 3.5)
    axes[2].set_ylim(-.25, 3.3)
    axes[2].set_title(r"3. $\xi=(e^{-i\pi/4}w)^{2/3}$", fontsize=12)
    axes[2].set_xlabel(r"$0<\arg\xi<\pi/3$", fontsize=11)
    fig.savefig(Path.cwd() / "2021-q6-crescent.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
