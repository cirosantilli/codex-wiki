"""Sketch Question 3(a)(iii); write the PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(6.4, 4.4), layout="constrained", facecolor="white")
    theta_end = 2 * np.pi / 3
    theta = np.linspace(0, theta_end, 401)
    tail = np.linspace(theta_end, np.pi, 201)
    radius = 1 + np.cos(theta)
    tail_radius = 1 + np.cos(tail)
    ax.plot(tail_radius * np.cos(tail), tail_radius * np.sin(tail), "--", color="#8b8b8b", linewidth=2, label="Continuation to the cusp")
    ax.plot(radius * np.cos(theta), radius * np.sin(theta), color="#236ba5", linewidth=3, label=r"Partial curve: $0\leq\theta\leq2\pi/3$")
    ax.scatter([2, -0.25, 0], [0, np.sqrt(3) / 4, 0], color=["#236ba5", "#236ba5", "#555555"], zorder=4)
    ax.annotate("Start $(2a,0)$", (2, 0), xytext=(1.2, -0.23))
    ax.annotate(r"$\theta_2=2\pi/3$", (-0.25, np.sqrt(3) / 4), xytext=(-0.43, 0.85), arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.annotate("Cusp", (0, 0), xytext=(0.13, 0.16), arrowprops={"arrowstyle": "->", "color": "#555555"})
    ax.axhline(0, color="#aaaaaa", linewidth=0.7, zorder=0)
    ax.axvline(0, color="#aaaaaa", linewidth=0.7, zorder=0)
    ax.set(xlabel="$x/a$", ylabel="$y/a$", xlim=(-0.55, 2.2), ylim=(-0.3, 1.65), title=r"A partial cardioid: $r=a(1+\cos\theta)$")
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", frameon=False, fontsize=9)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=115, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
