"""Plot normalized binary numbers with four significant bits; PNG goes to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Run via Makefile: make _media/floating-point-spacing.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12})
    fig, axes = plt.subplots(3, 1, figsize=(9.8, 5.5), sharex=True,
                             layout="constrained")
    fig.patch.set_facecolor("white")
    colors = ["#2166ac", "#27834b", "#ad433b"]
    for e, (ax, color) in enumerate(zip(axes, colors)):
        gap = 2.0 ** (e - 3)
        points = (1 + np.arange(8) / 8) * 2.0**e
        start, stop = 2.0**e, 2.0 ** (e + 1)
        assert np.array_equal(np.diff(points), np.full(7, gap))
        assert points[0] == start and points[-1] == stop - gap
        ax.set_facecolor("white")
        ax.axvspan(start, stop, color=color, alpha=0.07)
        ax.hlines(0, start, stop, color=color, lw=1.5)
        ax.scatter(points, np.zeros(8), color=color, s=38, zorder=4)
        ax.scatter([stop], [0], facecolors="white", edgecolors=color,
                   s=45, linewidths=1.5, zorder=5)
        # The open endpoint belongs to the next interval, not this one.
        ax.vlines(points[:2], 0.04, 0.30, color=color, lw=1)
        ax.annotate("", (points[1], 0.23), (points[0], 0.23),
                    arrowprops={"arrowstyle": "|-|", "color": color})
        fraction = ["1/8", "1/4", "1/2"][e]
        ax.text(points[1] + 0.22, 0.23, f"gap = {fraction}",
                va="center", color=color, weight="bold")
        ax.set_title(rf"$[{{{int(start)}}},{{{int(stop)}}})$: "
                     rf"$1.b_1b_2b_3\times 2^{{{e}}}$ — 8 values",
                     loc="left")
        ax.set(ylim=(-0.16, 0.48), yticks=[], xlim=(0.8, 8.3))
        ax.spines[["top", "left", "right", "bottom"]].set_visible(False)
        ax.tick_params(axis="x", length=0, labelbottom=True)
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
        ax.grid(axis="x", alpha=0.15)
    axes[-1].set_xlabel("Number line (the same horizontal scale in every row)")
    fig.suptitle("Floating-point spacing grows with magnitude\n"
                 "Toy binary format: p = 4 includes the leading 1", fontsize=15)
    fig.savefig(Path.cwd() / "floating-point-spacing.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
