"""Analytic leading-digit intervals; tested with Python 3.14.4, NumPy 2.3.5,
and Matplotlib 3.10.7. Write an opaque white PNG to the current directory.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    edges = np.arange(1, 11)
    logarithmic_edges = np.log10(edges)
    colors = ["#d0e4f1", "#fae0ba", "#d6ebce", "#e7d8ee", "#f5d2d2",
              "#cce8e5", "#f2e9bb", "#d8ddec", "#eadccf"]
    fig, axes = plt.subplots(2, 1, figsize=(10, 5.4), dpi=120)
    fig.patch.set_facecolor("white")
    titles = [r"Uniform fractional logarithm $Z$: probability = interval length",
              r"Uniform original number $X$ on $[1,10)$: probability = interval length / 9"]
    for ax, boundaries, title in zip(axes, [logarithmic_edges, edges], titles):
        ax.set_facecolor("white")
        for d, color, left, right in zip(range(1, 10), colors, boundaries[:-1], boundaries[1:]):
            ax.barh(0.6, right - left, left=left, height=0.6,
                    color=color, edgecolor="white", linewidth=1.5)
            ax.text((left + right) / 2, 0.6, str(d),
                    va="center", ha="center", fontsize=12, color="#222222")
        ax.set(xlim=(boundaries[0], boundaries[-1]), ylim=(0, 1.15), title=title)
        ax.set_yticks([])
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="x", labelsize=10)
    axes[0].set_xticks(np.linspace(0, 1, 11),
                      ["0"] + [f"{v / 10:.1f}" for v in range(1, 10)] + ["1"])
    axes[0].set_xlabel(r"$Z=\{\log_{10}X\}$; band d is $[\log_{10}d,\log_{10}(d+1))$")
    axes[1].set_xticks(edges)
    axes[1].set_xlabel(r"$X$; band d is $[d,d+1)$, with length 1")
    fig.suptitle("The coordinate made uniform determines the digit probabilities", fontsize=14)
    fig.text(0.5, 0.03,
             "Band labels are leading digits. Top: digit 1 has width 0.30103; digit 9 has width 0.04576.\n"
             "Bottom: all widths are equal. Analytic intervals, not an empirical dataset.",
             ha="center", fontsize=10, linespacing=1.5)
    fig.tight_layout(rect=(0, 0.12, 1, 0.94), h_pad=2.0)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
