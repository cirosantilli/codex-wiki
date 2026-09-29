"""Trace five fixed observations through sorting; opaque basename PNG to CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    values = np.array([0.7, 0.1, 0.9, 0.4, 0.2])
    order = np.argsort(values)
    ranks = np.empty(5, dtype=int)
    ranks[order] = np.arange(1, 6)
    colors = ["#246bce", "#ac5930", "#7554ab", "#21845b", "#a3720b"]
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 5.4), dpi=110)
    for ax in axes:
        ax.set(xlim=(0.5, 5.5), ylim=(-0.04, 1.04), ylabel="Observed value")
        ax.set_xticks(range(1, 6))
        ax.set_yticks(np.arange(0, 1.01, 0.2))
        ax.grid(axis="y", alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set(title="Original observations", xlabel="Original index i")
    axes[1].set(title="Order statistics (sorted values)", xlabel="Sorted position r")
    for i, value in enumerate(values):
        r = ranks[i]
        for ax, x, label in [(axes[0], i + 1, f"{value:.1f}  (rank {r})"),
                             (axes[1], r, f"{value:.1f}  (index {i + 1})")]:
            ax.scatter(x, value, s=85, color=colors[i], zorder=4)
            offset = -18 if ax is axes[1] and x == 1 else 13
            ax.annotate(label, (x, value), xytext=(0, offset), textcoords="offset points",
                        ha="left" if x == 1 else "right" if x == 5 else "center",
                        fontsize=10, color=colors[i])
    axes[1].scatter(3, values[order[2]], s=270, facecolors="none",
                    edgecolors="#21845b", linewidths=2, zorder=5)
    fig.suptitle("Sorting preserves values and changes their positions", fontsize=15, weight="bold")
    fig.text(0.5, 0.10, r"Third smallest: $x_{(3)}=x_4=0.4$ (the sample median)",
             ha="center", fontsize=12)
    fig.text(0.5, 0.045, "Fixed example, no random draws. Colors follow original indices 1 to 5.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.24, top=0.84, wspace=0.30)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
