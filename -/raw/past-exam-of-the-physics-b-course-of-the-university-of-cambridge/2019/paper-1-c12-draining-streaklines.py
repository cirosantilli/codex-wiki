#!/usr/bin/env python3
"""Original quasisteady spiral streaks; writes its PNG basename to cwd.

Tested: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7 (+dfsg1).
Dependencies are listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(5.4, 5.0), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.add_patch(Circle((0, 0), 1, fill=False, edgecolor=".3", lw=1.5))
    ax.add_patch(Circle((0, 0), .105, facecolor=".25", edgecolor=".25"))
    s = np.linspace(0, np.log(1/.12), 500)
    radius = np.exp(-s)
    for initial in np.linspace(0, 2*np.pi, 6)[:-1]:
        angle = initial+3*s
        x, y = radius*np.cos(angle), radius*np.sin(angle)
        ax.plot(x, y, color="#0072b2", lw=1.6)
        ax.scatter([x[0]], [y[0]], color="#d55e00", s=20, zorder=4)
        for j in [110, 340]:
            ax.annotate("", xy=(x[j+12], y[j+12]), xytext=(x[j], y[j]),
                        arrowprops={"arrowstyle": "-|>", "lw": 1.7, "color": "#0072b2"})
    ax.annotate("Finite drain core", xy=(.05, .03), xytext=(-1.12, -.9),
                arrowprops={"arrowstyle": "->", "color": ".35"}, fontsize=10)
    ax.text(0, -1.26, r"Illustration: $u_r=-D/r$, $u_\phi=C/r$, $C/D=3$",
            ha="center", fontsize=10)
    ax.set(xlim=(-1.3, 1.3), ylim=(-1.4, 1.2), aspect="equal",
           title="Late dye streaks spiral inward toward the drain")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
