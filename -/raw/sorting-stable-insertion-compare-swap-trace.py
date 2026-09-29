"""Draw an original adjacent-swap insertion-sort trace; write PNG to CWD.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media with MPLBACKEND=Agg and a writable MPLCONFIGDIR.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def insertion_trace(entries):
    """Return complete states after each key comparison, including stopped ties."""
    current = list(entries)
    steps = []
    for i in range(1, len(current)):
        j = i
        while j > 0:
            left, right = current[j - 1], current[j]
            swap = right[0] < left[0]
            if swap:
                current[j - 1], current[j] = right, left
            steps.append({"pass": i, "pair": (left, right), "swap": swap,
                          "positions": (j - 1, j), "state": tuple(current)})
            if not swap:
                break
            j -= 1
    return tuple(current), steps


def draw():
    original = ((2, "A"), (1, "B"), (2, "C"), (1, "D"))
    result, steps = insertion_trace(original)
    assert result == ((1, "B"), (1, "D"), (2, "A"), (2, "C"))
    assert len(steps) == 5 and sum(s["swap"] for s in steps) == 3
    fig, ax = plt.subplots(figsize=(9.4, 6.4), dpi=110, facecolor="white")
    ax.set(xlim=(-0.1, 10.0), ylim=(-0.45, 7.15))
    ax.axis("off")
    ax.text(0, 6.88, "Stable insertion sort: compare keys, swap whole entries",
            fontsize=15, weight="bold", color="#182f46")
    ax.text(0, 6.47, "Letter = original identity / payload; letters are never compared.",
            fontsize=11, color="#334b60")
    states = [original] + [s["state"] for s in steps]
    for row, state in enumerate(states):
        y = 5.65 - row * 0.94
        ax.text(0, y + 0.27, "Input" if row == 0 else f"Compare {row}",
                fontsize=11, va="center", weight="bold")
        for col, (key, identity) in enumerate(state):
            x = 1.25 + col * 0.88
            marked = row > 0 and col in steps[row - 1]["positions"]
            color = "#e5f0f9" if not marked else (
                "#fff0d2" if steps[row - 1]["swap"] else "#e0f2e7")
            ax.add_patch(FancyBboxPatch((x, y), 0.72, 0.57,
                         boxstyle="round,pad=0.03", facecolor=color,
                         edgecolor="#647b8d", linewidth=1.2))
            ax.text(x + 0.36, y + 0.285, f"{key}{identity}",
                    ha="center", va="center", fontsize=14, weight="bold")
        if row:
            step = steps[row - 1]
            left, right = step["pair"]
            label = f"{right[0]} < {left[0]}? "
            label += "yes: swap" if step["swap"] else "no: stop this pass"
            ax.text(4.98, y + 0.34, label, fontsize=12, va="center")
            ax.text(4.98, y + 0.02, f"Insert original position {step['pass']}",
                    fontsize=10, color="#526775", va="center")
    ax.text(0, -0.20, "5 key comparisons • 3 adjacent swaps • ties stay in arrival order",
            fontsize=12, weight="bold", color="#285c43")
    fig.subplots_adjust(left=0.035, right=0.99, bottom=0.03, top=0.99)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    draw()
