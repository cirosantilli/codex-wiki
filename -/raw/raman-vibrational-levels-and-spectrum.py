"""Draw molecular Raman energy bookkeeping and a calculated illustrative spectrum.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5 (root pyproject.toml).
Integrated radiant line strengths obey the off-resonant harmonic thermal model.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    h, c, kb = 6.62607015e-34, 299792458.0, 1.380649e-23
    excitation_nm, shift_cm, temperature = 532.0, 1000.0, 300.0
    nu0_cm = 1e7 / excitation_nm
    thermal = np.exp(-h * c * 100 * shift_cm / (kb * temperature))
    ratio = ((nu0_cm + shift_cm) / (nu0_cm - shift_cm)) ** 4 * thermal
    fig = plt.figure(figsize=(11, 7.7), dpi=110, facecolor="white")
    gs = fig.add_gridspec(2, 3, height_ratios=(1.15, 1), hspace=.48, wspace=.18)
    for i, (name, initial, final, color, emitted) in enumerate([
        ("Stokes", 0, 1, "#b44d28", r"$h(\nu_0-\nu_v)$"),
        ("Rayleigh", 0, 0, "#59616b", r"$h\nu_0$"),
        ("Anti-Stokes", 1, 0, "#267c9d", r"$h(\nu_0+\nu_v)$"),
    ]):
        ax = fig.add_subplot(gs[0, i])
        ax.set(xlim=(0, 1), ylim=(-.7, 4.3))
        ax.axis("off")
        ax.set_title(name, weight="bold", color=color, pad=16)
        for n in (0, 1):
            ax.plot([.08, .92], [n, n], color="#222222", lw=1.6)
            ax.text(.96, n, f"v = {n}", va="center", fontsize=10)
        virtual = 3.0 + initial
        ax.plot([.2, .82], [virtual, virtual], "--", color="#999999")
        ax.annotate("", xy=(.4, virtual), xytext=(.2, initial),
                    arrowprops={"arrowstyle": "->", "lw": 2, "color": "#5b56a6"})
        ax.annotate("", xy=(.82, final), xytext=(.6, virtual),
                    arrowprops={"arrowstyle": "->", "lw": 2, "color": color})
        ax.text(.08, (initial+virtual)/2, r"$h\nu_0$", color="#5b56a6", ha="right")
        ax.text(.74, (final+virtual)/2, emitted, color=color, ha="left", fontsize=10)
        ax.text(.5, -.48, f"Molecule: v = {initial} → {final}", ha="center", fontsize=10)
    ax = fig.add_subplot(gs[1, :])
    x = np.linspace(-1450, 1450, 18001)
    sigma = 25.0
    normalizer = sigma * np.sqrt(2*np.pi)
    def peak(center, area):
        return area * np.exp(-.5 * ((x-center)/sigma)**2) / normalizer
    stokes = peak(shift_cm, 1)
    anti = peak(-shift_cm, ratio)
    rayleigh = peak(0, 20)
    ax.plot(x, stokes + anti + rayleigh, color="#444444", lw=1.5)
    ax.fill_between(x, stokes, 0, color="#b44d28", alpha=.35)
    ax.fill_between(x, anti, 0, color="#267c9d", alpha=.5)
    ax.set_yscale("log")
    ax.set(xlim=(-1450, 1450), ylim=(1e-5, 1),
           xlabel=r"Signed Raman shift $\widetilde{\nu}_0-\widetilde{\nu}_s$ (cm$^{-1}$)",
           ylabel="Radiant spectral density\n(arbitrary units, log scale)")
    ax.set_xticks([-1000, 0, 1000])
    ax.grid(alpha=.2, axis="y")
    ax.text(-1000, .007, f"Anti-Stokes\n505.13 nm\nArea = {ratio:.5f}", ha="center", color="#267c9d", fontsize=10)
    ax.text(180, .18, "Rayleigh: 532 nm\nArea = 20 (chosen)", ha="left", fontsize=10)
    ax.text(1000, .06, "Stokes\n561.89 nm\nArea = 1", ha="center", color="#b44d28", fontsize=10)
    ax.set_title("Calculated one-mode spectrum: 1000 cm⁻¹, 532 nm excitation, 300 K", loc="left", fontsize=12, pad=12)
    fig.suptitle("Raman scattering exchanges molecular vibrational energy", fontsize=15, weight="bold", y=.98)
    fig.text(.5, .525, "Dashed levels are virtual intermediates, not occupied electronic levels.\n"
             "Arrow energies are schematic; vertical spacing is not to scale.", ha="center", fontsize=10)
    fig.text(.5, .025, "Original model, not a 1928 measurement. Equal Gaussian widths σ = 25 cm⁻¹ are chosen.\n"
             "Radiant anti-Stokes/Stokes area ratio includes the fourth power of the photon-frequency ratio.", ha="center", fontsize=10)
    fig.subplots_adjust(top=.86, bottom=.15, left=.105, right=.91)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
