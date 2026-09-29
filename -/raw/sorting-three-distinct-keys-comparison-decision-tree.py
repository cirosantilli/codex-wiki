"""Draw an original comparison decision tree; write matching PNG to CWD.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
The labels a,b,c identify original entries, not numeric values.
"""

from pathlib import Path

import matplotlib.pyplot as plt


# Internal nodes: (left entry, right entry, yes child, no child).
TREE = {
    "root": ("a", "b", "left", "right"),
    "left": ("b", "c", "abc", "left_inner"),
    "left_inner": ("a", "c", "acb", "cab"),
    "right": ("a", "c", "bac", "right_inner"),
    "right_inner": ("b", "c", "bca", "cba"),
}


def decision_trace(keys):
    node, outcomes = "root", []
    while node in TREE:
        left, right, yes, no = TREE[node]
        answer = keys[left] < keys[right]
        outcomes.append((node, answer))
        node = yes if answer else no
    return node, outcomes


def draw():
    positions = {
        "root": (0.50, 0.82), "left": (0.25, 0.59), "right": (0.75, 0.59),
        "abc": (0.085, 0.35), "left_inner": (0.34, 0.35),
        "bac": (0.62, 0.35), "right_inner": (0.86, 0.35),
        "acb": (0.23, 0.11), "cab": (0.45, 0.11),
        "bca": (0.76, 0.11), "cba": (0.96, 0.11),
    }
    fig, ax = plt.subplots(figsize=(10.0, 6.1), dpi=110, facecolor="white")
    ax.set(xlim=(-0.015, 1.065), ylim=(-0.105, 1.04))
    ax.axis("off")
    ax.text(0.5, 1.00, "Three distinct keys require six possible output orders",
            ha="center", fontsize=15, weight="bold", color="#182f46")
    ax.text(0.5, 0.925, "a, b, c identify original entries; each test compares their keys.",
            ha="center", fontsize=11, color="#334b60")
    for parent, (left, right, yes, no) in TREE.items():
        x0, y0 = positions[parent]
        for child, answer in ((yes, "yes"), (no, "no")):
            x1, y1 = positions[child]
            ax.annotate("", xy=(x1, y1 + 0.035), xytext=(x0, y0 - 0.035),
                        arrowprops={"arrowstyle": "->", "color": "#738596", "lw": 1.5})
            ax.text((x0 + x1) / 2, (y0 + y1) / 2, answer,
                    ha="center", fontsize=10, color="#324b5e",
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for node, (x, y) in positions.items():
        internal = node in TREE
        label = f"{TREE[node][0]} < {TREE[node][1]}?" if internal else "  ".join(node)
        ax.text(x, y, label, ha="center", va="center", fontsize=12, weight="bold",
                bbox={"boxstyle": "round,pad=0.45", "edgecolor": "#54758c",
                      "facecolor": "#e5f0f9" if internal else "#e0f2e7"})
        if not internal:
            ax.text(x, y - 0.067, "output order", ha="center", fontsize=9, color="#526775")
    ax.text(0.5, -0.06, "6 leaves = 3!     •     maximum depth = 3     •     2² < 6 ≤ 2³",
            ha="center", fontsize=12, weight="bold", color="#285c43")
    fig.subplots_adjust(left=0.025, right=0.985, bottom=0.035, top=0.985)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    draw()
