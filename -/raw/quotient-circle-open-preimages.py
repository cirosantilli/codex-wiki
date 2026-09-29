"""Draw the full-preimage test at a glued seam; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def circle(ax, two_sides):
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), color="#ced3db", lw=4)
    e = 1 / 8
    for start, stop in ([(0, e), (1 - e, 1)] if two_sides else [(0, e)]):
        theta = np.linspace(2 * np.pi * start, 2 * np.pi * stop, 100)
        ax.plot(np.cos(theta), np.sin(theta), color="#23846b" if two_sides else "#ba4a40", lw=7)
    ends = [e, 1 - e] if two_sides else [e]
    for t in ends:
        theta = 2 * np.pi * t
        ax.plot(np.cos(theta), np.sin(theta), "o", ms=8, markerfacecolor="white",
                markeredgecolor="#23846b" if two_sides else "#ba4a40", markeredgewidth=2, zorder=5)
    ax.plot(1, 0, "o", color="#253248", ms=7, zorder=6)
    ax.text(1.15, -0.30, "seam", fontsize=10)
    ax.set_aspect("equal")
    ax.set(xlim=(-1.25, 1.85), ylim=(-1.2, 1.2))
    ax.axis("off")


def interval(ax, two_sides):
    e = 1 / 8
    color = "#23846b" if two_sides else "#ba4a40"
    ax.plot([0, 1], [0, 0], color="#ced3db", lw=4)
    ax.plot([0, e], [0, 0], color=color, lw=7)
    if two_sides:
        ax.plot([1 - e, 1], [0, 0], color=color, lw=7)
    ax.plot([0, 1], [0, 0], "o", color=color, ms=8, zorder=5)
    for t in ([e, 1 - e] if two_sides else [e]):
        ax.plot(t, 0, "o", ms=8, markerfacecolor="white", markeredgecolor=color, markeredgewidth=2, zorder=6)
    for t, label in [(0, "0"), (e, r"$\varepsilon$"), (1 - e, r"$1-\varepsilon$"), (1, "1")]:
        ax.text(t, -0.15, label, ha="center", fontsize=12)
    if not two_sides:
        ax.annotate("isolated endpoint: not open", (1, 0.03), (0.47, 0.29), fontsize=11,
                    arrowprops={"arrowstyle": "->", "color": color}, color=color)
    ax.set(xlim=(-0.07, 1.07), ylim=(-0.48, 0.48))
    ax.axis("off")


def main():
    fig = plt.figure(figsize=(9, 6.2), facecolor="white")
    fig.suptitle("Test the entire preimage at the seam", fontsize=18, y=0.97)
    for row, two_sides in enumerate([True, False]):
        bottom = 0.53 if row == 0 else 0.12
        cax = fig.add_axes((0.07, bottom, 0.28, 0.30))
        iax = fig.add_axes((0.49, bottom + 0.005, 0.46, 0.28))
        circle(cax, two_sides)
        interval(iax, two_sides)
        color = "#23846b" if two_sides else "#ba4a40"
        heading = "Open seam neighbourhood" if two_sides else "One-sided arc: not open"
        fig.text(0.06, bottom + 0.33, heading, fontsize=14, color=color)
        fig.text(0.37, bottom + 0.15, r"$p^{-1}$" + "  →", fontsize=16, ha="center")
        formula = r"$[0,\varepsilon)\cup(1-\varepsilon,1]$" if two_sides else r"$[0,\varepsilon)\cup\{1\}$"
        fig.text(0.72, bottom - 0.025, formula, ha="center", fontsize=14)
    fig.text(0.5, 0.025, "Filled dots are included; hollow dots are excluded.  Shown: ε = 1/8.", ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
