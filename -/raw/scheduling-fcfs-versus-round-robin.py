"""Draw a single-CPU scheduling example with no switching cost or I/O blocking.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; write the opaque matching PNG to the current directory.
"""

from collections import deque
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


WORKLOAD = [("A", 0, 5), ("B", 1, 3), ("C", 2, 1)]
COLORS = {"A": "#155d8a", "B": "#187355", "C": "#a84b12"}


def schedule(quantum=None):
    """Queue arrivals through the slice endpoint before requeuing its task."""
    pending = deque(WORKLOAD)
    ready = deque()
    remaining = {name: burst for name, _, burst in WORKLOAD}
    time = 0
    intervals = []
    while pending or ready:
        if not ready and pending:
            time = max(time, pending[0][1])
        while pending and pending[0][1] <= time:
            ready.append(pending.popleft()[0])
        name = ready.popleft()
        duration = remaining[name] if quantum is None else min(quantum, remaining[name])
        end = time + duration
        intervals.append((name, time, end))
        remaining[name] -= duration
        while pending and pending[0][1] <= end:
            ready.append(pending.popleft()[0])
        if remaining[name]:
            ready.append(name)
        time = end
    return intervals


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(9.8, 4.6), dpi=110, facecolor="white")
    ax.set_facecolor("white")
    for y, label, intervals in [(1, "FCFS", schedule()),
                                (0, "Round robin\nquantum = 2", schedule(2))]:
        for name, start, end in intervals:
            ax.broken_barh([(start, end - start)], (y - 0.23, 0.46),
                          facecolors=COLORS[name], edgecolors="white", linewidth=2)
            ax.text((start + end) / 2, y, name, ha="center", va="center",
                    color="white", weight="bold", fontsize=15)
        ax.text(-0.3, y, label, ha="right", va="center", color="#203040")
    for name, arrival, burst in WORKLOAD:
        ax.annotate(f"{name} arrives\nburst {burst}", xy=(arrival, 1.3),
                    xytext=(arrival, 1.63), ha="center", color=COLORS[name],
                    fontsize=11, arrowprops={"arrowstyle": "-|>", "color": COLORS[name]})
    ax.set(xlim=(-0.5, 9.1), ylim=(-0.65, 2.05), xticks=np.arange(10),
           yticks=[], xlabel="Time (abstract units)")
    ax.grid(axis="x", color="#dfe5eb", linewidth=0.7)
    ax.set_axisbelow(True)
    for spine in ["top", "left", "right"]:
        ax.spines[spine].set_visible(False)
    fig.suptitle("Same work, different turns on one CPU", fontsize=17,
                 weight="bold", color="#203040", y=0.96)
    fig.text(0.5, 0.11, "At a slice boundary: queue new arrivals before the expired task.",
             ha="center", fontsize=11)
    fig.text(0.5, 0.055, "Toy model: zero overhead; no I/O blocking; no measured OS timings.",
             ha="center", fontsize=10.5)
    fig.subplots_adjust(left=0.20, right=0.98, top=0.84, bottom=0.27)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
