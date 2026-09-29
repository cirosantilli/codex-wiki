"""Draw deterministic bucket reassignment and a counterexample to dispersion.

Writes a PNG with this script's basename to CWD. Tested with Python 3.14,
matplotlib 3.10.7, and numpy 2.3.5; run from _media with MPLBACKEND=Agg.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    keys = [1, 5, 9, 2]
    layouts = {m: [[k for k in reversed(keys) if k % m == i] for i in range(m)]
               for m in [4, 8]}
    assert layouts[4] == [[], [9, 5, 1], [2], []]
    assert layouts[8] == [[], [9, 1], [2], [], [], [5], [], []]
    stubborn = [1, 9, 17, 25]
    assert all(k % m == 1 for k in stubborn for m in [4, 8])

    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=110)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set(xlim=(0, 10), ylim=(0, 6.5))
    ax.axis("off")
    ax.text(5, 6.16, "Resizing changes bucket indices, not key equality",
            ha="center", fontsize=17, weight="bold")
    ax.text(5, 5.75, "Constructed model • hₘ(k) = k mod m • the same four keys are retained",
            ha="center", fontsize=12)
    colors = {1: "#deedfa", 5: "#fff0ce", 9: "#deedfa", 2: "#e4f2e4"}
    for x, m in [(0.7, 4), (5.8, 8)]:
        ax.text(x + 1.55, 5.25, f"m = {m}, n = 4, α = {4 / m:g}", ha="center",
                fontsize=15, weight="bold")
        for i, chain in enumerate(layouts[m]):
            y = 4.66 - i * 0.4
            ax.text(x, y + 0.12, str(i), ha="center", va="center", fontsize=12)
            ax.add_patch(FancyBboxPatch((x + 0.22, y - 0.04), 0.36, 0.3,
                                      boxstyle="round,pad=0.02", facecolor="#f3f5f7",
                                      edgecolor="#6d8193"))
            if not chain:
                ax.text(x + 0.84, y + 0.12, "empty", va="center", fontsize=11,
                        color="#77828c")
            for j, k in enumerate(chain):
                start = x + 0.91 + j * 0.82
                ax.annotate("", xy=(start - 0.035, y + 0.12),
                            xytext=(x + 0.6 if j == 0 else start - 0.31, y + 0.12),
                            arrowprops=dict(arrowstyle="->", color="#35516b", lw=1.2))
                ax.add_patch(FancyBboxPatch((start, y - 0.04), 0.48, 0.3,
                                          boxstyle="round,pad=0.02", facecolor=colors[k],
                                          edgecolor="#35516b"))
                ax.text(start + 0.24, y + 0.12, str(k), ha="center", va="center", fontsize=12)
    ax.annotate("", xy=(5.32, 4.1), xytext=(4.08, 4.1),
                arrowprops=dict(arrowstyle="->", color="#35516b", lw=2))
    ax.text(4.7, 4.53, "recompute\nevery index", ha="center", fontsize=11)
    ax.text(2.45, 2.48, "5 moves to bucket 5.\n1 and 9 still collide in bucket 1.",
            ha="center", fontsize=12, linespacing=1.5)
    ax.plot([0.5, 9.5], [1.38, 1.38], color="#c1cdd7")
    ax.text(5, 1.05, "Counterexample: keys 1, 9, 17, 25 all remain in bucket 1",
            ha="center", fontsize=14, weight="bold")
    ax.text(5, 0.68, "mod 4:  [25 → 17 → 9 → 1]       mod 8:  [25 → 17 → 9 → 1]",
            ha="center", fontsize=13)
    ax.text(5, 0.25, "Doubling halves α here, but does not guarantee shorter chains.",
            ha="center", fontsize=12)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
