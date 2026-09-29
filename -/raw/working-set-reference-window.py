"""Illustrate a reference-count working set versus actual LRU residency.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; writes the matching opaque white PNG to the current directory.
The window counts memory references, not elapsed clock time.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
import numpy as np


def main():
    trace = [1, 2, 3, 4] * 5
    window = 4
    working_sets = [set(trace[max(0, t - window):t]) for t in range(1, 21)]
    resident_sets = []
    recency = []  # Oldest first; a hit also refreshes recency.
    for page in trace:
        if page in recency:
            recency.remove(page)
        elif len(recency) == 3:
            recency.pop(0)
        recency.append(page)
        resident_sets.append(set(recency))
    assert working_sets[4] == {1, 2, 3, 4}
    assert resident_sets[4] == {1, 3, 4}
    assert all(len(s) == 4 for s in working_sets[3:])
    assert all(len(s) == 3 for s in resident_sets[2:])

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(3, 1, figsize=(10.8, 8.0), dpi=110,
                             gridspec_kw={"height_ratios": [1.1, 1.1, 1.2]})
    fig.patch.set_facecolor("white")
    fig.suptitle("Recent demand and actual residency are different sets",
                 fontsize=18, fontweight="bold", y=0.97)
    fig.text(0.5, 0.90, "Trace: (1, 2, 3, 4) × 5  •  window Δ = 4 references  •  empty initial residency",
             ha="center", fontsize=11)
    pages = np.arange(1, 5)
    for ax, sets, color, title in zip(
        axes[:2], [working_sets, resident_sets], ["#2268a2", "#27816c"],
        ["Working set W(t, 4): distinct pages in the last four references",
         "Resident set: exact LRU with only three page frames"],
    ):
        matrix = np.array([[int(page in current) for current in sets] for page in pages])
        ax.imshow(matrix, aspect="auto", interpolation="nearest",
                  cmap=ListedColormap(["#f1f3f5", color]), vmin=0, vmax=1,
                  extent=(0.5, 20.5, 4.5, 0.5))
        ax.set(yticks=pages, ylabel="Page", xticks=np.arange(1, 21))
        ax.set_title(title, loc="left", pad=11, fontsize=12, fontweight="bold")
        ax.set_xticks(np.arange(0.5, 21), minor=True)
        ax.set_yticks(np.arange(0.5, 5), minor=True)
        ax.grid(which="minor", color="white", linewidth=1.5)
        ax.tick_params(which="minor", length=0)
        ax.tick_params(axis="x", labelbottom=False, length=0)
        ax.add_patch(Rectangle((4.5, 0.5), 1, 4, fill=False,
                               edgecolor="#ad4b12", linewidth=2.4, zorder=5))
    top = axes[0].secondary_xaxis("top")
    top.set_xticks(np.arange(1, 21), labels=trace)
    top.set_xlabel("Requested page at each reference", labelpad=5)
    # The window after reference 5 comprises references 2, 3, 4, 5.
    axes[0].add_patch(Rectangle((1.5, 0.5), 4, 4, fill=False,
                                edgecolor="#ad4b12", linewidth=1.8, linestyle="--", zorder=5))
    times = np.arange(0, 21)
    axes[2].step(times, [0] + [len(s) for s in working_sets], where="post",
                 color="#2268a2", linewidth=2.5, label="Working set size")
    axes[2].step(times, [0] + [len(s) for s in resident_sets], where="post",
                 color="#27816c", linewidth=2.5, linestyle="--", label="Resident set size (LRU, 3 frames)")
    axes[2].axvline(5, color="#ad4b12", linewidth=1.4, alpha=0.7)
    axes[2].set(xlim=(-0.2, 20.5), ylim=(-0.1, 4.65), yticks=np.arange(0, 5),
                xticks=np.arange(0, 21), xlabel="Reference index t (state immediately after access)",
                ylabel="Distinct pages")
    axes[2].grid(alpha=0.22)
    axes[2].legend(loc="lower right", framealpha=1, fontsize=10)
    axes[2].set_title("After warmup: four pages recently used, only three resident", loc="left", fontsize=12)
    fig.text(0.5, 0.032, "At t = 5: window [2, 3, 4, 1] → W = {1, 2, 3, 4}; resident set = {1, 3, 4}.\n"
             "Colored cells mean membership; pale cells mean absence. Orange marks t = 5 and its window.",
             ha="center", fontsize=11, linespacing=1.5)
    fig.subplots_adjust(left=0.085, right=0.98, top=0.79, bottom=0.14, hspace=0.4)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
