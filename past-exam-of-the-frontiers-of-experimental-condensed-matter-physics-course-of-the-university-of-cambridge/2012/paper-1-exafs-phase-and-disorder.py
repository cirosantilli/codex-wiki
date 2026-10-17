"""Independent single-shell phase and damping toy, not an exam-data fit."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    wavevector = np.linspace(3, 12, 1801)
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5), layout="constrained")
    for distance, color in [(2.0, "tab:blue"), (2.06, "tab:orange")]:
        signal = np.sin(2*wavevector*distance+.4)*np.exp(-2*.002*wavevector**2)
        axes[0].plot(wavevector, signal, color=color, label=fr"$R={distance:g}\,\AA$")
    axes[0].set(xlabel=r"Photoelectron wavenumber $k$ ($\AA^{-1}$)",
                ylabel="Normalized toy oscillation", title="Larger distance advances the phase")
    axes[0].legend(fontsize=9, loc="lower left")
    for variance in [0, .002, .006]:
        axes[1].plot(wavevector, np.exp(-2*variance*wavevector**2),
                     label=fr"$\sigma^2={variance:g}\,\AA^2$")
    axes[1].set(xlabel=r"Photoelectron wavenumber $k$ ($\AA^{-1}$)",
                ylabel="Gaussian disorder envelope", title="Relative disorder damps high k", ylim=(0, 1.05))
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.grid(alpha=.18)
    fig.suptitle("Independent EXAFS toy: no measured data or fitted sample parameters", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
