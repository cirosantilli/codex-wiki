"""Original three-matching diagram; write PNG basename to CWD."""
from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    matrix = np.array([[1, 1, 0], [1, 1, 1], [0, 1, 1]])
    matchings = [p for p in permutations(range(3))
                 if all(matrix[i, p[i]] for i in range(3))]
    assert matchings == [(0, 1, 2), (0, 2, 1), (1, 0, 2)]
    fig, axes = plt.subplots(1, 3, figsize=(9.8, 4.3), dpi=120)
    fig.patch.set_facecolor("white")
    for ax, matching in zip(axes, matchings):
        ys = np.array([2., 1., 0.])
        for i in range(3):
            for j in range(3):
                if matrix[i, j]:
                    ax.plot([0, 1], [ys[i], ys[j]],
                            color="#dedede", lw=1.5, zorder=1)
        for i, j in enumerate(matching):
            ax.plot([0, 1], [ys[i], ys[j]],
                    color="#2878a5", lw=3, zorder=2)
        ax.scatter([0]*3, ys, s=150, color="#2878a5", zorder=3)
        ax.scatter([1]*3, ys, s=150, color="#c05b20", zorder=3)
        for i in range(3):
            ax.text(-.08, ys[i], f"Person {i+1}", ha="right",
                    va="center", fontsize=11)
            ax.text(1.08, ys[i], f"Job {i+1}", va="center", fontsize=11)
        inversions = sum(matching[i] > matching[j]
                         for i in range(3) for j in range(i+1, 3))
        sign = "+1" if inversions % 2 == 0 else "-1"
        ax.set_title("Columns " + str(tuple(j+1 for j in matching)),
                     fontsize=12, pad=14)
        ax.text(.5, -.13, "Product = 1; permutation sign = " + sign,
                transform=ax.transAxes, ha="center", fontsize=10.5)
        ax.set_xlim(-.48, 1.48)
        ax.set_ylim(-.2, 2.2)
        ax.axis("off")
    fig.suptitle("All three permitted assignments: permanent 3, determinant -1",
                 fontsize=14, y=.98)
    fig.text(.5, .055,
             "Gray edges are allowed; blue edges form one perfect matching. "
             "Crossings do not share a vertex.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.035, right=.97, top=.78, bottom=.23, wspace=.12)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
