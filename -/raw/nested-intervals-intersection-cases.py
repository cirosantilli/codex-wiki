"""Original nested-interval comparison; write the PNG basename to CWD."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.4), dpi=120)
    fig.patch.set_facecolor("white")
    cases = [
        (lambda n: (1 - 1/n, 1 + 1/n), True,
         r"$I_n=[1-1/n,\,1+1/n]$", "Common intersection: {1}", (0, 2)),
        (lambda n: (1 - 1/n, 2 + 1/n), True,
         r"$J_n=[1-1/n,\,2+1/n]$", "Common intersection: [1, 2]", (0, 3)),
        (lambda n: (0, 1/n), False,
         r"$K_n=(0,\,1/n)$", "Common intersection: empty", (-.05, 1.05)),
    ]
    rows = [1, 2, 3, 4, 8, 16]
    for index, (ax, (bounds, closed, title, footer, limits)) in enumerate(
            zip(axes, cases)):
        for row, n in enumerate(rows):
            left, right = bounds(n)
            ax.plot([left, right], [row, row], color="#2878a5", lw=3,
                    zorder=2)
            ax.scatter([left, right], [row, row], s=48,
                       facecolor="#2878a5" if closed else "white",
                       edgecolor="#2878a5", linewidth=1.6, zorder=3)
        if index == 0:
            ax.axvline(1, color="#c05b20", ls="--", lw=1.3)
        elif index == 1:
            ax.axvspan(1, 2, color="#e8b870", alpha=.3)
        else:
            ax.axvline(0, color="#c05b20", ls="--", lw=1.3)
        ax.set_xlim(limits[0] - .08, limits[1] + .08)
        ax.set_ylim(5.6, -.65)
        ax.set_yticks(np.arange(len(rows)), [f"n = {n}" for n in rows])
        ax.set_title(title, fontsize=12, pad=14)
        ax.set_xlabel("Real number x", fontsize=11)
        ax.text(.5, -.28, footer, transform=ax.transAxes,
                ha="center", fontsize=11)
        ax.grid(axis="x", alpha=.17)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Nesting keeps restrictions consistent; endpoints decide what survives",
                 fontsize=14, y=.98)
    fig.subplots_adjust(left=.06, right=.98, top=.79, bottom=.26, wspace=.3)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
