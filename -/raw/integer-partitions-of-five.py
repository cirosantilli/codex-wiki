"""Enumerate and draw Ferrers diagrams; Python 3.14.4, matplotlib 3.10.7.

Write integer-partitions-of-five.png in the current directory.
"""

from itertools import combinations_with_replacement
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def partitions(total, largest=None):
    if total == 0:
        yield ()
        return
    if largest is None:
        largest = total
    for part in range(min(total, largest), 0, -1):
        for tail in partitions(total - part, part):
            yield (part,) + tail


def main():
    values = list(partitions(5))
    independent = {tuple(reversed(parts)) for length in range(1, 6)
                   for parts in combinations_with_replacement(range(1, 6), length)
                   if sum(parts) == 5}
    assert len(values) == 7 and set(values) == independent
    coefficients = [1] + [0] * 5
    for part in range(1, 6):
        for total in range(part, 6):
            coefficients[total] += coefficients[total - part]
    assert coefficients == [len(list(partitions(n))) for n in range(6)] == [1, 1, 2, 3, 5, 7]
    fig = plt.figure(figsize=(9, 5.9), dpi=120, facecolor="white")
    for index, parts in enumerate(values):
        row, column = divmod(index, 4)
        left = 0.03 + column * 0.24 + (0.12 if row == 1 else 0)
        bottom = 0.50 if row == 0 else 0.10
        ax = fig.add_axes((left, bottom, 0.22, 0.31))
        ax.set(xlim=(-0.5, 4.5), ylim=(4.5, -0.7))
        ax.set_aspect("equal")
        ax.axis("off")
        for i, part in enumerate(parts):
            ax.scatter(range(part), [i] * part, s=92, color="#186c9c")
        ax.set_title(" + ".join(map(str, parts)), fontsize=12, pad=8,
                     color="#253746")
    fig.suptitle("The seven integer partitions of five", fontsize=16, y=0.98)
    fig.text(0.5, 0.89, "One dot per unit; row lengths decrease from top to bottom.",
             ha="center", fontsize=11, color="#253746")
    fig.text(0.5, 0.035, "Order of summands is ignored: 3 + 2 and 2 + 3 give the same partition.",
             ha="center", fontsize=11, color="#253746")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)
    print(f"Independent enumerations agree: {values}; coefficients through degree five: {coefficients}.")


if __name__ == "__main__":
    main()
