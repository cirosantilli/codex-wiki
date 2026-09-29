"""Compute and draw backward-residual rerouting in a unit-capacity network.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Run: make _media/residual-flow-rerouting.png
Writes an opaque white PNG with this script's basename to the current directory.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


EDGES = (("s", "a"), ("s", "b"), ("a", "b"), ("a", "t"), ("b", "t"))
POSITION = {"s": (0, 0), "a": (2, 1.3), "b": (2, -1.3), "t": (4, 0)}
LABEL = {frozenset("sa"): (.9, .85), frozenset("sb"): (.9, -.85),
         frozenset("ab"): (2.36, 0), frozenset("at"): (3.1, .85),
         frozenset("bt"): (3.1, -.85)}
DARK, BLUE, ORANGE, GRAY = "#253746", "#24688f", "#b55c12", "#aab2ba"


def balance(flow, vertex):
    return sum(f for (u, v), f in flow.items() if u == vertex) - sum(
        f for (u, v), f in flow.items() if v == vertex)


def feasible(flow):
    return all(0 <= f <= 1 for f in flow.values()) and all(
        balance(flow, v) == 0 for v in ("a", "b"))


def residual(flow):
    arcs = {}
    for (u, v), amount in flow.items():
        if 1 - amount > 0:
            arcs[u, v] = 1 - amount
        if amount > 0:
            arcs[v, u] = amount
    return arcs


def reachable(arcs):
    seen, pending = {"s"}, ["s"]
    while pending:
        u = pending.pop()
        for (a, b), capacity in arcs.items():
            if a == u and capacity > 0 and b not in seen:
                seen.add(b)
                pending.append(b)
    return seen


def compute():
    first = dict.fromkeys(EDGES, 0)
    for edge in zip("sabt", "abt"):
        first[edge] += 1
    assert feasible(first) and balance(first, "s") == 1
    assert tuple(first.values()) == (1, 0, 1, 0, 1)
    forward_only = {e: 1 - f for e, f in first.items() if f < 1}
    assert reachable(forward_only) == {"s", "b"}
    arcs = residual(first)
    path = list(zip("sbat", "bat"))
    assert set(arcs) == {("a", "s"), ("s", "b"), ("b", "a"),
                         ("a", "t"), ("t", "b")}
    assert "t" in reachable(arcs)
    delta = min(arcs[e] for e in path)
    assert delta == arcs["b", "a"] == first["a", "b"] == 1
    final = first.copy()
    for u, v in path:
        if (u, v) in final:
            final[u, v] += delta
        else:
            final[v, u] -= delta
    assert feasible(final) and balance(final, "s") == -balance(final, "t") == 2
    assert tuple(final.values()) == (1, 1, 0, 1, 1)
    assert reachable(residual(final)) == {"s"}

    # Exhaustive feasible flows and all directed cuts give independent bounds.
    all_flows = [dict(zip(EDGES, values)) for values in product((0, 1), repeat=5)]
    optimum = max(balance(f, "s") for f in all_flows if feasible(f))
    sides = [{"s"} | {v for v, yes in zip(("a", "b"), included) if yes}
             for included in product((False, True), repeat=2)]
    cuts = [sum(u in side and v not in side for u, v in EDGES) for side in sides]
    assert optimum == min(cuts) == 2
    print("Verified: 32 integer assignments; first=(1,0,1,0,1); "
          "forward reachability={s,b}; residual s-b-a-t bottleneck=1; "
          "final=(1,1,0,1,1); maximum=min-cut=2; final residual reachability={s}.")
    return first, arcs, path, final


def draw(ax, edges, labels, highlighted, residual_panel=False):
    for u, v in edges:
        chosen = (u, v) in highlighted
        reverse = residual_panel and (u, v) == ("b", "a")
        color = ORANGE if residual_panel and chosen else BLUE if chosen else GRAY
        ax.add_patch(FancyArrowPatch(POSITION[u], POSITION[v], arrowstyle="-|>",
                                    mutation_scale=14, shrinkA=13, shrinkB=13,
                                    linewidth=2.6 if chosen else 1.5, color=color,
                                    linestyle="--" if reverse else "-", zorder=1))
        x, y = LABEL[frozenset((u, v))]
        ax.text(x, y, labels[u, v], fontsize=11, ha="center", va="center", color=color,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5}, zorder=3)
    for v, (x, y) in POSITION.items():
        ax.add_patch(Circle((x, y), .23, facecolor="white", edgecolor=DARK,
                            linewidth=1.3, zorder=2))
        ax.text(x, y, v, ha="center", va="center", fontsize=13, color=DARK, zorder=3)
    ax.set(xlim=(-.5, 4.5), ylim=(-1.8, 1.8), aspect="equal")
    ax.axis("off")


def main():
    first, arcs, path, final = compute()
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.6), dpi=120, facecolor="white")
    for ax, flow, title in ((axes[0], first, "1. Before: value 1"),
                            (axes[2], final, "3. After: value 2")):
        draw(ax, EDGES, {e: f"{flow[e]}/1" for e in EDGES},
             {e for e in EDGES if flow[e] > 0})
        ax.set_title(title, fontsize=12, color=DARK, pad=22)
        ax.text(2, 1.72, "Original edges: flow / capacity", ha="center", fontsize=10, color=DARK)
    draw(axes[1], arcs, {e: str(arcs[e]) for e in arcs}, set(path), residual_panel=True)
    axes[1].set_title("2. Augment: s → b → a → t", fontsize=12, color=ORANGE, pad=22)
    axes[1].text(2, 1.72, "Residual edges: remaining capacity", ha="center", fontsize=10, color=DARK)
    for ax, lines in zip(axes, (("First route: s → a → b → t", "No unused forward s–t path"),
                               ("Dashed b → a cancels a → b", "Bottleneck = 1; add one unit"),
                               ("Middle flow: 1 → 0", "Cut {s}: 1 + 1 = 2"))):
        for y, text in zip((-1.97, -2.3), lines):
            ax.text(2, y, text, ha="center", fontsize=11, color=DARK)
    fig.suptitle("Residual edges let a routing decision be revised", fontsize=15, color=DARK, y=.97)
    fig.text(.5, .865, "All original capacities are 1; only the middle panel shows residual edges",
             ha="center", fontsize=11, color=DARK)
    fig.text(.5, .055, "Update: increase s → b and a → t by 1; decrease a → b by 1. Conservation still holds.",
             ha="center", fontsize=11, color=DARK)
    fig.subplots_adjust(left=.02, right=.98, top=.71, bottom=.25, wspace=.16)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
