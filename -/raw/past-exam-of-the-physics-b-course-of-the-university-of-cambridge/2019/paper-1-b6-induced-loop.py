#!/usr/bin/env python3
"""Original loop-force diagram; writes its PNG basename to cwd.

Tested: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7 (+dfsg1).
Dependencies are listed in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    theta = np.deg2rad(40)
    normal = np.array([np.cos(theta), np.sin(theta)])
    tangent = np.array([-np.sin(theta), np.cos(theta)])
    fig, ax = plt.subplots(figsize=(6.4, 4.5), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(*np.column_stack((-tangent, tangent)), color=".65", lw=3)
    ax.plot([0, 1.25], [0, 0], "--", color=".6", lw=1)
    ax.annotate("", xy=1.15*normal, xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "lw": 1.7, "color": ".2"})
    ax.text(*(1.25*normal), r"$\mathbf{n}$", fontsize=13)
    arc = np.linspace(0, theta, 80)
    ax.plot(.43*np.cos(arc), .43*np.sin(arc), color=".3")
    ax.text(.49, .15, r"$\theta$", fontsize=12)
    for sign, marker, label in [(1, r"$\otimes$", "Current down"),
                                 (-1, r"$\odot$", "Current up")]:
        pos = sign*tangent
        ax.scatter(*pos, s=280, marker=marker, color="#7b3294", zorder=4)
        ax.annotate("", xy=pos+np.array([0, -.65*sign]), xytext=pos,
                    arrowprops={"arrowstyle": "-|>", "lw": 2, "color": "#d55e00"})
        ax.text(pos[0]+.15, pos[1]-.35*sign, r"$\mathbf{F}$", color="#b34800", fontsize=12)
        ax.text(pos[0]-.17, pos[1]+.18*sign, label,
                ha="right" if sign==1 else "left", fontsize=10)
    ax.annotate("", xy=(-.35, 1.27), xytext=(-1.35, 1.27),
                arrowprops={"arrowstyle": "-|>", "lw": 2.2, "color": "#0072b2"})
    ax.text(-.85, 1.39, r"Applied $\mathbf{B}$", ha="center", color="#0072b2", fontsize=11)
    ax.text(0, -1.42, "Top view: vertical sides project to the marked points.\n"
            "The force pair turns the normal away from the field.", ha="center", fontsize=10)
    ax.set(xlim=(-1.8, 1.8), ylim=(-1.65, 1.7), aspect="equal",
           title="Induced current and torque at positive applied field")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem+".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
