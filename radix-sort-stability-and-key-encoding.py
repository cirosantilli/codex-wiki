"""Original stability and order-preserving encoding diagram.

Python 3.14, matplotlib 3.10.7; run from _media to emit its basename PNG.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, x, y, text, color, width=2.0):
    ax.add_patch(FancyBboxPatch((x, y), width, 0.60,
                              boxstyle="round,pad=0.04,rounding_size=0.06",
                              edgecolor=color, facecolor="white", linewidth=1.5))
    ax.text(x + width / 2, y + 0.30, text, ha="center", va="center",
            fontsize=13, family="monospace", color=color)


def arrow(ax, start, end, color):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color=color, lw=1.5))


def main():
    signed = [-8, -3, -1, 0, 4, 7]
    words = ["", "a", "aa", "ab", "b"]
    encoded = ["".join(str({"a": 1, "b": 2}[c]) for c in w).ljust(3, "0") for w in words]
    assert encoded == ["000", "100", "110", "120", "200"]
    assert [int(s, 3) for s in encoded] == sorted(int(s, 3) for s in encoded)

    fig, ax = plt.subplots(figsize=(10, 7.4), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.025, right=0.99, bottom=0.035, top=0.98)
    ax.set(xlim=(0, 10), ylim=(0, 7.5))
    ax.axis("off")
    ink, good, bad = "#223349", "#21755e", "#af4935"
    ax.text(0.1, 7.16, "Two things a radix sort must preserve", fontsize=19,
            weight="bold", color=ink)
    ax.text(0.1, 6.68, "1  Stable ties retain the lower-digit order", fontsize=14,
            weight="bold", color=ink)
    box(ax, 0.15, 5.71, "042 A | 041 B", ink, 2.60)
    ax.text(1.45, 5.46, "input", fontsize=11, ha="center", color=ink)
    arrow(ax, (2.82, 6.01), (3.46, 6.01), ink)
    ax.text(3.12, 6.22, "units", fontsize=11, ha="center", color=ink)
    box(ax, 3.5, 5.71, "041 B | 042 A", ink, 2.60)
    ax.text(4.8, 5.46, "units ordered: 1 < 2", fontsize=11, ha="center", color=ink)
    arrow(ax, (6.15, 6.05), (6.86, 6.31), good)
    arrow(ax, (6.15, 5.96), (6.86, 5.29), bad)
    box(ax, 6.95, 6.01, "041 B | 042 A", good, 2.60)
    box(ax, 6.95, 4.99, "042 A | 041 B", bad, 2.60)
    ax.text(8.25, 6.75, "stable tens tie", fontsize=11, color=good, ha="center")
    ax.text(8.25, 4.73, "unstable tens tie", fontsize=11, color=bad, ha="center")
    ax.text(0.15, 4.43, "Both tens digits are 4. A final stable hundreds pass sees only zeros:",
            fontsize=12, color=ink)
    ax.text(0.15, 4.09, "it retains either result, including the incorrect order 42, 41.",
            fontsize=12, color=ink)
    ax.plot([0.1, 9.75], [3.76, 3.76], color="#bcc6d0", linewidth=1)
    ax.text(0.1, 3.36, "2  Encoded order must match the intended order", fontsize=14,
            weight="bold", color=ink)
    ax.text(0.15, 2.91, "Signed integers: add 8; then use four binary digits", fontsize=12, color=ink)
    for i, x in enumerate(signed):
        xx = 1.0 + i * 1.48
        ax.text(xx, 2.49, str(x).replace("-", "−"), fontsize=13, color=ink, ha="center")
        arrow(ax, (xx, 2.3), (xx, 2.02), good)
        ax.text(xx, 1.78, f"{x + 8:04b}", family="monospace", fontsize=13, color=good, ha="center")
    ax.text(0.15, 1.34, "Strings: a = 1, b = 2; append reserved end-marker zeros", fontsize=12, color=ink)
    for i, (word, code) in enumerate(zip(words, encoded)):
        xx = 1.10 + i * 1.84
        ax.text(xx, 0.92, word or "empty", fontsize=13, color=ink, ha="center")
        ax.text(xx, 0.47, code, family="monospace", fontsize=13, color=good, ha="center")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
