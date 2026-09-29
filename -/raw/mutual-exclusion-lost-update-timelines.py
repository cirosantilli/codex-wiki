"""Generate mutual-exclusion-lost-update-timelines.png in the working directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
The events are abstract sequentially consistent transitions, not machine code.
"""

from collections import Counter
from itertools import combinations
from pathlib import Path
import json

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def run_schedule(schedule, protected=False):
    """Execute one schedule; an unavailable acquisition is not an enabled step."""
    pcs, registers, shared, owner, trace = [0, 0], [None, None], 0, None, []
    for thread in schedule:
        pc = pcs[thread]
        if protected:
            if pc == 0:
                if owner is not None:
                    return None
                owner = thread
                label = "acquire mutex"
            elif pc == 4:
                assert owner == thread
                owner = None
                label = "release mutex"
            else:
                assert owner == thread
                label = None
            operation = pc - 1
        else:
            label, operation = None, pc
        if label is None:
            if operation == 0:
                registers[thread] = shared
                label = f"read x: r = {shared}"
            elif operation == 1:
                registers[thread] += 1
                label = f"add 1: r = {registers[thread]}"
            elif operation == 2:
                shared = registers[thread]
                label = f"write x = {shared}"
            else:
                raise AssertionError("Invalid program counter")
        pcs[thread] += 1
        trace.append((thread, label, shared))
    assert pcs == ([5, 5] if protected else [3, 3])
    return shared, trace


def enumerate_schedules(steps, protected=False):
    outcomes = Counter()
    for positions in combinations(range(2 * steps), steps):
        selected = set(positions)
        schedule = [0 if i in selected else 1 for i in range(2 * steps)]
        result = run_schedule(schedule, protected)
        if result is not None:
            outcomes[result[0]] += 1
    return outcomes


def draw_timeline(ax, trace, title, subtitle, protected):
    colors = ["#156a9a", "#8b4b9a"]
    ax.set_xlim(-0.9, 3.5)
    ax.set_ylim(len(trace) + 0.3, -1.8)
    ax.axis("off")
    ax.set_title(title + "\n" + subtitle, fontsize=13, pad=15)
    for column, name in zip([0, 1.55, 3.05], ["T1", "T2", "shared x"]):
        ax.text(column, -0.95, name, ha="center", weight="bold", fontsize=11)
    for column in [0, 1.55]:
        ax.plot([column, column], [-0.65, len(trace) - 0.55], color="#c6ccd1", lw=1.3, zorder=0)
    if protected:
        for column, start, stop, color in [(0, 0, 4, colors[0]), (1.55, 5, 9, colors[1])]:
            ax.add_patch(FancyBboxPatch((column - 0.68, start - 0.34), 1.36, stop - start + 0.68,
                                       boxstyle="round,pad=0.04", fc=color, ec="none", alpha=0.09))
        ax.text(1.55, 2, "waiting\n(no entry)", ha="center", va="center", fontsize=10, color="#61686e")
    for i, (thread, label, shared) in enumerate(trace):
        column = 1.55 * thread
        ax.text(-0.82, i, str(i + 1), ha="center", va="center", color="#69727a", fontsize=9)
        ax.text(column, i, label, ha="center", va="center", fontsize=10, color=colors[thread],
                bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=colors[thread]))
        ax.text(3.05, i, str(shared), ha="center", va="center", fontsize=11)
    ax.text(1.15, len(trace) - 0.15, f"final x = {trace[-1][2]}", ha="center", va="top", fontsize=12,
            weight="bold", color="#28703b" if protected else "#a43232")


def main():
    unprotected = enumerate_schedules(3)
    protected = enumerate_schedules(5, True)
    assert unprotected == Counter({1: 18, 2: 2})
    assert protected == Counter({2: 2})
    bad = run_schedule([0, 1, 0, 1, 0, 1])
    good = run_schedule([0] * 5 + [1] * 5, True)
    assert bad[0] == 1 and good[0] == 2
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 6.0), facecolor="white")
    draw_timeline(axes[0], bad[1], "Two increments without a mutex", "one of 18 lost-update orders (20 total)", False)
    draw_timeline(axes[1], good[1], "Protect the complete increment", "either thread may acquire first; both give x = 2", True)
    fig.text(0.5, 0.025, "Initial x = 0. Time goes downward; rows show logical steps, not measured durations.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.025, right=0.99, top=0.88, bottom=0.10, wspace=0.15)
    path = Path(__file__).stem + ".png"
    fig.savefig(path, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"image": path, "unprotected_orders": dict(unprotected), "mutex_orders": dict(protected)}))


if __name__ == "__main__":
    main()
