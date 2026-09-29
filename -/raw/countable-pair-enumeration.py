"""Generate countable-pair-enumeration.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Labels are exact Cantor pairing values for nonnegative integer coordinates.
"""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def pair(x, y):
    return (x + y) * (x + y + 1) // 2 + y


def main():
    ordered = [(d-y, y) for d in range(6) for y in range(d+1)]
    assert [pair(x, y) for x, y in ordered] == list(range(21))
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(7.8, 6.3), dpi=120, facecolor="white")
    for d in range(6):
        ax.plot([d, 0], [0, d], color="#c6cdd3", lw=1, zorder=0)
    for x in range(6):
        for y in range(6):
            shown = x+y <= 5
            ax.scatter(x, y, s=600 if shown else 220,
                       c="#d8eaf5" if shown else "#eeeeee", edgecolors="#557a92" if shown else "#bbbbbb")
            ax.text(x, y, str(pair(x,y)), ha="center", va="center",
                    fontsize=11 if shown else 9, color="#153c55" if shown else "#888888")
    for (x0,y0),(x1,y1) in zip(ordered, ordered[1:]):
        if x0+y0 == x1+y1:
            ax.annotate("", xy=(x1+.19, y1-.19), xytext=(x0-.19,y0+.19),
                        arrowprops={"arrowstyle":"->", "color":"#2878ad", "lw":1.4})
    ax.set(xlim=(-.55,5.6),ylim=(-.55,5.6),xticks=range(6),yticks=range(6),
           xlabel="First coordinate x",ylabel="Second coordinate y",
           title=r"Each pair receives one index: $\pi(x,y)=\frac{(x+y)(x+y+1)}{2}+y$")
    ax.set_aspect("equal")
    ax.grid(alpha=.1)
    fig.suptitle("A two-dimensional infinite grid can still be listed",fontsize=15)
    fig.text(.5,.028,"Blue: first 21 pairs, traversed by increasing x+y. Gray: later indices.\n"
             "Every pair has a finite coordinate sum, so every pair is eventually reached.",
             ha="center",fontsize=10)
    fig.tight_layout(rect=(0,.07,1,.94))
    fig.savefig(Path.cwd()/"countable-pair-enumeration.png",facecolor="white",transparent=False)
    plt.close(fig)
    print("First six pairs:", ordered[:6])


if __name__ == "__main__":
    main()
