"""Circular light rays for n=1/y; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Write the same-basename PNG into the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(7.6, 4.9), dpi=120, layout="constrained")
    colors = ["#2875a6", "#2b8c6b", "#b36725", "#974d8a"]
    ax.axhspan(0, 1, color="#e7f2f6", alpha=0.75)
    for degree, color in zip([15, 35, 60, 90], colors):
        theta = np.deg2rad(degree)
        angle = np.linspace(theta, 0, 900)
        radius = 1/np.sin(theta)
        x = radius*(np.cos(angle)-np.cos(theta))
        y = radius*np.sin(angle)
        ax.plot(x, y, color=color, lw=2, label=rf"$\theta={degree}^\circ$")
        mid = int(0.46*len(angle))
        ax.annotate("", (x[mid+40], y[mid+40]), (x[mid], y[mid]),
                    arrowprops={"arrowstyle": "->", "color": color, "lw": 1.8})
        ax.scatter([x[-1]], [0], facecolor="white", edgecolor=color, s=35, zorder=5)
    ax.plot([0, 0], [0, 1], "--", lw=1.4, color="0.4", label=r"$\theta=0^\circ$")
    ax.axhline(1, color="0.4", lw=1)
    ax.axhline(0, color="0.4", ls="--", lw=1)
    ax.scatter([0], [1], color="black", s=28, zorder=6)
    ax.annotate("Entry", (0, 1), (-0.09, 1.09), fontsize=10)
    ax.text(0.35, 1.06, r"Above: $\mu=1$", fontsize=11)
    ax.text(0.62, 0.80, r"Strip: $\mu=1/y$", fontsize=11)
    ax.text(0.36, -0.12, r"Limiting displacement: $D=\tan(\theta/2)\leq1$", fontsize=11)
    ax.set(xlim=(-0.12, 1.08), ylim=(-0.17, 1.17), xlabel="$x$", ylabel="$y$",
           title="Rays bend toward the lower boundary")
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_aspect("equal")
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.55), fontsize=10)
    ax.grid(alpha=0.13)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
