"""Illustrate unit-step random walks; tested with Python 3.14, NumPy/Matplotlib.

Run through make _media/random-walk-paths-and-drift.png. Output goes to CWD.
The shaded mean +/- one standard deviation is a scale, not a coverage claim.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    rng = np.random.default_rng(1905)
    n = np.arange(81)
    plt.rcParams.update({"font.size": 11, "axes.titlesize": 13})
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.4), dpi=120,
                             facecolor="white", sharex=True, sharey=True)
    for ax, p, count, colors in zip(
        axes, (0.5, 0.65), (4, 2),
        (("#2274a5", "#d27727", "#43876d", "#9258a2"),
         ("#2274a5", "#d27727")),
    ):
        mean = n * (2 * p - 1)
        sigma = np.sqrt(4 * n * p * (1 - p))
        ax.fill_between(n, mean - sigma, mean + sigma, color="#dfe5ec",
                        label=r"Mean $\pm$ one SD")
        for i, color in enumerate(colors):
            steps = np.where(rng.random(80) < p, 1, -1)
            path = np.concatenate(([0], np.cumsum(steps)))
            assert np.all(np.abs(np.diff(path)) == 1)
            assert np.all((path - n) % 2 == 0)
            ax.plot(n, path, color=color, lw=1.5, alpha=0.95,
                    label=f"Path {i + 1}")
        ax.plot(n, mean, color="#182b40", ls="--", lw=2.2,
                label=r"Mean $n(2p-1)$")
        ax.set(title=f"{'Fair' if p == 0.5 else 'Biased'}: p = {p:.2f}; {count} paths",
               xlabel="Step count n", xlim=(0, 80), ylim=(-23, 46))
        ax.set_xticks([0, 20, 40, 60, 80])
        ax.grid(color="#edf0f3")
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
        ax.legend(loc="upper left", fontsize=9, frameon=False)
    axes[0].set_ylabel(r"Position $S_n$ (unit steps)")
    fig.suptitle("Independent steps accumulate into wandering paths", fontsize=16)
    fig.text(0.5, 0.045,
             "Seed 1905; illustrative paths. Shading measures spread at each n;\n"
             "it is not a confidence interval or a guarantee that a path stays inside.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.22, top=0.83, wspace=0.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
