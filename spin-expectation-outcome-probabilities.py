"""Plot calculated spin-half outcome probabilities; tested with Python 3.14.

Run from _media; requires the root pyproject.toml NumPy/Matplotlib environment.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    angles = (np.pi / 3, np.pi / 2, 2 * np.pi / 3)
    labels = (r"$\theta=\pi/3$", r"$\theta=\pi/2$", r"$\theta=2\pi/3$")
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.1), sharey=True)
    for ax, theta, label in zip(axes, angles, labels):
        probabilities = np.array([np.sin(theta / 2)**2, np.cos(theta / 2)**2])
        mean = np.cos(theta) / 2
        ax.bar([-0.5, 0.5], probabilities, width=0.16,
               color=["#365d9d", "#16837b"], zorder=3)
        for x, p in zip([-0.5, 0.5], probabilities):
            ax.text(x, p + 0.035, f"{p:.2f}", ha="center")
        ax.axvline(mean, color="#c46a12", linestyle="--", linewidth=2)
        ax.text(mean, 0.99, f"mean = {mean:.2f}", ha="center",
                va="top", color="#9c4c00", fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
        ax.set(title=label, xlim=(-0.76, 0.76), ylim=(0, 1.08),
               xlabel=r"Outcome $S_z/\hbar$")
        ax.set_xticks([-0.5, 0, 0.5], [r"$-1/2$", "0", r"$+1/2$"])
        ax.grid(axis="y", alpha=0.18, zorder=0)
    axes[0].set_ylabel("Outcome probability")
    fig.suptitle("Two possible outcomes; their mean can lie between them", fontsize=15)
    fig.text(0.5, 0.025, "Calculated Born-rule probabilities, not observed counts",
             ha="center", color="#555555")
    fig.tight_layout(rect=(0, 0.06, 1, 0.91))
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
