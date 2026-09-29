"""Hypothetical 3D hydrogenic exciton positions, not an empirical spectrum.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media;
write the matching PNG to CWD. Equal sticks show positions only. The assumed
optical transitions are permitted; no oscillator strengths are calculated.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # SI values used only to calculate this hypothetical model.
    e = 1.602176634e-19
    hbar = 1.054571817e-34
    epsilon0 = 8.8541878128e-12
    m0 = 9.1093837015e-31
    me, mh, epsilon_r, gap_eV = 0.10 * m0, 0.40 * m0, 10.0, 1.500
    mu = me * mh / (me + mh)
    coulomb = e**2 / (4 * np.pi * epsilon0 * epsilon_r)
    radius_nm = hbar**2 / (mu * coulomb) * 1e9
    rydberg_meV = mu * coulomb**2 / (2 * hbar**2) / e * 1e3
    n = np.arange(1, 4)
    internal_meV = -rydberg_meV / n**2
    optical_eV = gap_eV + internal_meV / 1e3
    assert np.all(internal_meV < 0) and np.all(optical_eV < gap_eV)
    assert np.all(np.diff(optical_eV) > 0)
    assert np.isclose(rydberg_meV, 10.88455, rtol=1e-6)
    assert np.isclose(radius_nm, 6.61472, rtol=1e-6)

    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 5.8), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.28, top=0.78, wspace=0.48)

    left.set(xlim=(0, 1.22), ylim=(-12.1, 2), xticks=[],
             ylabel="Internal energy relative to continuum (meV)")
    left.set_title("Binding within the pair", fontweight="bold", pad=15)
    left.axhspan(0, 2, color="#eaf0f5")
    left.axhline(0, color="#555555", linestyle="--")
    left.text(0.03, 0.6, "Unbound continuum", fontsize=10)
    for ni, value in zip(n, internal_meV, strict=True):
        left.hlines(value, 0.10, 0.57, color="#246bb1", lw=2.8)
        left.text(0.62, value, f"n = {ni}: {value:.3f}", va="center", fontsize=10)
    left.annotate("", xy=(0.055, 0), xytext=(0.055, internal_meV[0]),
                  arrowprops={"arrowstyle": "<->", "color": "#c45e16", "lw": 2})
    left.text(0.13, -6.4, f"Separation cost\n{rydberg_meV:.3f} meV",
              color="#994810", fontsize=10)

    right.set(xlim=(-12.1, 2), ylim=(0, 1.37), yticks=[],
              xlabel=r"Photon energy offset $\hbar\omega-E_g$ (meV)")
    right.set_title("Optical creation from the crystal ground state",
                    fontweight="bold", fontsize=10, pad=15)
    right.axvspan(0, 2, color="#eaf0f5")
    right.axvline(0, color="#555555", linestyle="--")
    right.hlines(0, -12.1, 2, color="#555555", lw=1)
    for ni, position in zip(n, internal_meV, strict=True):
        right.vlines(position, 0, 0.90, color="#246bb1", lw=2.8)
    for ni, position, y in zip(n, internal_meV, [1.02, 1.20, 1.02], strict=True):
        right.text(position, y, f"n = {ni}", ha="center", fontsize=10)
    right.text(1.0, 0.46, "Unbound threshold", rotation=90, ha="center", fontsize=10)

    for ax in (left, right):
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Exciton binding lowers the optical creation energy", fontsize=15, y=0.96)
    fig.text(0.5, 0.87, r"Hypothetical 3D model: $m_e^*=0.10m_0$, $m_h^*=0.40m_0$, "
             r"$\epsilon_r=10$, $E_g=1.500$ eV", ha="center", fontsize=11)
    fig.text(0.5, 0.15, f"Reduced mass = 0.080 m₀   |   Radius scale = {radius_nm:.3f} nm\n"
             "Optical positions (eV): " + ",  ".join(f"{v:.6f}" for v in optical_eV),
             ha="center", fontsize=11)
    fig.text(0.5, 0.045, "Positions only: equal stick heights do not predict strengths or widths.\n"
             "Permitted transitions and negligible recoil assumed; not an empirical spectrum.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white",
                transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
