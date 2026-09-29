"""Independent identical gates with an all-open conduction requirement.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes an opaque white PNG to the current working directory.
"""
from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (curves, states) = plt.subplots(1, 2, figsize=(11.2, 5.5),
                                       facecolor="white")
    fig.subplots_adjust(left=.075, right=.98, bottom=.19, top=.77, wspace=.28)
    fig.suptitle(r"All gates must be open: channel probability = $p^q$", y=.97,
                 fontsize=16)
    fig.text(.5, .90, "Identical independent permissive gates • "
             "one conducting configuration for four gates", ha="center", fontsize=11)
    p = np.linspace(0., 1., 501)
    for q, color in [(1, "#207ea2"), (2, "#bc5b22"), (4, "#61459a")]:
        curves.plot(p, p ** q, lw=2.5, color=color, label=f"q = {q}: p" +
                    ({1: "", 2: "²", 4: "⁴"}[q]))
        curves.plot(.5, .5 ** q, "o", color=color, ms=6)
        curves.annotate(f"{.5 ** q:g}", (.5, .5 ** q),
                        xytext=(9, 5), textcoords="offset points", color=color,
                        fontsize=10)
    curves.axvline(.5, color="#8997a3", ls=":", lw=1)
    curves.set(xlim=(0, 1), ylim=(0, 1.04), xlabel="Gate-open probability p",
               ylabel="Whole-channel open probability", title="A. One, two or four gates")
    curves.legend(loc="upper left", fontsize=10)
    curves.grid(alpha=.16)

    states.set(xlim=(-.08, 4.08), ylim=(-.1, 4.3), aspect="equal")
    states.axis("off")
    states.set_title("B. Four gates at p = 0.5", pad=17)
    for index, bits in enumerate(product([0, 1], repeat=4)):
        row, col = divmod(index, 4)
        bottom = 3 - row
        conducting = all(bits)
        states.add_patch(FancyBboxPatch(
            (col + .04, bottom + .04), .91, .89,
            boxstyle="round,pad=.015", linewidth=1.6 if conducting else .8,
            facecolor="#e2f4e7" if conducting else "white",
            edgecolor="#277b42" if conducting else "#c7d0d8"))
        for gate, bit in enumerate(bits):
            states.add_patch(Circle((col + .20 + .19 * gate, bottom + .64), .061,
                                    facecolor="#207ea2" if bit else "white",
                                    edgecolor="#207ea2", linewidth=1.2))
        states.text(col + .495, bottom + .39, "".join(map(str, bits)),
                    ha="center", fontsize=10, family="DejaVu Sans Mono")
        states.text(col + .495, bottom + .16,
                    "conducts" if conducting else "blocked", ha="center", fontsize=9,
                    color="#277b42" if conducting else "#697784")
    states.text(2., 4.04, "Each configuration has probability 1/16", ha="center", fontsize=10)
    fig.text(.5, .07, "Filled circle / 1 = open gate; empty circle / 0 = closed gate. "
             "Only 1111 permits conduction: (0.5)⁴ = 0.0625.", ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
