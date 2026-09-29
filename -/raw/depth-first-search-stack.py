"""Compute recursive DFS and its call stack; write the PNG to the current directory.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Run from the repository with make _media/depth-first-search-stack.png.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


VERTICES = "ABCDEFG"
EDGES = ("AB", "AC", "BD", "BE", "CE", "CF", "EG", "FG")
POSITIONS = dict(zip(VERTICES, np.array([
    [0, 3], [-1, 2], [1, 2], [-1.8, 1], [-0.2, 1], [1.8, 1], [0.8, 0]
])))
DARK, BLUE, PURPLE = "#253746", "#24688f", "#704599"


def compute_dfs():
    adjacency = {v: sorted(b if a == v else a for a, b in EDGES if v in (a, b))
                 for v in VERTICES}
    seen, order, tree, stack, events = set(), [], [], [], []
    scans = 0

    def visit(u):
        nonlocal scans
        seen.add(u)
        order.append(u)
        stack.append(u)
        events.append(("Enter " + u, tuple(stack)))
        for v in adjacency[u]:
            scans += 1
            if v not in seen:
                tree.append(u + v)
                visit(v)
        assert stack.pop() == u
        events.append(("Return " + u, tuple(stack)))

    visit("A")
    # Simulate suspended adjacency-list iterators to check recursive equivalence.
    frames, marked, iterative, iterative_tree = [("A", iter(adjacency["A"]))], {"A"}, ["A"], []
    while frames:
        u, neighbors = frames[-1]
        v = next(neighbors, None)
        if v is None:
            frames.pop()
        elif v not in marked:
            marked.add(v)
            iterative.append(v)
            iterative_tree.append(u + v)
            frames.append((v, iter(adjacency[v])))
    assert order == iterative == list("ABDECFG")
    assert tree == iterative_tree == ["AB", "BD", "BE", "EC", "CF", "FG"]
    assert seen == set(VERTICES) and len(order) == len(seen) == 7
    assert scans == 16 and len(events) == 14
    assert max(len(state) for _, state in events) == 6
    assert dict(events)["Return D"] == ("A", "B")
    assert dict(events)["Enter G"] == tuple("ABECFG")
    assert [action for action, _ in events[8:]] == ["Return " + v for v in "GFCEBA"]

    # A stack that marks all reverse-ordered neighbors on push differs.
    pending, marked, eager = ["A"], {"A"}, []
    while pending:
        u = pending.pop()
        eager.append(u)
        for v in reversed(adjacency[u]):
            if v not in marked:
                marked.add(v)
                pending.append(v)
    assert eager == list("ABDEGFC") and eager != order
    return order, tree, events, scans


def draw_graph(ax, order, tree):
    highlighted = {frozenset(e) for e in tree}
    for a, b in EDGES:
        xy = np.array([POSITIONS[a], POSITIONS[b]])
        is_tree = frozenset((a, b)) in highlighted
        ax.plot(xy[:, 0], xy[:, 1], color=BLUE if is_tree else "#929ca6",
                lw=2.7 if is_tree else 1.7, ls="-" if is_tree else "--", zorder=1)
    for v, (x, y) in POSITIONS.items():
        ax.scatter(x, y, s=1100, facecolors="white", edgecolors=BLUE,
                   linewidths=1.8, zorder=3)
        ax.text(x, y, f"{v}\n{order.index(v) + 1}", ha="center", va="center",
                fontsize=12, linespacing=1.15, color=DARK, zorder=4)
    ax.set(xlim=(-2.3, 2.3), ylim=(-0.5, 3.5), aspect="equal")
    ax.axis("off")
    ax.set_title("Same graph; numbers show discovery order", fontsize=12, pad=12)


def main():
    order, tree, events, scans = compute_dfs()
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.7), dpi=120,
                             facecolor="white", gridspec_kw={"width_ratios": [1, 1.18]})
    draw_graph(axes[0], order, tree)
    ax = axes[1]
    ax.set(xlim=(0, 1), ylim=(-0.6, 9.6))
    ax.axis("off")
    ax.set_title("Call stack: oldest → current (top)", fontsize=12, pad=12)
    ax.text(0.02, 9.1, "Action", color=DARK, fontsize=11, fontweight="bold")
    ax.text(0.33, 9.1, "Active calls", color=DARK, fontsize=11, fontweight="bold")
    rows = events[:8] + [("Return rest", ())]
    for i, (action, state) in enumerate(rows):
        y = 8.35 - i * 0.91
        color = PURPLE if action.startswith("Enter") else DARK
        ax.text(0.02, y, action, fontsize=11, color=color, va="center")
        ax.text(0.33, y, " → ".join(state) if state else "empty", fontsize=11,
                color=color, va="center")
        ax.axhline(y - 0.37, xmin=0.02, xmax=0.96, color="#e6e9ed", lw=0.8)
    ax.text(0.02, -0.3, "Final returns: " + " → ".join(a.split()[1] for a, _ in events[8:]),
            fontsize=10, color=DARK)
    fig.suptitle("Depth-first search: finish a new branch before resuming its caller", fontsize=14)
    fig.text(0.5, 0.095, "Solid: discovery tree     Dashed: other graph edges     "
             "Scan neighbors alphabetically", ha="center", fontsize=10, color=DARK)
    fig.text(0.5, 0.05, "First discovery: " + " → ".join(order) + "     "
             "D finishes before E starts; discovery marks persist after return",
             ha="center", fontsize=10, color=DARK)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.84, bottom=0.19, wspace=0.1)
    fig.savefig(Path.cwd() / "depth-first-search-stack.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print(f"DFS: order={''.join(order)}; tree={tree}; scans={scans}; "
          f"stack_peak=6; entries=7; returns=7; eager_stack_order=ABDEGFC")


if __name__ == "__main__":
    main()
