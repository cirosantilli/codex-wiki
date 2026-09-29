"""Compare multiplication by a unit and a zero divisor modulo twelve.

Run from _media to write the PNG to CWD. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (distribution build 3.10.7+dfsg1).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12})
    fig, ax = plt.subplots(figsize=(9, 3.7), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.04, right=0.98, bottom=0.17, top=0.82)
    inputs = np.arange(12)
    palette = plt.get_cmap("tab20")
    colors = [palette(i) for i in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 2)]
    ax.text(-0.2, 2.45, "Input x", ha="right", va="center")
    for x in inputs:
        ax.text(x + 0.5, 2.45, str(x), ha="center", va="center")
    for factor, y in [(5, 1.55), (6, 0.2)]:
        outputs = factor * inputs % 12
        ax.text(-0.2, y + 0.35, f"{factor}x mod 12", ha="right", va="center")
        for x, output in zip(inputs, outputs):
            ax.add_patch(Rectangle((x + 0.03, y), 0.94, 0.7,
                                    facecolor=colors[output],
                                    edgecolor="#ffffff", linewidth=1))
            ax.text(x + 0.5, y + 0.35, str(output), ha="center",
                    va="center", color="#17212b", fontsize=13, weight="bold")
        note = ("Every output appears once; multiplying by 5 reverses the row"
                if factor == 5 else
                "Only 0 and 6 appear; inputs 0 and 2 both give 0")
        ax.text(6, y - 0.22, note, ha="center", va="center", fontsize=11)
    ax.set(xlim=(-2.1, 12.1), ylim=(-0.48, 2.8))
    ax.axis("off")
    fig.suptitle("Multiplication modulo twelve: reversible or many-to-one",
                 fontsize=15, y=0.96)
    fig.text(0.5, 0.075, "Units: 1, 5, 7, 11     |     Same output = same cell color",
             ha="center", fontsize=12)
    fig.savefig(Path.cwd() / "modular-multiplication-units-and-zero-divisors.png",
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
