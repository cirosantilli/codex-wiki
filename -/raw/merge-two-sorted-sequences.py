"""Compute a head-comparison trace and save an opaque PNG to cwd.

Tested with Python 3.14.4, Matplotlib 3.10.7 and NumPy 2.3.5.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


LEFT = (1, 4, 7)
RIGHT = (2, 3, 8, 9)


def merge_trace(left, right):
    output, trace = [], []
    i = j = 0
    while i < len(left) and j < len(right):
        a, b = left[i], right[j]
        take_left = a <= b
        chosen = a if take_left else b
        output.append(chosen)
        trace.append((a, b, take_left, tuple(output)))
        if take_left:
            i += 1
        else:
            j += 1
    remainder = tuple(left[i:]) + tuple(right[j:])
    return tuple(output) + remainder, trace, remainder


def cell(ax, x, y, value, chosen=False):
    ax.add_patch(FancyBboxPatch((x - 0.28, y - 0.23), 0.56, 0.46,
                              boxstyle="round,pad=0.04", linewidth=1,
                              facecolor="#ffe0ac" if chosen else "#e3eef8",
                              edgecolor="#577187", zorder=3))
    ax.text(x, y, str(value), ha="center", va="center", fontsize=14, zorder=4)


def main():
    output, trace, remainder = merge_trace(LEFT, RIGHT)
    assert output == (1, 2, 3, 4, 7, 8, 9)
    assert [(a, b) for a, b, _, _ in trace] == [(1, 2), (4, 2), (4, 3), (4, 8), (7, 8)]
    assert len(trace) == 5 and remainder == (8, 9)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    fig, ax = plt.subplots(figsize=(10, 6.6), facecolor="white")
    ax.text(0.1, 6.1, "Left: (1, 4, 7)       Right: (2, 3, 8, 9)", fontsize=14)
    for x, text in [(0.1, "Step"), (1.65, "Left head"), (3.15, "Right head"),
                    (4.8, "Take"), (6.05, "Output so far")]:
        ax.text(x, 5.5, text, fontsize=12, ha="left" if x in (0.1, 6.05) else "center")
    for step, (a, b, take_left, prefix) in enumerate(trace, 1):
        y = 5.0 - 0.8 * (step - 1)
        ax.text(0.28, y, str(step), va="center")
        cell(ax, 1.65, y, a, chosen=take_left)
        cell(ax, 3.15, y, b, chosen=not take_left)
        cell(ax, 4.8, y, prefix[-1], chosen=True)
        source_x = 1.99 if take_left else 3.49
        ax.annotate("", xy=(4.46, y), xytext=(source_x, y),
                    arrowprops={"arrowstyle": "->", "color": "#b36c16",
                                "connectionstyle": "arc3,rad=-0.24" if take_left else "arc3,rad=0"},
                    zorder=2)
        ax.text(6.05, y, "  ".join(map(str, prefix)), va="center", fontsize=14)
    ax.text(0.1, 0.88, "Left exhausted", fontsize=12, va="center")
    ax.text(3.15, 0.88, "8  9", ha="center", va="center", fontsize=14)
    ax.annotate("", xy=(5.7, 0.88), xytext=(3.6, 0.88),
                arrowprops={"arrowstyle": "->", "color": "#5a9270"})
    ax.text(6.05, 0.88, "  ".join(map(str, output)), va="center", fontsize=14)
    ax.text(0.1, 0.2, "5 head comparisons; append (8, 9) without comparing keys. Bound: 3 + 4 − 1 = 6.",
            fontsize=11, color="#172c3c")
    ax.set(xlim=(-0.05, 9.6), ylim=(-0.05, 6.6))
    ax.axis("off")
    fig.suptitle("Merge: compare the two heads, then advance one", fontsize=17, y=0.98)
    fig.subplots_adjust(left=0.025, right=0.99, top=0.91, bottom=0.025)
    fig.savefig(Path.cwd() / "merge-two-sorted-sequences.png", dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Output: {output}; head comparisons: {len(trace)}; appended remainder: {remainder}")


if __name__ == "__main__":
    main()
