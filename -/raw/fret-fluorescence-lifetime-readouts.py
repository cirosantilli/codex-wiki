"""Original FRET readout schematic; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes fret-fluorescence-lifetime-readouts.png to the CWD.
Spectra and lifetimes are synthetic, not CFP/YFP data. Equal yields and detection
efficiencies are assumed only in the idealized spectral comparison.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    donor, acceptor, artifact = "#007c91", "#ba7400", "#777777"
    fig = plt.figure(figsize=(9.4, 7.1), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.25])
    scheme = fig.add_subplot(grid[0, :])
    scheme.set(xlim=(0, 10), ylim=(0, 4.8))
    scheme.axis("off")

    def box(x, y, text, color):
        scheme.add_patch(FancyBboxPatch((x, y), 1.9, 0.65, boxstyle="round,pad=0.08", ec=color, fc="white", lw=1.8))
        scheme.text(x + 0.95, y + 0.325, text, ha="center", va="center", color=color, fontsize=12)

    def arrow(start, end, color, style="-", curve=0):
        scheme.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "color": color, "lw": 1.8, "linestyle": style, "connectionstyle": f"arc3,rad={curve}"})

    box(2.05, 2.6, "Donor excited", donor)
    box(6.05, 2.6, "Acceptor excited", acceptor)
    box(2.05, 0.5, "Donor channel", donor)
    box(6.05, 0.5, "Acceptor channel", acceptor)
    scheme.text(0.6, 2.9, "Donor\nexcitation", ha="center", va="center", color="#345cb0")
    arrow((1.15, 2.9), (1.95, 2.9), "#345cb0")
    arrow((4.05, 2.9), (5.95, 2.9), "#222222")
    scheme.text(5, 3.25, "Nonradiative transfer", ha="center", fontsize=11)
    arrow((3, 2.5), (3, 1.25), donor)
    scheme.text(2.9, 1.85, "Donor\nemission", ha="right", va="center", color=donor)
    arrow((7, 2.5), (7, 1.25), acceptor)
    scheme.text(7.1, 1.85, "Sensitized\nemission", ha="left", va="center", color=acceptor)
    arrow((1.1, 3.1), (6.25, 3.3), artifact, "--", -0.3)
    scheme.text(4.1, 4.35, "Direct acceptor excitation: acceptor-only control", ha="center", fontsize=10, color=artifact, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    arrow((3.65, 2.5), (6.4, 1.25), artifact, "--")
    scheme.text(4.9, 1.75, "Donor leakage:\ndonor-only control", ha="center", fontsize=10, color=artifact, bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})

    spectrum = fig.add_subplot(grid[1, 0])
    wavelength = np.linspace(410, 620, 1000)
    d = np.exp(-0.5 * ((wavelength - 480) / 18) ** 2)
    a = np.exp(-0.5 * ((wavelength - 550) / 18) ** 2)
    spectrum.plot(wavelength, d, "--", color=donor, lw=2, label="Donor, no acceptor")
    spectrum.plot(wavelength, 0.5 * d, color=donor, lw=2.5, label="Donor, E = 0.5")
    spectrum.plot(wavelength, 0.5 * a, color=acceptor, lw=2.5, label="Acceptor, E = 0.5")
    spectrum.set(xlabel="Illustrative wavelength (nm)", ylabel="Relative spectral intensity", ylim=(0, 1.08), title="Ideal fluorescence under donor excitation")
    spectrum.legend(frameon=False, fontsize=9, loc="upper right")
    spectrum.grid(alpha=0.15)

    lifetime = fig.add_subplot(grid[1, 1])
    time = np.linspace(0, 12, 800)
    lifetime.plot(time, np.exp(-time / 4), "--", color=donor, lw=2, label="No acceptor: τD = 4 ns")
    lifetime.plot(time, np.exp(-time / 2), color=donor, lw=2.5, label="With acceptor: τDA = 2 ns")
    lifetime.axhline(np.exp(-1), color="#999999", lw=1, linestyle=":")
    lifetime.text(10.5, np.exp(-1) + 0.04, "1/e", color="#555555", ha="center")
    lifetime.set(xlabel="Time after brief pulse (ns)", ylabel="Donor I(t) / I(0)", ylim=(0, 1.08), title="Lifetime changes the decay shape")
    lifetime.legend(frameon=False, fontsize=9, loc="upper right")
    lifetime.text(6.5, 0.58, "E = 1 − τDA / τD = 0.5", ha="center", fontsize=11)
    lifetime.grid(alpha=0.15)
    fig.suptitle("FRET fluorescence and lifetime readouts", fontsize=16)
    fig.get_layout_engine().set(rect=(0, 0.09, 1, 0.91))
    fig.text(0.5, 0.022, "Synthetic spectra and lifetimes; equal yields and collection assumed for the ideal emission panel.\nCrosstalk arrows are optical artifacts; the central transfer arrow carries no emitted photon.", ha="center", fontsize=10, color="#444444")
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=140, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
