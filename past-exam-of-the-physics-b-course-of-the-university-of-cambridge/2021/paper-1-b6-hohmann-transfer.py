#!/usr/bin/env python3
"""Construct a Hohmann transfer from r0 to 3r0, with original orbit geometry.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1 build),
matching the repository pyproject.toml. Writes the PNG basename into cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    angle = np.linspace(0, 2 * np.pi, 700)
    transfer_angle = np.linspace(0, np.pi, 400)
    fig, ax = plt.subplots(figsize=(6.8, 5.0), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.plot(np.cos(angle), np.sin(angle), color="#0072b2", linewidth=1.7, label=r"Initial circle: $r_0$")
    ax.plot(3 * np.cos(angle), 3 * np.sin(angle), color="#009e73", linewidth=1.7, label=r"Target circle: $3r_0$")
    ax.plot(-1 + 2 * np.cos(transfer_angle), np.sqrt(3) * np.sin(transfer_angle),
            color="#d55e00", linewidth=2.5, linestyle="--", label="Transfer coast")
    ax.plot(0, 0, "o", markersize=10, color="#555555")
    ax.text(0.13, -0.28, "Earth (focus)", fontsize=10)
    ax.plot([1, -3], [0, 0], "o", color="0.2", markersize=4)
    ax.annotate("", xy=(1, 1.02), xytext=(1, 0.08),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#0072b2"})
    ax.text(1.13, 0.45, "Burn 1\nprograde", fontsize=10, color="#0072b2")
    ax.annotate("", xy=(-3, -0.95), xytext=(-3, -0.07),
                arrowprops={"arrowstyle": "->", "lw": 2, "color": "#009e73"})
    ax.text(-2.83, -0.8, "Burn 2\nprograde", fontsize=10, color="#0072b2")
    for t in [0.8, 2.05]:
        point = np.array([-1 + 2 * np.cos(t), np.sqrt(3) * np.sin(t)])
        tangent = np.array([-2 * np.sin(t), np.sqrt(3) * np.cos(t)])
        tangent *= .27 / np.linalg.norm(tangent)
        ax.annotate("", xy=point + tangent, xytext=point - tangent,
                    arrowprops={"arrowstyle": "->", "color": "#d55e00", "lw": 1.8})
    ax.text(-1.35, 1.98, "Half an ellipse", fontsize=10, color="#b24b00")
    ax.set_aspect("equal")
    ax.set(xlim=(-3.65, 3.65), ylim=(-3.45, 3.55), title="Two tangential burns raise a circular orbit")
    ax.legend(loc="lower right", frameon=True, fontsize=9, facecolor="white", framealpha=.95)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
