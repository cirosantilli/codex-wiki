"""Draw endpoint gluing; run from _media with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


def main():
    colors = ["#2563a6", "#23926c", "#df9c27", "#8657a6"]
    seam = "#c43c4d"
    fig = plt.figure(figsize=(9, 4.5), facecolor="white")
    left = fig.add_axes((0.06, 0.22, 0.36, 0.58))
    right = fig.add_axes((0.59, 0.16, 0.35, 0.70))
    fig.suptitle("Identify just the two endpoints", fontsize=18, y=0.96)
    left.set(xlim=(-0.11, 1.11), ylim=(-0.7, 0.7))
    left.axis("off")
    for k, color in enumerate(colors):
        left.plot([k / 4, (k + 1) / 4], [0, 0], lw=7, color=color)
    for t, label in [(0, "0"), (0.25, "1/4"), (0.5, "1/2"), (0.75, "3/4"), (1, "1")]:
        left.plot(t, 0, "o", color=seam if t in (0, 1) else "#253248", ms=7, zorder=3)
        left.text(t, -0.16, label, ha="center", fontsize=12)
    left.text(0.5, 0.35, r"$I=[0,1]$", ha="center", fontsize=16)
    left.text(0.5, -0.43, r"$0\sim1$; all other classes are singletons", ha="center", fontsize=11)
    right.set_aspect("equal")
    right.set(xlim=(-1.5, 1.6), ylim=(-1.4, 1.4))
    right.axis("off")
    for k, color in enumerate(colors):
        theta = np.linspace(k * np.pi / 2, (k + 1) * np.pi / 2, 100)
        right.plot(np.cos(theta), np.sin(theta), lw=7, color=color)
    for t, label, xytext in [
        (0, "[0]=[1]", (1.13, 0)),
        (0.25, "[1/4]", (0, 1.24)),
        (0.5, "[1/2]", (-1.29, 0)),
        (0.75, "[3/4]", (0, -1.24)),
    ]:
        theta = 2 * np.pi * t
        right.plot(np.cos(theta), np.sin(theta), "o", color=seam if t == 0 else "#253248", ms=7)
        right.text(*xytext, label, ha="left" if t == 0 else "center", va="center", fontsize=11)
    right.text(0, 0, r"$I/{\sim}\ \cong\ S^1$", ha="center", va="center", fontsize=16)
    fig.add_artist(FancyArrowPatch((0.44, 0.53), (0.57, 0.53), transform=fig.transFigure,
                                  arrowstyle="-|>", mutation_scale=22, lw=2, color="#253248"))
    fig.text(0.505, 0.60, r"$q(t)=[t]$", ha="center", fontsize=13)
    fig.text(0.5, 0.05, r"Exact circle coordinates: $p(t)=(\cos(2\pi t),\sin(2\pi t))$", ha="center", fontsize=14)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
