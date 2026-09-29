"""Plot multiples of 12 and 18 and their shared event times.

Run from _media to save the PNG there. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7; dependencies are in pyproject.toml.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(8, 3.5), dpi=120)
    fig.subplots_adjust(left=0.18, right=0.97, bottom=0.26, top=0.78)
    common = np.array([0, 36, 72])
    for day in common:
        ax.axvspan(day - 1.3, day + 1.3, color="#e5f2e9", zorder=0)
    for period, row, color in [(12, 1, "#245a81"), (18, 0, "#b45c24")]:
        days = np.arange(0, 73, period)
        ax.hlines(row, 0, 72, color="#b9b9b9", linewidth=1, zorder=1)
        ax.scatter(days, np.full_like(days, row), marker="|", s=460,
                   linewidths=3, color=color, zorder=3)
        ax.scatter(common, np.full_like(common, row), s=115,
                   facecolors="none", edgecolors="#27764d", linewidths=2,
                   zorder=4)
    ax.annotate("First positive meeting: day 36", xy=(36, 1.15),
                xytext=(36, 1.60), ha="center", fontsize=12,
                arrowprops={"arrowstyle": "->", "color": "#27764d"})
    ax.set(xlim=(-3, 75), ylim=(-0.45, 1.9), xlabel="Days since both events started")
    ax.set_xticks(np.arange(0, 73, 6))
    ax.set_yticks([1, 0], ["Every 12 days", "Every 18 days"])
    ax.tick_params(axis="y", length=0, pad=10)
    for spine in ("top", "left", "right"):
        ax.spines[spine].set_visible(False)
    ax.text(0.5, -0.39, "Shared times: 0, 36, 72, …     |     lcm(12, 18) = 36",
            transform=ax.transAxes, ha="center", color="#27764d", fontsize=12)
    fig.suptitle("Two schedules starting together", fontsize=16, y=0.94)
    ax.set_facecolor("white")
    fig.savefig(Path.cwd() / "least-common-multiple-periods.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
