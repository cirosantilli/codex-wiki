"""Draw labelled-bin encodings; tested with Python 3.14.4, matplotlib 3.10.7.

Write stars-and-bars-three-bin-allocation.png in the current directory.
"""

from itertools import combinations, product
from math import comb
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def encode(counts):
    return "|".join("•" * count for count in counts)


def main():
    weak = {counts for counts in product(range(6), repeat=3) if sum(counts) == 5}
    positive = {counts for counts in weak if min(counts) >= 1}
    strings = {"".join("|" if i in bars else "•" for i in range(7))
               for bars in combinations(range(7), 2)}
    assert len(weak) == comb(7, 2) == 21
    assert len(positive) == comb(4, 2) == 6
    assert {encode(counts) for counts in weak} == strings
    assert {tuple(x - 1 for x in counts) for counts in positive} == {
        counts for counts in product(range(3), repeat=3) if sum(counts) == 2}
    rows = [((2, 1, 2), "Ordinary split"),
            ((2, 0, 3), "Adjacent bars: second bin empty"),
            ((0, 2, 3), "Left end bar: first bin empty"),
            ((2, 3, 0), "Right end bar: third bin empty")]
    colors = ["#186c9c", "#b85b19", "#34815c"]
    fig, ax = plt.subplots(figsize=(9, 5.9), dpi=120, facecolor="white")
    ax.set(xlim=(-0.6, 13), ylim=(-0.95, 7.4))
    ax.axis("off")
    for row, (counts, description) in enumerate(rows):
        y = 6 - 1.7 * row
        ax.text(-0.3, y + 0.65, description, fontsize=11, color="#253746")
        bin_index = 0
        for pos, symbol in enumerate(encode(counts)):
            if symbol == "|":
                ax.plot([pos, pos], [y - 0.25, y + 0.25],
                        color="#253746", linewidth=2.3)
                bin_index += 1
            else:
                ax.scatter(pos, y, s=110, color=colors[bin_index], zorder=3)
        ax.text(7.15, y, "→", fontsize=20, va="center", color="#253746")
        for bin_index, count in enumerate(counts):
            ax.text(8.3 + 1.7 * bin_index, y, str(count), ha="center", va="center",
                    fontsize=18, color=colors[bin_index])
    for bin_index, label in enumerate(["First bin", "Second bin", "Third bin"]):
        ax.text(8.3 + 1.7 * bin_index, 7.1, label, ha="center",
                fontsize=10, color=colors[bin_index])
    fig.suptitle("Five identical objects, three labelled bins", fontsize=16, y=0.98)
    fig.text(0.5, 0.025, "21 nonnegative count tuples; 6 positive count tuples. Two bars delimit three bins.",
             ha="center", fontsize=11, color="#253746")
    fig.subplots_adjust(left=0.04, right=0.99, bottom=0.09, top=0.90)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Verified {len(weak)} nonnegative and {len(positive)} positive tuples; "
          "bar-position enumeration and positive shifts agree.")


if __name__ == "__main__":
    main()
