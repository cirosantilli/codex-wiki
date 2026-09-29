"""Sextic Landau phase diagram; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Emit the PNG basename in caller CWD; respect caller MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(5.8, 4.1), dpi=160, facecolor="white")
    u = np.linspace(-2.1, 1.5, 900)
    boundary = np.where(u < 0, 3*u*u/16, 0)
    ax.fill_between(u, -.6, boundary, color="#deebf7")
    ax.fill_between(u, boundary, 1.25, color="#fff7bc")
    neg = np.linspace(-2.1, 0, 500)
    pos = np.linspace(0, 1.5, 300)
    ax.plot(neg, 3*neg*neg/16, color="#d95f0e", lw=2.1, label="First-order coexistence")
    ax.plot(pos, np.zeros_like(pos), color="#2171b5", lw=2.1, label="Continuous boundary")
    ax.plot(neg, neg*neg/4, color="0.45", ls="--", lw=1, label="Ordered spinodal")
    ax.plot(neg, np.zeros_like(neg), color="0.45", ls=":", lw=1.3, label="Disordered spinodal")
    ax.scatter([0], [0], color="#a50f15", s=45, zorder=5)
    ax.annotate("Tricritical point", xy=(0, 0), xytext=(.18, .35), fontsize=9,
                arrowprops={"arrowstyle": "->", "color": "#a50f15"}, color="#a50f15")
    ax.text(-.5, 1.03, r"Disordered: $M=0$", ha="center", fontsize=10)
    ax.text(.65, -.32, r"Ordered: $M\ne0$", ha="center", fontsize=10)
    ax.text(-1.8, .48, r"$r=3u^2/16$", rotation=-35, color="#a63603", fontsize=9)
    ax.set(xlim=(-2.1, 1.5), ylim=(-.6, 1.25), xlabel=r"Quartic coefficient $u$",
           ylabel=r"Quadratic coefficient $r$", title=r"Zero-field phase diagram ($v=1$)")
    ax.legend(loc="lower left", fontsize=7.5, framealpha=.95)
    ax.grid(alpha=.14)
    fig.tight_layout()
    fig.savefig(Path("paper-51-tricritical-phase-diagram.png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
