"""North-pole projection geometry; Python 3.14, Matplotlib 3.10, NumPy 2.3."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, (ax, eq) = plt.subplots(1, 2, figsize=(10.2, 4.7),
                                gridspec_kw={"width_ratios": [1.55, 1]})
    theta = np.linspace(0, 2 * np.pi, 500)
    ax.fill(np.cos(theta), np.sin(theta), color="#f3f6fa")
    ax.plot(np.cos(theta), np.sin(theta), color="#65788c", lw=1.7)
    ax.axhline(0, color="#394b59", lw=1.4)
    ax.axvline(0, color="#9aa8b4", lw=0.8)
    ax.annotate("", xy=(2.43, 0), xytext=(2.17, 0),
                arrowprops={"arrowstyle": "->", "color": "#394b59"})
    ax.annotate("", xy=(0, 1.35), xytext=(0, 1.12),
                arrowprops={"arrowstyle": "->", "color": "#394b59"})
    ax.text(2.4, -.16, "$X=x$")
    ax.text(.08, 1.25, "$Z$")
    ax.scatter([0, 0], [1, -1], c="#253746", s=35, zorder=5)
    ax.text(-.6, 1.06, "$N$ (infinity)")
    ax.text(-.63, -1.17, "$S$ ($z=0$)")
    for x, color in [(0.5, "#2468b4"), (2.0, "#bc5d1b")]:
        t = 2 / (1 + x*x)
        X, Z = t*x, 1-t
        ax.plot([0, x, X], [1, 0, Z], color=color, lw=2)
        ax.scatter([x, X], [0, Z], color=color, s=42, zorder=6)
    ax.text(.31, .08, "$z=1/2$", color="#2468b4")
    ax.text(1.82, -.21, "$z=2$", color="#bc5d1b")
    ax.annotate("$(4/5,0,-3/5)$", xy=(.8, -.6), xytext=(1.01, -.8),
                color="#2468b4", arrowprops={"arrowstyle": "-", "color": "#2468b4"})
    ax.annotate("$(4/5,0,3/5)$", xy=(.8, .6), xytext=(1.03, .82),
                color="#bc5d1b", arrowprops={"arrowstyle": "-", "color": "#bc5d1b"})
    ax.text(-1.23, -.22, "$Z=0$ plane", fontsize=11)
    ax.set(xlim=(-1.35, 2.55), ylim=(-1.3, 1.4), aspect="equal")
    ax.set_title("Real-axis section ($Y=0$)", pad=20)
    ax.axis("off")

    eq.plot(np.cos(theta), np.sin(theta), color="#65788c", lw=1.7)
    for end in [(1.38, 0), (0, 1.38)]:
        eq.annotate("", xy=end, xytext=(-end[0], -end[1]),
                    arrowprops={"arrowstyle": "->", "color": "#394b59"})
    eq.scatter([1, 0, -1, 0], [0, 1, 0, -1], c="#2468b4", s=36, zorder=5)
    for xy, label, offset in [((1, 0), "$1$", (8, 9)), ((0, 1), "$i$", (8, 5)),
                              ((-1, 0), "$-1$", (-25, 9)), ((0, -1), "$-i$", (8, -12))]:
        eq.annotate(label, xy, xytext=offset, textcoords="offset points")
    eq.text(1.27, -.23, "$X=x$")
    eq.text(.13, 1.31, "$Y=y$")
    eq.text(-1.25, -1.63, "Equator: $Z=0$, $|z|=1$\nPositive $Y$ means positive Im$(z)$", fontsize=11)
    eq.set(xlim=(-1.45, 1.55), ylim=(-1.72, 1.55), aspect="equal")
    eq.set_title("Equator viewed from positive $Z$", pad=20)
    eq.axis("off")
    fig.suptitle("Stereographic projection from the north pole", fontsize=16, y=.98)
    fig.subplots_adjust(left=.035, right=.98, top=.83, bottom=.08, wspace=.19)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
