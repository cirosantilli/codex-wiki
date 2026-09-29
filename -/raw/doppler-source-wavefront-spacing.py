"""Plot chosen subsonic wavefront geometry; emit the PNG into the CWD.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Lengths are in lambda_0 = c/f_s; the deliberately chosen source Mach ratio is 0.4.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    mach = 0.4
    fig, ax = plt.subplots(figsize=(8, 7), dpi=130, facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.14, top=0.83)
    for age in range(1, 6):
        center = -mach * age
        ax.add_patch(Circle((center, 0), age, fill=False, color="#2479a5", lw=1.8))
        ax.plot(center, 0, ".", color="#bb6a1a", ms=7, zorder=5)
    ax.axhline(0, color="#999999", lw=0.7, zorder=0)
    ax.plot(0, 0, "o", color="#b32632", ms=9, zorder=6)
    ax.annotate("source now", (0, 0), (0.2, -2.1),
                arrowprops={"arrowstyle": "->", "color": "#b32632"}, color="#b32632")
    ax.annotate("", (1.7, 0.45), (0.1, 0.45),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#b32632"})
    ax.text(0.65, 0.65, r"$v=0.4c$", color="#b32632", ha="center")
    # Each arrow spans intersections of adjacent fronts with the motion axis.
    for left, right, label in [(-5.6, -4.2, r"rear: $1.4\lambda_0$"),
                               (1.8, 2.4, r"front: $0.6\lambda_0$")]:
        ax.annotate("", (right, -0.55), (left, -0.55),
                    arrowprops={"arrowstyle": "<->", "color": "#252525", "lw": 1.5})
        ax.vlines([left, right], -0.7, 0.05, color="#555555", lw=0.8)
        ax.text((left + right) / 2, -1.18, label, ha="center", fontsize=11)
    ax.annotate("old emission positions", (-1.2, 0), (-4.4, 2.2),
                arrowprops={"arrowstyle": "->", "color": "#bb6a1a"},
                color="#9b5413", fontsize=11)
    fig.text(0.5, 0.025, "Blue circles: fronts emitted 1, 2, 3, 4, 5 periods ago",
             fontsize=10, ha="center")
    ax.set(xlim=(-7.4, 3.5), ylim=(-5.3, 5.3), aspect="equal",
           xlabel=r"Position along motion, $x/\lambda_0$", ylabel=r"Transverse position, $y/\lambda_0$")
    ax.set_xticks(np.arange(-7, 4, 1))
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Source motion compresses fronts ahead and spreads them behind", pad=12, fontsize=13)
    fig.suptitle(r"Chosen model: uniform still medium; $\lambda_0=c/f_s$; snapshot at $t=0$",
                 y=0.96, fontsize=12)
    fig.savefig(Path.cwd() / f"{Path(__file__).stem}.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
