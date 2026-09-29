"""Draw exact decoding of a known three-entry tuple; write PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media to place the generated image beside the other wiki media.
"""

from math import isqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def unpair(z):
    s = (isqrt(8 * z + 1) - 1) // 2
    y = z - s * (s + 1) // 2
    return s - y, y


def main():
    code = 257
    inner, last = unpair(code)
    first, second = unpair(inner)
    assert (inner, last, first, second) == (18, 4, 2, 3)
    fig, ax = plt.subplots(figsize=(7.5, 3.6), facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 4))
    ax.axis("off")
    fig.suptitle("Decode a known three-entry tuple", fontsize=15, y=0.96)
    boxes = [(0.3, 1.9, 1.6, str(code)),
             (3.0, 1.9, 2.4, f"({inner}, {last})"),
             (6.55, 1.9, 3.1, f"(({first}, {second}), {last})")]
    for x, y, width, text in boxes:
        ax.add_patch(FancyBboxPatch((x, y), width, 0.8, boxstyle="round,pad=0.06",
                                   linewidth=1.6, edgecolor="#2a6398", facecolor="#edf4fa"))
        ax.text(x + width / 2, y + 0.4, text, ha="center", va="center",
                fontsize=20, color="#183b56")
    for start, end in [(1.98, 2.91), (5.48, 6.46)]:
        ax.add_patch(FancyArrowPatch((start, 2.3), (end, 2.3), arrowstyle="-|>",
                                    mutation_scale=20, linewidth=1.8, color="#2a6398"))
    ax.text(2.45, 3.12, "Unpair 257", ha="center", fontsize=11, weight="bold")
    ax.text(5.98, 3.12, "Unpair 18", ha="center", fontsize=11, weight="bold")
    ax.text(2.6, 1.18, "T(22) = 253 ≤ 257 < 276 = T(23)\ny = 257 − 253 = 4;  x = 22 − 4 = 18",
            ha="center", fontsize=10, linespacing=1.65)
    ax.text(7.65, 1.18, "T(5) = 15 ≤ 18 < 21 = T(6)\ny = 18 − 15 = 3;  x = 5 − 3 = 2",
            ha="center", fontsize=10, linespacing=1.65)
    ax.text(5, 0.25, "Read as (2, 3, 4) with the agreed length and left-nesting convention.",
            ha="center", fontsize=11, color="#183b56")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.86, bottom=0.04)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
