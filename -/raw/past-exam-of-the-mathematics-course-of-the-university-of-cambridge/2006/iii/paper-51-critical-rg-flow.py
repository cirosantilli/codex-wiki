"""Linear saddle RG flow; Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Emit the PNG basename in caller CWD; respect caller MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(5.8, 3.9), dpi=160, facecolor="white")
    t = np.linspace(-1.8, 1.8, 65)
    w = np.linspace(-1.4, 1.4, 65)
    tt, ww = np.meshgrid(t, w)
    ax.streamplot(t, w, tt, -ww, color="0.60", linewidth=.8, density=.8, arrowsize=.85)
    ax.axvline(0, color="#2171b5", lw=1.6)
    ax.axhline(0, color="#d95f0e", lw=1.5)
    for a, b in [((0, 1.15), (0, .55)), ((0, -1.15), (0, -.55))]:
        ax.annotate("", xy=b, xytext=a, arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#2171b5"})
    for a, b in [((.35, 0), (1, 0)), ((-.35, 0), (-1, 0))]:
        ax.annotate("", xy=b, xytext=a, arrowprops={"arrowstyle": "->", "lw": 1.8, "color": "#d95f0e"})
    ax.scatter([0], [0], color="#a50f15", s=38, zorder=5)
    ax.text(.08, .15, "Critical fixed point", color="#a50f15", fontsize=9)
    ax.text(.08, 1.19, "Critical surface: t=0", color="#2171b5", fontsize=9)
    ax.text(.5, -.26, "Repulsive direction", color="#a63603", fontsize=9)
    ax.text(-1.08, -1.22, "Toward ordered phase", ha="center", fontsize=8)
    ax.text(1.0, -1.22, "Toward disordered phase", ha="center", fontsize=8)
    ax.set(xlim=(-1.8, 1.8), ylim=(-1.4, 1.4), xlabel=r"Relevant thermal field $t$",
           ylabel=r"Irrelevant field $w$", title=r"Coarse-graining flow: $\dot t=t,\ \dot w=-w$ ($h=0$)")
    ax.set_facecolor("white")
    fig.tight_layout()
    fig.savefig(Path("paper-51-critical-rg-flow.png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
