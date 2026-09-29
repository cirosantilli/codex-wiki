"""Seven labelled vertices: unique paths, deletion and insertion (Python 3.14).

Write tree-unique-paths.png in the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


EDGES = ((1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7))
POSITIONS = {1: (0, 2), 2: (-1, 1), 3: (1, 1),
             4: (-1.6, 0), 5: (-0.4, 0), 6: (1, 0), 7: (1, -1)}
BLUE, ORANGE, DARK = "#176997", "#c05422", "#273746"


def components(edges):
    remaining = set(POSITIONS)
    result = []
    while remaining:
        reached, todo = set(), [min(remaining)]
        while todo:
            v = todo.pop()
            if v in reached:
                continue
            reached.add(v)
            for a, b in edges:
                if a == v:
                    todo.append(b)
                elif b == v:
                    todo.append(a)
        result.append(reached)
        remaining -= reached
    return result


def draw(ax, edges, highlighted=(), orange_nodes=()):
    highlighted = {frozenset(e) for e in highlighted}
    for a, b in edges:
        color = ORANGE if frozenset((a, b)) in highlighted else BLUE
        ax.plot([POSITIONS[a][0], POSITIONS[b][0]],
                [POSITIONS[a][1], POSITIONS[b][1]], color=color,
                lw=3, zorder=1)
    for v, (x, y) in POSITIONS.items():
        color = ORANGE if v in orange_nodes else BLUE
        ax.scatter(x, y, s=580, color="white", edgecolors=color,
                   linewidths=2.2, zorder=3)
        ax.text(x, y, str(v), color=DARK, ha="center", va="center",
                fontsize=13, zorder=4)
    ax.set(xlim=(-1.95, 1.65), ylim=(-1.45, 2.55), aspect="equal")
    ax.axis("off")


def main():
    deleted = tuple(e for e in EDGES if e != (1, 3))
    inserted = EDGES + ((5, 7),)
    path = ((4, 2), (2, 1), (1, 3), (3, 6), (6, 7))
    cycle = ((5, 2), (2, 1), (1, 3), (3, 6), (6, 7), (7, 5))
    assert len(EDGES) == 6 and components(EDGES) == [set(range(1, 8))]
    assert components(deleted) == [{1, 2, 4, 5}, {3, 6, 7}]
    degrees = [sum(v in e for e in EDGES) for v in range(1, 8)]
    assert degrees == [2, 3, 2, 1, 1, 2, 1] and sum(degrees) == 12
    assert len(inserted) - len(POSITIONS) + len(components(inserted)) == 1
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.7), dpi=120,
                             facecolor="white")
    draw(axes[0], EDGES, path)
    draw(axes[1], deleted, ((3, 6), (6, 7)), (3, 6, 7))
    draw(axes[2], inserted, cycle)
    titles = ("Original tree: 7 vertices, 6 edges", "Delete edge 1–3: two components",
              "Add edge 5–7: one cycle")
    captions = ("Orange path: 4 → 2 → 1 → 3 → 6 → 7",
                "Blue: {1, 2, 4, 5}   Orange: {3, 6, 7}",
                "Orange cycle: 5 → 2 → 1 → 3 → 6 → 7 → 5")
    for ax, title, caption in zip(axes, titles, captions):
        ax.set_title(title, fontsize=11, pad=10)
        ax.text(0.5, -0.055, caption, transform=ax.transAxes, ha="center",
                fontsize=9, color=DARK)
    fig.suptitle("Unique routes make every tree edge indispensable", fontsize=14)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.86, bottom=0.15, wspace=0.08)
    fig.savefig(Path.cwd() / "tree-unique-paths.png", facecolor="white",
                transparent=False)
    plt.close(fig)
    print("Verified: degrees (2,3,2,1,1,2,1), sum 12; deletion gives 2 components.")


if __name__ == "__main__":
    main()
