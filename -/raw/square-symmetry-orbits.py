"""Verify D4 using exact coordinate permutations, then draw all eight symmetries.

Run from _media to write square-symmetry-orbits.png there. Tested with Python
3.14, matplotlib 3.10.7 and numpy 2.3.5 as specified by the root pyproject.toml.
"""

from itertools import permutations, product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


COORDS = ((1, 1), (-1, 1), (-1, -1), (1, -1))
LETTERS = "ABCD"


def compose(g, h):
    """Tuples record vertex images; apply h first, then g."""
    return tuple(g[h[i]] for i in range(4))


def square_model():
    """All signed coordinate permutations preserving the square, exactly."""
    coordinate_maps = {}
    for axes in permutations(range(2)):
        for signs in product((-1, 1), repeat=2):
            images = tuple(
                tuple(signs[j] * point[axes[j]] for j in range(2))
                for point in COORDS
            )
            permutation = tuple(COORDS.index(point) for point in images)
            coordinate_maps[permutation] = (axes, signs)
    identity = tuple(range(4))
    r = tuple(COORDS.index((-y, x)) for x, y in COORDS)
    s = tuple(COORDS.index((y, x)) for x, y in COORDS)
    powers = [identity]
    for _ in range(3):
        powers.append(compose(r, powers[-1]))
    labels = ("e", "r", "r²", "r³", "s", "rs", "r²s", "r³s")
    group = powers + [compose(p, s) for p in powers]
    assert len(coordinate_maps) == len(set(group)) == 8
    assert set(group) == set(coordinate_maps)
    actions = {
        "Vertices": (tuple(range(4)), lambda g, x: g[x]),
        "Edges": (
            tuple(frozenset((i, (i + 1) % 4)) for i in range(4)),
            lambda g, x: frozenset(g[i] for i in x),
        ),
        "Diagonals": (
            (frozenset((0, 2)), frozenset((1, 3))),
            lambda g, x: frozenset(g[i] for i in x),
        ),
        "Center": (
            ((0, 0),),
            lambda g, x: tuple(
                coordinate_maps[g][1][j] * x[coordinate_maps[g][0][j]]
                for j in range(2)
            ),
        ),
    }
    return group, dict(zip(group, labels)), actions


def verify_square():
    group, labels, actions = square_model()
    identity, r, s = group[0], group[1], group[4]
    assert compose(r, group[3]) == identity
    assert compose(s, s) == identity
    assert compose(compose(s, r), s) == group[3]
    for g in group:
        assert set(g) == set(range(4))
        assert compose(g, identity) == compose(identity, g) == g
        inverse = tuple(g.index(i) for i in range(4))
        assert inverse in group
        assert compose(g, inverse) == compose(inverse, g) == identity
        for h in group:
            assert compose(g, h) in group
            for k in group:
                assert compose(compose(g, h), k) == compose(g, compose(h, k))
    expected_sizes = {"Vertices": (4, 2), "Edges": (4, 2),
                      "Diagonals": (2, 4), "Center": (1, 8)}
    expected_stabilizers = {
        "Vertices": {"e", "s"}, "Edges": {"e", "rs"},
        "Diagonals": {"e", "r²", "s", "r²s"}, "Center": set(labels.values()),
    }
    cases = 0
    for name, (objects, act) in actions.items():
        for x in objects:
            assert act(identity, x) == x
            orbit = {act(g, x) for g in group}
            stabilizer = {g for g in group if act(g, x) == x}
            assert orbit == set(objects)
            assert (len(orbit), len(stabilizer)) == expected_sizes[name]
            assert len(orbit) * len(stabilizer) == len(group)
            for g in stabilizer:
                assert tuple(g.index(i) for i in range(4)) in stabilizer
                for h in stabilizer:
                    assert compose(g, h) in stabilizer
            for g, h in product(group, repeat=2):
                assert act(g, x) in objects
                assert act(compose(g, h), x) == act(g, act(h, x))
                cases += 1
        stabilizer = {labels[g] for g in group if act(g, objects[0]) == objects[0]}
        assert stabilizer == expected_stabilizers[name]
    print("D4: 8 signed coordinate permutations; 64 closure and 512 associativity cases.")
    print(f"All identities/inverses, {cases} action-law cases and 11 orbit/stabilizer products checked.")
    print("Vertices 4×2; edges 4×2; diagonals 2×4; center 1×8; every product equals 8.")
    return group, labels, actions


def main():
    group, labels, _ = verify_square()
    fig, axes = plt.subplots(2, 4, figsize=(10, 6.3), dpi=120, facecolor="white")
    outline = np.array(COORDS + (COORDS[0],))
    colors = ("#126b91", "#44833f", "#8b58a2", "#bc6721")
    for row in range(2):
        for column in range(4):
            ax = axes[row, column]
            g = group[column + 4 * row]
            color = colors[column]
            ax.plot(outline[:, 0], outline[:, 1], color="#697780", lw=1.6)
            ax.scatter(outline[:4, 0], outline[:4, 1], s=25, color="#697780")
            for original, image in enumerate(g):
                x, y = COORDS[image]
                ax.text(1.25 * x, 1.25 * y, LETTERS[original], fontsize=13,
                        ha="center", va="center",
                        color=color if original == 0 else "#27343d",
                        fontweight="bold" if original == 0 else "normal")
            target = COORDS[g[0]]
            ax.scatter(*target, s=190, facecolor="white", edgecolor=color,
                       linewidth=2.5, zorder=3)
            ax.scatter(*target, s=32, color=color, zorder=4)
            ax.set_title(labels[g], fontsize=16, pad=9, color=color)
            ax.set(xlim=(-1.55, 1.55), ylim=(-1.55, 1.55), aspect="equal")
            ax.axis("off")
            if row == 0:
                ax.text(0.5, 1.29, f"A goes to {LETTERS[column]}",
                        transform=ax.transAxes, ha="center", fontsize=13,
                        color=color, fontweight="bold")
    fig.suptitle("Eight square symmetries, four images of A", fontsize=19, y=0.97)
    fig.text(0.5, 0.055, "Each column: two transformations give the same image of A.\n"
             "Letters travel with their original vertices; the ring marks A's image.",
             ha="center", va="center", fontsize=12, color="#27343d")
    fig.subplots_adjust(left=0.04, right=0.96, bottom=0.14, top=0.77,
                        wspace=0.2, hspace=0.45)
    output = Path.cwd() / "square-symmetry-orbits.png"
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1200×756 pixels, opaque white background.")


if __name__ == "__main__":
    main()
