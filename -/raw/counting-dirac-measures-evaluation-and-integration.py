"""Original analytical example: one function, several integrals.

The exceptional value is specified, not a measurement or a delta density.
Tested environment: Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from _media; the output filename follows this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.8, 5.4), dpi=110, facecolor="white")
    fig.text(0.035, 0.945, "A changed point value: evaluation, summation, area", fontsize=20, weight="bold")
    fig.text(0.035, 0.89, "Analytical illustration: f(t) = t + 1, except f(1) = 5, on [0, 2]", fontsize=14)
    blue, orange, green = "#245e8e", "#b34f00", "#237344"
    ax = fig.add_axes([0.08, 0.20, 0.37, 0.59])
    t = np.linspace(0, 2, 401)
    ax.fill_between(t, 0, t + 1, color="#e4eef5")
    for left, right in ((0, 1), (1, 2)):
        segment = np.linspace(left, right, 101)
        ax.plot(segment, segment + 1, color=blue, lw=2.5)
    ax.scatter([0, 2], [1, 3], color=blue, s=55, zorder=5)
    ax.scatter([1], [2], facecolor="white", edgecolor=blue, linewidth=2, s=100, zorder=6)
    ax.scatter([1], [5], color=orange, s=85, zorder=6)
    ax.annotate("actual f(1) = 5", xy=(1, 5), xytext=(0.13, 5.55), fontsize=12,
                arrowprops={"arrowstyle": "->", "color": orange}, color=orange)
    ax.annotate("excluded value 2", xy=(1, 2), xytext=(1.16, 1.23), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": blue}, color=blue)
    ax.text(0.5, 0.47, "Lebesgue area = 4", fontsize=12, color=blue)
    ax.set(xlim=(-0.12, 2.12), ylim=(0, 6), xlabel="t", ylabel="f(t)", xticks=[0, 1, 2], yticks=range(7))
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.16)

    results = fig.add_axes([0.52, 0.17, 0.46, 0.65])
    results.set(xlim=(0, 1), ylim=(0, 1))
    results.axis("off")
    entries = [
        (0.90, r"Dirac $\delta_1$ on $[0,2]$", r"$\int f\,d\delta_1=f(1)=5$", orange),
        (0.66, r"Counting on $D=\{0,1,2\}$", r"$\int_D f\,d\#=1+5+3=9$", green),
        (0.42, r"Lebesgue $\lambda$ on $[0,2]$", r"$\int f\,d\lambda=\int_0^2(t+1)\,dt=4$", blue),
        (0.18, r"Counting on the whole $[0,2]$", r"$\int f\,d\#=\infty$", "#182838"),
    ]
    for y, label, formula, color in entries:
        results.text(0.01, y, label, fontsize=13, color=color, weight="bold")
        results.text(0.01, y - 0.10, formula, fontsize=17)
        if y > 0.2:
            results.axhline(y - 0.16, xmin=0.01, xmax=0.95, color="#d8dee4", lw=0.8)
    fig.text(0.08, 0.082, "The isolated point changes Dirac and finite counting integrals; it has zero Lebesgue length.", fontsize=12)
    fig.text(0.08, 0.035, "Whole-interval counting is infinite because f is at least 1 at infinitely many points.", fontsize=12, color="#536170")
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
