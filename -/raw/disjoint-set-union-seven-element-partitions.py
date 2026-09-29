"""Draw an original seven-member union ledger; write the PNG to the CWD.

Tested with Python 3.14, matplotlib 3.10.7; see pyproject.toml.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    blocks = [{i} for i in range(1, 8)]
    states = [[set(b) for b in blocks]]
    calls = [(2, 1), (4, 3), (2, 4), (6, 5), (2, 6), (1, 2)]
    labels = ["Initial singletons"]
    for x, y in calls:
        a = next(b for b in blocks if x in b)
        b = next(b for b in blocks if y in b)
        changed = a is not b
        if changed:
            blocks = [c for c in blocks if c is not a and c is not b] + [a | b]
        states.append(sorted([set(b) for b in blocks], key=min))
        labels.append(f"unite({x}, {y})" + ("" if changed else "  →  False"))
    assert [len(s) for s in states] == [7, 6, 5, 4, 3, 2, 2]
    assert states[-1] == [set(range(1, 7)), {7}]

    fig, ax = plt.subplots(figsize=(10.4, 5.8), dpi=120, facecolor="white")
    ax.set(xlim=(-3.6, 8.5), ylim=(-0.85, 7.5))
    ax.axis("off")
    palette = {1: "#d6eaf8", 2: "#d6eaf8", 3: "#e8daf1", 4: "#e8daf1",
               5: "#d6eddf", 6: "#d6eddf", 7: "#fde8c8"}
    for index, (state, label) in enumerate(zip(states, labels)):
        y = 6 - index
        ax.text(-3.45, y, label, va="center", fontsize=11, color="#17324d")
        for block in state:
            left, right = min(block) - 0.37, max(block) + 0.37
            box = FancyBboxPatch((left, y - 0.31), right - left, 0.62,
                                 boxstyle="round,pad=0.04,rounding_size=0.13",
                                 facecolor=palette[min(block)], edgecolor="#62778b", lw=1.1)
            ax.add_patch(box)
            for member in block:
                ax.text(member, y, str(member), ha="center", va="center", fontsize=12)
        ax.text(8.0, y, str(len(state)), ha="center", va="center", fontsize=12)
    ax.text(4, 6.75, "Same seven members at every step", ha="center", fontsize=12)
    ax.text(8, 6.75, "Blocks", ha="center", fontsize=11)
    ax.text(2.4, -0.75, "One enclosure = one block; the final call merges nothing.",
            ha="center", fontsize=11, color="#384d60")
    fig.suptitle("Union changes the partition only when two blocks differ", fontsize=16, y=0.97)
    fig.subplots_adjust(left=0.025, right=0.985, top=0.87, bottom=0.06)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
