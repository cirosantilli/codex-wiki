"""Illustrate the analytic DKW band, without simulating samples or coverage.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5.
Run from _media to write this generator's matching opaque PNG there.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    alpha = 0.1
    sizes = np.array([5, 50, 500])
    eps = np.sqrt(np.log(2 / alpha) / (2 * sizes))
    sample = np.array([1, 1, 2, 4, 6])
    edges = np.array([0, 1, 2, 4, 6, 7])
    # Exact right-continuous values at every edge, including both tied 1s.
    fn = np.count_nonzero(sample[:, None] <= edges[None, :], axis=0) / sample.size
    low, high = np.clip(fn - eps[0], 0, 1), np.clip(fn + eps[0], 0, 1)
    blue, orange = "#1767a1", "#c36b13"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (ax, width_ax) = plt.subplots(
        1, 2, figsize=(10.2, 5.3), gridspec_kw={"width_ratios": [1.3, 1]},
        facecolor="white",
    )
    fig.subplots_adjust(left=0.075, right=0.97, top=0.72, bottom=0.23, wspace=0.30)
    fig.suptitle("A band for the entire population CDF", fontsize=17, y=0.98)
    fig.text(0.5, 0.875,
             r"$\alpha=0.1,\quad \varepsilon_{n,\alpha}=\sqrt{\log(2/\alpha)/(2n)}$",
             ha="center", fontsize=14)
    ax.fill_between(edges, low, high, step="post", color=blue, alpha=0.16,
                    label="clipped confidence band")
    ax.step(edges, low, where="post", color=blue, lw=1, alpha=0.65)
    ax.step(edges, high, where="post", color=blue, lw=1, alpha=0.65)
    ax.step(edges, fn, where="post", color=blue, lw=2.3, label=r"$F_5$")
    ax.scatter([1, 2, 4, 6], [0.4, 0.6, 0.8, 1.0], s=25, color=blue, zorder=4)
    ax.set_title(r"Chosen sample [1, 1, 2, 4, 6]; $n=5$", fontsize=12)
    ax.set_xlim(0, 7)
    ax.set_ylim(-0.04, 1.04)
    ax.set_xticks(range(8))
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    ax.set_xlabel(r"Threshold $x$")
    ax.set_ylabel("Cumulative probability")
    ax.grid(axis="y", alpha=0.2)
    ax.legend(loc="lower right", fontsize=9, framealpha=1)
    width_ax.barh([2, 1, 0], eps, height=0.45, color=[blue, "#5797c5", "#98c4df"])
    width_ax.set_yticks([2, 1, 0], [r"$n=5$", r"$n=50$", r"$n=500$"])
    for row, value in zip([2, 1, 0], eps):
        width_ax.text(value + 0.015, row, f"{value:.5f}", va="center", fontsize=11)
    width_ax.set_xlim(0, 0.72)
    width_ax.set_ylim(-0.6, 2.6)
    width_ax.set_xticks([0, 0.2, 0.4, 0.6])
    width_ax.set_xlabel("Half-width before clipping")
    width_ax.set_title("Theoretical widths; no extra samples", fontsize=12)
    width_ax.grid(axis="x", alpha=0.2)
    width_ax.set_axisbelow(True)
    fig.text(0.5, 0.105,
             "IID sampling: probability ≥ 90% that every threshold is covered at a fixed n.",
             ha="center", fontsize=11, color=orange)
    fig.text(0.5, 0.05,
             "The chosen sample illustrates the procedure; coverage follows from the DKW inequality.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
