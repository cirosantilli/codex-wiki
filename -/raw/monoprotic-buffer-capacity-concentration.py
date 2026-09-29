"""Ideal monoprotic capacity; run from _media with Python 3.14.

Dependencies: matplotlib 3.10.7, numpy 2.3.5 (root pyproject.toml).
Stipulated constants describe a model, not measured material data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def capacity(ph, concentration, ka=1e-5, kw=1e-14):
    """Return pair and free-ion terms in mol/L per pH (c° = 1 mol/L)."""
    h = 10.0 ** (-np.asarray(ph))
    return np.log(10) * concentration * ka * h / (ka + h) ** 2, np.log(10) * (h + kw / h)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained", facecolor="white")
    ph = np.linspace(2, 8, 601)
    for concentration, color in [(0.1, "#2466a8"), (0.01, "#d45d18")]:
        pair, _ = capacity(ph, concentration)
        axes[0].plot(ph, pair * 1000, lw=2.5, color=color, label=f"C = {concentration:.3f} mol/L")
        axes[0].scatter([5], [np.log(10) * concentration / 4 * 1000], color=color, zorder=3)
    axes[0].axvline(5, color="0.55", ls=":", lw=1)
    axes[0].set(xlabel="pH", ylabel="Pair capacity (mmol/L per pH)", title="Same pKa, tenfold concentration difference", xlim=(2, 8), ylim=(0, 65))
    axes[0].text(5.13, 60, "pH = pKa = 5", fontsize=10)
    axes[0].legend(loc="upper left", frameon=False, fontsize=10)
    ph = np.linspace(2, 12, 1001)
    pair, water = capacity(ph, 0.01)
    axes[1].semilogy(ph, pair, color="#d45d18", lw=2, label="Acid/base pair")
    axes[1].semilogy(ph, water, color="#248471", lw=2, label="Free H⁺ and OH⁻")
    axes[1].semilogy(ph, pair + water, color="#333333", lw=2.5, label="Total")
    axes[1].set(xlabel="pH", ylabel="Capacity (mol/L per pH)", title="Water terms matter away from the pair peak", xlim=(2, 12), ylim=(1e-9, 0.05))
    axes[1].legend(loc="lower left", frameon=False, fontsize=10)
    for ax in axes:
        ax.grid(alpha=0.18)
        ax.set_facecolor("white")
    fig.suptitle("Calculated ideal monoprotic buffer: pKa = 5, Kw = 10⁻¹⁴", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
