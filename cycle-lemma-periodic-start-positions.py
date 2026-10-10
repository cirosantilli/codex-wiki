"""Original six-start comparison; write opaque PNG basename to the CWD.

Uses the repository's Python 3.14 / matplotlib environment; run from _media.
"""
from itertools import accumulate
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    word = (1, 1, -1, 1, 1, -1)
    fig, axes = plt.subplots(2, 3, figsize=(10.4, 6.2), dpi=120)
    fig.patch.set_facecolor("white")
    for r, ax in enumerate(axes.flat):
        rotated = word[r:] + word[:r]
        sums = [0, *accumulate(rotated)]
        good = min(sums[1:]) > 0
        color = "#17734a" if good else "#b14a31"
        ax.set_facecolor("white")
        ax.axhline(0, color="#333333", lw=1.2)
        ax.plot(range(7), sums, color=color, lw=2.3, marker="o", ms=5)
        ax.scatter([0], [0], facecolors="white", edgecolors="#333333",
                   s=60, zorder=4)
        for j, value in enumerate(sums[1:], 1):
            if value <= 0:
                ax.scatter([j], [value], color=color, marker="x", s=70,
                           linewidths=2, zorder=5)
        ax.set_title(f"Start {r}: " + ("GOOD" if good else "BAD") +
                     "\n" + ", ".join(map(str, rotated)),
                     fontsize=10.5, color=color)
        if good:
            ax.text(.5, .91, "Same good word; separate start",
                    transform=ax.transAxes, ha="center", fontsize=9,
                    color=color, bbox={"facecolor": "white", "edgecolor": "none"})
        ax.set_xticks(range(7))
        ax.set_yticks(range(-1, 4))
        ax.set_xlim(-.2, 6.2)
        ax.set_ylim(-1.35, 3.85)
        ax.set_xlabel("Number of increments read", fontsize=9.5)
        ax.set_ylabel("Partial sum", fontsize=9.5)
        ax.grid(alpha=.18)
        ax.spines[["right", "top"]].set_visible(False)
    fig.suptitle("A repeating block: six positions, three distinct rotated words",
                 fontsize=14, y=.98)
    fig.text(.5, .025,
             "Starts 0 and 3 count twice: two good positions, one distinct good word.\n"
             "Open dot: excluded empty prefix. Every nonempty prefix must be > 0.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.065, right=.98, top=.85, bottom=.17,
                        hspace=.65, wspace=.38)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
