"""Original Born-probability comparison of Z and Helstrom measurements.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7+dfsg1.
Run from _media; writes the matching opaque white PNG basename to cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    zero = np.array([1., 0.])
    plus = np.array([1., 1.]) / np.sqrt(2)
    states = [np.outer(zero, zero), np.outer(plus, plus)]
    eigenvalues, eigenvectors = np.linalg.eigh(states[0] - states[1])
    positive = eigenvectors[:, eigenvalues > 0]
    p_positive = positive @ positive.T
    measurements = [[states[0], np.eye(2) - states[0]],
                    [p_positive, np.eye(2) - p_positive]]
    probabilities = [np.array([[np.trace(effect @ state) for effect in effects]
                               for state in states]) for effects in measurements]
    successes = [0.5 * (values[0, 0] + values[1, 1]) for values in probabilities]
    gaps = [values[0, 0] - values[1, 0] for values in probabilities]
    blue, green, gold = "#2367a0", "#188454", "#a36d08"
    fig, axes = plt.subplots(1, 3, figsize=(10.6, 4.9), dpi=120,
                             gridspec_kw={"width_ratios": [1, 1, 0.85]})
    labels = [["0\nGuess zero", "1\nGuess plus"],
              ["+\nGuess zero", "−\nGuess plus"]]
    for idx, ax in enumerate(axes[:2]):
        x = np.arange(2)
        for state_idx, (color, label) in enumerate([(blue, r"Input $|0\rangle$"),
                                                   (green, r"Input $|+\rangle$")]):
            bars = ax.bar(x + (state_idx - 0.5) * 0.34,
                          probabilities[idx][state_idx], width=0.32,
                          color=color, label=label)
            ax.bar_label(bars, labels=[f"{v:.3f}" for v in probabilities[idx][state_idx]],
                         padding=4, fontsize=10)
        ax.set_xticks(x, labels[idx])
        ax.set_ylim(0, 1.15)
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_title(["Z measurement", "Optimal Helstrom measurement"][idx],
                     fontsize=12, pad=12)
        ax.set_xlabel(f"Outcome and decision\nEvent gap = TV = {gaps[idx]:.6f}",
                       labelpad=10, fontsize=10)
        ax.grid(axis="y", alpha=0.18)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Conditional outcome probability")
    bars = axes[2].bar([0, 1], successes, width=0.55, color=["#7c8791", gold])
    axes[2].bar_label(bars, labels=[f"{v:.6f}" for v in successes], padding=5,
                      fontsize=10)
    axes[2].set(ylim=(0, 1.15), title="Equal-prior success")
    axes[2].set_xticks([0, 1], ["Z", "Helstrom"])
    axes[2].set_yticks([0, 0.25, 0.5, 0.75, 1])
    axes[2].axhline(0.5, color="#555555", ls=":", lw=1.2)
    axes[2].text(0.5, 0.52, "Guessing: 0.5", ha="center", fontsize=10,
                 bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    axes[2].set_xlabel(f"Success gain: +{successes[1] - successes[0]:.6f}",
                       labelpad=10, fontsize=10)
    axes[2].grid(axis="y", alpha=0.18)
    axes[2].set_axisbelow(True)
    axes[2].spines[["top", "right"]].set_visible(False)
    fig.suptitle("Zero versus plus: the measurement basis changes distinguishability",
                 fontsize=15, y=0.97)
    handles, legend_labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, legend_labels, loc="upper center", bbox_to_anchor=(0.37, 0.9),
               ncol=2, frameon=False, fontsize=11)
    fig.text(0.5, 0.03,
             "For either input color, the two outcome probabilities sum to 1."
             "  Trials use separate copies.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.25, top=0.73, wspace=0.38)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
