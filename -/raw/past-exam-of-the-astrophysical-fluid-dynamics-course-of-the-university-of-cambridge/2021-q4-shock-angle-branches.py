#!/usr/bin/env python3
"""Plot derived oblique-shock angle branches, without copying source geometry.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1 build),
matching the repository pyproject.toml. Writes the PNG basename into cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    gamma = 5 / 3
    theta_max = np.arcsin(1 / gamma)
    theta = np.linspace(0, theta_max, 600)
    auxiliary = np.arcsin(np.clip(gamma * np.sin(theta), 0, 1))
    weak = (theta + auxiliary) / 2
    strong = (theta + np.pi - auxiliary) / 2
    degrees = 180 / np.pi
    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(theta * degrees, weak * degrees, linewidth=2.4, color="#0072b2", label="Weak branch")
    ax.plot(theta * degrees, strong * degrees, linewidth=2.4, color="#d55e00", label="Strong branch")
    ax.plot(theta_max * degrees, weak[-1] * degrees, "o", color="0.2", markersize=5)
    ax.annotate(r"Branches merge: $\theta_{\max}=\arcsin(1/\gamma)$",
                xy=(theta_max * degrees, weak[-1] * degrees), xytext=(9, 47),
                fontsize=10, arrowprops={"arrowstyle": "->", "color": "0.3"})
    ax.set(xlim=(0, theta_max * degrees + 1), ylim=(0, 93),
           xlabel=r"Flow turning angle $\theta$ (degrees)", ylabel=r"Shock angle $\beta$ (degrees)",
           title=r"Strong-shock limit $M\to\infty$, $\gamma=5/3$")
    ax.grid(alpha=0.2)
    ax.legend(loc="center left", frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
