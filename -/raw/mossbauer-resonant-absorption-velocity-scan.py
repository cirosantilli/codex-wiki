"""Original ideal Mössbauer scan; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python ../mossbauer-resonant-absorption-velocity-scan.py
The parameters are stipulated teaching values, not an isotope data set.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def transmission(velocity_mm_s, temperature_ratio=0.0):
    """Coherent elastic fraction modifies depth, with widths held fixed."""
    c = 299_792_458.0
    energy_ev = 20_000.0
    width_ev = 2.0e-7
    eta = 0.1
    coth = 1.0 if temperature_ratio == 0 else 1 / np.tanh(0.5 / temperature_ratio)
    depth = 0.25 * np.exp(-2 * eta * (coth - 1))
    shift_ev = energy_ev * np.asarray(velocity_mm_s) * 1.0e-3 / c
    return 1 - depth / (1 + (2 * shift_ev / width_ev) ** 2)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    fig = plt.figure(figsize=(10, 6.0), layout="constrained")
    grid = fig.add_gridspec(2, 1, height_ratios=[1.0, 3.2])
    scheme = fig.add_subplot(grid[0])
    scheme.set(xlim=(0, 10), ylim=(0, 1.5))
    scheme.axis("off")
    for x, width, label, color in [
        (0.2, 2.1, "Moving solid source\nembedded excited nuclei", "#e8f0fa"),
        (4.1, 2.1, "Solid absorber\nresonant nuclei", "#fcefdc"),
        (8.0, 1.8, "Detector\ncounts photons", "#e5f4ec"),
    ]:
        scheme.add_patch(FancyBboxPatch((x, 0.22), width, 0.72,
                         boxstyle="round,pad=0.03", facecolor=color, edgecolor="#444444"))
        scheme.text(x + width / 2, 0.58, label, ha="center", va="center", fontsize=10)
    for start, end in [(2.4, 4.0), (6.3, 7.9)]:
        scheme.annotate("", xy=(end, 0.58), xytext=(start, 0.58),
                        arrowprops={"arrowstyle": "->", "lw": 1.6})
    scheme.text(3.2, 0.96, r"$\gamma$ ray", ha="center")
    scheme.text(7.1, 0.96, "transmitted", ha="center", fontsize=10)
    scheme.annotate("+v: approach", xy=(2.1, 1.27), xytext=(0.25, 1.27),
                    va="center", arrowprops={"arrowstyle": "->"}, fontsize=10)
    scheme.set_title("A slow source motion scans a narrow nuclear resonance", pad=10)

    ax = fig.add_subplot(grid[1])
    velocity = np.linspace(-8, 8, 1601)
    ax.plot(velocity, transmission(velocity), lw=2.6, color="#225ca8",
            label=r"Cold: $k_BT/(\hbar\omega)=0$")
    ax.plot(velocity, transmission(velocity, 2), lw=2.6, color="#bd5b12",
            label=r"Warmer: $k_BT/(\hbar\omega)=2$")
    ax.axhline(1, color="0.4", lw=1, ls="--", label="Nonresonant comparison")
    half_width_mm_s = 299_792_458 * 1e-7 / 20_000 * 1e3
    ax.hlines(0.875, -half_width_mm_s, half_width_mm_s, color="#225ca8", ls=":")
    ax.vlines([-half_width_mm_s, half_width_mm_s], 0.715, 0.875,
              color="#225ca8", ls=":", lw=1)
    ax.scatter([-half_width_mm_s, half_width_mm_s], [0.875, 0.875],
               color="#225ca8", s=26, zorder=3)
    ax.annotate("Dip FWHM = 2.998 mm/s", xy=(0, 0.875), xytext=(-7.6, 0.81),
                arrowprops={"arrowstyle": "->", "color": "#225ca8"}, color="#225ca8")
    ax.annotate("7,500 expected counts\nfrom a 10,000-count baseline", xy=(0, 0.75),
                xytext=(2.6, 0.73), fontsize=10,
                arrowprops={"arrowstyle": "->", "color": "#225ca8"})
    ax.set(xlim=(-8, 8), ylim=(0.71, 1.025), xlabel="Source velocity towards absorber (mm/s)",
           ylabel=r"Expected transmission $I/I_0$")
    ax.grid(alpha=0.16)
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.94), fontsize=9, framealpha=0.95)
    scale = 20_000 * 1e-3 / 299_792_458 * 1e9
    secondary = ax.secondary_xaxis("top", functions=(lambda v: v * scale, lambda e: e / scale))
    secondary.set_xlabel(r"Doppler energy shift $\delta E$ (neV)")
    fig.text(0.5, -0.025, r"Stipulated: $E_\gamma=20$ keV; $\Gamma_s=\Gamma_a=10^{-7}$ eV; "
             r"$E_R/(\hbar\omega)=0.1$. Analytic model, no measured data.",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False,
                bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
