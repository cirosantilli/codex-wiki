"""Original Q6 sketch; PNG basename is written to the current directory.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), layout="constrained")
    fig.patch.set_facecolor("white")
    for ax, interval, limits, title in zip(
        axes,
        [(-1, 1), (-1, 0.2)],
        [(-2, 85), (-0.15, 4)],
        ["Requested interval", "Close view of the flat minimum"],
    ):
        x = np.linspace(*interval, 800)
        ax.set_facecolor("white")
        ax.plot(x, (1 + 2 * x) ** 4, color="#16648b", linewidth=2.4)
        ax.axhline(0, color="#666666", linewidth=0.7)
        ax.axvline(0, color="#666666", linewidth=0.7)
        ax.scatter([-0.5, 0], [0, 1], color="#ad3e2b", s=25, zorder=4)
        ax.set(xlim=interval, ylim=limits, xlabel="$x$", ylabel="$y$", title=title)
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].scatter([-1, 1], [1, 81], color="#16648b", s=25)
    axes[0].annotate("(1, 81)", (1, 81), xytext=(-52, -3), textcoords="offset points")
    axes[1].annotate("(-1/2, 0)", (-0.5, 0), xytext=(-28, 14), textcoords="offset points")
    axes[1].annotate("(0, 1)", (0, 1), xytext=(-47, 7), textcoords="offset points")
    fig.suptitle(r"$y=(1+2x)^4$")
    fig.savefig(Path("paper-1-quartic.png"), dpi=160, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
