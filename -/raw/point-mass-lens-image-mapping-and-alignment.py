"""Draw signed point-lens roots and exact alignment; output to the CWD.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
This is a theoretical diagram, not an observed sky image.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, (ax, ring) = plt.subplots(1, 2, figsize=(10.0, 4.7), facecolor="white", gridspec_kw={"width_ratios": [1.3, 1.0]})
    u = 0.6
    roots = (u + np.array([1.0, -1.0]) * np.sqrt(u**2 + 4)) / 2
    for start, end in [(-2.6, -0.15), (0.15, 2.6)]:
        x = np.linspace(start, end, 500)
        ax.plot(x, x - 1 / x, color="#263f56", lw=2)
    ax.axhline(u, color="#7d4394", lw=1.8, label=r"Source $u=0.6$")
    ax.axhline(0, color="#a1a1a1", lw=0.7)
    ax.axvline(0, color="#a1a1a1", lw=0.7)
    for r, color in zip(roots, ["#1268a1", "#bc472d"]):
        ax.scatter(r, u, s=65, color=color, zorder=5)
        ax.vlines(r, -3, u, color=color, linestyles="--", lw=1.2)
    ax.annotate("Outer image\n$x_+=1.344$\nPositive parity", (roots[0], u), (1.2, -1.9), color="#1268a1", fontsize=11, arrowprops={"arrowstyle": "->", "color": "#1268a1"})
    ax.annotate("Inner image\n$x_-=-0.744$\nNegative parity", (roots[1], u), (-2.48, 1.6), color="#bc472d", fontsize=11, arrowprops={"arrowstyle": "->", "color": "#bc472d"})
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-3, 3.5)
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_xlabel(r"Signed image angle $x=\theta/\theta_E$")
    ax.set_ylabel(r"Signed source angle $u=\beta/\theta_E$")
    ax.set_title(r"Offset source: $u=x-1/x$", fontsize=14, pad=13)
    ax.legend(loc="upper right", fontsize=10, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    t = np.linspace(0, 2 * np.pi, 500)
    ring.plot(np.cos(t), np.sin(t), color="#1268a1", lw=3)
    ring.axhline(0, color="#cccccc", lw=0.7)
    ring.axvline(0, color="#cccccc", lw=0.7)
    ring.scatter(0, 0, color="#7d4394", s=110, marker="*", zorder=5)
    ring.scatter([-1, 1], [0, 0], s=50, color="#bc472d", zorder=5)
    ring.annotate("", (np.cos(0.55), np.sin(0.55)), (0, 0), arrowprops={"arrowstyle": "->", "color": "#444444"})
    ring.text(0.42, 0.38, r"$\theta_E$", color="#444444")
    ring.text(0.02, -0.25, "Aligned source direction", ha="center", color="#7d4394", fontsize=10)
    ring.text(0, -1.35, "Red points: a diameter cut\nBlue circle: all image directions", ha="center", fontsize=10, linespacing=1.5)
    ring.set_title(r"Exact alignment: $\boldsymbol{\beta}=0$", fontsize=14, pad=13)
    ring.set_xlim(-1.65, 1.65)
    ring.set_ylim(-1.65, 1.65)
    ring.set_aspect("equal")
    ring.set_xlabel(r"$\theta_1/\theta_E$")
    ring.set_ylabel(r"$\theta_2/\theta_E$")
    ring.set_xticks([-1, 0, 1])
    ring.set_yticks([-1, 0, 1])
    ring.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Point-mass gravitational lens: two images or an Einstein ring", fontsize=16, y=0.97)
    fig.text(0.5, 0.015, "Ideal geometric-optics model; angles are normalized by the Einstein angular radius.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.17, top=0.79, wspace=0.33)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
