"""Original exact minimum-tail traces, including duplicate and witness pitfalls.

Tested with Python 3.14.4 and matplotlib 3.10.7. Run from _media:
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../increasing-subsequence-tails-trace.py
The opaque PNG is written to the current working directory.
"""

from bisect import bisect_left, bisect_right
from itertools import combinations
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


INPUT = (4, 1, 3, 2, 2, 5, 0)
TEAL, ORANGE, INK = "#007f86", "#b65716", "#203044"


def tail_trace(values, strict=False):
    tails, suppliers, parents, rows = [], [], [], []
    search = bisect_left if strict else bisect_right
    for i, value in enumerate(values, 1):
        slot = search(tails, value)
        parents.append(suppliers[slot-1] if slot else None)
        if slot == len(tails):
            tails.append(value)
            suppliers.append(i)
        else:
            tails[slot], suppliers[slot] = value, i
        rows.append(dict(index=i, value=value, slot=slot+1,
                         tails=tails.copy(), suppliers=suppliers.copy()))
    last = suppliers[-1] if suppliers else None
    witness = []
    while last is not None:
        witness.append(last)
        last = parents[last-1]
    return rows, parents, witness[::-1]


def enumerate_minimum_endings(values, strict=False):
    """Independent oracle: enumerate subsets and minimize their final values."""
    minima = []
    for size in range(1, len(values) + 1):
        ends = []
        for indices in combinations(range(len(values)), size):
            selected = [values[j] for j in indices]
            if all(a < b if strict else a <= b for a, b in zip(selected, selected[1:])):
                ends.append(selected[-1])
        if not ends:
            break
        minima.append(min(ends))
    return minima


def draw_panel(ax, rows, strict):
    color = ORANGE if strict else TEAL
    ax.set(xlim=(-.1, 6.1), ylim=(-1.6, 9.3))
    ax.axis("off")
    ax.text(3, 8.9, "Strict: replace first tail ≥ v" if strict else "Weak: replace first tail > v",
            color=color, ha="center", fontsize=14, fontweight="bold")
    labels = ["i", "v", "T₁", "T₂", "T₃", "T₄"]
    for col, label in enumerate(labels):
        ax.text(col+.5, 8.15, label, ha="center", va="center", fontsize=13, fontweight="bold")
    for row in rows:
        y = 7.35 - row["index"]
        ax.text(.5, y+.45, str(row["index"]), ha="center", va="center")
        ax.text(1.5, y+.45, str(row["value"]), ha="center", va="center", fontweight="bold")
        for slot in range(4):
            updated = slot+1 == row["slot"]
            present = slot < len(row["tails"])
            fill = ("#fff0e2" if strict else "#e1f3f2") if updated else "white"
            ax.add_patch(Rectangle((slot+2+.05, y+.03), .9, .84,
                         facecolor=fill, edgecolor=color if updated else "#d2dbe1",
                         lw=2 if updated else .8))
            text = f'{row["tails"][slot]}\n(i={row["suppliers"][slot]})' if present else "—"
            ax.text(slot+2+.5, y+.45, text, ha="center", va="center", fontsize=11,
                    color=color if updated else INK, linespacing=1.5)
    ax.text(3, -.75, "Final length: 3" if strict else "Final length: 4", ha="center",
            fontsize=14, color=color, fontweight="bold")


def main():
    results = {}
    for strict in (False, True):
        rows, parents, witness = tail_trace(INPUT, strict)
        assert enumerate_minimum_endings((), strict) == []
        for row in rows:
            assert row["tails"] == enumerate_minimum_endings(INPUT[:row["index"]], strict)
        assert len(witness) == len(rows[-1]["tails"])
        assert witness == sorted(set(witness))
        assert all(INPUT[a-1] < INPUT[b-1] if strict else INPUT[a-1] <= INPUT[b-1]
                   for a, b in zip(witness, witness[1:]))
        results["strict" if strict else "weak"] = dict(
            rows=rows, parents=parents, witness_indices=witness)
    assert results["weak"]["rows"][-1]["suppliers"] == [7, 4, 5, 6]
    assert results["strict"]["rows"][-1]["suppliers"] == [7, 5, 6]
    assert results["weak"]["witness_indices"] == [2, 4, 5, 6]

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                         "text.color": INK, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(10.4, 7.4), dpi=100, facecolor="white")
    fig.suptitle("Smallest endings summarize many different subsequences", fontsize=18,
                 fontweight="bold", y=.965)
    fig.text(.5, .914, "Exact toy input: (4, 1, 3, 2, 2, 5, 0) · not measured data",
             ha="center", fontsize=12)
    draw_panel(fig.add_axes((.035, .23, .445, .65)), results["weak"]["rows"], False)
    draw_panel(fig.add_axes((.52, .23, .445, .65)), results["strict"]["rows"], True)
    fig.text(.5, .235, "Outlined cell = replacement or append.  i in parentheses = supplier index.",
             ha="center", fontsize=12)
    fig.text(.5, .171, "Weak final tail values: (0, 2, 2, 5)    supplier indices: (7, 4, 5, 6)",
             ha="center", fontsize=13, fontweight="bold", color=TEAL)
    fig.text(.5, .122, "7 → 4 runs backward in the input: this table is not a subsequence.",
             ha="center", fontsize=13, color=INK)
    fig.text(.5, .069, "Saved predecessor chain: 6 → 5 → 4 → 2    actual witness: (1, 2, 2, 5)",
             ha="center", fontsize=12, color=TEAL)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=100, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"output": output.name, "input": INPUT, "checks": results}))


if __name__ == "__main__":
    main()
