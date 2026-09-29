"""Draw a phase-representative orbit and two relative-phase models.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
The circle is a complex scalar, not a Bloch sphere; no measured data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig = plt.figure(figsize=(11, 6.8), dpi=100, facecolor="white")
    ink, blue, orange = "#263746", "#206293", "#b65318"
    fig.text(0.5, 0.955, "Global phase: many representatives, one physical state",
             ha="center", fontsize=18, weight="bold", color=ink)
    circle = fig.add_axes((0.03, 0.51, 0.31, 0.34))
    circle.set_aspect("equal")
    circle.set(xlim=(-1.65, 1.65), ylim=(-1.5, 1.5))
    circle.axis("off")
    theta = np.linspace(0, 2 * np.pi, 401)
    circle.plot(np.cos(theta), np.sin(theta), color=blue, linewidth=2)
    circle.plot([-1.3, 1.3], [0, 0], color="#c6ced5", linewidth=1)
    circle.plot([0, 0], [-1.2, 1.2], color="#c6ced5", linewidth=1)
    circle.text(1.35, -0.08, "Re", fontsize=10, color=ink)
    circle.text(0.08, 1.28, "Im", fontsize=10, color=ink)
    labels = [(1, 0, "1", 1.14, 0.13), (0, 1, "i", -0.12, 1.12),
              (-1, 0, "−1", -1.38, 0.13), (0, -1, "−i", -0.15, -1.34)]
    for x, y, label, tx, ty in labels:
        circle.scatter([x], [y], color=blue, s=35, zorder=5)
        circle.text(tx, ty, label, color=blue)
    circle.text(0, 0.25, r"$e^{i\gamma}$", ha="center", fontsize=17, color=blue)
    fig.text(0.185, 0.49, r"$|+\rangle,\ i|+\rangle,\ -|+\rangle,\ -i|+\rangle$",
             ha="center", color=blue)
    overlay = fig.add_axes((0, 0, 1, 1))
    overlay.axis("off")
    overlay.add_patch(FancyArrowPatch((0.35, 0.68), (0.46, 0.68),
                                     arrowstyle="->", mutation_scale=20,
                                     color=blue, linewidth=2))
    overlay.add_patch(FancyBboxPatch((0.48, 0.52), 0.47, 0.30,
                                    boxstyle="round,pad=0.015", facecolor="#edf5fb",
                                    edgecolor=blue, linewidth=1.6))
    fig.text(0.715, 0.76, r"$(e^{i\gamma}|+\rangle)(e^{i\gamma}|+\rangle)^\dagger=\rho_+$",
             ha="center", fontsize=16, color=ink)
    fig.text(0.715, 0.655, "Same density operator for every γ\nZ: 50% / 50%       X: 100% / 0%",
             ha="center", va="center", color=ink)
    fig.text(0.715, 0.55, "Every measurement probability is unchanged", ha="center", color=blue)
    overlay.plot([0.04, 0.96], [0.445, 0.445], color="#d6dce1", transform=overlay.transAxes)
    overlay.set(xlim=(0, 1), ylim=(0, 1))
    fig.text(0.5, 0.395, "Relative phase: changing one component changes the state",
             ha="center", fontsize=16, weight="bold", color=ink)
    states = [
        (0.06, blue, r"$\phi=0:\quad (|0\rangle+|1\rangle)/\sqrt{2}$", [1, 0]),
        (0.56, orange, r"$\phi=\pi:\quad (|0\rangle-|1\rangle)/\sqrt{2}$", [0, 1]),
    ]
    for left, color, label, probs in states:
        fig.text(left + 0.19, 0.33, label, ha="center", color=color, fontsize=14)
        ax = fig.add_axes((left, 0.105, 0.38, 0.175))
        ax.barh([1, 0], probs, height=0.45, color=color)
        for y, p in zip([1, 0], probs):
            ax.text(min(p + 0.035, 1.035), y, f"{100 * p}%", va="center", color=ink)
        ax.set(xlim=(0, 1.23), ylim=(-0.5, 1.5), yticks=[1, 0],
               yticklabels=["X: +", "X: −"], xticks=[0, 0.5, 1],
               xticklabels=["0", "½", "1"])
        ax.tick_params(axis="both", length=0, labelsize=11)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.grid(axis="x", alpha=0.15)
        ax.set_axisbelow(True)
        fig.text(left + 0.19, 0.062, "Both retain Z: 50% / 50%", ha="center", fontsize=11, color=ink)
    fig.text(0.5, 0.017, "Original ideal probabilities • complex scalar circle, not Bloch geometry • not measured data",
             ha="center", fontsize=10.5, color=ink)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
