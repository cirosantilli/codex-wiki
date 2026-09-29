"""Draw ideal preparation alternatives; Python 3.14, matplotlib 3.10.7.

Run from _media. All numbers are Born-rule model probabilities, not data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(11, 6.8), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 11), ylim=(0, 6.8))
    ax.axis("off")
    blue, orange, ink = "#206293", "#b65318", "#263746"

    def box(x, y, w, h, label, color, fill):
        ax.add_patch(FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.08",
            facecolor=fill, edgecolor=color, linewidth=1.6,
        ))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", color=ink)

    def arrow(start, end, color):
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="->", mutation_scale=14,
            linewidth=1.6, color=color,
        ))

    ax.text(5.5, 6.55, "Same Z probabilities do not identify a quantum state",
            ha="center", va="center", fontsize=18, weight="bold", color=ink)
    ax.text(0.25, 5.94, "Coherent preparation: add amplitudes", color=blue, weight="bold")
    box(0.25, 4.85, 1.4, 0.68, r"Start $|0\rangle$", blue, "#edf5fb")
    box(2.2, 4.75, 2.5, 0.88, "Hadamard gate\n" + r"$|0\rangle\to|+\rangle$", blue, "#edf5fb")
    arrow((1.74, 5.19), (2.1, 5.19), blue)
    box(5.25, 4.75, 1.9, 0.88, r"$\rho_+=|+\rangle\langle+|$" + "\ncoherence retained", blue, "#edf5fb")
    arrow((4.8, 5.19), (5.14, 5.19), blue)
    box(8.0, 5.35, 2.6, 0.64, "Z: 0 / 1\n50% / 50%", blue, "#edf5fb")
    box(8.0, 4.1, 2.6, 0.64, "X: + / −\n100% / 0%", blue, "#edf5fb")
    arrow((7.25, 5.19), (7.65, 5.19), blue)
    arrow((7.65, 5.19), (7.9, 5.67), blue)
    arrow((7.65, 5.19), (7.9, 4.42), blue)
    ax.text(9.3, 3.66, "Choose one basis per fresh trial", ha="center", fontsize=10.5, color=ink)
    ax.plot([0.25, 10.7], [3.38, 3.38], color="#d6dce1", linewidth=1)
    ax.text(0.25, 3.06, "Incoherent preparation: average probabilities", color=orange, weight="bold")
    box(0.25, 1.76, 1.4, 0.85, "Fair random\nchoice", orange, "#fff3e9")
    box(2.2, 2.2, 2.5, 0.64, r"Prepare $|0\rangle$" + "\n50% of trials", orange, "#fff3e9")
    box(2.2, 1.08, 2.5, 0.64, r"Prepare $|1\rangle$" + "\n50% of trials", orange, "#fff3e9")
    arrow((1.74, 2.19), (2.1, 2.52), orange)
    arrow((1.74, 2.19), (2.1, 1.4), orange)
    box(5.25, 1.76, 1.9, 0.85, "Forget label\n" + r"$\rho_{\rm mix}=I/2$", orange, "#fff3e9")
    arrow((4.8, 2.52), (5.14, 2.19), orange)
    arrow((4.8, 1.4), (5.14, 2.19), orange)
    box(8.0, 2.55, 2.6, 0.64, "Z: 0 / 1\n50% / 50%", orange, "#fff3e9")
    box(8.0, 1.2, 2.6, 0.64, "X: + / −\n50% / 50%", orange, "#fff3e9")
    arrow((7.25, 2.19), (7.65, 2.19), orange)
    arrow((7.65, 2.19), (7.9, 2.87), orange)
    arrow((7.65, 2.19), (7.9, 1.52), orange)
    ax.text(3.45, 0.73, "Alternatives on different trials; no amplitude recombination",
            ha="center", fontsize=10.5, color=ink)
    ax.text(5.5, 0.21, "Ideal model • separate fresh preparations • ideal detection • not measured counts",
            ha="center", fontsize=11, color=ink)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
