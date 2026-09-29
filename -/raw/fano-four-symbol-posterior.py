"""Draw a theoretical Fano equality example; save the PNG basename to cwd.

Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Uses the repository's matplotlib/numpy environment; tested with Python 3.14.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def box(ax, xy, width, height, text, color):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.015",
                               facecolor=color, edgecolor="#516275", linewidth=1))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text,
            ha="center", va="center", fontsize=11, color="#132638")


def main():
    q = 0.3
    posterior = np.full((4, 4), q / 3)
    np.fill_diagonal(posterior, 1 - q)
    joint = posterior / 4
    assert np.allclose(joint.sum(axis=0), 0.25)
    assert np.allclose(joint.sum(axis=1), 0.25)
    assert np.isclose(1 - np.trace(joint), q)

    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(10.4, 5.4), facecolor="white")
    ax = fig.add_axes([0.07, 0.26, 0.34, 0.58])
    ax.imshow(posterior, vmin=0, vmax=0.7, cmap="Blues")
    for x in range(4):
        for y in range(4):
            ax.text(y, x, f"{posterior[x, y]:.1f}", ha="center", va="center",
                    color="white" if x == y else "#132638", fontsize=16)
    ax.set(xticks=range(4), xticklabels=list("ABCD"), yticks=range(4),
           yticklabels=list("ABCD"), xlabel="Observed report Y", ylabel="True symbol X",
           title="Posterior P(X = x | Y = y)")
    ax.set_xticks(np.arange(-0.5, 4, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 4, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", bottom=False, left=False)

    tree = fig.add_axes([0.46, 0.20, 0.52, 0.64])
    tree.set(xlim=(0, 1), ylim=(0, 1))
    tree.axis("off")
    tree.set_title("After report B: split by the error flag", pad=14)
    box(tree, (0.25, 0.77), 0.5, 0.16, "Decoder guesses B", "#edf3f9")
    box(tree, (0.03, 0.28), 0.36, 0.27, "Z = 0: correct\nX = B is known\n0 bits remain", "#e3f1fa")
    box(tree, (0.53, 0.28), 0.45, 0.27,
        "Z = 1: wrong\nX = A, C, or D\nEach has probability 1/3", "#fff0d8")
    for endpoint, label, label_xy in [((0.2, 0.55), "Probability 0.7", (0.19, 0.67)),
                                     ((0.755, 0.55), "Probability 0.3", (0.8, 0.67))]:
        tree.annotate("", endpoint, (0.5, 0.76),
                      arrowprops={"arrowstyle": "->", "color": "#516275", "lw": 1.6})
        tree.text(*label_xy, label, ha="center", fontsize=10)
    tree.text(0.755, 0.17, r"$\log_2 3$ bits remain after an error",
              ha="center", fontsize=10)
    tree.text(0.5, 0.015, r"Flag uncertainty: $h_2(0.3) = 0.8813$ bits", ha="center")

    fig.suptitle("Four symbols, symmetric errors: q = 0.3", fontsize=16, y=0.97)
    fig.text(0.5, 0.105,
             r"$H(X\mid Y) = h_2(0.3) + 0.3\log_2 3 = 1.3568$ bits",
             ha="center", fontsize=14)
    fig.text(0.5, 0.035, "Uniform input; identity decoder; theoretical toy probabilities, not measured data",
             ha="center", fontsize=10, color="#516275")
    fig.savefig(Path.cwd() / "fano-four-symbol-posterior.png", dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
