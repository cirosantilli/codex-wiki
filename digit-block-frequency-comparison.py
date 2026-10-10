"""Exact decimal prefix counts; save the same-basename PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
Reproduce: make _media/digit-block-frequency-comparison.png
The 100,000-digit samples are finite experiments, not normality proofs.
"""

from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter


def champernowne_prefix(length):
    parts = []
    total = 0
    value = 1
    while total < length:
        part = str(value)
        parts.append(part)
        total += len(part)
        value += 1
    return "".join(parts)[:length]


def block_counts(digits, width):
    counts = Counter(digits[i:i + width]
                     for i in range(len(digits) - width + 1))
    return np.array([counts[f"{n:0{width}d}"]
                     for n in range(10 ** width)], dtype=np.int64)


def main():
    length = 100_000
    champernowne = champernowne_prefix(length)
    periodic = "0123456789" * (length // 10)
    singles = [block_counts(s, 1) for s in (champernowne, periodic)]
    pairs = [block_counts(s, 2) for s in (champernowne, periodic)]
    assert singles[0].tolist() == [8642, 19753, 11111] + [8642] * 7
    assert pairs[0][[0, 1, 12, 99]].tolist() == [642, 1753, 2088, 753]
    allowed = [1, 12, 23, 34, 45, 56, 67, 78, 89, 90]
    assert np.flatnonzero(pairs[1]).tolist() == allowed
    assert pairs[1][allowed].tolist() == [10000] * 9 + [9999]
    assert all(c.sum() == length for c in singles)
    assert all(c.sum() == length - 1 for c in pairs)

    blue, orange, ink = "#246f9b", "#b76325", "#233746"
    fig, axes = plt.subplots(2, 2, figsize=(11, 7.2), dpi=110,
                             facecolor="white")
    digit_ax, table_ax, cham_ax, periodic_ax = axes.flat
    digits = np.arange(10)
    digit_ax.bar(digits - 0.19, singles[0] / length, width=0.38,
                 color=blue, label="Champernowne")
    digit_ax.bar(digits + 0.19, singles[1] / length, width=0.38,
                 color=orange, label="Periodic 0123456789")
    digit_ax.axhline(0.1, color=ink, ls="--", lw=1.2)
    digit_ax.set(xticks=digits, xlabel="Digit", ylabel="Count / 100,000",
                 ylim=(0, 0.235), title="Single digits: balance is only one test")
    digit_ax.yaxis.set_major_formatter(PercentFormatter(1))
    digit_ax.legend(loc="upper right", fontsize=9, frameon=False)

    rows = [["0", "8,642", "10,000"], ["1", "19,753", "10,000"],
            ["2", "11,111", "10,000"], ["Each of 3–9", "8,642", "10,000"],
            ["All digits", "100,000", "100,000"],
            ["Adjacent pairs", "99,999", "99,999"]]
    table = table_ax.table(cellText=rows,
                           colLabels=["Count", "Champernowne", "Periodic"],
                           cellLoc="center", colWidths=[0.35, 0.35, 0.3],
                           bbox=[0.02, 0.03, 0.96, 0.9])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d4dfe5")
        cell.set_facecolor("#edf3f7" if row == 0 else "white")
        cell.set_text_props(color=ink)
    table_ax.set_title("Exact integer counts in each prefix")
    table_ax.axis("off")

    for ax, counts, color, title in zip(
            [cham_ax, periodic_ax], pairs, [blue, orange],
            ["Champernowne: all 100 pairs occur",
             "Periodic: exactly 10 of 100 pairs occur"]):
        ax.bar(np.arange(100), counts / (length - 1), width=0.82, color=color)
        ax.axhline(0.01, color=ink, ls="--", lw=1.2,
                   label="Normal base-10 limit: 1/100")
        ax.set(xlim=(-2, 101), ylim=(0, 0.119),
               xticks=np.arange(0, 100, 10),
               xticklabels=[f"{n:02d}" for n in range(0, 100, 10)],
               xlabel="Adjacent pair (00 to 99)", ylabel="Count / 99,999",
               title=title)
        ax.yaxis.set_major_formatter(PercentFormatter(1))
        ax.legend(loc="upper right", fontsize=9, frameon=False)
    for pair in allowed:
        label_x = {89: 87.5, 90: 92}.get(pair, pair)
        periodic_ax.text(label_x, pairs[1][pair] / (length - 1) + 0.002,
                         f"{pair:02d}", ha="center", fontsize=8, color=orange)
    for ax in [digit_ax, cham_ax, periodic_ax]:
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", alpha=0.15)
        ax.set_axisbelow(True)
    fig.suptitle("100,000 decimal digits: finite frequencies, not a normality proof",
                 fontsize=15, y=0.98, color=ink)
    fig.text(0.5, 0.025,
             "Pairs overlap; both lower panels use the same vertical scale."
             "  Dashed lines show 1/10 for digits and 1/100 for pairs.",
             ha="center", fontsize=10, color=ink)
    fig.subplots_adjust(left=0.075, right=0.985, bottom=0.12,
                        top=0.88, hspace=0.48, wspace=0.23)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
