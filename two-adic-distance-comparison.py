"""Compare ordinary and 2-adic distances; write a white PNG to the CWD.

Tested with Python 3.14.4, NumPy 2.3.5, and Matplotlib 3.10.7.
"""

from fractions import Fraction
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def valuation_two(value):
    value = Fraction(value)
    if value == 0:
        raise ValueError("Zero has no finite valuation")

    def exponent(number):
        number = abs(number)
        count = 0
        while number % 2 == 0:
            number //= 2
            count += 1
        return count

    return exponent(value.numerator) - exponent(value.denominator)


def norm_two(value):
    return Fraction(0) if value == 0 else Fraction(2) ** -valuation_two(value)


def main():
    sample = np.arange(16)
    ordinary = np.abs(sample[:, None] - sample[None, :])
    adic = np.array([[float(norm_two(int(x - y))) for y in sample]
                     for x in sample])
    for value, exponent, norm in [(8, 3, Fraction(1, 8)),
                                  (12, 2, Fraction(1, 4)),
                                  (Fraction(3, 8), -3, Fraction(8)),
                                  (-7, 0, Fraction(1))]:
        assert valuation_two(value) == exponent
        assert norm_two(value) == norm
    assert norm_two(0) == 0
    assert adic[5, 13] == 1 / 8 and adic[5, 6] == 1
    for x in sample:
        for y in sample:
            for z in sample:
                assert adic[x, z] <= max(adic[x, y], adic[y, z])
    for n in range(1, 13):
        partial_sum = sum(2 ** k for k in range(n))
        assert partial_sum == 2 ** n - 1
        assert norm_two(partial_sum + 1) == Fraction(1, 2 ** n)

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.6), dpi=110)
    fig.patch.set_facecolor("white")
    for ax, distances, title, vmax, ticks, labels in [
        (axes[0], ordinary, r"Ordinary distance $|x-y|$", 15,
         [0, 1, 4, 8, 12, 15], ["0", "1", "4", "8", "12", "15"]),
        (axes[1], adic, r"2-adic distance $|x-y|_2$", 1,
         [0, 1 / 8, 1 / 4, 1 / 2, 1], ["0", "1/8", "1/4", "1/2", "1"]),
    ]:
        image = ax.imshow(distances, origin="lower", vmin=0, vmax=vmax,
                          cmap="Blues", interpolation="nearest")
        ax.set_xticks(sample, labels=[str(n) for n in sample], fontsize=8)
        ax.set_yticks(sample, labels=[str(n) for n in sample], fontsize=8)
        ax.set_xlabel("Integer y")
        ax.set_ylabel("Integer x")
        ax.set_title(title, fontsize=13, pad=12)
        bar = fig.colorbar(image, ax=ax, orientation="horizontal",
                           fraction=.055, pad=.13)
        bar.set_ticks(ticks, labels=labels)
        bar.set_label("Distance (separate scales)", fontsize=10)
        for y, color in [(6, "#d87915"), (13, "#a22482")]:
            ax.add_patch(Rectangle((y - .5, 4.5), 1, 1, fill=False,
                                   edgecolor=color, linewidth=2.2))
    fig.suptitle("The same integers, two notions of closeness", fontsize=16)
    fig.text(.5, .075,
             "Orange: (5, 6) has distances 1 and 1.   "
             "Purple: (5, 13) has distances 8 and 1/8.",
             ha="center", fontsize=10)
    fig.subplots_adjust(left=.06, right=.97, top=.86, bottom=.20, wspace=.24)
    fig.savefig(Path.cwd() / "two-adic-distance-comparison.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
