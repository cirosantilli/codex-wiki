#!/usr/bin/env python3
"""Plot independently computed isothermal wind and breeze branches.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (+dfsg1 build),
using dependencies already listed in the repository pyproject.toml.
The generator writes its PNG basename into the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def solve_log_w(rhs, upper):
    """Solve exp(y)-y=rhs on a chosen side of y=0, by bisection."""
    rhs = np.asarray(rhs)
    if upper:
        lower = np.zeros_like(rhs)
        higher = np.log(rhs + 1) + 2
    else:
        lower = -rhs - 2
        higher = np.zeros_like(rhs)
    for _ in range(80):
        middle = (lower + higher) / 2
        value = np.exp(middle) - middle
        move_lower = value < rhs if upper else value > rhs
        lower = np.where(move_lower, middle, lower)
        higher = np.where(move_lower, higher, middle)
    return (lower + higher) / 2


def branches(radius):
    base = 4 * np.log(radius) + 4 / radius
    rhs = base - 3
    wind = np.exp(np.where(radius < 1, solve_log_w(rhs, False),
                           solve_log_w(rhs, True)) / 2)
    breeze = np.exp(solve_log_w(base - 2, False) / 2)
    return wind, breeze


def main():
    radius = np.geomspace(.25, 1000, 750)
    wind, breeze = branches(radius)
    fig, ax = plt.subplots(figsize=(7.4, 4.3), dpi=120, facecolor="white")
    ax.set_facecolor("white")
    ax.semilogx(radius, wind, color="#0072b2", linewidth=2.4,
                label="Escaping transonic wind")
    ax.semilogx(radius, breeze, color="#d55e00", linewidth=2.1,
                label=r"Subsonic breeze ($C_0=-2$)")
    far = radius[radius >= 2.5]
    ax.semilogx(far, 2 * np.sqrt(np.log(far)), "--", color="0.4", linewidth=1.5,
                label=r"Large-radius estimate $2\sqrt{\ln x}$")
    ax.scatter([1], [1], s=35, color="#0072b2", zorder=4)
    ax.annotate("Regular sonic crossing", xy=(1, 1), xytext=(1.7, 1.0),
                arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=9)
    ax.text(12, .21, r"Breeze: $u\propto r^{-2}$, finite outer pressure", fontsize=9,
            color="#a24400")
    ax.set(xlabel=r"Radius $x=r/r_s$", ylabel=r"Outward speed $u/c$",
           title="Outward flow alone does not select the wind branch",
           xlim=(.25, 1000), ylim=(-.06, 5.8))
    ax.grid(alpha=.18)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
