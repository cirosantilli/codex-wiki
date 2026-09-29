"""Compare two exact chosen chain populations, never experimental data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5; run from _media.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


def main():
    living = np.array([10, 10, 10, 10])
    terminating = np.array([4, 4, 16, 16])
    for lengths in [living, terminating]:
        assert len(lengths) == 4 and lengths.sum() == 40 and lengths.mean() == 10
    assert living.var() == 0 and terminating.var() == 36
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.7), dpi=140, sharey=True,
                             facecolor="white")
    fig.suptitle("Two chosen continuations of four length-four chains", fontsize=17,
                 weight="bold", y=0.97)
    fig.text(0.5, 0.89, "24 remaining monomers • all 40 units incorporated at the end • no new chains",
             ha="center", fontsize=11)
    for ax, lengths, colors, title, stats in [
        (axes[0], living, ["#176aa3"] * 4, "All four remain active", "C = 4, A = 4, S = 40\nMean = 10; chosen variance = 0"),
        (axes[1], terminating, ["#6a737d"] * 2 + ["#176aa3"] * 2,
         "Two stop without joining", "C = 4, A = 2, S = 40\nMean = 10; chosen variance = 36"),
    ]:
        ax.bar(np.arange(4), lengths, color=colors, width=0.60)
        ax.axhline(10, color="#c8651a", linestyle="--", linewidth=1.5)
        ax.set(xticks=np.arange(4), xticklabels=["A", "B", "C", "D"], ylim=(0, 19),
               yticks=np.arange(0, 19, 2), xlabel="Individual chain")
        ax.set_title(title, fontsize=14, pad=12)
        for i, n in enumerate(lengths):
            ax.text(i, n + 0.45, str(n), ha="center", fontsize=12)
        ax.text(0.5, -0.26, stats, transform=ax.transAxes, ha="center", fontsize=11,
                linespacing=1.6)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color="#e4e7eb", linewidth=0.7)
    axes[0].set_ylabel("Incorporated monomeric units", fontsize=12)
    axes[0].legend(handles=[Patch(color="#176aa3", label="Active"),
                            Patch(color="#6a737d", label="Inactive")],
                   loc="upper left", frameon=False, fontsize=10)
    fig.text(0.5, 0.025, "Stipulated integer populations — not measurements or universal distribution shapes",
             ha="center", fontsize=11, color="#515b65")
    fig.subplots_adjust(left=0.08, right=0.98, top=0.78, bottom=0.28, wspace=0.20)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
