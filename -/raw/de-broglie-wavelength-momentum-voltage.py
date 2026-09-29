"""Formula plots; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; output uses this script's basename in the current directory.
No experimental observations are plotted.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

H = 6.62607015e-34  # J s, exact SI definition
E_CHARGE = 1.602176634e-19  # C, exact SI definition
E_MASS = 9.1093837139e-31  # kg, 2022 CODATA central value


def wavelength_from_voltage(voltage):
    """Nonrelativistic electron wavelength in metres, initially at rest."""
    return H / np.sqrt(2 * E_MASS * E_CHARGE * np.asarray(voltage))


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, (ax_p, ax_u) = plt.subplots(1, 2, figsize=(10, 4.6))
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.21, top=0.79, wspace=0.32)
    fig.suptitle("de Broglie wavelength: momentum and electron accelerating voltage", y=0.96, fontsize=14)
    fig.text(0.5, 0.87, "Calculated relations • negligible initial energy • no measured data",
             ha="center", color="#444444")

    momentum = np.geomspace(1e-24, 1.4e-23, 600)
    ax_p.loglog(momentum / 1e-24, H / momentum / 1e-9, color="#2367a2", lw=2.5)
    ax_p.set(xlabel=r"Momentum magnitude $p$ ($10^{-24}$ kg m s$^{-1}$)",
             ylabel=r"Wavelength $\lambda$ (nm)", title=r"Any free particle: $\lambda=h/p$")
    ax_p.set_xticks([1, 2, 4, 8, 12], labels=["1", "2", "4", "8", "12"])
    ax_p.set_yticks([0.05, 0.1, 0.2, 0.4, 0.6], labels=["0.05", "0.1", "0.2", "0.4", "0.6"])
    ax_p.minorticks_off()
    ax_p.grid(alpha=0.2)
    ax_p.text(0.08, 0.1, r"Double $p$ → halve $\lambda$", transform=ax_p.transAxes)

    voltage = np.geomspace(10, 500, 600)
    ax_u.loglog(voltage, wavelength_from_voltage(voltage) / 1e-9, color="#9a4f1b", lw=2.5)
    ax_u.set(xlabel=r"Accelerating voltage $U$ (V)", ylabel=r"Wavelength $\lambda$ (nm)",
             title=r"Electron: $\lambda=h/\sqrt{2m_e eU}$")
    for u, offset in [(54, (10, 15)), (100, (10, -28)), (400, (-105, 12))]:
        lam = float(wavelength_from_voltage(u) / 1e-9)
        ax_u.plot(u, lam, "o", color="#9a4f1b", ms=5)
        ax_u.annotate(f"{u} V: {lam:.4f} nm", (u, lam), xytext=offset,
                      textcoords="offset points", fontsize=10,
                      arrowprops={"arrowstyle": "-", "color": "#888888"})
    ax_u.set_xticks([10, 20, 50, 100, 200, 500], labels=["10", "20", "50", "100", "200", "500"])
    ax_u.set_yticks([0.05, 0.1, 0.2, 0.4], labels=["0.05", "0.1", "0.2", "0.4"])
    ax_u.minorticks_off()
    ax_u.grid(alpha=0.2)
    fig.text(0.5, 0.065, "Both axes use logarithmic scales.  Quadrupling voltage doubles momentum and halves wavelength.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
