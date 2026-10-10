"""Draw rotation invariance of normalized circle measure; write PNG in CWD.

Run from _media: python3 ../circle-group-rotation-invariance.py
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def panel(ax, start, end, color, title, endpoint_labels):
    theta = np.linspace(0, 2 * np.pi, 721)
    ax.plot(np.cos(theta), np.sin(theta), color="#9aa5ae", linewidth=1.6)
    ax.axhline(0, color="#e2e6ea", linewidth=1)
    ax.axvline(0, color="#e2e6ea", linewidth=1)
    arc = np.linspace(start, end, 161)
    ax.plot(np.cos(arc), np.sin(arc), color=color, linewidth=8,
            solid_capstyle="round")
    for angle, label in zip((start, end), endpoint_labels):
        point = np.array([np.cos(angle), np.sin(angle)])
        ax.plot([0, point[0]], [0, point[1]], color=color, linewidth=1.3)
        ax.scatter(*point, s=38, color=color, edgecolors="white", zorder=4)
        ax.text(*(1.21 * point), label, ha="center", va="center", fontsize=12)
    ax.text(1.08, -.12, "1", fontsize=11)
    ax.text(-.10, -1.16, r"$-i$", fontsize=11)
    ax.text(0, -.25, r"$\pi/3$", ha="center", color=color, fontsize=13)
    ax.set_title(title, fontsize=13, pad=10, color=color)
    ax.set(xlim=(-1.45, 1.45), ylim=(-1.4, 1.45), aspect="equal")
    ax.axis("off")


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.6), dpi=100)
    fig.patch.set_facecolor("white")
    fig.subplots_adjust(left=.05, right=.95, top=.79, bottom=.17, wspace=.32)
    fig.suptitle("Uniform angle measure survives a quarter-turn", y=.965,
                 fontsize=16)
    fig.text(.5, .86, r"$z\mapsto iz=e^{i\pi/2}z$  (counterclockwise)",
             ha="center", fontsize=13)
    panel(axes[0], np.pi / 6, np.pi / 2, "#187ca2", "Original arc A",
          (r"$\pi/6$", r"$\pi/2$"))
    panel(axes[1], 2 * np.pi / 3, np.pi, "#c76821", "Rotated arc iA",
          (r"$2\pi/3$", r"$\pi$"))
    fig.text(.5, .085, r"$\mu(A)=\mu(iA)=\dfrac{\pi/3}{2\pi}=\dfrac{1}{6}$",
             ha="center", fontsize=14)
    fig.savefig(Path.cwd() / "circle-group-rotation-invariance.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
