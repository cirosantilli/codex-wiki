"""Draw all orderings of ABC; tested with Python 3.14.4 and matplotlib 3.10.7+dfsg1.

Write factorial-permutation-choice-tree.png in the current directory.
"""

from itertools import permutations
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    words = ["".join(p) for p in permutations("ABC")]
    colors = {"A": "#246d9a", "B": "#b45925", "C": "#388363"}
    fig, ax = plt.subplots(figsize=(8.4, 5.4), dpi=120, facecolor="white")
    nodes = {"": (0, 2.5)}
    for depth in range(1, 4):
        for prefix in sorted({word[:depth] for word in words}):
            leaves = [i for i, word in enumerate(words) if word.startswith(prefix)]
            nodes[prefix] = (depth, sum(leaves) / len(leaves))
    for prefix, (x, y) in nodes.items():
        color = colors[prefix[0]] if prefix else "#344454"
        if prefix:
            parent_x, parent_y = nodes[prefix[:-1]]
            ax.plot([parent_x, x], [parent_y, y], color=color, lw=1.7, zorder=1)
        ax.text(x, y, prefix or "Start", ha="center", va="center", fontsize=14,
                color=color, zorder=2,
                bbox={"boxstyle": "round,pad=0.35", "fc": "white", "ec": color})
    for x, label in enumerate(["", "First: 3 choices", "Second: 2 choices", "Third: 1 choice"]):
        ax.text(x, 5.8, label, ha="center", fontsize=11, color="#344454")
    ax.set(xlim=(-0.35, 3.55), ylim=(6.2, -0.6))
    ax.axis("off")
    fig.suptitle("Three distinct letters, six complete orderings", fontsize=16)
    fig.text(0.5, 0.04, "ABC    ACB    BAC    BCA    CAB    CBA       |       3 × 2 × 1 = 3! = 6",
             ha="center", fontsize=12, color="#344454")
    fig.subplots_adjust(left=0.03, right=0.97, top=0.88, bottom=0.1)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
