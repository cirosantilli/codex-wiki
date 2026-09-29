"""Draw an original dense matrix-chain cost example; emit PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7; no external data.
"""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 6.3), dpi=100)
    fig.patch.set_facecolor("white")
    fig.suptitle("Same product, different intermediate dimensions", fontsize=20, y=0.96)
    fig.text(0.5, 0.865, "A: 12 × 5       B: 5 × 40       C: 40 × 3", ha="center", fontsize=15)
    colors = ["#9c443e", "#187569"]
    for ax, color in zip(axes, colors):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        def node(x, y, label, leaf=False):
            ax.text(x, y, label, ha="center", va="center", fontsize=13,
                    bbox=dict(boxstyle="round,pad=0.55", facecolor="white" if leaf else "#f0f5f7",
                              edgecolor="#566c79" if leaf else color, linewidth=1.6), zorder=3)

        def edge(start, end):
            ax.plot([start[0], end[0]], [start[1], end[1]], color=color, linewidth=2, zorder=1)

        if ax is axes[0]:
            root, intermediate = (0.61, 0.70), (0.34, 0.42)
            leaves = [(0.10, 0.10), (0.49, 0.10), (0.88, 0.10)]
            node(*root, "(AB)C: 12 × 3\nlocal cost: 1440")
            node(*intermediate, "AB: 12 × 40\nlocal cost: 2400")
            edge(root, intermediate)
            edge(root, leaves[2])
            edge(intermediate, leaves[0])
            edge(intermediate, leaves[1])
            ax.text(0.5, 0.96, "(AB)C", ha="center", fontsize=21, color=color)
            ax.text(0.5, -0.09, "Total: 2400 + 1440 = 3840", ha="center", fontsize=16, color=color)
        else:
            root, intermediate = (0.39, 0.70), (0.66, 0.42)
            leaves = [(0.12, 0.10), (0.51, 0.10), (0.90, 0.10)]
            node(*root, "A(BC): 12 × 3\nlocal cost: 180")
            node(*intermediate, "BC: 5 × 3\nlocal cost: 600")
            edge(root, leaves[0])
            edge(root, intermediate)
            edge(intermediate, leaves[1])
            edge(intermediate, leaves[2])
            ax.text(0.5, 0.96, "A(BC)", ha="center", fontsize=21, color=color)
            ax.text(0.5, -0.09, "Total: 600 + 180 = 780", ha="center", fontsize=16, color=color)
        for pos, label in zip(leaves, ["A\n12 × 5", "B\n5 × 40", "C\n40 × 3"]):
            node(*pos, label, leaf=True)

    fig.text(0.5, 0.035, "Exact operation counts in ordinary dense multiplication; not measured running times.",
             ha="center", fontsize=12, color="#47535c")
    fig.subplots_adjust(left=0.05, right=0.95, bottom=0.20, top=0.78, wspace=0.15)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
