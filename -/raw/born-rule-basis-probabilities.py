"""Compare Z and X measurement probabilities for three relative phases.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Build with: make _media/born-rule-basis-probabilities.png
Writes an opaque white PNG with this script's basename to the working directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({
        "font.size": 11,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })
    phases = np.array([0.0, np.pi / 2, np.pi])
    states = np.column_stack((
        np.full(3, np.sqrt(3) / 2), np.exp(1j * phases) / 2,
    ))
    hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    z_probabilities = np.abs(states)**2
    x_probabilities = np.abs(states @ hadamard.T)**2

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.6), sharey=True)
    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.72,
                        wspace=0.18)
    fig.suptitle("Relative phase becomes visible in another measurement basis",
                 fontsize=14, y=0.98)
    fig.text(0.5, 0.87,
             r"$|\psi_\phi\rangle=(\sqrt{3}/2)|0\rangle"
             r"+(e^{i\phi}/2)|1\rangle$", ha="center", fontsize=13)

    centers = np.arange(3)
    width = 0.32
    colors = ("#226f9c", "#b45a13")
    specifications = (
        (axes[0], z_probabilities, "Z: computational basis", ("0", "1")),
        (axes[1], x_probabilities, "X: Hadamard basis", ("+", "−")),
    )
    for ax, probabilities, title, labels in specifications:
        ax.set_axisbelow(True)
        ax.grid(axis="y", color="#e4e4e4", linewidth=0.8)
        for column, (color, label) in enumerate(zip(colors, labels)):
            positions = centers + (column - 0.5) * width
            bars = ax.bar(positions, probabilities[:, column], width=width,
                          color=color, label=f"Outcome {label}", zorder=3)
            ax.bar_label(bars, labels=[f"{p:.3f}" for p in probabilities[:, column]],
                         padding=4, fontsize=10)
        ax.set_title(title, fontsize=12, pad=30)
        ax.set_xticks(centers, [r"$0$", r"$\pi/2$", r"$\pi$"])
        ax.set_xlabel(r"Relative phase $\phi$")
        ax.set_ylim(0, 1.08)
        ax.set_yticks(np.linspace(0, 1, 5))
        ax.legend(loc="lower center", frameon=False, fontsize=9,
                  bbox_to_anchor=(0.5, 1.005), ncol=2)
    axes[0].set_ylabel("Outcome probability")
    fig.savefig(Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
