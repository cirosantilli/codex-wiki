"""Draw the worked knapsack table in cwd; Python 3.14.4 and Matplotlib.

All numerical checks use the standard library. Make invokes this script from
_media, where it writes knapsack-dynamic-programming.png.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


WEIGHTS = (2, 3, 4)
VALUES = (3, 4, 5)
CAPACITY = 5
EXPECTED = ((0, 0, 0, 0, 0, 0), (0, 0, 3, 3, 3, 3),
            (0, 0, 3, 4, 4, 7), (0, 0, 3, 4, 5, 7))
ORANGE = "#b75516"
BLUE = "#225e88"
INK = "#172b3b"


def table(weights, values, capacity):
    rows = [[0] * (capacity + 1)]
    for weight, value in zip(weights, values):
        previous = rows[-1]
        rows.append([max(previous[w], value + previous[w - weight])
                     if w >= weight else previous[w]
                     for w in range(capacity + 1)])
    return rows


def check_example(rows):
    assert tuple(map(tuple, rows)) == EXPECTED
    for i, row in enumerate(rows):
        for capacity, best in enumerate(row):
            candidates = [sum(v * b for v, b in zip(VALUES[:i], bits))
                          for bits in product((0, 1), repeat=i)
                          if sum(w * b for w, b in zip(WEIGHTS[:i], bits)) <= capacity]
            assert best == max(candidates)
    winners = [bits for bits in product((0, 1), repeat=3)
               if sum(w * b for w, b in zip(WEIGHTS, bits)) <= CAPACITY
               and sum(v * b for v, b in zip(VALUES, bits)) == rows[-1][-1]]
    assert winners == [(1, 1, 0)]

    compressed = [0] * (CAPACITY + 1)
    for i, (weight, value) in enumerate(zip(WEIGHTS, VALUES), start=1):
        for w in range(CAPACITY, weight - 1, -1):
            compressed[w] = max(compressed[w], value + compressed[w - weight])
        assert compressed == rows[i]
    ascending = [0] * (CAPACITY + 1)
    for w in range(WEIGHTS[0], CAPACITY + 1):
        ascending[w] = max(ascending[w], VALUES[0] + ascending[w - WEIGHTS[0]])
    assert ascending[4] == 6 > rows[1][4] == 3
    assert table((0, 2), (2, 3), 2) == [[0, 0, 0], [2, 2, 2], [2, 2, 5]]
    assert WEIGHTS[0] + WEIGHTS[1] == CAPACITY
    assert VALUES[0] + VALUES[1] == 7
    assert CAPACITY - WEIGHTS[2] == 1 < min(WEIGHTS)
    print("Verified all 24 table cells by subset enumeration; unique optimum (1,1,0),")
    print("weight 5, value 7; descending updates, ascending reuse, zero-weight base cases.")


def main():
    rows = table(WEIGHTS, VALUES, CAPACITY)
    check_example(rows)
    plt.rcParams.update({"font.size": 13, "text.color": INK})
    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=110, facecolor="white")
    fig.subplots_adjust(left=0.03, right=0.98, top=0.84, bottom=0.07)
    fig.suptitle("0/1 knapsack: each row allows one more item", fontsize=18, y=0.96)
    ax.text(3.5, 5.14, "Weights: 2, 3, 4     Values: 3, 4, 5     Capacity: 5",
            ha="center", fontsize=13)
    ax.text(-1.15, 4.48, "Allowed items", ha="center", fontsize=12)
    ax.text(3.5, 4.78, r"Capacity $W$", ha="center", fontsize=13)
    labels = ("None", "Item 1", "Items 1, 2", "Items 1, 2, 3")
    path = {(3, 5), (2, 5), (1, 2), (0, 0)}
    for w in range(CAPACITY + 1):
        ax.text(w + 1, 4.40, str(w), ha="center", va="center", fontsize=14)
    for i, row in enumerate(rows):
        y = 3.8 - i * 0.77
        ax.text(-1.15, y, labels[i], ha="center", va="center", fontsize=12)
        ax.text(0.05, y, rf"$V_{i}(W)$", ha="center", va="center", fontsize=13)
        for w, value in enumerate(row):
            selected = (i, w) in path
            ax.add_patch(Rectangle((w + 0.58, y - 0.31), 0.84, 0.62,
                                   facecolor="#fff0e5" if selected else "#f2f6f9",
                                   edgecolor=ORANGE if selected else "#b5c5d0",
                                   linewidth=2.3 if selected else 0.8))
            ax.text(w + 1, y, str(value), ha="center", va="center", fontsize=16,
                    color=ORANGE if selected else BLUE, weight="bold" if selected else "normal")
    ax.text(2.7, 0.82, r"$V_2(5)=\max(3,\ 4+3)=7$", ha="center", fontsize=15)
    ax.text(2.7, 0.34, r"$V_3(5)=\max(7,\ 5+0)=7$", ha="center", fontsize=15)
    ax.text(2.7, -0.22, "Recover a selection: skip item 3, take item 2, take item 1",
            ha="center", fontsize=12, color=ORANGE)
    ax.text(2.7, -0.66, "Take weights 3 + 2 = 5; earn values 4 + 3 = 7",
            ha="center", fontsize=13)
    ax.set(xlim=(-2.15, 6.7), ylim=(-1, 5.3))
    ax.axis("off")
    output = Path.cwd() / Path(__file__).with_suffix(".png").name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1100 x 638 pixels, opaque white background.")


if __name__ == "__main__":
    main()
