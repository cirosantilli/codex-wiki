"""Enumerate S3 with rightmost-first composition and draw both coset partitions."""

from itertools import permutations
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def compose(a, b):
    """Apply b first, then a; tuples record the images of 1, 2, 3."""
    return tuple(a[b[i] - 1] for i in range(3))


def main():
    labels = {
        (1, 2, 3): "e", (2, 1, 3): "(12)", (3, 2, 1): "(13)",
        (1, 3, 2): "(23)", (2, 3, 1): "(123)", (3, 1, 2): "(132)",
    }
    group = set(permutations((1, 2, 3)))
    e, t, u, v = (1, 2, 3), (2, 1, 3), (3, 2, 1), (1, 3, 2)
    subgroup = {e, t}
    assert compose(t, t) == e
    assert compose(u, t) == (2, 3, 1)
    assert compose(t, u) == (3, 1, 2)
    left = {g: frozenset(compose(g, h) for h in subgroup) for g in group}
    right = {g: frozenset(compose(h, g) for h in subgroup) for g in group}
    for family in (left, right):
        parts = set(family.values())
        assert len(parts) == 3
        assert set.union(*(set(part) for part in parts)) == group
        for a in family.values():
            assert len(a) == 2
            for b in family.values():
                assert a == b or a.isdisjoint(b)
    assert {labels[p] for p in left[u]} == {"(13)", "(123)"}
    assert {labels[p] for p in left[v]} == {"(23)", "(132)"}
    assert {labels[p] for p in right[u]} == {"(13)", "(132)"}
    assert {labels[p] for p in right[v]} == {"(23)", "(123)"}
    assert left[e] == left[t] == frozenset(subgroup)
    assert left[compose(e, u)] != left[compose(t, u)]
    for a in group:
        inverse_a = tuple(a.index(i) + 1 for i in (1, 2, 3))
        inverses = frozenset(tuple(p.index(i) + 1 for i in (1, 2, 3)) for p in left[a])
        assert inverses == right[inverse_a]
        for b in group:
            inverse_b = tuple(b.index(i) + 1 for i in (1, 2, 3))
            assert (left[a] == left[b]) == (compose(inverse_b, a) in subgroup)
            assert left[compose(a, b)] == frozenset(compose(a, p) for p in left[b])
    print("S3: 12 cosets, 72 coset pairs, and all 36 left-coset membership/action cases checked.")
    print("(13)H = {(13),(123)}; H(13) = {(13),(132)}; both partitions have 3 parts of size 2.")

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), dpi=120)
    representatives = [e, u, v]
    colors = ["#3c8152", "#176997", "#bb5c19"]
    order = list(labels)
    for ax, family, side in zip(axes, (left, right), ("left", "right")):
        for i, representative in enumerate(representatives):
            y = 2 - i
            label = "H" if representative == e else (
                labels[representative] + "H" if side == "left" else "H" + labels[representative])
            ax.text(0, y, label, ha="left", va="center", color=colors[i], fontsize=15)
            members = sorted(family[representative], key=order.index)
            for j, member in enumerate(members):
                ax.text(1.65 + j * 1.55, y, labels[member], ha="center", va="center",
                        fontsize=15, color=colors[i],
                        bbox={"boxstyle": "round,pad=0.45", "facecolor": "white",
                              "edgecolor": colors[i], "linewidth": 2})
        ax.set_xlim(-0.1, 4.1)
        ax.set_ylim(-0.6, 2.65)
        ax.axis("off")
        ax.set_title(f"{side.capitalize()} cosets: " + ("gH" if side == "left" else "Hg"),
                     fontsize=15, pad=12)
    fig.suptitle(r"$S_3,\quad H=\{e,(12)\}$: the three-cycles change rows",
                 fontsize=17, y=0.95)
    fig.text(0.5, 0.11, "Composition applies the rightmost permutation first.",
             ha="center", fontsize=12, color="#263746")
    fig.text(0.5, 0.045, "Each side contains every permutation exactly once: 3 cosets × 2 members = 6.",
             ha="center", fontsize=11, color="#263746")
    fig.subplots_adjust(left=0.035, right=0.98, top=0.74, bottom=0.2, wspace=0.13)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
