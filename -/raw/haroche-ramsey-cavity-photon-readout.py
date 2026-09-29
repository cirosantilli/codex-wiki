"""Draw a functional cavity-QED meter, not a scaled laboratory apparatus.

Tested with Python 3.14, matplotlib 3.10.7, and numpy 2.3.5.
Run from _media; the PNG is written in the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch, FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11.6, 5.4), dpi=120, facecolor="white")
    ax.set(xlim=(0, 13), ylim=(0, 5.2))
    ax.axis("off")
    blue, orange, ink = "#246aa5", "#b55f12", "#183047"
    ax.text(6.5, 4.94, "Read the atom; keep the cavity field available", ha="center",
            color=ink, fontsize=17, weight="bold")
    ax.text(6.5, 4.57, "Functional schematic · not to scale", ha="center", color="#536574")
    stages = [(0.2, 2.15, "Preparation"), (2.85, 1.55, r"$R_1$"),
              (4.9, 2.8, "Cavity C"), (8.2, 1.55, r"$R_2$"),
              (10.25, 2.55, "Atomic detection")]
    for x, w, label in stages:
        ax.add_patch(FancyBboxPatch((x, 2.03), w, 2.12, boxstyle="round,pad=0.025",
                                   facecolor="#f4f8fc", edgecolor=blue, linewidth=1.5))
        ax.text(x + w / 2, 3.87, label, ha="center", color=ink, fontsize=12, weight="bold")
    for left, right in zip(stages, stages[1:]):
        x = left[0] + left[1]
        ax.add_patch(FancyArrowPatch((x + .04, 2.9), (right[0] - .05, 2.9),
                                    arrowstyle="-|>", mutation_scale=14, color=orange, lw=2))
    ax.text(1.275, 3.27, "Rb beam\nvelocity selection", ha="center", linespacing=1.5)
    ax.text(1.275, 2.49, "circular Rydberg\nlevels 50, 51", ha="center", linespacing=1.5)
    ax.text(3.625, 3.24, r"$\pi/2$ pulse", ha="center")
    ax.text(3.625, 2.6, "prepare\nsuperposition", ha="center", linespacing=1.5)
    for x, angle in [(5.35, 0), (7.25, 180)]:
        ax.add_patch(Arc((x, 3.04), .55, 1.1, theta1=105 + angle,
                         theta2=255 + angle, color=blue, linewidth=3))
    xs = np.linspace(5.55, 7.05, 240)
    ax.plot(xs, 3.04 + .16 * np.sin((xs - 5.55) * np.pi * 6), color=blue, lw=1.7)
    ax.scatter([6.3], [3.04], s=50, color=orange, zorder=4)
    ax.text(6.3, 2.45, "dispersive coupling\nphase shift depends on n", ha="center", linespacing=1.5)
    ax.text(8.975, 3.24, r"$\pi/2$ pulse", ha="center")
    ax.text(8.975, 2.6, "phase →\npopulation", ha="center", linespacing=1.5)
    ax.text(11.525, 3.22, "state-selective\nfield ionization", ha="center", linespacing=1.5)
    ax.text(11.525, 2.47, r"record $e$ or $g$", ha="center", color=orange, weight="bold")
    ax.text(6.3, 1.54, "Superconducting microwave cavity stores the field", ha="center", color=blue)
    ax.text(6.5, 1.0, "Fresh atoms repeat the interrogation → conditional photon-number distribution",
            ha="center", color=ink, fontsize=11.5)
    ax.text(6.5, .48, "QND protects photon number ideally; field phase can change. Cavity losses remain.",
            ha="center", color="#536574", fontsize=10.5)
    fig.subplots_adjust(left=.025, right=.975, top=.98, bottom=.025)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
