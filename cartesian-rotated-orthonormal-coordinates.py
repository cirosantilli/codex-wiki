"""Draw orthonormal coordinates; run from _media to write the matching PNG.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    u = np.array([np.sqrt(3) / 2, 0.5])
    v = np.array([-0.5, np.sqrt(3) / 2])
    p = np.array([2.0, 1.0])
    alpha, beta = np.column_stack((u, v)).T @ p
    a, b = alpha * u, beta * v
    fig = plt.figure(figsize=(8, 6), dpi=120, facecolor="white")
    ax = fig.add_axes([0.11, 0.27, 0.82, 0.63], facecolor="white")
    ax.set(xlim=(-0.75, 2.7), ylim=(-0.6, 2.05), aspect="equal")
    ax.set_xlabel("Reference x coordinate")
    ax.set_ylabel("Reference y coordinate")
    ax.axhline(0, color="0.77", lw=1)
    ax.axvline(0, color="0.77", lw=1)
    for direction, color in [(u, "#176ca4"), (v, "#b45515")]:
        ends = np.array([-3 * direction, 3 * direction])
        ax.plot(ends[:, 0], ends[:, 1], color=color, lw=1, alpha=0.5)
    ax.plot([a[0], p[0]], [a[1], p[1]], "--", color="#b45515", lw=2)
    ax.plot([b[0], p[0]], [b[1], p[1]], "--", color="#176ca4", lw=1.5)
    for start, end, color, width in [
        (np.zeros(2), p, "#563678", 2.5),
        (np.zeros(2), a, "#176ca4", 2.5),
        (a, p, "#b45515", 2.3),
        (np.zeros(2), u, "#176ca4", 2),
        (np.zeros(2), v, "#b45515", 2),
    ]:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops={"arrowstyle": "->", "color": color, "lw": width})
    ax.scatter([a[0], b[0], p[0]], [a[1], b[1], p[1]], color="0.2", s=22, zorder=5)
    ax.text(-0.19, -0.23, "$O$", color="0.2")
    ax.text(u[0] - 0.10, u[1] + 0.05, "$u$", color="#176ca4")
    ax.text(v[0] - 0.13, v[1] + 0.05, "$v$", color="#b45515")
    ax.text(1.23, 0.86, r"$\alpha u$", color="#176ca4")
    ax.annotate(r"$\beta v$", xy=(a + p) / 2, xytext=(2.27, 1.35),
                color="#b45515", arrowprops={"arrowstyle": "-", "color": "#b45515"})
    ax.text(2.05, 0.82, "$p=(2,1)$", color="#563678")
    ax.set_title("Rotated orthonormal axes: perpendicular readings", pad=12)
    fig.text(0.5, 0.14, r"$p=\alpha u+\beta v,\quad \alpha=p\cdot u=\sqrt{3}+1/2,\quad"
             r"\beta=p\cdot v=-1+\sqrt{3}/2$", ha="center", fontsize=12)
    fig.text(0.5, 0.07, r"$\alpha\approx2.232,\quad\beta\approx-0.134,\quad"
             r"\|p\|^2=\alpha^2+\beta^2=5$", ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
