"""Generate fifo-belady-anomaly-frame-comparison.png in the working directory.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg. Original state and count comparison.
"""

from collections import deque
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

TRACE = (1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5)


def fifo(capacity):
    """Queue-based implementation, separate from the fixed-slot trace generator."""
    queue = deque()
    rows, misses = [], 0
    for page in TRACE:
        hit = page in queue
        if not hit:
            misses += 1
            if len(queue) == capacity:
                queue.popleft()
            queue.append(page)
        rows.append(dict(queue=tuple(queue), hit=hit, misses=misses))
    return rows


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(12, 7.2), dpi=100,
                                     gridspec_kw={"height_ratios": [1, 1.1]})
    fig.patch.set_facecolor("white")
    fig.suptitle("FIFO: one more frame produces one more miss", fontsize=17, y=.975)
    top.set_xlim(-1.8, 12)
    top.set_ylim(6.4, -.7)
    top.axis("off")
    rows3, rows4 = fifo(3), fifo(4)
    labels = ["Access index", "Reference", "3-frame queue", "Outcome", "4-frame queue", "Outcome"]
    for y, label in enumerate(labels):
        top.text(-.14, y, label, ha="right", va="center", fontsize=10)
    for i, (a, b) in enumerate(zip(rows3, rows4)):
        values = [str(i + 1), str(TRACE[i]), "".join(map(str, a["queue"])), "H" if a["hit"] else "M",
                  "".join(map(str, b["queue"])), "H" if b["hit"] else "M"]
        for y, value in enumerate(values):
            fill = "#eaf1f8" if y in (0, 1) else "white"
            if y in (3, 5):
                hit = a["hit"] if y == 3 else b["hit"]
                fill = "#d9eee5" if hit else "#f8dfd7"
            top.add_patch(Rectangle((i, y - .43), .99, .86, facecolor=fill,
                                    edgecolor="#ccd2d8", linewidth=.6))
            top.text(i + .5, y, value, ha="center", va="center", fontsize=11)
    top.text(5.1, 6.05, "Queue order: oldest → newest. Digits are separate page labels, not addresses.",
             ha="center", fontsize=10)
    for rows, label, color in [(rows3, "3 frames: 9 misses", "#167b9a"),
                               (rows4, "4 frames: 10 misses", "#b64430")]:
        bottom.step(range(13), [0] + [r["misses"] for r in rows], where="post",
                    color=color, linewidth=2, marker="o", label=label)
    bottom.set(xlim=(0, 12.3), ylim=(0, 11), xlabel="Number of references processed",
               ylabel="Cumulative misses", xticks=range(13), yticks=range(0, 11, 2))
    bottom.grid(alpha=.2)
    bottom.spines[["top", "right"]].set_visible(False)
    bottom.legend(loc="upper left", frameon=False)
    bottom.annotate("After reference 7: page 1 is in the 3-frame set\nbut absent from the 4-frame set.",
                    xy=(7, 7), xytext=(6.3, 2.5), fontsize=10,
                    arrowprops={"arrowstyle": "->", "color": "#52616b"})
    fig.text(.5, .02, "Identical trace and empty start; hits do not refresh FIFO arrival order.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.13, right=.975, top=.9, bottom=.13, hspace=.35)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
