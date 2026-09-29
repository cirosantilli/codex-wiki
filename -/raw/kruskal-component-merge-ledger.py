"""Draw component memberships, not union-find pointers; Python 3.14/matplotlib 3.10.7."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(11, 6.5), facecolor="white")
    fig.suptitle("The component ledger: reject a cycle, keep the partition",
                 fontsize=17, fontweight="bold", y=.96)
    rows = [
        ("Start", [["A"], ["B"], ["C"], ["D"], ["E"]], "—", 5, 0),
        ("AB  ·  1", [["A", "B"], ["C"], ["D"], ["E"]], "Different → merge", 4, 1),
        ("BC  ·  2", [["A", "B", "C"], ["D"], ["E"]], "Different → merge", 3, 3),
        ("AC  ·  3", [["A", "B", "C"], ["D"], ["E"]], "Same → reject", 3, 3),
        ("CD  ·  4", [["A", "B", "C", "D"], ["E"]], "Different → merge", 2, 7),
        ("DE  ·  5", [["A", "B", "C", "D", "E"]], "Different → merge", 1, 12),
    ]
    palette = {"A": "#d3eee6", "B": "#e0e8fa", "C": "#fff0ce",
               "D": "#e8dff4", "E": "#e0e9ee"}
    for x, title in [(.1, "Examined edge\n· weight"), (2.05, "Partition after decision"),
                     (5.95, "Endpoint blocks\nbefore decision"), (8.3, "Components"), (9.75, "Cost")]:
        ax.text(x, 6.55, title, fontweight="bold", ha="center" if x >= 8 else "left", va="center")
    for i, (edge, blocks, decision, count, cost) in enumerate(rows):
        y = 5.7 - i * .86
        if i == 3:
            ax.add_patch(FancyBboxPatch((-.1, y - .36), 10.25, .72,
                         boxstyle="round,pad=0.03", fc="#fff0f1", ec="none"))
        ax.text(.1, y, edge, va="center", fontweight="bold", color="#bf3346" if i == 3 else "#23374d")
        for block in blocks:
            start, end = ord(block[0]) - 65, ord(block[-1]) - 65
            x = 2.05 + start * .67
            ax.add_patch(FancyBboxPatch((x, y - .25), (end - start + 1) * .67 - .07, .5,
                         boxstyle="round,pad=0.025", fc=palette[block[0]], ec="#6c8597", lw=1))
            for v in block:
                ax.text(2.05 + (ord(v) - 65) * .67 + .3, y, v,
                        ha="center", va="center", fontweight="bold")
        ax.text(5.95, y, decision, va="center", color="#bf3346" if i == 3 else "#23374d")
        ax.text(8.3, y, str(count), ha="center", va="center")
        ax.text(9.75, y, str(cost), ha="center", va="center", fontweight="bold")
    ax.text(5, -.02, "find(u) = find(v)  ⇔  same block     |     union(u, v) merges different blocks",
            ha="center", fontsize=12, color="#23374d")
    ax.text(5, -.52, "Each acceptance: components −1, accepted edges +1.   Stop at 1 component and 4 edges.",
            ha="center", fontsize=11, color="#23374d")
    ax.set(xlim=(-.2, 10.3), ylim=(-.85, 7.05))
    ax.axis("off")
    fig.subplots_adjust(left=.04, right=.98, top=.85, bottom=.06)
    fig.savefig(Path(__file__).stem + ".png", dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
