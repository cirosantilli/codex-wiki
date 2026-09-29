"""Original ideal-diode and corrected activation plots; write PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
No experimental data are used. The illustrative constant band gap is 0.50 eV.
"""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.3, 3.6), facecolor="white")
    bias = np.linspace(-6, 2.2, 900)
    axes[0].plot(bias, np.expm1(bias), color="#1768ab", lw=2)
    axes[0].axhline(-1, color="#9b6735", ls="--", lw=1)
    axes[0].axhline(0, color="#aeb7bf", lw=0.7)
    axes[0].axvline(0, color="#aeb7bf", lw=0.7)
    axes[0].text(-5.6, -0.61, r"Reverse saturation: $-I_s$", fontsize=9)
    axes[0].set(xlabel=r"$eV/(k_BT)$", ylabel=r"$I/I_s$", xlim=(-6, 2.2), ylim=(-1.5, 8.5))
    axes[0].set_title("Ideal diffusion diode", fontsize=11)

    k_b_ev = 8.617333262145e-5
    gap = 0.50
    temperature = np.linspace(200, 500, 600)
    inverse_scaled = 1000 / temperature
    log_ratio = -gap / k_b_ev * (1 / temperature - 1 / 300)
    axes[1].plot(inverse_scaled, log_ratio, color="#27734a", lw=2)
    axes[1].set(xlabel=r"$10^3/T$ ($\mathrm{K}^{-1}$)",
                ylabel=r"$\log[(n_i^2/T^3)/(n_i^2/T^3)_{300\,\mathrm{K}}]$",
                xlim=(2, 5))
    axes[1].set_title(r"Transport-corrected activation ($E_g=0.50$ eV)", fontsize=11)
    axes[1].text(0.06, 0.12, r"Slope $=-E_g/(10^3 k_B)$", transform=axes[1].transAxes, fontsize=10)
    for ax in axes:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(w_pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=125, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
