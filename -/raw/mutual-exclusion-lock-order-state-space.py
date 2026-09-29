"""Generate mutual-exclusion-lock-order-state-space.png in the working directory.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Exhaust the reachable states of two one-shot lock users under sequential consistency.
An unavailable acquisition blocks; no timeouts, retries or forced unlocks are modeled.
"""

from collections import deque
from pathlib import Path
import json

import matplotlib.pyplot as plt


def successors(state, orders):
    """State is (pc1, pc2, owner_of_A, owner_of_B); owner -1 means free."""
    pcs, owners = list(state[:2]), list(state[2:])
    for thread, pc in enumerate(pcs):
        if pc == 4:
            continue
        first, second = orders[thread]
        lock = [first, second, second, first][pc]
        new_owners, new_pcs = owners.copy(), pcs.copy()
        if pc < 2:
            if owners[lock] != -1:
                continue
            new_owners[lock] = thread
        else:
            assert owners[lock] == thread
            new_owners[lock] = -1
        new_pcs[thread] += 1
        yield tuple(new_pcs + new_owners), thread


def explore(orders):
    initial = (0, 0, -1, -1)
    seen, queue, edges = {initial}, deque([initial]), []
    while queue:
        state = queue.popleft()
        for target, thread in successors(state, orders):
            edges.append((state, target, thread))
            if target not in seen:
                seen.add(target)
                queue.append(target)
    deadlocks = sorted(state for state in seen if state[:2] != (4, 4) and not list(successors(state, orders)))
    # For these programs the progress pair uniquely determines lock ownership.
    assert len({state[:2] for state in seen}) == len(seen)
    return seen, edges, deadlocks


def draw_graph(ax, result, title, orders_text):
    states, edges, deadlocks = result
    for source, target, thread in edges:
        ax.annotate("", xy=target[:2], xytext=source[:2],
                    arrowprops=dict(arrowstyle="->", color=["#156a9a", "#8b4b9a"][thread],
                                    lw=1.7, shrinkA=10, shrinkB=10), zorder=1)
    for state in sorted(states):
        color = "#b83d36" if state in deadlocks else "#32834c" if state[:2] == (4, 4) else "#ffffff"
        ax.scatter(*state[:2], s=250, facecolor=color, edgecolor="#52616b", lw=1.3, zorder=3)
    if deadlocks:
        ax.annotate("both hold their first lock;\nneither can acquire the second", xy=(1, 1), xytext=(2.25, 1.25),
                    fontsize=10, color="#a42b29", ha="center",
                    arrowprops=dict(arrowstyle="->", color="#a42b29"))
    ax.text(4, 4.35, "both finished", color="#28703b", ha="center", fontsize=10)
    ax.set_title(title + "\n" + orders_text, fontsize=12, pad=16)
    ax.set_xlim(-0.4, 4.5)
    ax.set_ylim(-0.4, 4.65)
    ax.set_xticks(range(5))
    ax.set_yticks(range(5))
    ax.set_xlabel("T1 completed lock operations", fontsize=11)
    ax.set_ylabel("T2 completed lock operations", fontsize=11)
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.15)
    ax.text(0.5, -0.22, f"{len(states)} reachable states; {len(deadlocks)} deadlock state(s)",
            transform=ax.transAxes, ha="center", fontsize=10)


def main():
    opposite = explore(((0, 1), (1, 0)))
    ordered = explore(((0, 1), (0, 1)))
    assert opposite[2] == [(1, 1, 0, 1)]
    assert ordered[2] == []
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 6.3), facecolor="white")
    draw_graph(axes[0], opposite, "Opposite acquisition orders", "T1: A, B, release B, release A   |   T2: B, A, release A, release B")
    draw_graph(axes[1], ordered, "One shared acquisition order", "both: A, B, release B, release A")
    fig.text(0.5, 0.085, "Blue arrows: T1 advances. Purple arrows: T2 advances. Only reachable states are drawn.",
             ha="center", fontsize=10)
    fig.text(0.5, 0.045, "Each arrow is one enabled acquire or release. Blocked acquisitions have no outgoing arrow.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.84, bottom=0.26, wspace=0.28)
    path = Path(__file__).stem + ".png"
    fig.savefig(path, dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps({"image": path, "opposite": {"states": len(opposite[0]), "edges": len(opposite[1]),
                     "deadlocks": opposite[2]}, "ordered": {"states": len(ordered[0]), "edges": len(ordered[1]),
                     "deadlocks": ordered[2]}}))


if __name__ == "__main__":
    main()
