"""Original diagrams for Oxford A15272W1 (2024), question 2.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Only the named PNG is written, always in the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def fermion(ax, a, b):
    a, b = np.asarray(a), np.asarray(b)
    ax.plot(*np.stack([a, b]).T, color="black", lw=1.7)
    ax.annotate("", xy=a + .60 * (b-a), xytext=a + .40 * (b-a),
                arrowprops={"arrowstyle": "-|>", "color": "black", "lw": 1.5})


def photon(ax, a, b):
    a, b = np.asarray(a), np.asarray(b)
    v = b-a
    normal = np.array([-v[1], v[0]]) / np.linalg.norm(v)
    t = np.linspace(0, 1, 400)
    pts = a[:, None] + v[:, None]*t + .028*normal[:, None]*np.sin(12*np.pi*t)
    ax.plot(*pts, color="#21669b", lw=1.5)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.5), facecolor="white")
    for ax in axes:
        ax.set(xlim=(-1.3, 1.3), ylim=(-1, 1.3), aspect="equal")
        ax.set_axis_off()
    points = [(0, .65), (-.63, -.43), (.63, -.43)]
    ends = [(0, 1.12), (-1.08, -.69), (1.08, -.69)]
    labels = [(0, 1.20, r"$1:\ k_1,\mu$"), (-.91, -.91, r"$2:\ k_2,\nu$"), (.91, -.91, r"$3:\ k_3,\rho$")]
    for ax, direction in zip(axes[:2], [1, -1]):
        ax.set_title("Triangle: (1 2 3)" if direction == 1 else "Triangle: (1 3 2)", fontsize=12, pad=15)
        for i in range(3):
            a, b = points[i], points[(i+1) % 3]
            fermion(ax, a, b) if direction == 1 else fermion(ax, b, a)
            photon(ax, points[i], ends[i])
            ax.plot(*points[i], "o", color="black", ms=4)
        for x, y, label in labels:
            ax.text(x, y, label, ha="center", va="center", fontsize=10.5)
    ax = axes[2]
    ax.set_title("Box: (1 2 3 4)", fontsize=12, pad=15)
    points = [(-.55, .55), (.55, .55), (.55, -.55), (-.55, -.55)]
    ends = [(-.98, .98), (.98, .98), (.98, -.98), (-.98, -.98)]
    for i in range(4):
        fermion(ax, points[i], points[(i+1) % 4])
        photon(ax, points[i], ends[i])
        ax.plot(*points[i], "o", color="black", ms=4)
    for x, y, label in [(-1.03, 1.16, r"$1:\mu$"), (1.03, 1.16, r"$2:\nu$"),
                        (1.10, -.76, r"$3:\rho$"), (-1.10, -.76, r"$4:\sigma$")]:
        ax.text(x, y, label, ha="center", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=125, facecolor="white", transparent=False, bbox_inches="tight", pad_inches=.14)
    plt.close(fig)


if __name__ == "__main__":
    main()
