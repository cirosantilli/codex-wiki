"""Draw two explicit schedules of an abstract indivisible-step counter model.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; write the opaque matching PNG to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def trace(schedule):
    """Return states after each step, keeping each thread's register separate."""
    x, registers, next_step = 0, [None, None], [0, 0]
    rows = [("Initial", "—", "—", x, None)]
    for step, thread in enumerate(schedule, 1):
        action = ("load x", "add 1", "store r")[next_step[thread]]
        if next_step[thread] == 0:
            registers[thread] = x
        elif next_step[thread] == 1:
            registers[thread] += 1
        else:
            x = registers[thread]
        next_step[thread] += 1
        rows.append((f"{step}. T{thread + 1}: {action}",
                     *["—" if r is None else str(r) for r in registers], x, thread))
    assert next_step == [3, 3]
    return rows


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
    ink, blue, green, red = "#203040", "#155d8a", "#187355", "#a0392a"
    fig, ax = plt.subplots(figsize=(11, 6.3), dpi=110, facecolor="white")
    ax.set(xlim=(0, 11), ylim=(0, 6.3), facecolor="white")
    ax.axis("off")
    ax.text(5.5, 6.04, "Two increments: separate registers, one shared counter",
            ha="center", fontsize=17, weight="bold", color=ink)
    ax.text(5.5, 5.62, "Abstract model: each load / add / store is indivisible; time runs downward",
            ha="center", fontsize=11, color=ink)

    panels = [(0.3, "Interleaved: lost update", [0, 1, 0, 1, 0, 1], 1, red),
              (5.85, "Serial: T1 then T2", [0, 0, 0, 1, 1, 1], 2, green)]
    row_positions = np.linspace(4.27, 1.57, 7)
    for left, title, schedule, result, color in panels:
        rows = trace(schedule)
        assert rows[-1][3] == result
        ax.text(left + 2.4, 5.09, title, ha="center", fontsize=14,
                weight="bold", color=color)
        ax.add_patch(Rectangle((left + 3.86, 1.34), 0.92, 3.5,
                               facecolor="#fff1dc", edgecolor="none"))
        ax.text(left + 0.05, 4.74, "Logical step", color=ink, weight="bold")
        for offset, label, label_color in [(2.65, "r1", blue), (3.45, "r2", green),
                                            (4.32, "shared x", ink)]:
            ax.text(left + offset, 4.74, label, ha="center", fontsize=11,
                    color=label_color, weight="bold")
        for y, (action, r1, r2, x, thread) in zip(row_positions, rows):
            active_color = ink if thread is None else (blue, green)[thread]
            ax.plot([left, left + 4.85], [y - 0.23, y - 0.23],
                    color="#d7dfe5", lw=0.7)
            ax.text(left + 0.05, y, action, va="center", color=active_color)
            ax.text(left + 2.65, y, r1, ha="center", va="center", color=blue)
            ax.text(left + 3.45, y, r2, ha="center", va="center", color=green)
            ax.text(left + 4.32, y, str(x), ha="center", va="center",
                    color=ink, weight="bold")
        ax.text(left + 2.4, 0.94, f"Final x = {result}", ha="center", fontsize=15,
                weight="bold", color=color)
    ax.text(5.5, 0.48, "A load reads the latest preceding store. Adding changes only that thread's register.",
            ha="center", fontsize=11, color=ink)
    ax.text(5.5, 0.12, "This is not an unprotected C program: C data races have undefined behavior.",
            ha="center", fontsize=11, color=ink)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"),
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
