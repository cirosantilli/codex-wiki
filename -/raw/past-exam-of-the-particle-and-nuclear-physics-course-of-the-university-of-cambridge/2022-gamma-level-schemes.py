"""Original solution diagrams for the 2022 Particle and Nuclear Physics exam.

Writes the PNG basename into the current working directory.
Dependencies are declared in the repository pyproject.toml.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    schemes = [[0, 0.440, 2.076, 2.982], [0, 0.906, 2.542, 2.982]]
    gamma = {440: 1, 906: 2, 1636: 3, 2076: 4, 2542: 5, 2982: 6}
    pairs = [(1, 0), (2, 0), (3, 0), (2, 1), (3, 1), (3, 2)]
    colours = ["#26618c", "#ac4b22", "#665199", "#327951", "#a24f87", "#667021"]
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 5.1), sharey=True)
    for ax, levels, title in zip(axes, schemes, ["Scheme A", "Scheme B"]):
        for i, energy in enumerate(levels):
            ax.hlines(energy, 0, 1.28, color="#444444", linewidth=1.15)
            ax.text(-0.04, energy, f"{energy:.3f}", ha="right", va="center", fontsize=10)
            ax.text(1.31, energy, "Ground" if i == 0 else f"E{i}", ha="left", va="center", fontsize=10)
        for x, (upper, lower), colour in zip(np.linspace(0.12, 1.13, 6), pairs, colours):
            number = gamma[round(1000 * (levels[upper] - levels[lower]))]
            ax.annotate("", xy=(x, levels[lower] + 0.015), xytext=(x, levels[upper] - 0.015),
                        arrowprops={"arrowstyle": "->", "lw": 1.6, "color": colour})
            ax.text(x + 0.025, (levels[upper] + levels[lower]) / 2, rf"$\gamma_{number}$",
                    color=colour, ha="left", va="center", fontsize=12,
                    bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.4})
        ax.set_title(title, fontsize=13, pad=12)
        ax.set_xlim(-0.31, 1.62)
        ax.set_ylim(-0.18, 3.22)
        ax.axis("off")
    fig.suptitle("Reconstructed excitation levels and photon assignments", fontsize=14)
    fig.text(0.5, 0.035, "Excitation energies in MeV; arrow positions are schematic.", ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.07, 1, 0.94), w_pad=2.8)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
