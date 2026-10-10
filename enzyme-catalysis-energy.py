"""Draw illustrative catalytic free-energy barriers; write basename.png in cwd.

Uses the repository's Python 3.14, NumPy and Matplotlib dependencies.
The curves are constructed schematics, not fitted molecular data.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def profile(x, peak):
    """Smooth each half between G(S)=0, G(peak)=peak, G(P)=-10."""
    t = np.where(x <= 0.5, 2 * x, 2 * x - 1)
    smooth = t**2 * (3 - 2 * t)
    return np.where(x <= 0.5, peak * smooth, peak + (-10 - peak) * smooth)


def main():
    x = np.linspace(0, 1, 501)
    orange, blue = "#b65f1b", "#176b92"
    fig, ax = plt.subplots(figsize=(8.2, 4.9), layout="constrained")
    fig.set_facecolor("white")
    ax.set_facecolor("white")
    for peak, color, label in [
        (60, orange, "Uncatalysed route"),
        (40, blue, "Enzyme-catalysed route"),
    ]:
        ax.plot(x, profile(x, peak), color=color, lw=2.7, label=label)
        ax.plot(0.5, peak, "o", color=color, ms=5)
        ax.annotate(f"{peak}", (0.5, peak), xytext=(8, 4),
                    textcoords="offset points", color=color, fontsize=11)
    for value in [0, -10]:
        ax.axhline(value, color="#9da6ac", ls=":", lw=1)
    for xpos, peak, color, label in [
        (0.20, 60, orange, "Forward barrier: 60"),
        (0.32, 40, blue, "Forward barrier: 40"),
    ]:
        ax.annotate("", (xpos, peak), (xpos, 0),
                    arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.5})
        ax.text(xpos - 0.017, peak / 2, label, rotation=90,
                ha="right", va="center", color=color, fontsize=9,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.annotate("", (0.93, 0), (0.93, -10),
                arrowprops={"arrowstyle": "<->", "color": "#343c44", "lw": 1.5})
    ax.text(0.91, 9, "Same endpoint change\nΔG = −10 kJ/mol", ha="center",
            va="bottom", fontsize=10)
    ax.text(0.01, -15, "Reactants + free enzyme\nG = 0", ha="left", va="top", fontsize=10)
    ax.text(0.99, -15, "Products + free enzyme\nG = −10 kJ/mol", ha="right", va="top", fontsize=10)
    ax.set(xlim=(-0.02, 1.02), ylim=(-31, 78), xticks=[],
           ylabel="Illustrative Gibbs free energy (kJ/mol)",
           xlabel="Progress along a reaction route (not time)")
    ax.set_title("A lower barrier, the same overall free-energy change", fontsize=13)
    ax.legend(loc="upper left", frameon=False, fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path(Path(__file__).stem + ".png"), dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)
    print("Illustrative forward barriers: 60, 40 kJ/mol; reverse: 70, 50; ΔG: −10")


if __name__ == "__main__":
    main()
