"""Original finite-mass Bohr ladder; run from _media. Python 3.14, matplotlib 3.10."""

from pathlib import Path
import math

import matplotlib.pyplot as plt


def main():
    e, h, c = 1.602176634e-19, 6.62607015e-34, 299792458.0
    epsilon = 8.8541878128e-12
    electron, proton = 9.1093837015e-31, 1.67262192369e-27
    mu = electron * proton / (electron + proton)
    hbar = h / (2 * math.pi)
    kappa = e**2 / (4 * math.pi * epsilon)
    binding = mu * kappa**2 / (2 * hbar**2)

    def energy(n):
        return -binding / (e * n**2)

    def wavelength(upper, lower):
        return h * c / (binding * (lower**-2 - upper**-2)) * 1e9

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(11, 6.2), dpi=110)
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.14, top=0.80, wspace=0.28)
    fig.suptitle("Hydrogen: energy differences become emitted light", fontsize=17, y=0.97)
    fig.text(0.5, 0.895, "Calculated circular Bohr model · finite proton mass · vacuum wavelengths",
             ha="center", color="#444444")

    for ax in axes:
        ax.set_xlim(0, 5.3)
        ax.set_xticks([])
        ax.set_ylabel("Internal energy (eV)")
        ax.axhline(0, color="#555555", linestyle="--", linewidth=1)
        ax.text(0.08, 0.08, "Ionization threshold", fontsize=10,
                transform=ax.get_yaxis_transform(), va="bottom")
        for n in range(1, 7):
            ax.hlines(energy(n), 0.2, 4.45, color="#374c67", linewidth=1.4)
        ax.spines["bottom"].set_visible(False)

    full, zoom = axes
    full.set_ylim(-14.4, 0.75)
    full.set_title("Lyman emissions to n = 1", pad=17)
    full.text(4.54, energy(1), "n = 1", va="center")
    full.text(4.54, energy(2), "n = 2", va="center")
    full.annotate("n = 3–6", xy=(4.4, energy(4)), xytext=(3.2, -2.25),
                  arrowprops={"arrowstyle": "-", "color": "#777777"}, fontsize=10)
    for x, upper, color in [(1.2, 2, "#7e57a3"), (2.7, 3, "#4d77a5")]:
        full.annotate("", xy=(x, energy(1)), xytext=(x, energy(upper)),
                      arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.5,
                                  "mutation_scale": 14})
        full.text(x + 0.13, -8.0, f"{upper} → 1\n{wavelength(upper, 1):.3f} nm",
                  color=color, va="center", fontsize=11)

    zoom.set_ylim(-3.8, 0.30)
    zoom.set_title("Expanded Balmer emissions to n = 2", pad=17)
    for n in range(2, 7):
        zoom.text(4.54, energy(n), f"n = {n}", va="center", fontsize=10)
    colors = ["#b33b36", "#258a8a", "#4866ae", "#85529c"]
    for x, upper, color in zip([0.6, 1.7, 2.8, 3.9], range(3, 7), colors):
        zoom.annotate("", xy=(x, energy(2)), xytext=(x, energy(upper)),
                      arrowprops={"arrowstyle": "-|>", "color": color, "lw": 2.4,
                                  "mutation_scale": 13})
        zoom.text(x + 0.10, -2.5, f"{upper} → 2\n{wavelength(upper, 2):.3f} nm",
                  color=color, rotation=90, va="center", ha="left", fontsize=10)

    fig.text(0.5, 0.035, "Arrows show energy loss, not electron paths. Higher levels and line intensities are omitted.",
             ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
