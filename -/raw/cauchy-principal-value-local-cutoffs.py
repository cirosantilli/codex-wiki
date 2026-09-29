"""Illustrate exact cutoff dependence of 1/x; no measured data.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Output is this script's basename with .png, in the current directory.
Tested: Python 3.14.4, Matplotlib 3.10.7+dfsg1, NumPy 2.3.5.
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    blue, orange, purple = "#246a9b", "#bf5529", "#805ca0"
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "axes.facecolor": "white"})
    fig = plt.figure(figsize=(10, 6.6), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.05])
    fig.suptitle("The cutoff rule determines the cancellation", fontsize=18)
    for ax, em, ep, title in [
        (fig.add_subplot(grid[0, 0]), 0.18, 0.18, "Equal widths: signed sum = 0"),
        (fig.add_subplot(grid[0, 1]), 0.36, 0.18, r"Unequal widths: signed sum = $\log 2$"),
    ]:
        left = np.linspace(-1, -em, 600)
        right = np.linspace(ep, 1, 600)
        for x, color in [(left, blue), (right, orange)]:
            ax.plot(x, 1/x, color=color, lw=2)
            ax.fill_between(x, 0, 1/x, color=color, alpha=0.22)
        ax.axvspan(-em, ep, color="#efefef", zorder=0)
        ax.axhline(0, color="#555555", lw=0.8)
        ax.axvline(0, color="#999999", lw=0.8, ls=":")
        ax.text(-0.68, -3.6, rf"$\log\varepsilon_-={np.log(em):.2f}$", color=blue)
        ax.text(0.30, 3.5, rf"$-\log\varepsilon_+={-np.log(ep):.2f}$", color=orange)
        ax.set_xticks([-1, -em, 0, ep, 1],
                      ["−1", r"$-\varepsilon_-$", "0", r"$\varepsilon_+$", "1"])
        ax.set(xlim=(-1.04, 1.04), ylim=(-6, 6), ylabel=r"$1/x$", xlabel=r"$x$")
        ax.set_title(title, fontsize=12)

    ax = fig.add_subplot(grid[1, :])
    s = np.linspace(0.75, 7, 500)
    ax.plot(s, s, color=orange, lw=1.8, label=r"Right integral: $-\log\varepsilon=s$")
    ax.plot(s, -s, color=blue, lw=1.8, label=r"Left integral: $\log\varepsilon=-s$")
    ax.plot(s, np.zeros_like(s), color="#222222", lw=2.5,
            label=r"Equal cutoffs: sum $=0$")
    ax.plot(s, np.full_like(s, np.log(2)), color=purple, lw=2, ls="--",
            label=r"$\varepsilon_-=2\varepsilon_+$: sum $=\log 2$")
    ax.plot(s, -s, color="#417f55", lw=2, ls=":",
            label=r"$\varepsilon_-=\varepsilon_+^2$: sum $=-s$")
    ax.set(xlabel=r"$s=\log(1/\varepsilon_+)$  (larger $s$ means a smaller gap)",
           ylabel="Truncated integral", xlim=(0.75, 7), ylim=(-7.5, 7.5))
    ax.grid(alpha=0.18)
    ax.legend(loc="upper left", fontsize=10, framealpha=1)
    ax.set_title("Both cutoffs shrink; different paths still give different answers", fontsize=12)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"symmetric_sum": 0, "ratio_two_sum": float(np.log(2)),
                      "unequal_endpoints_minus_one_to_two": float(np.log(2)),
                      "squared_left_cutoff_sum_at_s_seven": -7}))


if __name__ == "__main__":
    main()
