"""Group all length-four binary strings by type; write a PNG to the CWD."""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    strings = ["".join(x) for x in product("01", repeat=4)]
    groups = [[s for s in strings if s.count("1") == k] for k in range(5)]
    assert [len(g) for g in groups] == [1, 4, 6, 4, 1]
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 5.2))
    ax.axis("off")
    ax.text(5, 4.95, "Sixteen strings, five empirical distributions", ha="center", fontsize=17)
    ax.text(5, 4.52, "Every column is one type class; order varies, counts stay fixed", ha="center", fontsize=11)
    for k, group in enumerate(groups):
        left = 0.16 + 1.96 * k
        ax.add_patch(FancyBboxPatch((left, 0.66), 1.8, 3.55,
            boxstyle="round,pad=0.035", facecolor="#eff6fb" if k != 2 else "#e5f4e9",
            edgecolor="#28734b" if k == 2 else "#49718b", linewidth=1.5))
        center = left + 0.9
        ax.text(center, 3.98, f"{k} ones", ha="center", fontsize=12, weight="bold")
        ax.text(center, 3.58, f"q(1) = {k}/4", ha="center", fontsize=11)
        for j, string in enumerate(group):
            ax.text(center, 3.1 - j * 0.34, string, ha="center", fontsize=13,
                family="monospace", color="#184f33" if k == 2 else "#233e52")
        ax.text(center, 0.95, f"{len(group)} string" + ("s" if len(group) != 1 else ""),
            ha="center", fontsize=11, weight="bold")
    ax.text(5, 0.23, "For an independent identically distributed source, strings in one column have equal probability.",
        ha="center", fontsize=10)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
