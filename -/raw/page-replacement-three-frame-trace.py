"""Generate page-replacement-three-frame-trace.png in the working directory.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg. This is a synthetic demand-paging model.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

TRACE = (1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5)
POLICIES = ("FIFO", "LRU", "OPT", "CLOCK")


def simulate(policy, trace=TRACE, capacity=3, writes=()):
    """Fixed slots; FIFO arrival order, exact LRU, farthest-future OPT, or CLOCK.

    CLOCK starts at slot zero; each miss scans from the hand, clears set bits,
    installs with bit one and advances the hand. A hit sets its bit only.
    OPT ties select the lowest slot. Writes are one-based reference indices.
    Every fill is clean; writes mark dirty; no background or terminal writeback.
    """
    if policy not in POLICIES or capacity < 1:
        raise ValueError("Unknown policy or nonpositive capacity")
    slots = [None] * capacity
    bits = [0] * capacity
    dirty = [False] * capacity
    arrival, recency = [], []
    hand = misses = writebacks = 0
    rows = []
    for i, page in enumerate(trace):
        hit = page in slots
        victim = None
        if hit:
            slot = slots.index(page)
        else:
            misses += 1
            if policy == "CLOCK":
                while slots[hand] is not None and bits[hand]:
                    bits[hand] = 0
                    hand = (hand + 1) % capacity
                slot = hand
                hand = (hand + 1) % capacity
            elif None in slots:
                slot = slots.index(None)
            elif policy == "FIFO":
                slot = slots.index(arrival[0])
            elif policy == "LRU":
                slot = slots.index(recency[0])
            else:
                def next_use(j):
                    return next((k for k in range(i + 1, len(trace))
                                 if trace[k] == slots[j]), float("inf"))
                slot = max(range(capacity), key=next_use)
            victim = slots[slot]
            writebacks += int(dirty[slot])
            if victim is not None:
                arrival.remove(victim)
                recency.remove(victim)
            slots[slot] = page
            dirty[slot] = False
            arrival.append(page)
        if page in recency:
            recency.remove(page)
        recency.append(page)
        bits[slot] = 1
        if i + 1 in writes:
            dirty[slot] = True
        rows.append(dict(page=page, hit=hit, victim=victim, slots=tuple(slots),
                         bits=tuple(bits), hand=hand, misses=misses,
                         writebacks=writebacks, dirty=tuple(dirty),
                         arrival=tuple(arrival), recency=tuple(recency)))
    return rows


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, axes = plt.subplots(4, 1, figsize=(12, 11.2), dpi=100)
    fig.patch.set_facecolor("white")
    fig.suptitle("One page-reference trace, three initially empty frames", fontsize=17, y=.982)
    fig.text(.5, .942, "Fixed frame positions; states AFTER each access. M = miss, H = hit.",
             ha="center", fontsize=11)
    for ax, policy in zip(axes, POLICIES):
        rows = simulate(policy)
        ax.set_xlim(-1.4, 12)
        ax.set_ylim(6.6, -.75)
        ax.axis("off")
        ax.text(-1.3, -.45, policy, weight="bold", fontsize=13)
        ax.text(12, -.45, f"{rows[-1]['misses']} misses", ha="right", weight="bold")
        labels = ["Access index", "Reference", "Frame 1", "Frame 2", "Frame 3", "Outcome", "Evicted"]
        for y, label in enumerate(labels):
            ax.text(-.12, y, label, ha="right", va="center", fontsize=10)
        for i, row in enumerate(rows):
            values = [str(i + 1), str(row["page"])]
            for slot, page in enumerate(row["slots"]):
                value = "–" if page is None else str(page)
                if policy == "CLOCK" and page is not None:
                    value += f"/{row['bits'][slot]}"
                if policy == "CLOCK" and slot == row["hand"]:
                    value = "→" + value
                values.append(value)
            values += ["H" if row["hit"] else "M",
                       "–" if row["victim"] is None else str(row["victim"])]
            for y, value in enumerate(values):
                fill = "#eaf1f8" if y in (0, 1) else "white"
                if y == 5:
                    fill = "#d9eee5" if row["hit"] else "#f8dfd7"
                ax.add_patch(Rectangle((i, y - .44), .99, .88,
                                       facecolor=fill, edgecolor="#ccd2d8", linewidth=.6))
                ax.text(i + .5, y, value, ha="center", va="center", fontsize=11)
    fig.text(.5, .032, "CLOCK: cell = page / reference bit; → marks the NEXT hand position.",
             ha="center", fontsize=11)
    fig.text(.5, .012, "OPT: ties choose the lowest frame number. No prefetch, writes or external eviction.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.12, right=.98, top=.912, bottom=.068, hspace=.28)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
