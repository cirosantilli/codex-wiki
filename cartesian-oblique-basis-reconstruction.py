"""Draw oblique coordinates; run from _media to write the matching PNG.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    b1 = np.array([1.0, 0.0])
    b2 = np.array([1.0, 1.0])
    p = np.array([2.0, 1.0])
    fig = plt.figure(figsize=(8, 6), dpi=120, facecolor="white")
    ax = fig.add_axes([0.11, 0.27, 0.82, 0.63], facecolor="white")
    ax.set(xlim=(-0.75, 2.7), ylim=(-0.6, 2.05), aspect="equal")
    ax.set_xlabel("Reference x coordinate")
    ax.set_ylabel("Reference y coordinate")
    ax.axhline(0, color="0.77", lw=1)
    ax.axvline(0, color="0.77", lw=1)
    for direction, color in [(b1, "#176ca4"), (b2, "#b45515")]:
        ends = np.array([-3 * direction, 3 * direction])
        ax.plot(ends[:, 0], ends[:, 1], color=color, lw=1, alpha=0.5)
    ax.plot([b2[0], p[0]], [b2[1], p[1]], "--", color="#176ca4", lw=2)
    ax.plot([b1[0], p[0]], [b1[1], p[1]], "--", color="#b45515", lw=1.5)
    for start, end, color, width in [
        (np.zeros(2), p, "#563678", 2.5),
        (np.zeros(2), b1, "#176ca4", 2.5),
        (b1, p, "#b45515", 2.5),
        (np.zeros(2), b2, "#b45515", 2),
    ]:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": width})
    ax.scatter([b1[0], b2[0], p[0]], [b1[1], b2[1], p[1]], color="0.2", s=22, zorder=5)
    ax.text(-0.19, -0.23, "$O$", color="0.2")
    ax.text(0.72, -0.23, "$1b_1$", color="#176ca4")
    ax.text(0.58, 0.84, "$b_2$", color="#b45515")
    ax.text(1.59, 0.38, "$1b_2$", color="#b45515")
    ax.text(2.05, 0.82, "$p=(2,1)$", color="#563678")
    ax.text(1.42, 1.13, "parallel to $b_1$", color="#176ca4", fontsize=11)
    ax.set_title("Oblique axes: parallel-axis reconstruction", pad=12)
    fig.text(0.5, 0.14, r"$p=1b_1+1b_2,\quad [p]_{\mathcal{B}}=(1,1)^T$",
             ha="center", fontsize=12)
    fig.text(0.5, 0.07, r"$p\cdot b_1=2,\quad p\cdot b_2=3\quad$ (not coordinates)",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
