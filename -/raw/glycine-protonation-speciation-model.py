"""Draw the stipulated ideal three-state glycine model (Python 3.14).

Run from _media; dependencies are recorded in the root pyproject.toml.
The fractions are calculated, not experimental measurements. Activity
coefficients are one; the minor uncharged amino/carboxyl form is omitted.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


PKA1, PKA2 = 2.35, 9.78
PI = (PKA1 + PKA2) / 2
COLORS = ("#1764a1", "#21835b", "#c25823")


def fractions(ph):
    h = 10.0 ** (-np.asarray(ph))
    k1, k2 = 10.0**-PKA1, 10.0**-PKA2
    denominator = h * h + k1 * h + k1 * k2
    return np.array([h * h, k1 * h, np.full_like(h, k1 * k2)]) / denominator


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(11, 7.6), dpi=100, facecolor="white")
    fig.suptitle("Glycine protonation and speciation — ideal model", fontsize=19, y=0.97)
    fig.text(0.5, 0.919, "Stipulated pKa₁ = 2.35, pKa₂ = 9.78; calculated pI = 6.065",
             ha="center", color="#333333")
    scheme = fig.add_axes((0.035, 0.67, 0.93, 0.21))
    scheme.axis("off")
    structures = (r"$\mathrm{H_3N^{+}{-}CH_2{-}COOH}$",
                  r"$\mathrm{H_3N^{+}{-}CH_2{-}COO^{-}}$",
                  r"$\mathrm{H_2N{-}CH_2{-}COO^{-}}$")
    for x, formula, name, color in zip((0.16, 0.5, 0.84), structures,
                                      ("G⁺: cation", "G⁰: zwitterion", "G⁻: anion"), COLORS):
        scheme.text(x, 0.76, formula, ha="center", fontsize=17, color=color)
        scheme.text(x, 0.51, name, ha="center", fontsize=14, color=color)
    scheme.text(0.16, 0.29, "net charge +1", ha="center")
    scheme.text(0.5, 0.29, "net charge 0", ha="center")
    scheme.text(0.84, 0.29, "net charge −1", ha="center")
    for a, b, label in ((0.25, 0.41, "lose H⁺; pKa₁"), (0.59, 0.75, "lose H⁺; pKa₂")):
        scheme.annotate("", (b, 0.03), (a, 0.03), arrowprops={"arrowstyle": "<->", "color": "#555555"})
        scheme.text((a + b) / 2, 0.13, label, ha="center", fontsize=11)
    ax = fig.add_axes((0.09, 0.14, 0.87, 0.45))
    ph = np.linspace(0, 14, 1401)
    for fraction, label, color in zip(fractions(ph), ("G⁺", "G⁰ (zwitterion)", "G⁻"), COLORS):
        ax.plot(ph, fraction, color=color, lw=2.8, label=label)
    for x, label in ((PKA1, "pKa₁"), (PI, "pI"), (PKA2, "pKa₂")):
        ax.axvline(x, color="#777777", lw=1.1, ls=":")
        ax.text(x, 0.88, label, ha="center", bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    ax.set(xlim=(0, 14), ylim=(0, 1.04), xlabel="pH", ylabel="Calculated fraction of total glycine")
    ax.set_xticks(np.arange(0, 15, 2))
    ax.grid(alpha=0.17)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.16), ncols=3, frameon=False)
    fig.text(0.5, 0.04, "Charge units: elementary charge e. At pI: 99.9615% G⁰; 0.0193% each G⁺ and G⁻.",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
