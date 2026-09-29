"""Draw hits, misses and cumulative misses for a four-page cyclic trace.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; writes the matching opaque white PNG to the current directory.
Exact LRU, initially empty frames, demand paging and no prefetching are assumed.
"""

from collections import OrderedDict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


def lru_misses(trace, capacity):
    resident = OrderedDict()
    misses = []
    for page in trace:
        missed = page not in resident
        misses.append(missed)
        if missed and len(resident) == capacity:
            resident.popitem(last=False)
        resident[page] = None
        resident.move_to_end(page)
    return np.array(misses, dtype=bool)


def main():
    trace = [1, 2, 3, 4] * 5
    times = np.arange(1, 21)
    miss3 = lru_misses(trace, 3)
    miss4 = lru_misses(trace, 4)
    assert miss3.sum() == 20 and miss4.sum() == 4
    assert miss3[4:].sum() == 16 and miss4[4:].sum() == 0

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    orange, teal, blue = "#af4d16", "#227a67", "#2268a2"
    fig, (ax, counts) = plt.subplots(2, 1, figsize=(10.8, 6.5), dpi=110,
                                    gridspec_kw={"height_ratios": [1, 1.7]})
    fig.patch.set_facecolor("white")
    fig.suptitle("One extra frame stops repeated misses in this cyclic trace",
                 fontsize=18, fontweight="bold", y=0.975)
    fig.text(0.5, 0.90, "Exact LRU  •  20 references: (1, 2, 3, 4) × 5  •  start empty  •  no prefetching",
             ha="center", fontsize=11)
    for target in (ax, counts):
        target.axvspan(0.5, 4.5, color="#fff0dc", zorder=0)
        target.axvline(4.5, color="#8b642a", linestyle=":", linewidth=1.4)
        target.set_xlim(0.5, 20.5)
        target.set_xticks(times)
    for row, missed in [(1, miss3), (0, miss4)]:
        ax.scatter(times[missed], np.full(missed.sum(), row), color=orange,
                   marker="s", s=210, zorder=3)
        ax.scatter(times[~missed], np.full((~missed).sum(), row), color=teal,
                   marker="o", s=210, zorder=3)
        for t, flag in zip(times, missed):
            ax.text(t, row, "M" if flag else "H", color="white", fontsize=9,
                    ha="center", va="center", fontweight="bold", zorder=4)
    ax.set(ylim=(-0.45, 1.7), yticks=[0, 1], yticklabels=["4 frames", "3 frames"])
    ax.tick_params(axis="x", labelbottom=False, length=0)
    top = ax.secondary_xaxis("top")
    top.set_xticks(times, labels=trace)
    top.set_xlabel("Requested page", labelpad=6)
    ax.text(2.5, 1.42, "Initial loads", ha="center", color="#795623", fontsize=10)
    ax.text(12.5, 1.42, "References 5–20: 3 frames → 16 misses; 4 frames → 0 misses",
            ha="center", fontsize=10)
    counts.step(np.arange(0, 21), np.r_[0, np.cumsum(miss3)], where="post",
                color=orange, linewidth=2.6, label="3 frames: 20 / 20 misses (100%)")
    counts.step(np.arange(0, 21), np.r_[0, np.cumsum(miss4)], where="post",
                color=blue, linewidth=2.6, label="4 frames: 4 / 20 misses (20%)")
    counts.set(ylim=(-0.5, 21), yticks=[0, 4, 8, 12, 16, 20],
               xlabel="Reference index (state immediately after access)", ylabel="Cumulative misses")
    counts.grid(alpha=0.22)
    counts.legend(loc="upper left", framealpha=1, fontsize=10)
    counts.text(12.5, 5.3, "Four compulsory misses, then only hits", ha="center", color=blue)
    fig.legend(handles=[Line2D([], [], color=orange, marker="s", linestyle="", label="M: miss / nonresident fault"),
                        Line2D([], [], color=teal, marker="o", linestyle="", label="H: resident hit")],
               loc="lower center", bbox_to_anchor=(0.5, 0.055), ncol=2, frameon=False, fontsize=11)
    fig.text(0.5, 0.021, "Miss counts alone describe residency. Thrashing also requires repeated costly page cycling.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.105, right=0.98, top=0.785, bottom=0.18, hspace=0.29)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
