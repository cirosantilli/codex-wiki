"""Original diagrams for Oxford A15272W1 (2024), question 3.

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
    ax.annotate("", xy=a + .62 * (b-a), xytext=a + .40 * (b-a),
                arrowprops={"arrowstyle": "-|>", "color": "black", "lw": 1.5})


def boson(ax, a, b):
    a, b = np.asarray(a), np.asarray(b)
    v = b-a
    normal = np.array([-v[1], v[0]]) / np.linalg.norm(v)
    t = np.linspace(0, 1, 400)
    pts = a[:, None] + v[:, None]*t + .030*normal[:, None]*np.sin(14*np.pi*t)
    ax.plot(*pts, color="#21669b", lw=1.5)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.4), facecolor="white")
    for ax in axes:
        ax.set(xlim=(-1.28, 1.28), ylim=(-.95, 1.2), aspect="equal")
        ax.set_axis_off()
        ax.text(-.98, -.88, r"$\psi(p_1)$", ha="center", fontsize=11)
        ax.text(.98, -.88, r"$\bar\psi(p_2)$", ha="center", fontsize=11)
    for ax, order in zip(axes[:2], [(1, 2), (2, 1)]):
        ax.set_title("Ordered exchange: " + ("t" if order == (1, 2) else "u"), fontsize=12, pad=15)
        left, right = (-.4, -.18), (.4, -.18)
        fermion(ax, (-1.02, -.62), left)
        fermion(ax, left, right)
        fermion(ax, right, (1.02, -.62))
        boson(ax, left, (-.91, .79))
        boson(ax, right, (.91, .79))
        for point in [left, right]:
            ax.plot(*point, "o", color="black", ms=4)
        for x, which in [(-.86, order[0]), (.86, order[1])]:
            ax.text(x, 1.00, r"$k_1,a,\mu$" if which == 1 else r"$k_2,b,\nu$", ha="center", fontsize=11)
        ax.text(0, -.46, r"$p_1-k_1$" if order == (1, 2) else r"$p_1-k_2$", ha="center", fontsize=11)
    ax = axes[2]
    ax.set_title("Annihilation: s", fontsize=12, pad=15)
    lower, upper = (0, -.40), (0, .36)
    fermion(ax, (-1.02, -.62), lower)
    fermion(ax, lower, (1.02, -.62))
    boson(ax, lower, upper)
    boson(ax, upper, (-.91, .79))
    boson(ax, upper, (.91, .79))
    for point in [lower, upper]:
        ax.plot(*point, "o", color="black", ms=4)
    ax.text(-.86, 1.00, r"$k_1,a,\mu$", ha="center", fontsize=11)
    ax.text(.86, 1.00, r"$k_2,b,\nu$", ha="center", fontsize=11)
    ax.text(.13, -.08, r"$q,c$", fontsize=11)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=125, facecolor="white", transparent=False, bbox_inches="tight", pad_inches=.14)
    plt.close(fig)


if __name__ == "__main__":
    main()
