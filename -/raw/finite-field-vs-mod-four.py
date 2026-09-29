"""Compare F4's permutation with a collapsing map modulo four; PNG to cwd.

Tested with Python 3.14.4 and the repository's matplotlib dependency.
Field products are computed by polynomial multiplication and binary reduction.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def field_multiply(x, y):
    raw = 0
    for bit in range(2):
        if y & (1 << bit):
            raw ^= x << bit
    if raw & 4:
        raw ^= 0b111  # t**2 + t + 1
    return raw


def node(ax, point, label, color):
    ax.add_patch(Circle(point, 0.26, facecolor=color, edgecolor="#52616e", lw=1.2,
                        zorder=3))
    ax.text(*point, label, fontsize=13 if "+" in label else 17,
            ha="center", va="center", zorder=4)


def edge(ax, start, end, color, curve=0):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "lw": 2.2, "color": color,
                            "shrinkA": 20, "shrinkB": 20, "mutation_scale": 16,
                            "connectionstyle": f"arc3,rad={curve}"}, zorder=2)


def loop(ax, point, color):
    x, y = point
    ax.annotate("", xy=(x + 0.20, y + 0.16), xytext=(x - 0.20, y + 0.16),
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2,
                            "mutation_scale": 15, "connectionstyle": "arc3,rad=-2.4"})


def main():
    field_outputs = [field_multiply(2, x) for x in range(4)]
    ring_outputs = [(2 * x) % 4 for x in range(4)]
    assert field_outputs == [0, 2, 3, 1]
    assert ring_outputs == [0, 2, 0, 2]
    assert len(set(field_outputs)) == 4 and len(set(ring_outputs)) == 2
    assert [(1 ^ 1), (1 + 1) % 4] == [0, 2]
    assert [field_multiply(x, x) for x in range(1, 4)] == [1, 3, 2]
    assert [x for x in range(1, 4)
            if any((x * y) % 4 == 1 for y in range(1, 4))] == [1, 3]
    swap = [0, 1, 3, 2]
    for x in range(4):
        for y in range(4):
            assert swap[x ^ y] == swap[x] ^ swap[y]
            assert swap[field_multiply(x, y)] == field_multiply(swap[x], swap[y])
    print("Multiply by alpha in F4:", field_outputs)
    print("Multiply by 2 modulo 4:", ring_outputs)
    print("Checked characteristic 2 versus 4, modular units {1,3}, and alpha swap isomorphism.")

    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.9), dpi=120, facecolor="white")
    blue, orange = "#176997", "#a8521e"
    for ax in axes:
        ax.set_xlim(-2.45, 2.45)
        ax.set_ylim(-1.35, 3.3)
        ax.set_aspect("equal")
        ax.axis("off")
    left, right = axes
    left.text(0, 3.05, r"Field $\mathbb{F}_4$", fontsize=19, ha="center", weight="bold")
    right.text(0, 3.05, r"Ring $\mathbb{Z}/4\mathbb{Z}$", fontsize=19, ha="center", weight="bold")
    left.text(0, 2.58, r"$1+1=0$     (characteristic 2)", fontsize=13, ha="center")
    right.text(0, 2.58, r"$1+1=2\ne0$     (characteristic 4)", fontsize=13, ha="center")
    left.text(0, 2.12, r"Multiply by $\alpha$", fontsize=14, ha="center", color=blue)
    right.text(0, 2.12, "Multiply by 2", fontsize=14, ha="center", color=orange)

    field_points = {0: (-1.8, 0.7), 1: (0, 1.35), 2: (-0.7, -0.25), 3: (1.35, -0.25)}
    field_labels = ["0", "1", r"$\alpha$", r"$\alpha+1$"]
    colors = ["#f0f2f4", "#cce8f6", "#f9ddb3", "#ded5ed"]
    for x, point in field_points.items():
        node(left, point, field_labels[x], colors[x])
        if x:
            edge(left, point, field_points[field_outputs[x]], blue, curve=0.1)
    loop(left, field_points[0], blue)
    ring_points = {0: (-1.2, 0), 1: (-1.2, 1.35), 2: (1.2, 0), 3: (1.2, 1.35)}
    for x, point in ring_points.items():
        node(right, point, str(x), colors[x])
        if x:
            edge(right, point, ring_points[ring_outputs[x]], orange,
                 curve=0.1 if x == 1 else 0)
    loop(right, ring_points[0], orange)
    left.text(0, -0.9, "All three nonzero elements have inverses.", ha="center", fontsize=11)
    left.text(0, -1.2, "Four distinct inputs → four distinct outputs", ha="center", fontsize=11, color=blue)
    right.text(0, -0.9, r"$2^2=0$: nonzero 2 has no inverse.", ha="center", fontsize=11)
    right.text(0, -1.2, "Four distinct inputs → only two outputs", ha="center", fontsize=11, color=orange)
    fig.suptitle("Same number of elements, different arithmetic", fontsize=18, y=0.96)
    fig.subplots_adjust(left=0.035, right=0.98, top=0.89, bottom=0.065, wspace=0.12)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
