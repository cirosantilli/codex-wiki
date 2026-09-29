"""Plot Couette wall slip and its geometric extrapolation; save PNG to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(7.2, 5.5), dpi=120)
    fig.subplots_adjust(left=0.13, right=0.96, bottom=0.13, top=0.79)
    fig.suptitle("Slip length is a geometric extrapolation", fontsize=17, y=0.96)
    fig.text(0.5, 0.88, "Stationary slipping bottom; moving no-slip top",
             ha="center", fontsize=12)
    ax.axhspan(-0.86, 0, color="#eeeeee")
    ax.axhline(0, color="#334155", lw=1.8)
    ax.axhline(1, color="#334155", lw=1.8)
    colors = ["#334155", "#1976a3", "#bc5528"]
    z = np.linspace(0, 1, 250)
    for beta, color in zip([0, 0.25, 0.75], colors):
        u = (z + beta) / (1 + beta)
        assert np.isclose(u[0], beta / (1 + beta))
        assert np.isclose(u[-1], 1)
        ax.plot(u, z, color=color, lw=2.7, label=rf"$b/H={beta:g}$")
        ax.scatter([u[0]], [0], s=30, color=color, zorder=5)
        if beta:
            inside = np.linspace(-beta, 0, 100)
            ax.plot((inside + beta) / (1 + beta), inside,
                    color=color, ls="--", lw=2)
            ax.scatter([0], [-beta], color=color, s=35, zorder=5)
            ax.annotate(rf"$z=-b=-{beta:g}H$", (0, -beta),
                        xytext=(14, -2), textcoords="offset points",
                        color=color, va="center", fontsize=11)
    ax.text(0.95, -0.55, "Solid wall\n(dashed lines are fictitious)",
            ha="right", color="#475569", fontsize=10)
    ax.text(0.97, 0.08, "Bottom: wall speed = 0", ha="right", fontsize=10)
    ax.annotate("Top: wall speed = U", (1, 1), xytext=(0.45, 1.13),
                ha="center", fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#334155"})
    ax.set(xlim=(-0.045, 1.05), ylim=(-0.86, 1.21),
           xlabel=r"Tangential fluid velocity $u/U$",
           ylabel=r"Normal position $z/H$")
    ax.set_title(r"$u/U=(z/H+b/H)/(1+b/H)$", pad=12, fontsize=13)
    ax.legend(loc="upper left", bbox_to_anchor=(0.01, 0.93), framealpha=1)
    ax.grid(alpha=0.17)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
