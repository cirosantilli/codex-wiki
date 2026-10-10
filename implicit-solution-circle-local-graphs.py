"""Draw regular circular levels and a singular crossing level.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5:
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../implicit-solution-circle-local-graphs.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.facecolor": "white"})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 5.4), layout="constrained", facecolor="white")
    theta = np.linspace(0, 2 * np.pi, 1001)
    for radius in [1, 2, 2.5]:
        ax.plot(radius * np.cos(theta), radius * np.sin(theta),
                color="#c7cdd4", linewidth=1.2, zorder=1)
    ax.plot(2 * np.cos(theta), 2 * np.sin(theta), color="#547aab", linewidth=2, zorder=2)
    branch_x = np.linspace(-0.45, 1.55, 300)
    ax.plot(branch_x, np.sqrt(4 - branch_x**2), color="#167a50", linewidth=4, zorder=3)
    px, py = 1, np.sqrt(3)
    tangent_x = np.linspace(0.3, 1.7, 100)
    ax.plot(tangent_x, py - (tangent_x - px) / np.sqrt(3),
            color="#167a50", linestyle="--", linewidth=1.5, zorder=4)
    ax.scatter([px], [py], color="#167a50", s=40, zorder=5)
    ax.annotate(r"$y=\sqrt{4-x^2}$" + "\n" + r"$F_y\ne0$: local graph",
                xy=(px, py), xytext=(-2.6, 2.7), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#167a50"})
    ax.plot([2, 2], [-0.85, 0.85], "--", color="#b43b30", linewidth=1.6)
    ax.scatter([2, -2], [0, 0], facecolors="white", edgecolors="#b43b30", s=60, linewidths=2, zorder=5)
    ax.annotate(r"$F_y=0,\ F_x\ne0$" + "\nVertical tangent\nScalar ODE undefined",
                xy=(2, 0), xytext=(0.1, -2.9), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#b43b30"})
    ax.scatter([0], [0], color="#444b53", s=35, zorder=5)
    ax.text(-2.6, -2.55, "C = 0: isolated point", fontsize=11, color="#444b53")
    ax.set(title=r"$F=x^2+y^2$: circle $C=4$", xlim=(-3.05, 3.05), ylim=(-3.2, 3.35),
           xlabel="x", ylabel="y")

    t = np.linspace(-2, 2, 301)
    bx.plot(t, t, color="#235eab", linewidth=2.4, label="y = x")
    bx.plot(t, -t, color="#a645a2", linewidth=2.4, label="y = −x")
    bx.scatter([0], [0], color="#b43b30", s=55, zorder=5)
    bx.annotate(r"$G_x=G_y=0$" + "\nTwo branches cross",
                xy=(0, 0), xytext=(-2.5, 2.3), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#b43b30"})
    bx.text(0, -2.7, r"Both solve $yy'=x$, including at $(0,0)$." + "\n" +
            r"Dividing to get $y'=x/y$ excludes $(0,0)$.",
            ha="center", va="center", fontsize=11)
    bx.set(title=r"$G=y^2-x^2$: singular level $G=0$", xlim=(-3.05, 3.05),
           ylim=(-3.2, 3.35), xlabel="x", ylabel="y")
    bx.legend(loc="upper right", fontsize=11, frameon=False)
    for axis in (ax, bx):
        axis.set_aspect("equal", adjustable="box")
        axis.axhline(0, color="#e0e3e7", linewidth=0.8, zorder=0)
        axis.axvline(0, color="#e0e3e7", linewidth=0.8, zorder=0)
        axis.set_xticks([-2, -1, 0, 1, 2])
        axis.set_yticks([-2, -1, 0, 1, 2])
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
