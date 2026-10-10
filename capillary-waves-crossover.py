"""Plot stipulated deep-water gravity-capillary theory, never measured data.

Run from _media:
MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../capillary-waves-crossover.py
Tested: Python 3.14.4, matplotlib 3.10.7+dfsg1, numpy 2.3.5.
The matching opaque white PNG basename is written to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np


def main():
    gamma, rho, g = 0.072, 1000.0, 9.81  # N/m, kg/m³, m/s²: stipulated.
    ell = np.sqrt(gamma / (rho * g))
    crossover_mm = 2 * np.pi * ell * 1000
    wavelength_mm = np.geomspace(0.8, 100, 1200)
    k = 2 * np.pi / (wavelength_mm / 1000)
    omega = np.sqrt(g * k + gamma * k**3 / rho)
    cp = omega / k
    cg = (g + 3 * gamma * k**2 / rho) / (2 * omega)
    ratio = gamma * k**2 / (rho * g)
    cmin = (4 * g * gamma / rho)**0.25

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, (speed, balance) = plt.subplots(1, 2, figsize=(10.5, 5.0))
    fig.patch.set_facecolor("white")
    fig.suptitle("Gravity and surface tension meet at one wavelength", fontsize=17,
                 weight="bold", y=0.97)
    fig.text(0.5, 0.90,
             "Ideal deep-water theory • γ = 0.072 N/m, ρ = 1000 kg/m³, g = 9.81 m/s² • no measured data",
             ha="center", fontsize=10)
    for ax in (speed, balance):
        ax.set_facecolor("white")
        ax.axvspan(0.8, crossover_mm, color="#eaf3fa")
        ax.axvspan(crossover_mm, 100, color="#fff4e4")
        ax.axvline(crossover_mm, color="#45505a", linestyle=":", linewidth=1.4)
        ax.set_xscale("log")
        ax.set_xlim(0.8, 100)
        ax.set_xticks([1, 3, 10, 30, 100])
        ax.xaxis.set_major_formatter(ScalarFormatter())
        ax.set_xlabel("Wavelength λ (mm)")
        ax.grid(alpha=0.18, which="major")

    speed.plot(wavelength_mm, cp, color="#1765a8", linewidth=2.5,
               label=r"Crests: $c_p = \omega/k$")
    speed.plot(wavelength_mm, cg, color="#bf5b13", linewidth=2.5,
               label=r"Packet: $c_g = d\omega/dk$")
    speed.plot(crossover_mm, cmin, "o", color="#28333d", markersize=6)
    speed.annotate(f"Phase-speed minimum\n{cmin:.3f} m/s; here " + r"$c_p = c_g$",
                   xy=(crossover_mm, cmin), xytext=(7, 0.56), fontsize=10,
                   arrowprops={"arrowstyle": "->", "color": "#45505a"})
    speed.text(1.0, 0.075, r"Short waves: $c_g \to 3c_p/2$", fontsize=10, color="#8c420d")
    speed.text(23, 0.075, "Long waves:\n" + r"$c_g \to c_p/2$", fontsize=10, color="#8c420d")
    speed.set_ylim(0, 1.23)
    speed.set_ylabel("Speed (m/s)")
    speed.set_title("A crest and its packet have different speeds", fontsize=11, pad=12)
    speed.legend(loc="upper right", frameon=False, fontsize=10)

    balance.plot(wavelength_mm, ratio, color="#476849", linewidth=2.5)
    balance.axhline(1, color="#45505a", linestyle="--", linewidth=1.1)
    balance.plot(crossover_mm, 1, "o", color="#28333d", markersize=6)
    balance.set_yscale("log")
    balance.set_ylim(0.02, 800)
    balance.set_ylabel(r"Restoring-term ratio $(\gamma k^3/\rho)/(gk)$")
    balance.set_title(r"Equality uses $\lambda = 2\pi\ell_c$, rather than $\lambda = \ell_c$", fontsize=11, pad=12)
    balance.text(1.2, 150, "Surface tension dominates", color="#1765a8", fontsize=10)
    balance.text(23, 0.055, "Gravity dominates", color="#996014", fontsize=10)
    balance.annotate("Equal terms at\n" + r"$\lambda = 2\pi\ell_c$" + f" = {crossover_mm:.2f} mm",
                     xy=(crossover_mm, 1), xytext=(8, 25), fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": "#45505a"})
    balance.axvline(ell * 1000, color="#7f8c96", linestyle="--", linewidth=1)
    balance.text(ell * 1000 * 1.10, 0.13, r"$\ell_c$" + f" = {ell*1000:.2f} mm\n(length scale)",
                 fontsize=9, color="#52616b")
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.13, top=0.78, wspace=0.31)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
