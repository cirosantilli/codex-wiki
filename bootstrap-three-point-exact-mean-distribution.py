"""Enumerate every ordered bootstrap sample; emit the matching PNG in CWD."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    counts = Counter(sum(sample) for sample in product((1, 2, 4), repeat=3))
    sums = np.arange(3, 13)
    means = sums / 3
    weights = np.array([counts[int(s)] for s in sums])
    assert weights.sum() == 27
    assert sum(Fraction(s, 3)*Fraction(c, 27) for s, c in counts.items()) == Fraction(7, 3)
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=120)
    fig.patch.set_facecolor("white")
    ax.bar(means, weights/27, width=.23, color="#397a9e", edgecolor="#20556f", zorder=3)
    for x, c in zip(means, weights):
        ax.text(x, c/27+.008, f"{c}/27", ha="center", fontsize=12)
    ax.axvline(7/3, color="#a15820", ls="--", lw=1.7, label=r"Original mean $7/3$")
    ax.set_xticks(means, [str(Fraction(int(s), 3)) for s in sums], fontsize=12)
    ax.set_xlabel(r"Bootstrap sample mean $\overline{X}^{*}$", fontsize=14)
    ax.set_ylabel("Exact conditional probability", fontsize=13)
    ax.set_ylim(0, .28)
    ax.set_xlim(.78, 4.23)
    ax.set_title("All 27 ordered resamples of (1, 2, 4)", fontsize=19, weight="bold", pad=20)
    ax.grid(axis="y", color="#dddddd", lw=.7, zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", frameon=False, fontsize=11)
    fig.text(.5, .035, r"Counts are exact enumeration, not simulated frequencies.   $\mathrm{Var}_{*}(\overline{X}^{*})=14/27$", ha="center", fontsize=12)
    fig.subplots_adjust(left=.1, right=.97, top=.85, bottom=.19)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
