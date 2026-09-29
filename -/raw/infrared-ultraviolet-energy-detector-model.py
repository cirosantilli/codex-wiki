"""Original photon-energy plot and abstract detector-substitution diagram.

The band boundaries use CIE S 017:2020. The apparatus abstracts the method
described by Larason and Houston, NIST SP 250-41 (2008), not their drawing.
No measured spectral response or historical data are reproduced.
Run from _media with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

PLANCK = 6.62607015e-34  # J s, SI exact
LIGHT_SPEED = 299792458.0  # m/s, SI exact


def photon_energy(wavelength_nm):
    return PLANCK * LIGHT_SPEED / (np.asarray(wavelength_nm) * 1e-9)


def box(ax, x, y, width, height, text, color="#edf3f6"):
    ax.add_patch(FancyBboxPatch((x, y), width, height,
                               boxstyle="round,pad=0.04,rounding_size=0.10",
                               facecolor=color, edgecolor="#536575", lw=1.3))
    ax.text(x + width / 2, y + height / 2, text, ha="center", va="center", fontsize=10)


def arrow(ax, start, end, label=None):
    ax.annotate("", end, start, arrowprops={"arrowstyle": "->", "lw": 1.6,
                                           "color": "#405363"})
    if label:
        ax.text((start[0] + end[0]) / 2, start[1] + 0.13, label,
                ha="center", fontsize=9)


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig = plt.figure(figsize=(9.3, 8.0), layout="constrained")
    energy, detector = fig.subplots(2, 1, gridspec_kw={"height_ratios": [1.05, 1.0]})
    fig.suptitle("Photon energy and detector readout are different quantities", fontsize=16)
    wavelength = np.geomspace(100, 1e6, 1000)
    energy.axvspan(100, 400, facecolor="#e9e0f2")
    energy.axvspan(400, 780, facecolor="#e4f1e8")
    energy.axvspan(780, 1e6, facecolor="#f6e9df")
    energy.loglog(wavelength, photon_energy(wavelength), color="#253f50", lw=2.2)
    energy.set(xlim=(100, 1e6), ylim=(1e-22, 5e-18),
               ylabel="Energy per photon (J)", xlabel="Vacuum wavelength (logarithmic scale)")
    energy.set_xticks([100, 400, 780, 1e4, 1e5, 1e6],
                      ["100 nm", "400", "780 nm", "10 µm", "100 µm", "1 mm"])
    energy.minorticks_off()
    energy.grid(which="major", alpha=0.2)
    energy.text(190, 2.5e-18, "Ultraviolet", ha="center", color="#5f3c7e")
    energy.text(558, 2.5e-18, "Visible", ha="center", color="#356344", fontsize=10)
    energy.text(20000, 2.5e-18, "Infrared", ha="center", color="#7b4d36")
    for nm, offset, text in [(254, (28, -10), "254 nm UV\n7.82 × 10⁻¹⁹ J"),
                             (940, (24, -34), "940 nm IR\n2.11 × 10⁻¹⁹ J"),
                             (10000, (22, 12), "10 µm IR\n1.99 × 10⁻²⁰ J")]:
        energy.plot(nm, photon_energy(nm), "o", color="#253f50", ms=5)
        energy.annotate(text, (nm, photon_energy(nm)), xytext=offset,
                        textcoords="offset points", fontsize=10,
                        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.95},
                        arrowprops={"arrowstyle": "-", "color": "#61737e"})
    energy.set_title(r"A. Calculation: $E=hc/\lambda$; bands follow the stated CIE convention", loc="left")
    energy.text(0.98, 0.025, "Boundaries are conventions, not sharp limits of vision.",
                transform=energy.transAxes, ha="right", fontsize=9, color="#4b5961")

    detector.set(xlim=(0, 12), ylim=(0, 5.2))
    detector.axis("off")
    detector.set_title("B. Measuring spectral responsivity — abstract apparatus", loc="left")
    box(detector, 0.1, 3.4, 1.3, 0.9, "Source")
    box(detector, 2.0, 3.4, 2.0, 0.9, "Wavelength\nselection")
    box(detector, 4.5, 3.4, 1.25, 0.9, "Shutter")
    box(detector, 6.35, 3.4, 1.45, 0.9, "Beam\nsplitter")
    box(detector, 8.65, 3.25, 3.1, 1.2, "Standard / test detector\nSame position, successively",
        color="#e8f1ea")
    box(detector, 6.3, 1.8, 1.7, 0.9, "Monitor\ndetector")
    arrow(detector, (1.4, 3.85), (2.0, 3.85))
    arrow(detector, (4.0, 3.85), (4.5, 3.85))
    arrow(detector, (5.75, 3.85), (6.35, 3.85))
    arrow(detector, (7.8, 3.85), (8.65, 3.85))
    arrow(detector, (7.075, 3.4), (7.075, 2.7))
    detector.text(10.2, 2.65, "I: dark-subtracted current", ha="center", fontsize=10)
    detector.text(7.15, 1.35, "M: tracks source drift", ha="center", fontsize=10)
    detector.text(0.15, 2.30, "Controls: dark baseline, wavelength scale,\n"
                  "beam geometry, temperature, unwanted light.", fontsize=10, va="center")
    detector.text(0.15, 0.80, r"$R_{\rm test}=R_{\rm std}\," 
                  r"\frac{I_{\rm test}/M_{\rm test}}{I_{\rm std}/M_{\rm std}}$",
                  fontsize=16)
    detector.text(7.0, 0.65, "Illustrative arithmetic only:\n"
                  "0.15 A/W × (1.6 / 2.0) = 0.12 A/W", fontsize=10)
    detector.text(0.15, 0.02, "No measured detector curves; the top plot is a physical-law calculation.",
                  fontsize=9, color="#4b5961")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
