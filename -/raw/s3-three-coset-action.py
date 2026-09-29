"""Draw the faithful S3 action on three left cosets; save PNG to cwd."""

from itertools import permutations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def compose(p, q):
    """Rightmost permutation acts first; tuples store images of 1, 2, 3."""
    return tuple(p[j - 1] for j in q)


def main():
    group = list(permutations((1, 2, 3)))
    e, t, r = (1, 2, 3), (2, 1, 3), (2, 3, 1)
    h = {e, t}
    reps = [(3, 2, 1), (1, 3, 2), e]
    cosets = [frozenset(compose(a, b) for b in h) for a in reps]
    assert [set(p[2] for p in c) for c in cosets] == [{1}, {2}, {3}]
    assert set.union(*(set(c) for c in cosets)) == set(group)
    assert all(len(c) == 2 for c in cosets)
    actions = {}
    for g in group:
        actions[g] = tuple(cosets.index(frozenset(compose(g, a) for a in c))
                           for c in cosets)
        assert actions[g] == tuple(i - 1 for i in g)
    stabilizers = [{g for g in group if actions[g][i] == i} for i in range(3)]
    assert stabilizers == [{e, (1, 3, 2)}, {e, (3, 2, 1)}, {e, t}]
    assert set.intersection(*stabilizers) == {e}
    assert len(set(actions.values())) == 6
    assert actions[t] == (1, 0, 2) and actions[r] == (1, 2, 0)
    for a in group:
        for b in group:
            assert actions[compose(a, b)] == tuple(actions[a][j] for j in actions[b])

    ink, gray = "#243344", "#d7dfe6"
    colors = ["#166b99", "#a55719", "#387650"]
    fig = plt.figure(figsize=(10, 7.2), dpi=110, facecolor="white")
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(.5, .962, r"$S_3$ on three left cosets: every operation is visible",
            ha="center", va="center", fontsize=18, color=ink)
    ax.text(.5, .915, r"$H=\{e,(12)\}$; products apply the rightmost factor first",
            ha="center", fontsize=12, color=ink)
    members = [r"$\{(13),(123)\}$", r"$\{(23),(132)\}$", r"$\{e,(12)\}$"]
    for i, x in enumerate((.19, .5, .81)):
        ax.add_patch(FancyBboxPatch((x - .14, .715), .28, .145,
                     boxstyle="round,pad=0.006", facecolor="white",
                     edgecolor=colors[i], linewidth=1.8))
        ax.text(x, .82, rf"$C_{i+1}$", ha="center", fontsize=17, color=colors[i])
        ax.text(x, .775, members[i], ha="center", fontsize=13, color=ink)
        ax.text(x, .732, f"Both members send 3 to {i+1}", ha="center", fontsize=11,
                color=colors[i])

    for left, g, label in ((.045, t, r"Left multiply by $(12)$"),
                            (.53, r, r"Left multiply by $(123)$")):
        ax.text(left + .205, .665, label, ha="center", fontsize=14, color=ink)
        xs = [left + .06 + .145 * i for i in range(3)]
        ax.text(left, .605, "in", ha="right", fontsize=10, color=ink)
        ax.text(left, .365, "out", ha="right", fontsize=10, color=ink)
        for i, x in enumerate(xs):
            dest = actions[g][i]
            ax.annotate("", xy=(xs[dest], .392), xytext=(x, .575),
                        arrowprops={"arrowstyle": "-|>", "lw": 2,
                                    "color": colors[i], "mutation_scale": 16})
            for y in (.607, .367):
                ax.text(x, y, rf"$C_{i+1}$", ha="center", va="center", fontsize=14,
                        color=colors[i], bbox={"facecolor": "white",
                        "edgecolor": colors[i], "boxstyle": "round,pad=.3"})
        ax.text(left + .205, .304,
                "One label fixed; two exchanged" if g == t else "All three labels cycle",
                ha="center", fontsize=12, color=ink)
    ax.plot([.025, .975], [.265, .265], color=gray, lw=1.5)
    ax.text(.5, .225, "An element is invisible only if it lies in all three stabilizers",
            ha="center", fontsize=13, color=ink)
    ax.text(.5, .157, r"$\{e,(23)\}\ \cap\ \{e,(13)\}\ \cap\ \{e,(12)\}=\{e\}$",
            ha="center", fontsize=18, color=ink)
    ax.text(.5, .078, "3 cosets • 6 distinct induced permutations • trivial kernel",
            ha="center", fontsize=13, color=ink)
    out = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(out, facecolor="white", transparent=False)
    plt.close(fig)
    print("Checked 18 coset images, 36 composition identities, all stabilizers and kernel.")
    print(out)


if __name__ == "__main__":
    main()
