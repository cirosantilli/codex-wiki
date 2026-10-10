"""Original rotation paths; run from _media to write the PNG basename there.

Uses the repository's Python 3.14 / matplotlib environment.
"""
from itertools import accumulate
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    word = (1, 1, 1, -1)
    fig, axes = plt.subplots(2, 2, figsize=(8.2, 6.4), dpi=120)
    fig.patch.set_facecolor("white")
    for r, ax in enumerate(axes.flat):
        rotated = word[r:] + word[:r]
        sums = [0, *accumulate(rotated)]
        good = min(sums[1:]) > 0
        color = "#17734a" if good else "#b14a31"
        ax.set_facecolor("white")
        ax.axhline(0, color="#333333", lw=1.2)
        ax.plot(range(5), sums, color=color, lw=2.5, marker="o", ms=6)
        ax.scatter([0], [0], facecolors="white", edgecolors="#333333",
                   s=70, zorder=4)
        for j, value in enumerate(sums[1:], 1):
            if value <= 0:
                ax.scatter([j], [value], color=color, marker="x", s=95,
                           linewidths=2.4, zorder=5)
        ax.set_title(f"Start {r}: {rotated}\n" +
                     ("GOOD: all nonempty sums > 0" if good else
                      "BAD: a nonempty sum is <= 0"), fontsize=11, color=color)
        ax.set_xticks(range(5))
        ax.set_yticks(range(-1, 4))
        ax.set_xlim(-.15, 4.15)
        ax.set_ylim(-1.35, 3.35)
        ax.set_xlabel("Number of increments read", fontsize=10)
        ax.set_ylabel("Partial sum", fontsize=10)
        ax.grid(alpha=.18)
        ax.spines[["right", "top"]].set_visible(False)
    fig.suptitle("Sum 2, increments at most 1: exactly two good starts",
                 fontsize=14, y=.98)
    fig.text(.5, .025,
             "Open dot: empty prefix (excluded). Crosses: failed nonempty prefixes.\n"
             "Every path ends at 2; touching zero still fails strict positivity.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.09, right=.97, top=.85, bottom=.17,
                        hspace=.65, wspace=.32)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
