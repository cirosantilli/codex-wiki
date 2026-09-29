"""Draw a counting toy, with an explicitly finite pool of targets.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Tested with Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
Output: second-messenger-amplification.png in the current directory.
All counts and capacities are chosen assumptions, not measured pathway data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


OUTPUT = Path("second-messenger-amplification.png")
RELAYS_PER_RECEPTOR = 5
TARGETS_PER_RELAY = 20
TARGET_POOL = 250
INK = "#24364a"
BLUE = "#1d6696"
GREEN = "#237b63"
ORANGE = "#b96720"


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig = plt.figure(figsize=(9, 6.7), dpi=120, facecolor="white")
    grid = fig.add_gridspec(2, 1, height_ratios=(1, 1.18), hspace=0.52,
                          left=0.13, right=0.94, bottom=0.12, top=0.85)
    top = fig.add_subplot(grid[0])
    top.set(xlim=(0, 10), ylim=(0, 3))
    top.axis("off")
    fig.suptitle("Amplification by repeated action: a counting toy", fontsize=16,
                 weight="bold", color=INK, y=0.97)
    fig.text(0.5, 0.914, "Assumed counts and capacity; not measured biological data",
             ha="center", color=INK, fontsize=11)
    top.text(0, 2.8, "A. Two sequential counting intervals; all targets distinct", color=INK,
             weight="bold", fontsize=11.5)
    top.scatter([0.95], [1.4], s=450, marker="s", color=BLUE)
    top.scatter(np.full(5, 4.4), np.linspace(0.55, 2.25, 5), s=65, color=GREEN)
    cols, rows = np.meshgrid(np.arange(10), np.arange(10))
    top.scatter(7.15 + 0.20 * cols.ravel(), 0.55 + 0.19 * rows.ravel(),
                s=15, color=ORANGE)
    for left, right, label in ((1.7, 3.75, "× 5"), (4.95, 6.7, "× 20")):
        top.add_patch(FancyArrowPatch((left, 1.4), (right, 1.4), arrowstyle="-|>",
                      mutation_scale=18, linewidth=1.7, color=INK))
        top.text((left + right) / 2, 1.8, label, ha="center", color=INK, fontsize=13)
    for x, text in ((0.95, "1 active receptor"), (4.4, "5 active relays"),
                    (8.05, "100 active targets")):
        top.text(x, 0.12, text, color=INK, ha="center", fontsize=10.5)
    bottom = fig.add_subplot(grid[1])
    counts = np.arange(6)
    unlimited = RELAYS_PER_RECEPTOR * TARGETS_PER_RELAY * counts
    limited = np.minimum(unlimited, TARGET_POOL)
    bottom.plot(counts, unlimited, "o--", color=BLUE, label="Enough targets: 100 N₀",
                linewidth=1.6, markersize=5)
    bottom.plot(counts, limited, "s-", color=ORANGE, label="Pool of 250: min(100 N₀, 250)",
                linewidth=2.0, markersize=6)
    bottom.set(xlim=(-0.15, 5.15), ylim=(-15, 555), xticks=counts,
               xlabel="Number of activated receptors, N₀", ylabel="Number of active targets, N₂")
    bottom.set_title("B. A finite target pool limits the output", loc="left", fontsize=11.5,
                     color=INK, weight="bold", pad=10)
    bottom.spines[["top", "right"]].set_visible(False)
    bottom.grid(axis="y", color="#dfe5ec", linewidth=0.7)
    bottom.legend(loc="upper left", frameon=False, fontsize=10)
    bottom.annotate("3 receptors → 250 targets", xy=(3, 250), xytext=(2.5, 365),
                    fontsize=10, color=ORANGE,
                    arrowprops={"arrowstyle": "->", "color": ORANGE})
    fig.text(0.5, 0.025, "Markers denote integer inputs. Joining lines guide the eye; they are not time courses.",
             ha="center", fontsize=10, color=INK)
    fig.savefig(OUTPUT, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
