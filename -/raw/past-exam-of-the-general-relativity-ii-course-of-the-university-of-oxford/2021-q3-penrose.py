"""Original conformal-strip diagram for Oxford General Relativity II 2021, Q3.

Run from this directory; output is 2021-q3-penrose.png in the working directory.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(figsize=(6.6, 8.5), dpi=130, facecolor="white")
    ax.set_facecolor("white")
    x = np.linspace(-0.5, 0.5, 801)
    ax.fill_between(x, x, 1 - x, color="#e8bd68", alpha=0.38)
    for j in range(-2, 4):
        ax.plot(x, x + 2 * j, "--", color="#236b9e", lw=1.6)
        ax.plot(x, 1 - x + 2 * j, "--", color="#236b9e", lw=1.6)
    ax.plot(x, 1 - x, color="#236b9e", lw=2.5)
    ax.vlines([-0.5, 0.5], -0.74, 2.74, color="#222222", lw=2)
    for y in [-0.5, 1.5]:
        ax.plot(-0.5, y, "o", ms=6, mfc="white", mec="#236b9e", zorder=5)
    for y in [0.5, 2.5]:
        ax.plot(0.5, y, "o", ms=6, mfc="white", mec="#236b9e", zorder=5)
    ax.text(-0.21, 0.43, "Original patch\n" + r"$\lambda>0$", ha="center", va="center", fontsize=11)
    ax.text(0.15, 1.37, r"$\lambda<0$", ha="center", fontsize=11)
    ax.text(0.00, 0.10, r"$T=X$", color="#236b9e", rotation=45, ha="center", fontsize=10)
    ax.text(0.02, 1.05, r"$T+X=\pi$", color="#236b9e", rotation=-45, ha="center", fontsize=10)
    ax.text(0.00, 2.10, r"$T-X=2\pi$", color="#236b9e", rotation=45, ha="center", fontsize=10)
    ax.text(-0.60, 0.95, r"$\lambda\to+\infty$", rotation=90, ha="center", va="center", fontsize=12)
    ax.text(0.60, 0.95, r"$\lambda\to-\infty$", rotation=90, ha="center", va="center", fontsize=12)
    ax.text(-0.82, 0.95, "Timelike conformal boundary", rotation=90, ha="center", va="center", fontsize=10)
    ax.text(0.82, 0.95, "Timelike conformal boundary", rotation=90, ha="center", va="center", fontsize=10)
    for y, dy in [(-0.60, -0.12), (2.60, 0.12)]:
        ax.annotate("", xy=(0, y + dy), xytext=(0, y - dy), arrowprops={"arrowstyle": "->", "lw": 1.6})
    ax.set(xlim=(-0.98, 0.98), ylim=(-0.76, 2.76), aspect="equal")
    ax.set_xticks([-0.5, 0, 0.5], [r"$-\frac{1}{2}$", "$0$", r"$\frac{1}{2}$"])
    ax.set_yticks([-0.5, 0, 0.5, 1, 1.5, 2, 2.5], [r"$-\frac{1}{2}$", "$0$", r"$\frac{1}{2}$", "$1$", r"$\frac{3}{2}$", "$2$", r"$\frac{5}{2}$"])
    ax.set_xlabel(r"$X/\pi$", fontsize=12)
    ax.set_ylabel(r"$T/\pi$", fontsize=12)
    ax.set_title("Maximal extension: an infinite strip\n" + r"$\widetilde{\mathrm{AdS}}_2\times S^2$", fontsize=13, pad=13)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.065, r"Blue lines: $\lambda=0$. Solid blue: the horizon in chart (a).", ha="center", fontsize=9)
    fig.text(0.5, 0.041, "Arrows continue indefinitely; time is not identified.", ha="center", fontsize=9)
    fig.text(0.5, 0.017, r"Edge circles are excluded; each interior point represents $S^2$ of radius $m$.", ha="center", fontsize=9)
    fig.subplots_adjust(left=0.12, right=0.94, bottom=0.16, top=0.90)
    fig.savefig(Path.cwd() / "2021-q3-penrose.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
