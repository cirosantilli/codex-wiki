"""Enumerate S3 and draw its conjugacy classes; save a white PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Products act on the rightmost factor first. Tuples give images of 1, 2, 3.
"""

from itertools import permutations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def compose(left, right):
    return tuple(left[i - 1] for i in right)


def inverse(p):
    return tuple(p.index(i) + 1 for i in range(1, 4))


def conjugate(g, x):
    return compose(compose(g, x), inverse(g))


def cycle_label(p):
    unseen = set(range(1, 4))
    cycles = []
    while unseen:
        i = min(unseen)
        cycle = []
        while i in unseen:
            unseen.remove(i)
            cycle.append(str(i))
            i = p[i - 1]
        if len(cycle) > 1:
            cycles.append("(" + "".join(cycle) + ")")
    return "".join(cycles) or "e"


def compute():
    group = tuple(permutations((1, 2, 3)))
    e, t, r = (1, 2, 3), (2, 1, 3), (2, 3, 1)
    classes = [{conjugate(g, x) for g in group} for x in (e, t, r)]
    centralizers = [{g for g in group if compose(g, x) == compose(x, g)}
                   for x in (e, t, r)]
    assert [len(c) for c in classes] == [1, 3, 2]
    assert [len(c) for c in centralizers] == [6, 2, 3]
    assert set.union(*classes) == set(group)
    assert sum(map(len, classes)) == len(group)
    # Verify all six elements, not just the three representatives.
    for x in group:
        orbit = {conjugate(g, x) for g in group}
        stabilizer = {g for g in group if compose(g, x) == compose(x, g)}
        assert len(orbit) * len(stabilizer) == len(group)
        assert orbit in classes
    assert conjugate(r, t) == (1, 3, 2)
    assert conjugate(t, r) == inverse(r)
    center = {x for x in group if all(compose(g, x) == compose(x, g)
                                     for g in group)}
    assert center == {e}
    return group, classes, centralizers


def main():
    group, classes, centralizers = compute()
    plt.rcParams.update({"font.size": 13, "figure.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(9.6, 5.0), dpi=100)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(0.5, 0.94, "Six permutations, three conjugacy classes",
            ha="center", fontsize=19, weight="bold")
    all_labels = [cycle_label(p) for orbit in classes for p in sorted(orbit, key=cycle_label)]
    ax.text(0.5, 0.86, "S₃ = {" + ", ".join(all_labels) + "}",
            ha="center", fontsize=15)
    titles = ("Identity", "Transpositions", "Three-cycles")
    colors = ("#475569", "#2166a5", "#b65b13")
    for j, (orbit, centralizer, title, color) in enumerate(
            zip(classes, centralizers, titles, colors, strict=True)):
        left = 0.035 + j * 0.32
        middle = left + 0.145
        ax.add_patch(FancyBboxPatch((left, 0.32), 0.29, 0.46,
                                   boxstyle="round,pad=0.008", facecolor="#f8fafc",
                                   edgecolor=color, linewidth=2))
        ax.text(middle, 0.715, title, ha="center", color=color, weight="bold")
        labels = sorted(cycle_label(p) for p in orbit)
        ax.text(middle, 0.615, "  ".join(labels), ha="center", fontsize=18, color=color)
        ax.text(middle, 0.525, f"Class size: {len(orbit)}", ha="center", weight="bold")
        c_text = ("C(e) = S₃" if j == 0 else
                  "C((12)) = {e, (12)}" if j == 1 else
                  "C((123)) = {e, (123), (132)}")
        ax.text(middle, 0.435, c_text, ha="center", fontsize=11)
        ax.text(middle, 0.365, f"6 / {len(centralizer)} = {len(orbit)}",
                ha="center", fontsize=15)
    ax.text(0.5, 0.235, "Class equation:  6 = 1 + 3 + 2       Center: {e}",
            ha="center", fontsize=16, weight="bold")
    ax.text(0.5, 0.135, "Relabel with g = (123):  (12) → (g(1) g(2)) = (23)",
            ha="center", fontsize=14)
    ax.text(0.5, 0.065, "Conjugation: g x g⁻¹. Apply the rightmost factor first.",
            ha="center", fontsize=12, color="#475569")
    fig.subplots_adjust(left=0.01, right=0.99, bottom=0.02, top=0.99)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print({"elements": len(group), "class_sizes": list(map(len, classes)),
           "centralizer_sizes": list(map(len, centralizers)), "center": ["e"]})


if __name__ == "__main__":
    main()
