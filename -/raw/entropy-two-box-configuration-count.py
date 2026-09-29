"""Enumerate the 16 binary configurations of four distinguishable labels.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python3
../entropy-two-box-configuration-count.py
Writes its matching PNG basename to the current working directory.
Tested with Python 3.14.4, Matplotlib 3.10.7 (Debian +dfsg1).
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    strings = ["".join(bits) for bits in product("01", repeat=4)]
    groups = [[s for s in strings if s.count("0") == k] for k in range(5)]
    blue, orange, gray = "#216b9d", "#ac4b14", "#52616b"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.5, 6.4), dpi=120)
    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.03, top=0.80)
    fig.suptitle("Four labeled particles: sixteen configurations, five occupancies", fontsize=15, y=0.96)
    fig.text(0.5, 0.89, "Digits refer to labels A, B, C, D in that order.  0 = left; 1 = right.", ha="center")
    fig.text(0.5, 0.845, "Each configuration has probability 1/16 in the unrestricted uniform model.",
             ha="center", fontsize=11)
    ax.set(xlim=(-0.55, 4.55), ylim=(-2.65, 7.5))
    ax.axis("off")
    for k, group in enumerate(groups):
        ax.text(k, 7.20, f"k = {k} left", ha="center", weight="bold")
        ax.text(k, 6.70, f"Count {len(group)}; P = {len(group)}/16", ha="center", fontsize=10.5)
        for row, s in enumerate(group):
            y = 5.95 - row * 0.81
            edge = orange if s == "0000" else gray
            ax.add_patch(FancyBboxPatch((k - 0.37, y - 0.29), 0.74, 0.58,
                                       boxstyle="round,pad=0.06", facecolor="white",
                                       edgecolor=edge, linewidth=2 if s == "0000" else 1.0))
            for i, bit in enumerate(s):
                ax.text(k + (i - 1.5) * 0.15, y, bit, ha="center", va="center",
                        color=blue if bit == "0" else orange, fontfamily="monospace", fontsize=15)
        ax.text(k, 0.92, rf"$S/k_B=\ln {len(group)}$", ha="center", fontsize=11)
    ax.plot([-0.43, -0.43, 4.43, 4.43], [6.40, 0.48, 0.48, 6.40],
            color=blue, linewidth=1.6)
    ax.text(2, 0.03, r"Union of all columns: $\Omega=16$, $S/k_B=\ln 16=4\ln 2$", ha="center", color=blue)
    ax.add_patch(FancyBboxPatch((-0.30, -1.79), 1.85, 1.05,
                               boxstyle="round,pad=0.08", facecolor="white", edgecolor=orange, linewidth=1.8))
    ax.text(0.62, -1.03, "Initial restriction: all-left", ha="center", fontsize=11)
    ax.text(0.62, -1.46, r"0000 only: $\Omega=1$, $S=0$", ha="center", fontsize=11)
    ax.annotate("", xy=(2.25, -1.26), xytext=(1.7, -1.26),
                arrowprops={"arrowstyle": "->", "color": blue, "lw": 2})
    ax.text(3.27, -1.00, "Restriction removed: all 16", ha="center", fontsize=11, color=blue)
    ax.text(3.27, -1.48, r"$\Delta S=4k_B\ln2$", ha="center", fontsize=12, color=blue)
    ax.text(2, -2.32, "Balanced occupancy (k = 2) is just six configurations, not the whole allowed set.",
            ha="center", fontsize=11)
    fig.savefig(Path.cwd() / "entropy-two-box-configuration-count.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
