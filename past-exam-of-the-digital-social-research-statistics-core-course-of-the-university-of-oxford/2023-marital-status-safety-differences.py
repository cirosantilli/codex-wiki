"""Render original contrasts from the held 2023 Statistics Core table counts.

Output goes to the current working directory. Intervals are unadjusted normal
approximations for independent proportions, not the paper's omnibus tests.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    labels = ["Pooled", "Single", "Married", "Living with partner", "Divorced", "Widowed"]
    none = np.array([[289, 208, 233], [73, 64, 78], [119, 80, 90], [51, 37, 35], [28, 15, 25], [18, 12, 5]])
    some = np.array([[353, 373, 351], [62, 68, 80], [186, 201, 181], [32, 46, 35], [42, 36, 35], [31, 22, 20]])
    n0, n1 = none.sum(axis=1), some.sum(axis=1)
    p0, p1 = none / n0[:, None], some / n1[:, None]
    difference = 100 * (p1 - p0)
    se = 100 * np.sqrt(p0 * (1 - p0) / n0[:, None] + p1 * (1 - p1) / n1[:, None])
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 5.3), dpi=100, sharey=True)
    y = np.arange(len(labels))
    for ax, column, heading, colour in zip(axes, [0, 2], ["Feeling very safe", "Feeling unsafe"], ["#17658f", "#a74b1b"]):
        ax.axvline(0, color="#606060", linewidth=1)
        ax.axhspan(-0.40, 0.40, color="#eeeeee", zorder=0)
        ax.errorbar(difference[:, column], y, xerr=1.96 * se[:, column], fmt="o", color=colour, ecolor=colour, capsize=3, linewidth=1.5, markersize=5)
        ax.set_title(heading, fontsize=12)
        ax.set_xlim(-30, 35)
        ax.set_xticks([-30, -15, 0, 15, 30])
        ax.set_xlabel("Some bad experiences minus none\n(percentage points)")
        ax.grid(axis="x", alpha=0.20)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_ylim(len(labels) - 0.55, -0.65)
    axes[0].set_yticks(y, labels)
    fig.suptitle("Safety-category differences by marital status", fontsize=14, y=0.98)
    fig.subplots_adjust(left=0.21, right=0.97, bottom=0.23, top=0.86, wspace=0.20)
    fig.text(0.02, 0.075, "Points: differences calculated from counts. Bars: unadjusted 95% normal intervals.", fontsize=9)
    fig.text(0.02, 0.035, "The pooled row reuses the stratum data. These descriptive differences do not identify causal effects.", fontsize=9)
    fig.savefig(Path.cwd() / "2023-marital-status-safety-differences.png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
