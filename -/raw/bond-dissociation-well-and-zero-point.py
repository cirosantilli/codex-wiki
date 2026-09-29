"""Stipulated Morse well; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes the matching PNG basename to the current directory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    depth, quantum = 2.0, 0.2  # eV; invented model, no measured molecule
    zero_point = quantum / 2 - quantum**2 / (16 * depth)
    ground = -depth + zero_point
    x = np.linspace(-0.9, 5.2, 900)
    potential = depth * ((1 - np.exp(-x)) ** 2 - 1)
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.6, 5.3), layout="constrained",
                           facecolor="white")
    ax.set_facecolor("white")
    ax.plot(x, potential, color="#215b87", linewidth=2.5)
    ax.axhline(0, color="#333333", linestyle="--", linewidth=1.4)
    ax.hlines(-depth, -0.15, 2.6, color="#999999", linestyle=":")
    ax.hlines(ground, -0.19, 1.15, color="#b15b00", linewidth=2.0)
    ax.text(1.18, ground + 0.06, f"$v=0$: ${ground:.5f}$ eV", color="#9a5000")
    ax.text(0.4, -2.19, "Well minimum: −2.0000 eV", fontsize=11)
    for xpos, bottom, label, color in [
        (2.75, -depth, r"$D_e=2.0000$ eV", "#215b87"),
        (4.15, ground, f"$D_0={-ground:.5f}$ eV", "#9a5000"),
    ]:
        ax.annotate("", xy=(xpos, 0), xytext=(xpos, bottom),
                    arrowprops={"arrowstyle": "<->", "color": color,
                                "linewidth": 1.8})
        ax.text(xpos + 0.11, -1.1, label, rotation=90, va="center",
                color=color)
    ax.annotate(f"Zero-point energy: {zero_point:.5f} eV", xy=(0.02, ground),
                xytext=(-0.68, -1.03), fontsize=11,
                arrowprops={"arrowstyle": "->", "color": "#9a5000"},
                color="#9a5000")
    ax.text(1.45, 0.09, "Separated ground-state atoms: zero energy", fontsize=11)
    ax.set(xlim=(-0.9, 5.15), ylim=(-2.3, 0.47),
           xlabel=r"Scaled bond extension $x=a(r-r_e)$",
           ylabel="Energy per molecule (eV)",
           title="A stipulated well: two starting levels, one dissociation limit")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
