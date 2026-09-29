"""Draw exact memoized Fibonacci lookups and cache lifetime effects.

Run from _media with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def evaluate(n, memo):
    lookups, stores = [], []

    def fib(k):
        hit = k in memo
        lookups.append((k, hit))
        if hit:
            return memo[k]
        value = k if k < 2 else fib(k - 1) + fib(k - 2)
        memo[k] = value
        stores.append(k)
        return value

    value = fib(n)
    return value, lookups, stores


def main():
    memo = {}
    cold = evaluate(5, memo)
    assert cold == (5, [(5, False), (4, False), (3, False), (2, False), (1, False),
                        (0, False), (1, True), (2, True), (3, True)], [1, 0, 2, 3, 4, 5])
    records = [("F(5), empty cache", cold, "0–5")]
    records.append(("F(5), retain cache", evaluate(5, memo), "0–5"))
    records.append(("F(6), retain cache", evaluate(6, memo), "0–6"))
    memo.clear()
    records.append(("Clear; F(5) again", evaluate(5, memo), "0–5"))
    fig, ax = plt.subplots(figsize=(11, 5.7), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(-0.7, 8.7), ylim=(-4.55, 1.6))
    ax.axis("off")
    ax.text(4, 1.15, "Lookup order for F(5), starting empty", ha="center", fontsize=17)
    for i, (n, hit) in enumerate(cold[1]):
        fill = "#b9e5df" if hit else "#ffe0a7"
        ax.add_patch(FancyBboxPatch((i - 0.38, -0.1), 0.76, 0.8,
                                   boxstyle="round,pad=0.04", facecolor=fill,
                                   edgecolor="#37434e", lw=1))
        ax.text(i, 0.44, f"F({n})", ha="center", fontsize=12)
        ax.text(i, 0.07, "HIT" if hit else "MISS", ha="center", fontsize=10)
    ax.text(4, -0.55, "9 wrapper calls = 6 body evaluations + 3 reused answers",
            ha="center", fontsize=12)
    ax.text(4, -0.95, "Store on return: 1 → 0 → 2 → 3 → 4 → 5  (arguments, not values)",
            ha="center", fontsize=11, color="#37434e")
    columns = ["Next request / action", "Value", "Calls", "Bodies", "Hits", "Stored keys"]
    data = []
    for name, (value, lookups, stores), keys in records:
        hits = sum(hit for _, hit in lookups)
        data.append([name, value, len(lookups), len(stores), hits, keys])
    table = ax.table(cellText=data, colLabels=columns, cellLoc="center",
                     colWidths=[0.32, 0.10, 0.11, 0.11, 0.10, 0.16],
                     bbox=[0.02, 0.10, 0.96, 0.39])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#aab5bf")
        cell.set_facecolor("#e5ecf0" if row == 0 else "white")
        if row == 0:
            cell.set_text_props(weight="bold")
    ax.text(4, -4.45, "Sequential calls • cache every completed value • no eviction • left child first",
            ha="center", fontsize=11, color="#37434e")
    fig.subplots_adjust(left=0.025, right=0.975, top=0.96, bottom=0.03)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
