"""Plot original stipulated LED photon and energy accounting.

Run from _media; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

H = 6.62607015e-34
C = 299792458.0
Q = 1.602176634e-19


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 6.2), dpi=120, facecolor="white")
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.38, top=0.82, wspace=0.36)
    fig.suptitle("Blue LED: photon energy and a chosen efficiency budget", size=17, weight="bold", y=0.965)
    fig.text(0.5, 0.895, "Illustrative calculations; no historical device values used", ha="center", color="#52616f")
    wavelengths = np.linspace(350, 750, 401)
    energies = H * C / (wavelengths * 1e-9) / Q
    ax1.plot(wavelengths, energies, color="#425d9e", lw=2.4)
    ax1.set(xlabel="Vacuum wavelength λ (nm)", ylabel="Photon energy (eV)",
            xlim=(350, 750), ylim=(1.5, 3.65), title="One photon: E = hc / λ")
    ax1.grid(alpha=0.2)
    for wavelength, label, color, offset in [
        (450, "450 nm blue\n2.755 eV", "#325fc5", (15, 14)),
        (560, "560 nm converted\n2.214 eV", "#ab7905", (14, 13)),
    ]:
        energy = H * C / (wavelength * 1e-9) / Q
        ax1.scatter(wavelength, energy, color=color, s=42, zorder=3)
        ax1.annotate(label, (wavelength, energy), xytext=offset,
                     textcoords="offset points", color=color, fontsize=10)

    values = np.array([100, 90, 72, 36])
    labels = ["Electrical\npairs", "Active-layer\npairs", "Internal\nphotons", "Escaped\nphotons"]
    colors = ["#8898ad", "#5896a9", "#5778c0", "#395bb2"]
    bars = ax2.bar(np.arange(4), values, width=0.66, color=colors)
    ax2.set(ylim=(0, 118), ylabel="Events per 100 electrical pairs", title="Count each stage separately")
    ax2.set_xticks(np.arange(4), labels, fontsize=10)
    ax2.spines[["top", "right"]].set_visible(False)
    for bar, value in zip(bars, values):
        ax2.text(bar.get_x() + bar.get_width() / 2, value + 2, str(value), ha="center", weight="bold")
    ax2.text(0.5, 0.96, "×0.90        ×0.80        ×0.50", transform=ax2.transAxes,
             ha="center", size=10, color="#37495d")
    eqe = 0.9 * 0.8 * 0.5
    energy = H * C / (450e-9)
    wpe = eqe * energy / (Q * 3.2)
    retention = 0.4 + 0.6 * 0.9 * 450 / 560
    fig.text(0.075, 0.13,
             f"Chosen bare LED: I = 20 mA, V = 3.20 V\n"
             f"EQE = {eqe:.0%}; optical/electrical power = {wpe:.2%}",
             size=11, linespacing=1.7)
    fig.text(0.57, 0.13,
             "Separate converter: absorbs 60% of blue; yield 0.90\n"
             f"100 incident → 40 blue + 54 converted photons\n"
             f"Energy retained = {retention:.2%}; color not predicted",
             size=10.5, linespacing=1.6)
    fig.savefig(Path(__file__).stem + ".png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
