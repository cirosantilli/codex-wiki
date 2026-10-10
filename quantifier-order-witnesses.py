"""Generate quantifier-order-witnesses.png in cwd.

Tested with Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
The finite display illustrates arguments for all natural numbers.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle


def main():
    n = np.arange(6)
    m = np.arange(7)
    relation = m[None, :] > n[:, None]
    assert relation[np.arange(6), n + 1].all()
    fixed = 3
    assert np.array_equal(relation[:, fixed], [True, True, True, False, False, False])
    fig, axes = plt.subplots(1, 2, figsize=(9.3, 4.7), dpi=120, facecolor="white")
    titles = [r"$\forall n\,\exists m\ (m>n)$: true",
              r"$\exists m\,\forall n\ (m>n)$: false"]
    for ax, title in zip(axes, titles):
        ax.imshow(relation, cmap=ListedColormap(["#f3f3f3", "#dcebe5"]),
                  vmin=0, vmax=1, interpolation="nearest")
        ax.set(xticks=m, yticks=n, xlabel="Candidate witness m", ylabel="Input n",
               title=title)
        ax.set_xticks(np.arange(-.5, 7, 1), minor=True)
        ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
        ax.grid(which="minor", color="white", linewidth=2)
        ax.tick_params(which="minor", bottom=False, left=False)
        for i in n:
            for j in m:
                ax.text(j, i, "T" if relation[i, j] else "F", ha="center",
                        va="center", fontsize=10, color="#5e6964")
    for i in n:
        axes[0].add_patch(Rectangle((i + .5, i - .5), 1, 1, fill=False,
                                   edgecolor="#1764ab", linewidth=2.2, zorder=3))
    axes[1].add_patch(Rectangle((fixed - .5, -.5), 1, len(n), fill=False,
                               edgecolor="#b44032", linewidth=2.2, zorder=3))
    axes[1].text(fixed, fixed, "F", ha="center", va="center", color="#a12821",
                 fontsize=13, fontweight="bold")
    axes[0].text(.5, -.23, r"Blue boxes: choose $m=n+1$ for each $n$.",
                 transform=axes[0].transAxes, ha="center", fontsize=11)
    axes[1].text(.5, -.23, r"Red column: $m=3$ fails at $n=3$.",
                 transform=axes[1].transAxes, ha="center", fontsize=11)
    fig.suptitle("Quantifier order controls witness dependence", fontsize=16, y=.97)
    fig.text(.5, .035, r"Only a finite window is drawn. Any fixed $m$ fails at $n=m$, since $m>m$ is false.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=.07, right=.98, top=.82, bottom=.28, wspace=.30)
    fig.savefig(Path.cwd() / "quantifier-order-witnesses.png", facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
