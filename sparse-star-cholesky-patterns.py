"""Original matrix/factor sparsity comparison; emit PNG in the working directory.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle
import numpy as np


BLUE = "#23649a"
ORANGE = "#c34e18"


def pattern(ax, data, labels, original=None):
    for i in range(5):
        for j in range(5):
            color = "white"
            if abs(data[i, j]) > 1e-12:
                color = ORANGE if original is not None and original[i, j] == 0 else BLUE
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1,
                                   fc=color, ec="#c8cdd2", lw=0.8))
    ax.set(xticks=range(5), yticks=range(5), xticklabels=labels, yticklabels=labels,
           xlim=(-0.5, 4.5), ylim=(4.5, -0.5), aspect="equal")
    ax.xaxis.tick_top()
    ax.tick_params(length=0, pad=5)
    for spine in ax.spines.values():
        spine.set_visible(False)


def main():
    a = np.diag([5., 2., 2., 2., 2.])
    a[0, 1:] = a[1:, 0] = -1
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 2, figsize=(8.8, 7.2))
    fig.subplots_adjust(left=0.08, right=0.94, top=0.82, bottom=0.13,
                        hspace=0.45, wspace=0.38)
    fig.suptitle("One matrix, two orderings, different factor storage", y=0.98, fontsize=17)
    fig.text(0.5, 0.915, r"$B=PAP^T=CC^T$    ·    each square is one matrix position",
             ha="center", fontsize=12)
    counts = []
    for row, order in enumerate(([0, 1, 2, 3, 4], [1, 2, 3, 4, 0])):
        b = a[np.ix_(order, order)]
        c = np.linalg.cholesky(b)
        np.testing.assert_allclose(c @ c.T, b, atol=1e-14)
        labels = [["c", "1", "2", "3", "4"][i] for i in order]
        pattern(axes[row, 0], b, labels)
        pattern(axes[row, 1], c, labels, original=np.tril(b))
        count = int(np.count_nonzero(abs(c) > 1e-12))
        fills = int(np.count_nonzero((abs(c) > 1e-12) & (np.tril(b) == 0)))
        counts.append((count, fills))
        axes[row, 0].set_title("B: center first" if row == 0 else "B: leaves first", pad=24)
        axes[row, 1].set_title(f"C: {count} entries, {fills} fill positions", pad=24)
        axes[row, 0].text(0.5, -0.09, "13 entries in all; 9 in lower triangle",
                           transform=axes[row, 0].transAxes, ha="center", fontsize=10)
        axes[row, 1].text(0.5, -0.09, "Count includes the five diagonal entries",
                           transform=axes[row, 1].transAxes, ha="center", fontsize=10)
    assert counts == [(15, 6), (9, 0)]
    fig.legend(handles=[Patch(fc=BLUE, label="Original nonzero position"),
                        Patch(fc=ORANGE, label="Fill position"),
                        Patch(fc="white", ec="#c8cdd2", label="Zero")],
               loc="lower center", bbox_to_anchor=(0.5, 0.01), frameon=False, ncol=3)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
