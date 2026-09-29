"""Illustrate hash-value equality versus table-bucket equality on toy keys.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../hash-collision-key-identity.py
Writes this script's basename as an opaque white PNG to the current directory.
Tested with Python 3.14.4, Matplotlib 3.10.7; uses no measured data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    keys = (2, 6, 18)
    hashes = tuple(k % 16 for k in keys)
    buckets = tuple(h % 4 for h in hashes)
    assert hashes == (2, 6, 2) and buckets == (2, 2, 2)
    assert 34 % 16 == 2 and 34 not in keys

    orange, blue, gray = "#b85419", "#23678c", "#586470"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9, 5), dpi=120)
    fig.subplots_adjust(left=0.025, right=0.98, bottom=0.1, top=0.81)
    ax.set(xlim=(0, 10), ylim=(-0.55, 4.1))
    ax.axis("off")
    fig.suptitle("A shared bucket can hide different hash values", fontsize=16, y=0.96)
    fig.text(0.5, 0.885, r"Toy functions: $h(k)=k\;\mathrm{mod}\;16$,   $b(k)=h(k)\;\mathrm{mod}\;4$",
             ha="center", fontsize=13)

    def box(x, y, text, color, width=1.1):
        ax.add_patch(FancyBboxPatch((x-width/2, y-0.25), width, 0.5,
                                   boxstyle="round,pad=0.035", linewidth=1.6,
                                   edgecolor=color, facecolor="white", zorder=3))
        ax.text(x, y, text, ha="center", va="center", color=color, weight="bold", zorder=4)

    def arrow(start, end, color, rad=0):
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15,
                                    linewidth=1.7, color=color,
                                    connectionstyle=f"arc3,rad={rad}", zorder=2))

    for x, title in [(0.9, "Distinct keys"), (4.0, "Hash value"), (7.8, "Table bucket")]:
        ax.text(x, 3.9, title, ha="center", weight="bold")
    for key, y, color in [(2, 3.2, orange), (6, 2.1, blue), (18, 1.0, orange)]:
        box(0.9, y, str(key), color)
        target_y = 2.85 if key != 6 else 1.65
        arrow((1.5, y), (3.4, target_y), color, 0.07 if key == 18 else 0)
    box(4.0, 2.85, "2", orange)
    box(4.0, 1.65, "6", blue)
    box(7.8, 2.2, "2", gray, 1.4)
    arrow((4.6, 2.85), (7.0, 2.28), orange)
    arrow((4.6, 1.65), (7.0, 2.12), blue)
    ax.text(4.0, 0.92, "2 and 18 share h\n6 has a different h", ha="center", color=gray)
    ax.text(7.8, 2.85, "All three share b", ha="center", color=gray)
    arrow((7.8, 1.9), (6.0, 0.63), gray)
    for x, key, color in [(6.0, 2, orange), (7.55, 6, blue), (9.1, 18, orange)]:
        box(x, 0.32, f"key {key}", color, 1.15)
    arrow((6.6, 0.32), (6.93, 0.32), gray)
    arrow((8.15, 0.32), (8.48, 0.32), gray)
    ax.text(7.55, -0.24, "Chaining keeps the original keys", ha="center", fontsize=11, color=gray)
    fig.text(0.5, 0.035, "Same hash or bucket does not prove equal keys. Compare the stored keys.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
