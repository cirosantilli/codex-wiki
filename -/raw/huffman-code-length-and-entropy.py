"""Original weighted-length and entropy comparison; save PNG basename to cwd.

Tested with Python 3.14.4 and Matplotlib 3.10.7 (repository dependencies).
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-mpl python3 ../huffman-code-length-and-entropy.py
"""

from fractions import Fraction
from math import log2
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    probabilities = list(map(Fraction, ("0.4", "0.3", "0.2", "0.1")))
    codes = ["0", "10", "110", "111"]
    lengths = list(map(len, codes))
    weighted = [p * length for p, length in zip(probabilities, lengths)]
    mean = sum(weighted)
    entropy = -sum(float(p) * log2(float(p)) for p in probabilities)
    assert mean == Fraction(19, 10)
    assert sum(Fraction(1, 2**length) for length in lengths) == 1
    assert abs(entropy - 1.8464393446710154) < 1e-12
    colors = ["#2d6faa", "#168475", "#b16813", "#9059a0"]
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained", facecolor="white")
    left.bar(range(4), list(map(float, weighted)), color=colors, width=0.65)
    for i, (p, length, contribution) in enumerate(zip(probabilities, lengths, weighted)):
        left.text(i, float(contribution) + 0.023, f"{float(p):.1f} × {length} = {float(contribution):.1f}", ha="center", fontsize=10)
    left.set(xticks=range(4), xticklabels=[f"{s}: {c}" for s, c in zip("ABCD", codes)],
             ylim=(0, 0.80), ylabel="Contribution to mean (bits per source symbol)",
             title="Weight each codeword length by its probability")
    left.text(0.5, 0.91, "0.4 + 0.6 + 0.6 + 0.3 = 1.9", transform=left.transAxes, ha="center", fontsize=12)
    values = [entropy, float(mean), 2.0]
    right.bar(range(3), values, color=["#93a3b5", "#168475", "#2d6faa"], width=0.60)
    for i, value in enumerate(values):
        right.text(i, value + 0.045, f"{value:.6f}" if i == 0 else f"{value:.1f}", ha="center", fontsize=12)
    right.set(xticks=range(3), xticklabels=["Entropy\nlower bound", "Huffman\nmean", "Fixed\nlength"],
              ylim=(0, 2.40), ylabel="Bits per source symbol", title="Compare the mean with its limits")
    for ax in (left, right):
        ax.set_facecolor("white")
        ax.set_axisbelow(True)
        ax.grid(axis="y", alpha=0.22)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Huffman saves 5% of the fixed-length payload on average", fontsize=14)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
