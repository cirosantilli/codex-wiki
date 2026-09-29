"""Draw the transitive, nonfaithful S3 action on two left cosets; PNG to cwd."""

from itertools import permutations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def compose(p, q):
    return tuple(p[j - 1] for j in q)


def main():
    group = list(permutations((1, 2, 3)))
    e, t, r = (1, 2, 3), (2, 1, 3), (2, 3, 1)
    n = {e, r, compose(r, r)}
    cosets = [frozenset(n), frozenset(compose(t, a) for a in n)]
    assert cosets[0].isdisjoint(cosets[1])
    assert set.union(*(set(c) for c in cosets)) == set(group)
    actions = {g: tuple(cosets.index(frozenset(compose(g, a) for a in c))
                       for c in cosets) for g in group}
    assert {g for g in group if actions[g] == (0, 1)} == n
    assert set(actions.values()) == {(0, 1), (1, 0)}
    assert actions[r] == (0, 1) and actions[t] == (1, 0)
    assert [{g for g in group if actions[g][i] == i} for i in range(2)] == [n, n]
    for a in group:
        for b in group:
            assert actions[compose(a, b)] == tuple(actions[a][j] for j in actions[b])

    ink, blue, orange, gray = "#243344", "#166b99", "#a55719", "#d7dfe6"
    fig = plt.figure(figsize=(10, 6.4), dpi=110, facecolor="white")
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(.5, .953, r"$S_3$ on two left cosets: transitive, with a hidden kernel",
            ha="center", fontsize=18, color=ink)
    ax.text(.5, .9, r"$N=A_3=\{e,(123),(132)\}$ is normal",
            ha="center", fontsize=13, color=ink)
    for x, color, label, members, explanation in (
        (.265, blue, r"$E=N$", r"$\{e,(123),(132)\}$", "Even permutations"),
        (.735, orange, r"$O=(12)N$", r"$\{(12),(13),(23)\}$", "Odd permutations")):
        ax.add_patch(FancyBboxPatch((x - .21, .696), .42, .15,
                     boxstyle="round,pad=.006", facecolor="white", edgecolor=color, lw=1.8))
        ax.text(x, .802, label, ha="center", fontsize=17, color=color)
        ax.text(x, .755, members, ha="center", fontsize=15, color=ink)
        ax.text(x, .711, explanation, ha="center", fontsize=11, color=color)
    for left, g, label in ((.065, r, r"$(123)$ fixes both labels"),
                            (.565, t, r"$(12)$ exchanges the labels")):
        ax.text(left + .18, .641, label, ha="center", fontsize=13, color=ink)
        xs = (left + .045, left + .305)
        for i, x in enumerate(xs):
            color = (blue, orange)[i]
            ax.annotate("", xy=(xs[actions[g][i]], .413), xytext=(x, .552),
                        arrowprops={"arrowstyle": "-|>", "lw": 2.5,
                                    "color": color, "mutation_scale": 17})
            for y in (.584, .381):
                ax.text(x, y, (r"$E$", r"$O$")[i], ha="center", va="center",
                        fontsize=16, color=color, bbox={"facecolor": "white",
                        "edgecolor": color, "boxstyle": "round,pad=.3"})
    ax.plot([.035, .965], [.315, .315], color=gray, lw=1.5)
    ax.text(.095, .262, r"$e,\ (123),\ (132)$", color=blue, fontsize=15)
    ax.text(.535, .262, "all induce the identity", color=ink, fontsize=13)
    ax.text(.095, .207, r"$(12),\ (13),\ (23)$", color=orange, fontsize=15)
    ax.text(.535, .207, "all induce the exchange", color=ink, fontsize=13)
    ax.text(.5, .124, r"$\ker\rho=N,\qquad S_3/N\cong C_2$",
            ha="center", fontsize=18, color=ink)
    ax.text(.5, .05, "2 cosets • 2 distinct induced permutations • 3 invisible elements",
            ha="center", fontsize=13, color=ink)
    out = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(out, facecolor="white", transparent=False)
    plt.close(fig)
    print("Checked 12 coset images, 36 composition identities, transitivity and kernel A3.")
    print(out)


if __name__ == "__main__":
    main()
