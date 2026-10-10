"""Draw an original four-matrix DP table and its split certificate.

Tested with Python 3.14, matplotlib 3.10.7; emit PNG in the CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def chain_table(p):
    n = len(p) - 1
    costs, splits = {}, {}
    for i in range(1, n + 1):
        costs[i, i] = 0
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            candidates = [(costs[i, k] + costs[k + 1, j] + p[i - 1] * p[k] * p[j], k)
                          for k in range(i, j)]
            costs[i, j], splits[i, j] = min(candidates)
    return costs, splits


def main():
    costs, splits = chain_table([12, 5, 40, 3, 15])
    fig = plt.figure(figsize=(11.8, 7.2), dpi=100, facecolor="white")
    fig.suptitle("Four matrices: costs and an optimal grouping", fontsize=20, y=0.96)
    fig.text(0.5, 0.88, "A: 12 × 5     B: 5 × 40     C: 40 × 3     D: 3 × 15", ha="center", fontsize=14)
    orange, ink = "#b25916", "#263e50"
    table_ax = fig.add_axes([0.05, 0.30, 0.40, 0.46])
    table_ax.set_xlim(-0.6, 4)
    table_ax.set_ylim(-0.1, 4.6)
    table_ax.axis("off")
    table_ax.text(1.7, 4.5, "Minimum costs m[i, j]", ha="center", fontsize=16, color=ink)
    active = {(1, 4), (1, 3), (2, 3)}
    for i in range(1, 5):
        table_ax.text(-0.34, 4 - i + 0.45, str(i), ha="center", va="center", fontsize=14)
        table_ax.text(i - 0.5, 4.13, str(i), ha="center", va="center", fontsize=14)
        for j in range(1, 5):
            x, y = j - 1, 4 - i
            used = (i, j) in active
            face = "#fff0df" if used else ("#edf3f7" if i <= j else "#f6f6f6")
            table_ax.add_patch(Rectangle((x, y), 1, 0.9, facecolor=face,
                                         edgecolor=orange if used else "#aab7bf", linewidth=2 if used else 1))
            table_ax.text(x + 0.5, y + 0.45, str(costs[i, j]) if i <= j else "—",
                          ha="center", va="center", fontsize=16, color=orange if used else ink)
    table_ax.text(-0.34, 4.13, "i / j", ha="center", fontsize=11)
    fig.text(0.24, 0.265, "Fill by increasing interval length.\nOrange: nonsingleton intervals in the optimum.",
             ha="center", fontsize=12, color=ink)

    tree_ax = fig.add_axes([0.50, 0.30, 0.46, 0.46])
    tree_ax.set_xlim(0, 1)
    tree_ax.set_ylim(-0.06, 1.13)
    tree_ax.axis("off")
    tree_ax.text(0.5, 1.12, "Follow both children at each split", ha="center", fontsize=16, color=ink)
    positions = {(1, 4): (0.63, 0.94), (1, 3): (0.38, 0.62), (2, 3): (0.49, 0.30),
                 (1, 1): (0.07, 0.01), (2, 2): (0.34, 0.01), (3, 3): (0.64, 0.01), (4, 4): (0.91, 0.01)}
    for interval in active:
        i, j = interval
        k = splits[interval]
        for child in [(i, k), (k + 1, j)]:
            start, end = positions[interval], positions[child]
            tree_ax.plot([start[0], end[0]], [start[1], end[1]], color=orange, linewidth=1.8, zorder=1)
    for (i, j), (x, y) in positions.items():
        if i == j:
            label = f"{'ABCD'[i - 1]}\nstop: i = j"
        else:
            label = f"[{i}, {j}]: cost {costs[i, j]}\nsplit k = {splits[i, j]}"
        tree_ax.text(x, y, label, ha="center", va="center", fontsize=11.5,
                     bbox=dict(boxstyle="round,pad=0.45", facecolor="white" if i == j else "#fff0df",
                               edgecolor=ink if i == j else orange, linewidth=1.4), zorder=3)

    fig.text(0.05, 0.17, "Final candidates:", fontsize=13, color=ink)
    for x, k, cost in [(0.28, 1, 1725), (0.53, 2, 11400), (0.78, 3, 1320)]:
        fig.text(x, 0.17, f"k = {k}:  {cost}", fontsize=14, color=orange if k == 3 else ink,
                 bbox=dict(facecolor="#fff0df" if k == 3 else "white", edgecolor=orange if k == 3 else "none", pad=5))
    fig.text(0.5, 0.09, "Recovered grouping: (A(BC))D       600 + 180 + 540 = 1320", ha="center", fontsize=16, color=orange)
    fig.text(0.5, 0.03, "Original dimension example; counts scalar multiplications, not elapsed time.", ha="center", fontsize=11, color=ink)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
