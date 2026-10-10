"""Compare coherent and mixed qubits using matrices and measurement outcomes.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory; writes an opaque white PNG in cwd.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    zero, one = np.eye(2)
    plus, minus = (zero + one) / np.sqrt(2), (zero - one) / np.sqrt(2)
    coherent = np.outer(plus, plus)
    mixture = (np.outer(zero, zero) + np.outer(one, one)) / 2
    states = (coherent, mixture)
    colors = ("#245f91", "#ba601b")
    labels = (r"Pure $|+\rangle$", r"Equal choice of $|0\rangle$, $|1\rangle$")
    cmap = LinearSegmentedColormap.from_list("matrix_values", ["white", "#8cb8d8"])
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.6), dpi=120,
                             gridspec_kw={"height_ratios": [1.05, 1]})
    for ax, state, label in zip(axes[0], states, labels):
        ax.imshow(state, cmap=cmap, vmin=0, vmax=0.5)
        ax.set(xticks=[0, 1], yticks=[0, 1], xticklabels=["0", "1"],
               yticklabels=["0", "1"], xlabel="Column (computational basis)",
               ylabel="Row", title=label)
        for row in range(2):
            for col in range(2):
                ax.text(col, row, f"{state[row, col]:.2f}", ha="center", va="center",
                        fontsize=19, color="#153d59")
        ax.set_xticks(np.arange(-0.5, 2, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 2, 1), minor=True)
        ax.grid(which="minor", color="#536f82", linewidth=0.8)
        ax.tick_params(which="both", length=0)
    for ax, vectors, ticks, title in zip(
            axes[1], ((zero, one), (plus, minus)),
            ((r"$|0\rangle$", r"$|1\rangle$"), (r"$|+\rangle$", r"$|-\rangle$")),
            ("Z measurement: same populations", "X measurement: different outcomes")):
        positions = np.arange(2)
        width = 0.32
        for idx, (state, color) in enumerate(zip(states, colors)):
            probabilities = [float(v @ state @ v) for v in vectors]
            bars = ax.bar(positions + (idx - 0.5) * width, probabilities,
                          width=width, color=color,
                          label=(r"Pure $|+\rangle$" if idx == 0 else r"Mixture $I/2$"))
            ax.bar_label(bars, labels=[f"{p:.2f}" for p in probabilities], padding=3,
                         fontsize=11)
        ax.set(xticks=positions, xticklabels=ticks, ylim=(0, 1.16),
               yticks=[0, 0.5, 1], ylabel="Outcome probability", title=title)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_axisbelow(True)
        ax.grid(axis="y", alpha=0.18)
    axes[1, 0].legend(frameon=False, fontsize=10, loc="upper center")
    fig.suptitle("Coherence versus mixture: matrices in the computational basis", fontsize=15)
    fig.tight_layout(rect=(0, 0.04, 1, 0.96), h_pad=1.3)
    fig.text(0.5, 0.016, "Z and X tests use separate identically prepared copies.",
             ha="center", fontsize=11, color="#444444")
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
