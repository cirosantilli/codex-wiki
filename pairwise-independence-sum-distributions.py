"""Original exact sum comparison. Tested: Python 3.14.4, Matplotlib 3.10.7.

Run from _media; writes the matching PNG basename to the current directory.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    parity_sums = [u + v + (u ^ v) for u, v in product((0, 1), repeat=2)]
    iid_sums = [sum(t) for t in product((0, 1), repeat=3)]
    laws = [[Fraction(values.count(s), len(values)) for s in range(4)]
            for values in (parity_sums, iid_sums)]
    for law in laws:
        mean = sum(s*p for s, p in enumerate(law))
        variance = sum((s-mean)**2*p for s, p in enumerate(law))
        assert mean == Fraction(3, 2) and variance == Fraction(3, 4)
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=120, facecolor="white")
    colors = ["#24759c", "#dc8b35"]
    labels = ["Parity: pairwise independent", "Binomial(3, 1/2): mutually independent"]
    width = .34
    for i, (law, color, label) in enumerate(zip(laws, colors, labels)):
        positions = [s + (i-.5)*width for s in range(4)]
        ax.bar(positions, [float(p) for p in law], width=width,
               color=color, label=label, zorder=3)
        for x, p in zip(positions, law):
            ax.text(x, float(p)+.018, str(p), ha="center", va="bottom", fontsize=12)
    ax.set_title("Same mean and variance, different sum laws", fontsize=17, pad=18)
    ax.set_xlabel("Sum of the three bits")
    ax.set_ylabel("Probability")
    ax.set_xticks(range(4))
    ax.set_yticks([0, .25, .5, .75], ["0", "1/4", "1/2", "3/4"])
    ax.set_ylim(0, 1.0)
    ax.set_xlim(-.6, 3.6)
    ax.grid(axis="y", color="#e2e8ec", zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=11)
    fig.text(.5, .05, "Both: mean = 3/2, variance = 3/4.    Parity sum: values 1 and 3 are impossible.",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=.12, right=.97, top=.86, bottom=.20)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
