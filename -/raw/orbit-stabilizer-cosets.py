"""Check coset/orbit bijections and S3/C4 examples; draw the square counts.

Run from _media to write orbit-stabilizer-cosets.png there. Loads the exact
coordinate model from the adjacent square-symmetry-orbits.py. Tested with
Python 3.14, matplotlib 3.10.7 and numpy 2.3.5 from the root pyproject.toml.
"""

from itertools import permutations, product
from pathlib import Path
import runpy

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def verify_cosets(group, actions, compose):
    count = 0
    for objects, act in actions.values():
        for x in objects:
            stabilizer = {g for g in group if act(g, x) == x}
            parts = {frozenset(compose(g, h) for h in stabilizer) for g in group}
            assert set().union(*parts) == set(group)
            assert all(len(part) == len(stabilizer) for part in parts)
            assert len(parts) * len(stabilizer) == len(group)
            images = {}
            for part in parts:
                targets = {act(g, x) for g in part}
                assert len(targets) == 1  # Independent of representative.
                target = next(iter(targets))
                assert target not in images  # Injective.
                images[target] = part
                for other in parts:
                    assert part == other or part.isdisjoint(other)
            assert set(images) == {act(g, x) for g in group}  # Surjective.
            count += 1
    print(f"Coset partitions and well-defined bijections checked for all {count} objects.")


def verify_other_examples():
    group = tuple(permutations(range(1, 4)))
    objects = tuple(product(range(1, 4), repeat=2))

    def compose(g, h):
        return tuple(g[h[i] - 1] for i in range(3))

    def act(g, x):
        return g[x[0] - 1], g[x[1] - 1]

    identity = (1, 2, 3)
    for x in objects:
        assert act(identity, x) == x
        orbit = {act(g, x) for g in group}
        stabilizer = {g for g in group if act(g, x) == x}
        assert orbit == {y for y in objects if (y[0] == y[1]) == (x[0] == x[1])}
        assert (len(orbit), len(stabilizer)) == ((3, 2) if x[0] == x[1] else (6, 1))
        for g, h in product(group, repeat=2):
            assert act(compose(g, h), x) == act(g, act(h, x))
    assert {g for g in group if act(g, (1, 1)) == (1, 1)} == {identity, (1, 3, 2)}
    assert {g for g in group if act(g, (1, 2)) == (1, 2)} == {identity}
    verify_cosets(group, {"ordered pairs": (objects, act)}, compose)
    print("S3: 324 action-law cases; all 9 ordered pairs; orbit/stabilizer sizes 3×2 and 6×1.")

    def parity_act(k, x):
        return (x + k) % 2

    for x in range(2):
        assert parity_act(0, x) == x
        assert {parity_act(k, x) for k in range(4)} == {0, 1}
        assert {k for k in range(4) if parity_act(k, x) == x} == {0, 2}
        for k, ell in product(range(4), repeat=2):
            assert parity_act((k + ell) % 4, x) == parity_act(k, parity_act(ell, x))
    kernel = {k for k in range(4) if all(parity_act(k, x) == x for x in range(2))}
    assert kernel == {0, 2}
    verify_cosets(tuple(range(4)), {"two points": (tuple(range(2)), parity_act)},
                  lambda k, ell: (k + ell) % 4)
    print("C4: 32 action-law cases; kernel {0,2}; both orbit/stabilizer sizes 2×2.")


def box(ax, x, y, width, height, text, color="#126b91", size=13):
    ax.add_patch(FancyBboxPatch((x - width / 2, y - height / 2), width, height,
                               boxstyle="round,pad=0.02", linewidth=1.5,
                               edgecolor=color, facecolor="white", zorder=2))
    ax.text(x, y, text, ha="center", va="center", fontsize=size,
            color="#27343d", linespacing=1.5, zorder=3)


def main():
    model = runpy.run_path(str(Path(__file__).with_name("square-symmetry-orbits.py")))
    group, labels, actions = model["verify_square"]()
    compose = model["compose"]
    verify_cosets(group, actions, compose)
    verify_other_examples()

    fig, axes = plt.subplots(1, 2, figsize=(11, 6), dpi=120, facecolor="white",
                             gridspec_kw={"width_ratios": (1, 1.15)})
    left, right = axes
    for ax in axes:
        ax.set(xlim=(0, 10), ylim=(0, 10))
        ax.axis("off")
    left.set_title("Four cosets → four images of A", fontsize=15, pad=14)
    left.text(5, 9.35, "H = stabilizer of A = {e, s}", ha="center", fontsize=13)
    stabilizer = {g for g in group if g[0] == 0}
    colors = ("#126b91", "#44833f", "#8b58a2", "#bc6721")
    for k, (coset_label, color) in enumerate(zip(("H", "rH", "r²H", "r³H"), colors)):
        y = 7.6 - 1.65 * k
        members = {compose(group[k], h) for h in stabilizer}
        assert members == {group[k], group[k + 4]}
        text = f"{coset_label} = {{{labels[group[k]]}, {labels[group[k + 4]]}}}"
        box(left, 3.1, y, 5.35, 1.05, text, color)
        left.annotate("", xy=(7.3, y), xytext=(5.8, y),
                      arrowprops={"arrowstyle": "->", "color": color, "lw": 1.7})
        box(left, 8, y, 1.2, 1.05, "ABCD"[k], color, size=16)
    left.text(5, 0.7, "8 transformations / 2 per image = 4 images", ha="center", fontsize=12)

    right.set_title("One group, four different actions", fontsize=15, pad=14)
    box(right, 5, 8.9, 4.7, 0.9, "D₄ has 8 elements", size=15)
    root = (5, 8.43)
    positions = ((2.35, 5.85), (7.65, 5.85), (2.35, 2.7), (7.65, 2.7))
    for (name, (objects, act)), (x, y), color in zip(actions.items(), positions, colors):
        point = objects[0]
        orbit_size = len({act(g, point) for g in group})
        stabilizer_size = sum(act(g, point) == point for g in group)
        # Use outer lanes for the lower two branches to avoid upper boxes.
        if y < 4:
            lane = 0.12 if x < 5 else 9.88
            right.plot((root[0], lane, lane, x), (root[1], 7.8, 3.6, 3.6),
                       color=color, lw=1.3, zorder=1)
            right.plot((x, x), (3.6, y + 0.8), color=color, lw=1.3, zorder=1)
        else:
            right.plot((root[0], x), (root[1], y + 0.8), color=color, lw=1.3, zorder=1)
        image_word = "image" if orbit_size == 1 else "images"
        text = f"{name}\n{orbit_size} {image_word} × {stabilizer_size} fixing\n= 8"
        box(right, x, y, 4.15, 1.55, text, color, size=12)
    right.text(5, 0.6, "Each branch moves a different kind of object.", ha="center", fontsize=12)
    fig.suptitle("Orbit–stabilizer: count images, then count repetitions", fontsize=18, y=0.97)
    fig.subplots_adjust(left=0.025, right=0.975, top=0.84, bottom=0.06, wspace=0.16)
    output = Path.cwd() / "orbit-stabilizer-cosets.png"
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Wrote {output.name}: 1320×720 pixels, opaque white background.")


if __name__ == "__main__":
    main()
