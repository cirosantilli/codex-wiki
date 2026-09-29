"""Illustrate a global two-component scalar potential, in dimensionless units.

Run from _media; tested with Python 3.14, matplotlib 3.10.7, NumPy 2.3.5.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def potential(x, y, h=0.0):
    return (x * x + y * y - 1.0) ** 2 / 4.0 - h * x


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.25), layout="constrained")
    xy = np.linspace(-1.5, 1.5, 301)
    x, y = np.meshgrid(xy, xy)
    theta = np.linspace(-np.pi, np.pi, 501)
    h = 0.15
    w = np.roots([1, 0, -1, -h])
    w = float(w[np.isreal(w)].real.max())
    for ax, source, title in zip(axes[:2], (0.0, h),
                                 ("No source: a circle of minima", "Positive source: one minimum")):
        ax.contourf(x, y, potential(x, y, source),
                    levels=np.linspace(-0.18, 1.6, 25), cmap="Blues", extend="max")
        ax.plot(np.cos(theta), np.sin(theta), "--", color="#c76c18", lw=2,
                label=r"$r=v=1$ reference")
        ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel=r"$\phi_1/v$",
               ylabel=r"$\phi_2/v$", title=title, aspect="equal")
        ax.set_xticks([-1, 0, 1])
        ax.set_yticks([-1, 0, 1])
    axes[0].plot(1, 0, "o", color="#a93226", ms=7)
    axes[0].annotate("chosen point", xy=(1, 0), xytext=(-0.9, -1.25),
                     arrowprops={"arrowstyle": "->", "color": "#a93226"})
    axes[0].annotate("radial", xy=(1.43, 0), xytext=(0.27, 0.08),
                     arrowprops={"arrowstyle": "->", "color": "#a93226"}, color="#a93226")
    axes[0].annotate("angular", xy=(0.7, 0.7), xytext=(-1.3, 1.15),
                     arrowprops={"arrowstyle": "->", "connectionstyle": "arc3,rad=-0.2"})
    axes[1].plot(w, 0, "o", color="#a93226", ms=7)
    axes[1].annotate(r"$h=0.15$", xy=(1.25, -1.1), xytext=(-0.65, -1.15),
                     arrowprops={"arrowstyle": "->", "lw": 2, "color": "#a93226"})
    axes[1].text(0, 1.18, rf"$w={w:.3f}>v$", ha="center")
    q = np.linspace(-0.6, 0.6, 501)
    ax = axes[2]
    ax.plot(q, potential(1 + q, 0), color="#a93226", lw=2.2,
            label=r"radial $r=1+q$, $h=0$")
    ax.plot(q, potential(np.cos(q), np.sin(q)), color="#137b70", lw=2.5,
            label=r"angular $\theta=q$, $h=0$")
    ax.plot(q, h * w * (1 - np.cos(q)), color="#c76c18", lw=2.2, ls="--",
            label=r"angular $r=w$, $h=0.15$")
    ax.set(xlabel=r"displacement $q$ (model units)", ylabel=r"$U-U_{\min}$ along each path",
           title="Angular flatness and source lifting", ylim=(-0.015, 0.43))
    ax.legend(loc="upper left", fontsize=9)
    ax.text(0.03, 0.53, "At h = 0: radial curvature = 2\nangular curvature = 0",
            transform=ax.transAxes, fontsize=10)
    fig.suptitle(r"Global symmetry: $U_h=(\phi_1^2+\phi_2^2-1)^2/4-h\phi_1$", fontsize=15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
