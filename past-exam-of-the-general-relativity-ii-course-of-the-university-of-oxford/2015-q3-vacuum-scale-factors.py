"""Original scale-factor comparison for Oxford General Relativity II 2015 Q3(e).

Run from the mirrored _media directory: output goes only to the current directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject.toml).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t = np.linspace(-2.0, 1.8, 501)
    t_open = np.linspace(0.0, 1.8, 301)
    fig, ax = plt.subplots(figsize=(7.4, 4.8), dpi=145, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(t, np.exp(t), color="#1764a0", lw=2.5,
            label=r"$k=0:\quad H_\Lambda a=e^T$")
    ax.plot(t, np.cosh(t), color="#a34283", lw=2.5,
            label=r"$k=+1:\quad H_\Lambda a=\cosh T$")
    ax.plot(t_open, np.sinh(t_open), color="#227e4d", lw=2.5,
            label=r"$k=-1:\quad H_\Lambda a=\sinh T,\ T>0$")
    ax.plot(0, 0, marker="o", mfc="white", mec="#227e4d", ms=7,
            mew=1.7, zorder=6, clip_on=False)
    ax.scatter([0], [1], color="#a34283", s=27, zorder=5)
    ax.annotate("Open slicing begins here\n(coordinate boundary)",
                xy=(0, 0), xytext=(-1.85, 1.00), fontsize=9,
                arrowprops={"arrowstyle": "->", "color": "#444444"},
                color="#333333")
    ax.annotate("Closed minimum", xy=(0, 1), xytext=(0.42, 0.65),
                fontsize=9, color="#a34283",
                arrowprops={"arrowstyle": "->", "color": "#a34283"})
    ax.axvline(0, color="#aaaaaa", lw=0.8, zorder=0)
    ax.set(xlim=(-2, 1.8), ylim=(0, 6.3),
           xlabel=r"Dimensionless cosmic time $T=H_\Lambda(t-t_c)$",
           ylabel=r"Dimensionless scale factor $H_\Lambda a(t)$",
           title="One positive vacuum density, three spatial slicings")
    ax.grid(color="#dddddd", alpha=0.75, lw=0.6)
    ax.legend(loc="upper left", framealpha=1, facecolor="white", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path.cwd() / "2015-q3-vacuum-scale-factors.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
