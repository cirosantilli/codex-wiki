"""Original independent-choice probability inventory; PNG basename to CWD."""
from fractions import Fraction
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np


def main():
    rows = [(Fraction(3, 4), Fraction(1, 4)),
            (Fraction(1, 5), Fraction(4, 5))]
    outcomes = list(product(range(2), repeat=2))
    probabilities = [rows[0][i]*rows[1][j] for i, j in outcomes]
    distinct = [i != j for i, j in outcomes]
    assert sum(probabilities) == 1
    assert sum(p for p, valid in zip(probabilities, distinct) if valid) == Fraction(13, 20)
    fig, ax = plt.subplots(figsize=(7.6, 4.5), dpi=120)
    fig.patch.set_facecolor("white")
    values = [float(p) for p in probabilities]
    colors = ["#28865b" if valid else "#999999" for valid in distinct]
    xs = np.arange(4)
    ax.bar(xs, values, color=colors, width=.63)
    for i, probability in enumerate(probabilities):
        ax.text(i, float(probability)+.018,
                f"{probability} = {float(probability):.2f}",
                ha="center", fontsize=11)
    ax.set_xticks(xs, [str(tuple(x+1 for x in outcome)) for outcome in outcomes])
    ax.set_ylim(0, .73)
    ax.set_xlabel("Ordered choices (first person, second person)", fontsize=11)
    ax.set_ylabel("Probability", fontsize=11)
    ax.grid(axis="y", alpha=.17)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(handles=[Patch(color="#28865b", label="Distinct: total 0.65"),
                       Patch(color="#999999", label="Same label: total 0.35")],
              fontsize=11, frameon=False, loc="upper right")
    fig.suptitle("The permanent adds the distinct-choice probabilities",
                 fontsize=14, y=.98)
    ax.set_title("Independent choices: first (3/4, 1/4), second (1/5, 4/5)",
                 fontsize=11.5, pad=12)
    fig.subplots_adjust(left=.1, right=.98, top=.78, bottom=.19)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
