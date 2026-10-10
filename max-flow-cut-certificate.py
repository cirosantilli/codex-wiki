"""Draw a computed flow and two equal-capacity directed cuts.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
Run: make _media/max-flow-cut-certificate.png
Writes an opaque white PNG with this script's basename to the current directory.
"""

from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon


VERTICES = ("s", "a", "b", "t")
EDGES = (("s", "a"), ("s", "b"), ("a", "b"), ("a", "t"), ("b", "t"))
CAPACITY = dict(zip(EDGES, (3, 2, 1, 2, 3)))
FLOW = dict(zip(EDGES, (3, 2, 1, 2, 3)))
POSITION = {"s": (0, 0), "a": (2, 1.3), "b": (2, -1.3), "t": (4, 0)}
LABEL = {("s", "a"): (.9, .85), ("s", "b"): (.9, -.85),
         ("a", "b"): (2.36, 0), ("a", "t"): (3.1, .85),
         ("b", "t"): (3.1, -.85)}
DARK, BLUE, CUT = "#253746", "#24688f", "#b26116"


def balance(flow, vertex):
    return sum(amount for (u, v), amount in flow.items() if u == vertex) - sum(
        amount for (u, v), amount in flow.items() if v == vertex)


def feasible(flow):
    return (all(0 <= flow[e] <= CAPACITY[e] for e in EDGES)
            and all(balance(flow, v) == 0 for v in ("a", "b")))


def verify():
    assert feasible(FLOW)
    assert balance(FLOW, "s") == -balance(FLOW, "t") == 5
    cuts = {}
    for included in product((False, True), repeat=2):
        side = frozenset(("s",)) | frozenset(v for v, yes in zip(("a", "b"), included) if yes)
        outgoing = [e for e in EDGES if e[0] in side and e[1] not in side]
        incoming = [e for e in EDGES if e[0] not in side and e[1] in side]
        cuts[side] = sum(CAPACITY[e] for e in outgoing)
        assert sum(FLOW[e] for e in outgoing) - sum(FLOW[e] for e in incoming) == 5
        assert balance(FLOW, "s") <= cuts[side]
    assert [cuts[frozenset(s)] for s in (("s",), ("s", "a"), ("s", "b"),
                                        ("s", "a", "b"))] == [5, 5, 6, 5]

    # Exhaustive feasible integer flows independently confirm the optimum.
    candidates = [dict(zip(EDGES, values)) for values in product(
        *(range(CAPACITY[e] + 1) for e in EDGES))]
    values = [balance(f, "s") for f in candidates if feasible(f)]
    assert max(values) == min(cuts.values()) == 5

    # Check the deliberately indirect first augmentation, then the two direct ones.
    f = dict.fromkeys(EDGES, 0)
    for path, amount, expected in (("sabt", 1, 1), ("sat", 2, 3), ("sbt", 2, 5)):
        path_edges = list(zip(path, path[1:]))
        assert min(CAPACITY[e] - f[e] for e in path_edges) == amount
        for edge in path_edges:
            f[edge] += amount
        assert feasible(f) and balance(f, "s") == expected
    assert f == FLOW
    print("Verified: 288 integer assignments; maximum=5; cuts=[5,5,6,5]; "
          "balances a=b=0; augmentation values=[1,3,5].")


def draw(ax, side):
    if side == {"s"}:
        region = [(-.45, -1.8), (1, -1.8), (1, 1.8), (-.45, 1.8)]
        boundary = [(1, -1.8), (1, 1.8)]
        title, equation = "Source side S = {s}", "Cut capacity: 3 + 2 = 5"
    else:
        region = [(-.45, -1.8), (1, -1.8), (1, 0), (3, 0), (3, 1.8), (-.45, 1.8)]
        boundary = [(1, -1.8), (1, 0), (3, 0), (3, 1.8)]
        title, equation = "Source side S = {s, a}", "Cut capacity: 2 + 1 + 2 = 5"
    ax.add_patch(Polygon(region, facecolor="#e6f1e8", edgecolor="none", zorder=0))
    ax.plot(*zip(*boundary), ls="--", color=CUT, lw=2.2, zorder=1)
    for u, v in EDGES:
        ax.add_patch(FancyArrowPatch(POSITION[u], POSITION[v], arrowstyle="-|>",
                                    mutation_scale=15, shrinkA=16, shrinkB=16,
                                    linewidth=2, color=BLUE, zorder=2))
        x, y = LABEL[u, v]
        ax.text(x, y, f"{FLOW[u, v]}/{CAPACITY[u, v]}", ha="center", va="center",
                fontsize=12, color=DARK, zorder=4,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.7})
    for v, (x, y) in POSITION.items():
        ax.add_patch(Circle((x, y), .22, facecolor="#c9e4ce" if v in side else "white",
                            edgecolor=DARK, linewidth=1.4, zorder=3))
        ax.text(x, y, v, ha="center", va="center", fontsize=14, color=DARK, zorder=4)
    ax.set(xlim=(-.5, 4.5), ylim=(-1.85, 1.85), aspect="equal")
    ax.axis("off")
    ax.set_title(title, fontsize=12, color=DARK)
    ax.text(2, -2.08, equation, ha="center", fontsize=12, color=CUT)


def main():
    verify()
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.6), dpi=120, facecolor="white")
    for ax, side in zip(axes, ({"s"}, {"s", "a"})):
        draw(ax, side)
    fig.suptitle("Maximum flow = minimum cut = 5", fontsize=15, color=DARK, y=.97)
    fig.text(.5, .88, "Same flow in both panels  •  Edge labels: flow / capacity",
             ha="center", fontsize=11, color=DARK)
    fig.text(.5, .095, "Conservation at a: 3 = 1 + 2    |    at b: 2 + 1 = 3",
             ha="center", fontsize=11, color=DARK)
    fig.text(.5, .035, "Shading: source side    Dashed line: cut    Count only arrows leaving the shading",
             ha="center", fontsize=10, color=DARK)
    fig.subplots_adjust(left=.025, right=.975, top=.81, bottom=.22, wspace=.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
