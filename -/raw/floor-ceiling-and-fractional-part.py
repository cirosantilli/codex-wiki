"""Endpoint conventions and the periodic fractional part, including negatives."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(11.2, 6.8), layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=(1.35, 1))
    floor_ax = fig.add_subplot(grid[0, 0])
    ceil_ax = fig.add_subplot(grid[0, 1])
    frac_ax = fig.add_subplot(grid[1, :])
    integers = np.arange(-3, 4)
    for ax, name, color in ((floor_ax, "Floor: greatest integer not exceeding x", "#167e8d"),
                            (ceil_ax, "Ceiling: least integer not below x", "#c26030")):
        ax.plot([-3, 3], [-3, 3], "--", color="#88959e", lw=1, label="y = x")
        for n in range(-3, 3):
            y = n if ax is floor_ax else n + 1
            ax.plot([n, n + 1], [y, y], color=color, lw=2.2)
            open_end = n + 1 if ax is floor_ax else n
            ax.scatter([open_end], [y], facecolors="white", edgecolors=color,
                       s=46, zorder=5, linewidths=1.5)
        ax.scatter(integers, integers, color=color, s=30, zorder=6)
        ax.set(title=name, xlabel="Input x", xlim=(-3.18, 3.18),
               ylim=(-3.35, 3.35), xticks=integers, yticks=integers)
        ax.grid(alpha=0.16)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper left", fontsize=10)
    floor_ax.set_ylabel(r"$\lfloor x\rfloor$")
    ceil_ax.set_ylabel(r"$\lceil x\rceil$")
    for n in range(-3, 3):
        frac_ax.plot([n, n + 1], [0, 1], color="#6b61a2", lw=2.1)
        frac_ax.scatter([n + 1], [1], facecolors="white", edgecolors="#6b61a2",
                        s=46, linewidths=1.5, zorder=5)
    frac_ax.scatter(integers, np.zeros_like(integers), color="#6b61a2",
                   s=30, zorder=6)
    frac_ax.scatter([-2.7], [.3], color="#24343e", s=32, zorder=7)
    frac_ax.annotate(r"$\{-2.7\}=0.3$", (-2.7, .3), xytext=(-2.25, .55),
                     arrowprops={"arrowstyle": "->", "color": "#405660"},
                     fontsize=12)
    frac_ax.set(title="Fractional part repeats with period one",
                xlabel="Input x", ylabel=r"$\{x\}=x-\lfloor x\rfloor$",
                xlim=(-3.18, 3.18), ylim=(-.11, 1.13), xticks=integers)
    frac_ax.grid(alpha=.16)
    frac_ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Directed integer bounds and the amount left above the floor", fontsize=17)
    fig.get_layout_engine().set(rect=(0, .055, 1, .92))
    fig.text(.5, .017, "Filled points are included; hollow points are excluded. At every integer, floor = ceiling and fractional part = 0.",
             ha="center", fontsize=10)
    x = np.linspace(-7, 7, 2801)
    assert np.all(np.floor(x) <= x) and np.all(x < np.floor(x) + 1)
    assert np.all(np.ceil(x) - 1 < x) and np.all(x <= np.ceil(x))
    assert np.array_equal(np.ceil(x), -np.floor(-x))
    assert np.allclose((x + 5) - np.floor(x + 5), x - np.floor(x), atol=2e-15)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
