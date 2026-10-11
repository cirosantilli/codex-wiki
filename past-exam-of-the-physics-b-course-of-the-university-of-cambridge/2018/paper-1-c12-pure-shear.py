#!/usr/bin/env python3
"""Draw the strain/stress interpretation of shear; write the PNG basename to cwd.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1).
Dependencies are already listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np


def arrow(ax, start, end):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "lw": 1.8, "color": "#d55e00"})


def main():
    fig, axes = plt.subplots(1, 2, figsize=(8.3, 4.1), dpi=120, facecolor="white")
    diamond = np.array([[1,0],[0,1],[-1,0],[0,-1],[1,0]], dtype=float)
    deformed = diamond*np.array([.78,1.22])
    ax = axes[0]
    ax.plot(diamond[:,0], diamond[:,1], "--", color=".6", lw=1.2, label="Before")
    ax.plot(deformed[:,0], deformed[:,1], color="#0072b2", lw=2, label="After")
    arrow(ax, (1.48,0), (1.03,0));arrow(ax, (-1.48,0), (-1.03,0))
    arrow(ax, (0,1.30), (0,1.7));arrow(ax, (0,-1.30), (0,-1.7))
    ax.text(1.15,.19, r"$-S$", color="#b34700", fontsize=11)
    ax.text(.12,1.43, r"$+S$", color="#b34700", fontsize=11)
    ax.text(-1.55,-1.96, r"$\epsilon_{xx}=-e,\quad\epsilon_{yy}=+e$", fontsize=11)
    ax.set_title("Compression and transverse stretch")
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    ax = axes[1]
    ax.add_patch(Polygon([[-.8,-.8],[.8,-.8],[.8,.8],[-.8,.8]], closed=True,
                         facecolor="#e9f2f8", edgecolor="#0072b2", lw=1.5))
    arrow(ax, (-.35,1.03), (.35,1.03))
    arrow(ax, (.35,-1.03), (-.35,-1.03))
    arrow(ax, (1.03,-.35), (1.03,.35))
    arrow(ax, (-1.03,.35), (-1.03,-.35))
    ax.text(.12,1.27, r"$\tau=S$", fontsize=11, color="#b34700")
    ax.text(-1.36,-1.96, r"Rotated faces: $\gamma=2e,\quad S=G\gamma$", fontsize=11)
    ax.text(0,-1.48, r"Face axes are at $45^\circ$ to the principal axes", ha="center", fontsize=9)
    ax.set_title("The same stress resolved on rotated faces")
    for ax in axes:
        ax.set_facecolor("white")
        ax.set(xlim=(-1.8,1.8), ylim=(-2.1,1.85), aspect="equal")
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
