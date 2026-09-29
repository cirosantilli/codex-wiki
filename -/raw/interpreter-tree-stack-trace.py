"""Compare an original expression tree and stack trace; emit PNG into CWD.

Tested with Python 3.14, matplotlib 3.10.7; no optional dependencies.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    fig, ax = plt.subplots(figsize=(10, 6.4), dpi=120, facecolor="white")
    ax.set(xlim=(0, 10), ylim=(0, 6.4))
    ax.axis("off")
    ink = "#243746"
    ax.text(5, 6.08, "Same expression, same input, two execution paths",
            ha="center", fontsize=16, weight="bold", color=ink)
    ax.text(5, 5.65, "x*(2+3)-4       x = 7       exact integer arithmetic",
            ha="center", fontsize=12, color=ink)
    ax.text(2.45, 5.2, "Original AST evaluation", ha="center", fontsize=13,
            weight="bold", color=ink)
    nodes = {
        "sub": (2.6, 4.4, "−", "31"),
        "mul": (1.65, 3.4, "×", "35"),
        "four": (3.6, 3.4, "4", ""),
        "x": (0.7, 2.4, "x", "7"),
        "add": (2.5, 2.4, "+", "5"),
        "two": (1.8, 1.4, "2", ""),
        "three": (3.2, 1.4, "3", ""),
    }
    for parent, child in [("sub", "mul"), ("sub", "four"), ("mul", "x"),
                           ("mul", "add"), ("add", "two"), ("add", "three")]:
        px, py, *_ = nodes[parent]
        cx, cy, *_ = nodes[child]
        ax.plot([px, cx], [py-0.18, cy+0.18], color=ink, linewidth=1.3, zorder=1)
    for x, y, label, value in nodes.values():
        ax.add_patch(FancyBboxPatch((x-0.29, y-0.2), 0.58, 0.4,
                                   boxstyle="round,pad=0.06", facecolor="#e9f2fc",
                                   edgecolor=ink, zorder=2))
        ax.text(x, y, label, ha="center", va="center", fontsize=15, color=ink)
        if value:
            ax.text(x+0.38, y+0.08, "→ " + value, fontsize=11, color="#28734a")
    ax.text(2.45, 0.67, "2+3 → 5       7×5 → 35       35−4 → 31",
            ha="center", fontsize=11, color=ink)
    ax.plot([4.85, 4.85], [0.45, 5.25], color="#d2dae0", linewidth=1)
    ax.text(7.35, 5.2, "Folded stack instruction trace", ha="center",
            fontsize=13, weight="bold", color=ink)
    rows = [("initial", "[]"), ("LOAD x", "[7]"), ("PUSH 5", "[7, 5]"),
            ("MUL", "[35]"), ("PUSH 4", "[35, 4]"), ("SUB", "[31]")]
    ax.text(5.5, 4.65, "Instruction", fontsize=11, weight="bold", color=ink)
    ax.text(7.75, 4.65, "Stack after", fontsize=11, weight="bold", color=ink)
    for i, (instruction, stack) in enumerate(rows):
        y = 4.2 - i*0.5
        if i % 2 == 1:
            ax.add_patch(FancyBboxPatch((5.35, y-0.18), 4.1, 0.36,
                                       boxstyle="square,pad=0", facecolor="#edf7ee",
                                       edgecolor="none"))
        ax.text(5.5, y, instruction, fontsize=12, family="monospace", va="center", color=ink)
        ax.text(7.75, y, stack, fontsize=12, family="monospace", va="center", color=ink)
    ax.text(7.35, 0.96, "Stack top is on the right.", ha="center", fontsize=11, color=ink)
    ax.text(7.35, 0.55, "SUB pops right = 4, then left = 35.", ha="center", fontsize=11, color=ink)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
