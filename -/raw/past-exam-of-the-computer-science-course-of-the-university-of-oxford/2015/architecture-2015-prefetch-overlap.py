"""Synthetic one-node-ahead prefetch schedule; output PNG in the current directory.

Tested with Python 3.14, Matplotlib 3.10.7 and NumPy 2.3.5, as documented
in the repository pyproject.toml. No machine-specific latency claim is made.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    fig, axes = plt.subplots(2, 1, figsize=(10, 5.4), sharex=True)
    fig.set_facecolor("white")
    colors = {"compute": "#3274a1", "transfer": "#df8f44", "hint": "#40865b"}

    def block(ax, start, duration, lane, kind, label):
        ax.broken_barh([(start, duration)], (lane - .27, .54),
                      facecolors=colors[kind], edgecolors="white", linewidth=1)
        if label:
            ax.text(start + duration / 2, lane, label, ha="center", va="center",
                    color="white", fontsize=9)

    ax = axes[0]
    block(ax, 0, 120, 1, "compute", "process node i")
    block(ax, 120, 100, 0, "transfer", "demand fetch i+1")
    block(ax, 220, 120, 1, "compute", "process node i+1")
    ax.plot([120, 220], [1, 1], color=colors["transfer"], linestyle=":", linewidth=3)
    ax.text(170, 1.38, "CPU waits", ha="center", fontsize=9, color="#985516")
    ax.axvline(220, color="#555555", linestyle="--", linewidth=.8)
    ax.set_title("No prefetch: processing starts are 220 cycles apart", loc="left", fontsize=11)

    ax = axes[1]
    block(ax, 0, 1, 1, "hint", "")
    block(ax, 1, 120, 1, "compute", "process node i")
    block(ax, 1, 100, 0, "transfer", "prefetch i+1")
    block(ax, 121, 1, 1, "hint", "")
    block(ax, 122, 120, 1, "compute", "process node i+1")
    block(ax, 122, 100, 0, "transfer", "prefetch i+2")
    block(ax, 242, 1, 1, "hint", "")
    block(ax, 243, 110, 1, "compute", "process node i+2")
    ax.annotate("1-cycle hint", xy=(.5, 1.23), xytext=(37, 1.6),
                ha="center", fontsize=9, arrowprops={"arrowstyle": "->", "lw": .8})
    ax.axvline(122, color="#555555", linestyle="--", linewidth=.8)
    ax.set_title("Prefetch: processing starts are 121 cycles apart", loc="left", fontsize=11)
    ax.set_xlabel("Cycles after current node becomes available")

    for ax in axes:
        ax.set_facecolor("white")
        ax.set_yticks([0, 1], ["Transfer", "CPU"])
        ax.set_ylim(-.6, 1.9)
        ax.set_xlim(-5, 355)
        ax.grid(axis="x", color="#dddddd", linewidth=.6)
        ax.set_axisbelow(True)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="y", length=0)
    fig.suptitle("Overlap the next node's transfer with the current node's work", fontsize=13)
    fig.legend(handles=[Patch(color=colors["compute"], label="120 cycles of independent work"),
                        Patch(color=colors["transfer"], label="100-cycle transfer"),
                        Patch(color=colors["hint"], label="1-cycle hint")],
               loc="lower center", ncol=3, frameon=False, fontsize=9)
    fig.subplots_adjust(left=.10, right=.98, top=.86, bottom=.17, hspace=.56)
    fig.savefig(Path.cwd() / "architecture-2015-prefetch-overlap.png", dpi=110,
                facecolor="white", transparent=False,
                metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
