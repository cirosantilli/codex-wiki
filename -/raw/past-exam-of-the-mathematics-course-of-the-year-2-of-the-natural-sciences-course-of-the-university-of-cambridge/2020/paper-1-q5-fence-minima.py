"""Original solution sketches for the three fence minimizers.

Write the PNG basename in the current working directory. Tested with Python
3.14.4, matplotlib 3.10.7 and numpy 2.3.5; dependencies are declared in the
repository's top-level pyproject.toml.
"""

from pathlib import Path
from math import pi, sin, sinh

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def bisect_increasing(function, left, right, target):
    for _ in range(80):
        midpoint = (left + right) / 2
        if function(midpoint) < target:
            left = midpoint
        else:
            right = midpoint
    return (left + right) / 2


def main():
    a, length = 1.0, 2.7
    ratio = length / (2 * a)
    angle = bisect_increasing(lambda t: t / sin(t), 1e-8, pi / 2, ratio)
    radius = a / sin(angle)
    q = bisect_increasing(lambda t: sinh(t) / t, 1e-8, 4.0, ratio)
    scale = a / q
    x = np.linspace(-a, a, 601)
    y_a = x - a * np.sinh(x) / np.sinh(a)
    y_b = np.sqrt(radius**2 - a**2) - np.sqrt(radius**2 - x**2)
    y_c = scale * (np.cosh(x / scale) - np.cosh(a / scale))
    fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.75), layout="constrained")
    fig.patch.set_facecolor("white")
    titles = ["Company A: unconstrained length", "Company B: circular arc",
              "Company C: catenary"]
    formulas = [r"$y=x-a\sinh x/\sinh a$",
                r"$L=2R\arcsin(a/R)$", r"$L=2b\sinh(a/b)$"]
    for ax, y, title, formula in zip(axes, [y_a, y_b, y_c], titles, formulas):
        ax.axhline(0, color="#888888", lw=0.9)
        ax.plot(x / a, y / a, color="#2463a5", lw=2.4)
        ax.plot([-1, 1], [0, 0], "o", color="black", ms=3.5)
        ax.set(xlabel=r"$x/a$", ylabel=r"$y/a$", title=title, xlim=(-1.08, 1.08))
        ax.set_xticks([-1, 0, 1])
        ax.spines[["top", "right"]].set_visible(False)
        ax.text(0.5, 0.04, formula, transform=ax.transAxes, ha="center", fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    height = max(abs(y_a.min()), abs(y_a.max()))
    axes[0].set_ylim(-1.35 * height, 1.35 * height)
    for ax in axes[1:]:
        ax.set_ylim(-1.0, 0.14)
    fig.suptitle(r"Original minimizing-curve sketches: $a=1$; fixed length $L=2.7a$ for B and C",
                 fontsize=12)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
