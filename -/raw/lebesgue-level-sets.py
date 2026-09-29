"""Horizontal layers for x**2 on [0, 1]; Python 3.14, NumPy, Matplotlib.

Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp; saves the PNG
with this script's basename to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0.0, 1.0, 4001)
    t = np.linspace(0.0, 1.0, 4001)
    widths = 1.0 - np.sqrt(t)
    vertical_area = np.trapezoid(x**2, x)
    horizontal_area = np.trapezoid(widths, t)
    assert abs(vertical_area - 1.0 / 3.0) < 1e-7
    assert abs(horizontal_area - 1.0 / 3.0) < 1e-6
    assert 1.0 - np.sqrt(0.25) == 0.5

    plt.rcParams.update({
        "font.size": 12,
        "axes.titlesize": 14,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    })
    fig, (left, right) = plt.subplots(
        1, 2, figsize=(10.8, 4.6), dpi=130, constrained_layout=True
    )
    blue = "#236e92"
    orange = "#b76013"
    left.fill_between(x, 0, x**2, color="#dcecf3")
    left.plot(x, x**2, color=blue, lw=2.6)
    left.text(0.28, 0.83, r"$f(x)=x^2$", color=blue, fontsize=14)
    left.text(0.68, 0.1, r"area $=1/3$", fontsize=13, ha="center")

    # A band illustrates width(t) dt; the exact slice is the line at t = 1/4.
    band_t = np.linspace(0.25, 0.30, 201)
    left.fill_betweenx(band_t, np.sqrt(band_t), 1.0, color="#f5d4b4")
    left.hlines(0.25, 0.0, 0.5, color="#707070", ls="--", lw=1.2)
    left.vlines(0.5, 0.0, 0.25, color="#707070", ls="--", lw=1.2)
    left.plot([0.5, 1.0], [0.25, 0.25], color=orange, lw=3)
    left.plot(0.5, 0.25, "o", color=orange, mfc="white", ms=7, mew=1.8)
    left.plot(1.0, 0.25, "o", color=orange, ms=7)
    left.annotate(
        r"$\{x:x^2>1/4\}=(1/2,1]$" + "\nwidth = 1/2",
        xy=(0.76, 0.275), xytext=(0.12, 0.51),
        arrowprops={"arrowstyle": "->", "color": orange},
        color=orange, fontsize=12,
    )
    left.set(
        title="Horizontal slices of the area",
        xlabel=r"position $x$", ylabel=r"height $t$",
        xlim=(0, 1.03), ylim=(0, 1.04),
    )

    right.fill_between(t, 0, widths, color="#dcecf3")
    right.plot(t, widths, color=blue, lw=2.6)
    right.plot(0.25, 0.5, "o", color=orange, ms=7)
    right.vlines(0.25, 0, 0.5, color=orange, lw=1.2, ls="--")
    right.hlines(0.5, 0, 0.25, color=orange, lw=1.2, ls="--")
    right.annotate(
        r"$t=1/4$: width $=1/2$",
        xy=(0.25, 0.5), xytext=(0.40, 0.68),
        arrowprops={"arrowstyle": "->", "color": orange},
        color=orange, fontsize=12,
    )
    right.text(0.40, 0.08, r"$\int_0^1(1-\sqrt{t})\,dt=1/3$",
               ha="center", fontsize=14,
               bbox={"facecolor": "white", "edgecolor": "none", "pad": 4})
    right.set(
        title=r"Slice width $\lambda\{x:x^2>t\}=1-\sqrt{t}$",
        xlabel=r"height $t$", ylabel="length of the superlevel set",
        xlim=(0, 1.03), ylim=(0, 1.04),
    )
    for ax in (left, right):
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax.grid(alpha=0.18)
        ax.set_axisbelow(True)
    output = Path(Path(__file__).with_suffix(".png").name)
    fig.savefig(output, transparent=False)
    plt.close(fig)
    print(f"Saved {output}; vertical area = {vertical_area:.9f}, "
          f"horizontal area = {horizontal_area:.9f}; exact area = 1/3.")


if __name__ == "__main__":
    main()
