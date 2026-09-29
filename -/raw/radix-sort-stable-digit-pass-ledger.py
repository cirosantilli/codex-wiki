"""Original LSD radix-sort ledger; run from _media with Python 3.14.

Uses matplotlib 3.10.7. Writes the matching opaque white PNG to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


def stable_pass(records, place, radix=10):
    buckets = [[] for _ in range(radix)]
    for record in records:
        buckets[record[0] // radix**place % radix].append(record)
    return [record for bucket in buckets for record in bucket]


def main():
    records = list(zip([314, 27, 305, 42, 217, 5, 127, 40], "ABCDEFGH"))
    rows = [records]
    for place in range(3):
        rows.append(stable_pass(rows[-1], place))
    assert [r[0] for r in rows[-1]] == sorted(r[0] for r in records)
    for p, row in enumerate(rows[1:], start=1):
        assert [k % 10**p for k, _ in row] == sorted(k % 10**p for k, _ in records)

    fig, ax = plt.subplots(figsize=(10, 6.6), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.02, right=0.99, bottom=0.035, top=0.985)
    ax.set(xlim=(0, 10), ylim=(0, 6.7))
    ax.axis("off")
    ink = "#223349"
    orange, green = "#ffe0ad", "#d7efe7"
    ax.text(0.12, 6.43, "Radix sort: retain each lower-digit ordering", fontsize=19,
            weight="bold", color=ink)
    ax.text(0.12, 6.03, "Eight complete records · decimal keys · width 3", fontsize=12, color=ink)
    labels = ["Input", "1  Units", "2  Tens", "3  Hundreds"]
    for p, row in enumerate(rows):
        y = 5.1 - p * 1.25
        ax.text(0.12, y + 0.21, labels[p], fontsize=13, color=ink, weight="bold")
        for col, (key, label) in enumerate(row):
            x = 1.85 + col * 0.99
            card = FancyBboxPatch((x, y - 0.1), 0.87, 0.77,
                                 boxstyle="round,pad=0.025,rounding_size=0.05",
                                 facecolor="white", edgecolor="#8b9aaa", linewidth=1)
            ax.add_patch(card)
            for pos, char in enumerate(f"{key:03d}"):
                place = 2 - pos
                xx = x + 0.13 + pos * 0.22
                if p and place <= p - 1:
                    ax.add_patch(Rectangle((xx - 0.1, y + 0.23), 0.20, 0.32,
                                           facecolor=orange if place == p - 1 else green,
                                           edgecolor="none"))
                ax.text(xx, y + 0.38, char, fontsize=15, family="monospace",
                        ha="center", va="center", color=ink)
            ax.text(x + 0.435, y + 0.04, f"record {label}", fontsize=10, ha="center", color=ink)
            if p:
                ax.text(x + 0.435, y - 0.40, f"{key % 10**p:0{p}d}",
                        fontsize=12, family="monospace", ha="center", color="#206653")
        if p:
            ax.text(0.12, y - 0.4, "Ordered suffix:", fontsize=10, color="#206653")
    ax.add_patch(Rectangle((0.15, 0.62), 0.21, 0.21, facecolor=orange, edgecolor="none"))
    ax.text(0.43, 0.72, "digit read this pass", fontsize=11, va="center", color=ink)
    ax.add_patch(Rectangle((3.0, 0.62), 0.21, 0.21, facecolor=green, edgecolor="none"))
    ax.text(3.28, 0.72, "lower positions already processed", fontsize=11, va="center", color=ink)
    ax.text(0.15, 0.22, "Units order is not whole-key order: 314 still comes before 305.",
            fontsize=12, color=ink)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
