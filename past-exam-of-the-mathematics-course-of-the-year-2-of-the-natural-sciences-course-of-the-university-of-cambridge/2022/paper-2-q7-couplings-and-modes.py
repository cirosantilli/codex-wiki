"""NST IB 2022 paper 2 Q7: coupling graph and modes; save the PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see the root pyproject.toml.
Each edge means a pair of parallel strings, with combined stiffness k.
"""

from pathlib import Path
import itertools

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.7),
                             gridspec_kw={"width_ratios": [1, 1.85]}, facecolor="white")
    graph, modes_ax = axes
    for ax in axes:
        ax.set_facecolor("white")
        ax.axis("off")
    positions = np.array([[0, 1], [-1, 0], [0, -1], [1, 0]], dtype=float)
    for i, j in itertools.combinations(range(4), 2):
        graph.plot(*positions[[i, j]].T, lw=1.8,
                   color="#b86d27" if i == 0 else "#3275ad", zorder=1)
    for i, point in enumerate(positions):
        graph.scatter(*point, s=430, marker="s" if i == 0 else "o",
                      color="#48545f" if i == 0 else "#1f4768", zorder=2)
        graph.text(*point, str(i), ha="center", va="center", color="white", fontsize=11)
    graph.text(0, 1.37, "Fixed beam", ha="center", fontsize=11)
    graph.text(0, -1.45, "Each edge: stiffness $k$", ha="center", fontsize=11)
    graph.set(xlim=(-1.5, 1.5), ylim=(-1.65, 1.65), aspect="equal")
    graph.set_title("Six connecting pairs", fontsize=12, pad=14)

    patterns = ((1, 1, 1), (1, -1, 0), (1, 1, -2))
    centers = (0, 1.3, 2.6)
    labels = (r"$(1,1,1)$", r"$(1,-1,0)$", r"$(1,1,-2)$")
    frequencies = (r"$\omega=\sqrt{k}$", r"$\omega=2\sqrt{k}$", r"$\omega=2\sqrt{k}$")
    levels = (0.75, 0, -0.75)
    for center, values, label, frequency in zip(centers, patterns, labels, frequencies):
        norm = np.linalg.norm(values)
        for bar, (level, value) in enumerate(zip(levels, values), start=1):
            modes_ax.plot([center - 0.31, center + 0.02], [level, level],
                          color="#303e4a", lw=4, solid_capstyle="butt")
            if center == 0:
                modes_ax.text(center - 0.44, level, str(bar), ha="right", va="center", fontsize=10)
            if value:
                length = 0.58 * value / norm
                modes_ax.annotate("", xy=(center + 0.21, level + length / 2),
                                  xytext=(center + 0.21, level - length / 2),
                                  arrowprops=dict(arrowstyle="-|>", lw=2.5, mutation_scale=14,
                                                  color="#1768ab" if value > 0 else "#c46324",
                                                  shrinkA=0, shrinkB=0))
            else:
                modes_ax.scatter(center + 0.21, level, s=17, color="#727c84")
        modes_ax.text(center, 1.26, label, ha="center", fontsize=11)
        modes_ax.text(center, -1.35, frequency, ha="center", fontsize=12)
    modes_ax.set(xlim=(-0.8, 3.1), ylim=(-1.7, 1.7))
    modes_ax.set_title("Equal-mass vertical displacement patterns", fontsize=12, pad=14)
    fig.tight_layout(pad=1.1, w_pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
