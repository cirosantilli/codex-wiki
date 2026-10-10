"""Draw verified modulo-seven buckets and the records retained by chaining.

Generate with: make _media/hash-bucket-collisions.png
Writes an opaque white PNG with this basename to the current directory.
Tested with Python 3.14.4 and Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    keys = [0, 2, 3, 10, 11, 17, 24]
    buckets = [[] for _ in range(7)]
    for key in keys:
        buckets[key % 7].append(key)
    assert [key % 7 for key in keys] == [0, 2, 3, 3, 4, 3, 3]
    assert buckets[3] == [3, 10, 17, 24]
    assert sorted(key for bucket in buckets for key in bucket) == sorted(keys)
    assert 10 in buckets[10 % 7] and 31 not in buckets[31 % 7]
    assert 31 % 7 == 3

    blue, orange, gray = "#246b9c", "#b95122", "#62717d"
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.0, 5.2), dpi=120)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.83, bottom=0.15)
    ax.set(xlim=(0, 10), ylim=(-0.65, 7.25))
    ax.axis("off")
    fig.suptitle(r"Same bucket does not mean same key: $h(k)=k\;\mathrm{mod}\;7$",
                 fontsize=16, y=0.96)
    ax.text(0.9, 7.0, "Stored keys", ha="center", weight="bold")
    ax.text(4.2, 7.0, "Bucket", ha="center", weight="bold")
    ax.text(7.3, 7.0, "Records kept by chaining", ha="center", weight="bold")

    def box(x, y, label, color, width=0.65):
        patch = FancyBboxPatch((x - width / 2, y - 0.27), width, 0.54,
                               boxstyle="round,pad=0.04", linewidth=1.5,
                               edgecolor=color, facecolor="white", zorder=3)
        ax.add_patch(patch)
        ax.text(x, y, str(label), ha="center", va="center", color=color,
                weight="bold", zorder=4)

    for row, key in enumerate(keys):
        y = 6 - row
        bucket = key % 7
        color = orange if bucket == 3 else blue
        box(0.9, y, key, color)
        ax.add_patch(FancyArrowPatch((1.35, y), (3.8, 6 - bucket),
                                    arrowstyle="->", mutation_scale=12,
                                    linewidth=1.4, color=color, alpha=0.78))

    for index, chain in enumerate(buckets):
        y = 6 - index
        color = orange if index == 3 else blue
        box(4.2, y, index, color)
        if not chain:
            ax.text(5.45, y, "empty", ha="center", va="center", color=gray,
                    fontsize=11)
            continue
        previous = 4.2
        for column, key in enumerate(chain):
            x = 5.45 + 1.2 * column
            box(x, y, key, color)
            ax.add_patch(FancyArrowPatch((previous + 0.4, y), (x - 0.4, y),
                                        arrowstyle="->", mutation_scale=11,
                                        linewidth=1.3, color=color))
            previous = x

    fig.text(0.5, 0.085, "Find 10: bucket 3, compare 3 then 10; keep both records.",
             ha="center", fontsize=12)
    fig.text(0.5, 0.035, "Find 31: bucket 3, compare all four keys, report absent.",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "hash-bucket-collisions.png", transparent=False)
    plt.close(fig)
    print(f"Bucket counts: {[len(bucket) for bucket in buckets]}; "
          "10 found after 2 comparisons; 31 absent after 4 comparisons")


if __name__ == "__main__":
    main()
