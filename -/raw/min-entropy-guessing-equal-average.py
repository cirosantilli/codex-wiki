"""Exact toy sources: equal Shannon entropy, unequal single-guess success.

Run from _media with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
All heights are specified probabilities, not observations or simulations.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    sources = [("Uniform on four possible outcomes", np.array([.25, .25, .25, .25, 0.]),
                ["1/4", "1/4", "1/4", "1/4", "0"], "Any of A–D is a best guess", "2", "1/4"),
               ("One common outcome, four rare alternatives", np.array([.5, .125, .125, .125, .125]),
                ["1/2", "1/8", "1/8", "1/8", "1/8"], "A is the unique best guess", "1", "1/2")]
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 6.4), dpi=100, sharey=True)
    fig.subplots_adjust(left=.08, right=.98, top=.76, bottom=.30, wspace=.18)
    fig.suptitle("Same average surprise, different best guesses", fontsize=19, y=.96)
    fig.text(.5, .89, "Analytical probability models • base-two logarithms • no measured data",
             ha="center", color="#52606d", fontsize=11)
    for ax, (title, p, labels, rule, minimum, success) in zip(axes, sources):
        positive = p > 0
        entropy = float(-np.sum(p[positive] * np.log2(p[positive])))
        min_entropy = float(-np.log2(p.max()))
        assert np.isclose(p.sum(), 1) and np.isclose(entropy, 2)
        assert np.isclose(min_entropy, float(minimum))
        colors = ["#cc6e22" if value == p.max() else "#287aa0" for value in p]
        ax.bar(np.arange(5), p, width=.66, color=colors, edgecolor="white")
        for i, (value, label) in enumerate(zip(p, labels)):
            ax.text(i, value + .014, label, ha="center", va="bottom", fontsize=12)
        ax.set_title(title, fontsize=12, pad=15)
        ax.set_xticks(np.arange(5), list("ABCDE"))
        ax.set_ylim(0, .59)
        ax.set_yticks([0, .125, .25, .375, .5], ["0", "1/8", "1/4", "3/8", "1/2"])
        ax.set_xlabel("Outcome")
        ax.grid(axis="y", alpha=.18)
        ax.set_axisbelow(True)
        ax.text(.5, -.22, rule, transform=ax.transAxes, ha="center", color="#a64d11", fontsize=12)
        ax.text(.5, -.33, f"Best single-guess success = {success}", transform=ax.transAxes, ha="center")
        ax.text(.5, -.44, f"Shannon entropy = 2 bits; min-entropy = {minimum} bit" + ("s" if minimum == "2" else ""),
                transform=ax.transAxes, ha="center", fontsize=11)
    axes[0].set_ylabel("Probability")
    fig.text(.5, .06, "Orange marks optimal guesses. An impossible outcome contributes zero to average surprise.",
             ha="center", fontsize=11, color="#52606d")
    fig.savefig(Path(__file__).with_suffix('.png').name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
