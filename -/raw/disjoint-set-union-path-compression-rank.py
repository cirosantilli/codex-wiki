"""Draw the original rank/compression trace; write its PNG to the CWD.

Tested with Python 3.14, matplotlib 3.10.7; see pyproject.toml.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


def main():
    parent = list(range(8))
    rank = [0] * 8

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != x:
            following = parent[x]
            parent[x] = root
            x = following
        return root

    def unite(x, y):
        a, b = find(x), find(y)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True

    for call in [(2, 1), (4, 3), (2, 4), (6, 5), (2, 6)]:
        assert unite(*call)
    assert not unite(1, 2)
    before = parent[1:]
    assert before == [2, 2, 4, 2, 6, 2, 7]
    ranks = rank[1:]
    assert ranks == [0, 2, 0, 1, 0, 1, 0]
    assert find(3) == 2
    assert parent[1:] == [2, 2, 2, 2, 6, 2, 7]
    assert find(5) == 2
    after = parent[1:]
    assert after == [2, 2, 2, 2, 2, 2, 7] and rank[1:] == ranks

    fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.0), dpi=120, facecolor="white")
    positions = [
        {2: (2.6, 2.6), 1: (0.7, 1.45), 4: (2.6, 1.45), 6: (4.5, 1.45),
         3: (2.6, 0.3), 5: (4.5, 0.3), 7: (5.8, 2.6)},
        {2: (2.6, 2.6), 1: (0.35, 1.05), 3: (1.45, 1.05), 4: (2.6, 1.05),
         5: (3.75, 1.05), 6: (4.85, 1.05), 7: (5.8, 2.6)},
    ]
    for ax, parents, pos, title in zip(axes, [before, after], positions,
                                     ["Before compression queries", "After find(3), then find(5)"]):
        ax.set(xlim=(-0.2, 6.5), ylim=(-0.85, 3.45), aspect="equal")
        ax.axis("off")
        ax.set_title(title, fontsize=13, pad=8)
        for node, par in enumerate(parents, 1):
            if node != par:
                changed = node in (3, 5)
                ax.add_patch(FancyArrowPatch(pos[node], pos[par], arrowstyle="-|>",
                                            mutation_scale=15, shrinkA=15, shrinkB=15,
                                            linewidth=2 if changed else 1.4,
                                            color="#bd4c32" if changed else "#607385"))
        for node, (x, y) in pos.items():
            ax.add_patch(Circle((x, y), 0.21, facecolor="#fde8c8" if node == 7 else "#d6eaf8",
                                edgecolor="#17324d", linewidth=1.3, zorder=3))
            ax.text(x, y, str(node), ha="center", va="center", fontsize=12, zorder=4)
            ax.text(x + 0.23, y + 0.23, f"r={ranks[node - 1]}", fontsize=10, color="#384d60")
        ax.text(2.7, -0.5, "Root 2: height " + ("2" if parents == before else "1") + "; rank 2",
                ha="center", fontsize=12, color="#17324d")
    fig.suptitle("Parent routes shorten; stored ranks do not change", fontsize=16, y=0.97)
    fig.text(0.5, 0.045, "Arrows point to parents. Red marks the two compressed routes. Root 7 stays separate.",
             ha="center", fontsize=11, color="#384d60")
    fig.subplots_adjust(left=0.03, right=0.98, top=0.83, bottom=0.12, wspace=0.08)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
