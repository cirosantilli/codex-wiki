"""Original weak/strict subsequence trace; no measured data.

Tested with Python 3.14.4 and matplotlib 3.10.7. Run from _media:
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../increasing-subsequence-dp-witness.py
The opaque PNG is written to the current working directory.
"""

from itertools import combinations
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


INPUT = (4, 1, 3, 2, 2, 5, 0)
TEAL, ORANGE, INK = "#007f86", "#b65716", "#203044"


def ending_dp(values, strict=False):
    lengths, parents = [], []
    for i, value in enumerate(values):
        eligible = [j for j in range(i)
                    if (values[j] < value if strict else values[j] <= value)]
        parent = max(eligible, key=lambda j: lengths[j]) if eligible else None
        lengths.append(1 if parent is None else lengths[parent] + 1)
        parents.append(parent)
    if not values:
        return lengths, parents, []
    last = max(range(len(values)), key=lambda j: lengths[j])
    witness = []
    while last is not None:
        witness.append(last + 1)
        last = parents[last]
    return lengths, parents, witness[::-1]


def enumerate_endings(values, strict=False):
    """Independent oracle: enumerate all index subsets, without a recurrence."""
    best = [0] * len(values)
    valid_count = 0
    for size in range(1, len(values) + 1):
        for indices in combinations(range(len(values)), size):
            selected = [values[j] for j in indices]
            valid = all(a < b if strict else a <= b
                        for a, b in zip(selected, selected[1:]))
            if valid:
                valid_count += 1
                best[indices[-1]] = max(best[indices[-1]], size)
    return best, valid_count


def main():
    results = {}
    for strict in (False, True):
        lengths, parents, witness = ending_dp(INPUT, strict)
        prefix_counts = []
        for stop in range(len(INPUT) + 1):
            oracle, count = enumerate_endings(INPUT[:stop], strict)
            assert ending_dp(INPUT[:stop], strict)[0] == oracle
            prefix_counts.append(count)
        assert len(witness) == max(lengths)
        assert witness == sorted(set(witness))
        assert all(INPUT[a-1] < INPUT[b-1] if strict else INPUT[a-1] <= INPUT[b-1]
                   for a, b in zip(witness, witness[1:]))
        results["strict" if strict else "weak"] = dict(
            lengths=lengths, parents=[None if j is None else j+1 for j in parents],
            witness_indices=witness, valid_subsequences_by_prefix=prefix_counts)

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                         "text.color": INK, "axes.labelcolor": INK,
                         "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(9.6, 7.0), dpi=100, facecolor="white")
    fig.suptitle("An increasing subsequence can skip positions", fontsize=19,
                 fontweight="bold", x=.5, y=.965)
    fig.text(.5, .915, "Exact toy input: (4, 1, 3, 2, 2, 5, 0) · not measured data",
             ha="center", fontsize=12)
    ax = fig.add_axes((.10, .50, .84, .34))
    ax.plot(range(1, 8), INPUT, color="#d5dce1", lw=1.5, zorder=1)
    ax.scatter(range(1, 8), INPUT, color="#85929e", s=95, zorder=3)
    witness = results["weak"]["witness_indices"]
    for a, b in zip(witness, witness[1:]):
        ax.add_patch(FancyArrowPatch((a, INPUT[a-1]), (b, INPUT[b-1]),
                     arrowstyle="-|>", mutation_scale=19, color=TEAL, lw=3,
                     shrinkA=10, shrinkB=10, zorder=4))
    ax.scatter(witness, [INPUT[i-1] for i in witness], color=TEAL, s=140, zorder=5)
    for i, value in enumerate(INPUT, 1):
        ax.annotate(str(value), (i, value), xytext=(0, 12),
                    textcoords="offset points", ha="center", fontsize=13,
                    fontweight="bold", color=TEAL if i in witness else INK)
    ax.text(4.5, 3.7, "equal values allowed", color=TEAL, ha="center", fontsize=12)
    ax.set(xlim=(.6, 7.4), ylim=(-.6, 6.2), xticks=range(1, 8), yticks=range(6),
           xlabel="Input index i (order is preserved)", ylabel="Value xᵢ")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e9edf1")

    ax_table = fig.add_axes((.08, .13, .86, .25))
    ax_table.axis("off")
    weak, strict = results["weak"], results["strict"]
    rows = [list(range(1, 8)), list(INPUT), weak["lengths"], strict["lengths"]]
    table = ax_table.table(cellText=rows,
                           rowLabels=["index i", "value xᵢ", "weak dᵢ (≤)", "strict dᵢ (<)"],
                           cellLoc="center", rowLoc="right", bbox=(.16, .13, .84, .87))
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#d2dbe1")
        cell.set_facecolor("white")
        if row == 2:
            cell.get_text().set_color(TEAL)
            if col >= 0 and col+1 in witness:
                cell.set_facecolor("#e1f3f2")
        if row == 3:
            cell.get_text().set_color(ORANGE)
    fig.text(.5, .405, "Lengths ending at each index (the last entry need not be optimal)",
             ha="center", fontsize=12, fontweight="bold")
    fig.text(.5, .104, "Weak reconstruction: 6 → 5 → 4 → 2, then reverse", ha="center", color=TEAL)
    fig.text(.5, .060, "Weak optimum: (1, 2, 2, 5), length 4   |   Strict optimum: (1, 3, 5), length 3",
             ha="center", fontsize=12)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": output.name, "input": INPUT, "checks": results}))


if __name__ == "__main__":
    main()
