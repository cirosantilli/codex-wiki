"""Draw an exact synthetic read trace, including resident slots and LRU order.

Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
Run from _media with MPLBACKEND=Agg and MPLCONFIGDIR in /tmp.
The matching PNG basename is written to the current working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt


ADDRESSES = (0, 4, 32, 0, 16, 32, 4, 48, 52, 0, 16, 0)
BLOCK_BYTES = 16
CAPACITY = 2


def enumerate_trace():
    """Keep physical slots fixed; keep recency separately, oldest first."""
    slots = [None] * CAPACITY
    recency = []
    seen = set()
    rows = []
    for step, address in enumerate(ADDRESSES, 1):
        line = address // BLOCK_BYTES
        hit = line in recency
        victim = None
        if hit:
            recency.remove(line)
        else:
            if len(recency) == CAPACITY:
                victim = recency.pop(0)
                slot = slots.index(victim)
            else:
                slot = slots.index(None)
            slots[slot] = line
        recency.append(line)
        outcome = "H" if hit else ("M cold" if line not in seen else "M capacity")
        rows.append((step, address, line, outcome, victim, tuple(slots), tuple(recency)))
        seen.add(line)
    return rows


def main():
    rows = enumerate_trace()
    assert sum(row[3] == "H" for row in rows) == 5
    assert rows[3][6] == (2, 0) and rows[4][4] == 2
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(10.4, 6.4), dpi=120)
    fig.patch.set_facecolor("white")
    ax.axis("off")
    fig.suptitle("Fully associative LRU: identity, slots, and recency", fontsize=17,
                 fontweight="bold", y=0.96)
    fig.text(0.5, 0.905, "Synthetic byte reads • 16 bytes / line • 2 resident slots • initially empty",
             ha="center", fontsize=11)
    labels = ["Read", "Address", "Line q", "Outcome", "Evict q", "Slot 0", "Slot 1", "LRU → MRU"]
    def entry(value):
        return "—" if value is None else str(value)
    cells = [[str(i), str(a), str(q), outcome, entry(victim), entry(slots[0]),
              entry(slots[1]), " → ".join(map(str, order))]
             for i, a, q, outcome, victim, slots, order in rows]
    table = ax.table(cellText=cells, colLabels=labels, cellLoc="center", loc="center",
                     colWidths=[0.065, 0.09, 0.09, 0.16, 0.105, 0.1, 0.1, 0.18],
                     bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("#ccd4df")
        cell.set_linewidth(0.6)
        if r == 0:
            cell.set_facecolor("#e5edf7")
            cell.set_text_props(weight="bold", color="#18354f")
        else:
            cell.set_facecolor("white" if r % 2 else "#f5f7fa")
            if c == 3:
                cell.set_facecolor("#d9eee5" if rows[r - 1][3] == "H" else "#f8e5dd")
            if r in (4, 5) and c in (4, 7):
                cell.set_text_props(weight="bold")
    fig.text(0.5, 0.095, "5 hits • 7 misses = 4 cold + 3 capacity\n"
             "Read 4 refreshes line 0; read 5 therefore evicts line 2. Slots do not move on hits.",
             ha="center", fontsize=11, linespacing=1.6)
    fig.text(0.5, 0.035, "No prefetching, writes, invalidations, or overlapping requests. H = hit; M = miss.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.045, right=0.955, top=0.855, bottom=0.19)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
