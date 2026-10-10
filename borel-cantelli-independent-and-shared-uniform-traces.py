"""Generate finite fresh-input and shared-input event traces in the current directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    n = np.arange(1, 121)
    probabilities = 1 / (n + 1)
    # Two reproducible, independent streams; neither searches for particular traces.
    shared_rng = np.random.default_rng(18)
    fresh_rng = np.random.default_rng(19)
    shared_u = shared_rng.random(6)
    independent = fresh_rng.random((6, n.size)) <= probabilities
    shared = shared_u[:, None] <= probabilities
    assert np.all(shared[:, 1:] <= shared[:, :-1])
    assert np.array_equal(shared.sum(axis=1), np.minimum(120, np.maximum(0, np.floor(1 / shared_u).astype(int) - 1)))

    plt.rcParams.update({"font.size": 11, "axes.titlesize": 12, "figure.facecolor": "white"})
    fig, axes = plt.subplots(2, 1, figsize=(10, 6.1), layout="constrained", sharex=True)
    for ax, hits, color, title in zip(
        axes, [independent, shared], ["#2463a0", "#b55318"],
        [r"Fresh input at every index: $A_n=\{U_n\leq1/(n+1)\}$",
         r"One shared input per row: $A_n=\{U\leq1/(n+1)\}$"],
    ):
        for row, trace in enumerate(hits):
            y = 6 - row
            ax.hlines(y, 1, 120, color="#dedede", lw=1)
            ax.scatter(n[trace], np.full(trace.sum(), y), color=color, s=30, zorder=3)
        ax.set_title(title, loc="left")
        ax.set_ylim(0.4, 6.6)
        ax.set_yticks(np.arange(1, 7))
        ax.set_ylabel("Simulated row")
        ax.set_xscale("log")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="x", alpha=0.18)
    axes[1].set_yticklabels([f"{6-i}  (U={shared_u[5-i]:.3f})" for i in range(6)])
    axes[0].set_yticklabels([str(6-i) for i in range(6)])
    axes[1].set_xlim(0.9, 140)
    axes[1].set_xticks([1, 2, 5, 10, 20, 50, 120], labels=["1", "2", "5", "10", "20", "50", "120"])
    axes[1].set_xlabel("Event index n (logarithmic scale); dot = occurrence")
    fig.suptitle("Same probabilities, different dependence", fontsize=15)
    fig.supxlabel("Only 120 indices are shown: finite traces do not prove infinite-time claims.", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
