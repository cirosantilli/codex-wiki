"""Original Lorentz/Drude model plots; write the PNG to cwd.

Tested with Python 3.14, NumPy and Matplotlib; see root pyproject.toml.
All parameters are illustrative dimensionless model values.
"""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    omega = np.linspace(0, 2.5, 2200)
    single = 1 + 0.4 / (1 - omega**2 - 0.12j * omega)
    multiple = np.ones_like(omega, dtype=complex)
    resonances = ((0.65, 0.18, 0.06), (1.25, 0.25, 0.08), (1.85, 0.22, 0.10))
    for resonance, strength, damping in resonances:
        multiple += strength / (resonance**2 - omega**2 - 1j * damping * omega)
    fig, axes = plt.subplots(3, 2, figsize=(9.5, 8.4), facecolor="white")
    blue, orange = "#1768ab", "#c36a24"
    for row, data, title, marks in (
        (0, single, "One bound-electron resonance", [1]),
        (1, multiple, "Three bound-electron resonances", [r[0] for r in resonances]),
    ):
        axes[row, 0].plot(omega, data.real, color=blue, lw=1.8)
        axes[row, 1].plot(omega, data.imag, color=orange, lw=1.8)
        for ax in axes[row]:
            ax.set_xlim(0, 2.5)
            ax.axhline(0, color="#aeb6bf", lw=0.6)
            for mark in marks:
                ax.axvline(mark, color="#aeb6bf", lw=0.7, ls=":")
            ax.set_xlabel(r"$\omega/\omega_{\rm ref}$")
        axes[row, 0].axhline(1, color="#8a939c", lw=0.7, ls="--")
        axes[row, 0].set_ylabel(r"$\epsilon_r'$ (dispersion)")
        axes[row, 1].set_ylabel(r"$\epsilon_r''$ (loss)")
        axes[row, 0].set_title(title, fontsize=11)
        axes[row, 1].set_title(r"Positive loss for $e^{-i\omega t}$", fontsize=11)

    w = np.linspace(0.025, 3, 2400)
    gamma = 0.08
    drude = 1 - 1 / (w * (w + 1j * gamma))
    index = np.sqrt(drude)
    reflectance = abs((index - 1) / (index + 1))**2
    axes[2, 0].plot(w, drude.real, color=blue, label=r"$\epsilon_r'$", lw=1.8)
    axes[2, 0].plot(w, drude.imag, color=orange, label=r"$\epsilon_r''$", lw=1.8)
    axes[2, 0].set_yscale("symlog", linthresh=1)
    axes[2, 0].set_ylabel("Drude permittivity (symmetric log scale)")
    axes[2, 0].set_title(r"Free electrons: $\gamma/\omega_p=0.08$", fontsize=11)
    axes[2, 0].legend(frameon=False)
    axes[2, 1].plot(w, reflectance, color="#27734a", lw=2)
    axes[2, 1].set(ylim=(-0.025, 1.05), ylabel=r"Normal-incidence reflectance $R$")
    axes[2, 1].set_title("Reflecting metal to plasma-edge transmission", fontsize=11)
    for ax in axes[2]:
        ax.set(xlim=(0, 3), xlabel=r"$\omega/\omega_p$")
        ax.axvline(np.sqrt(1 - gamma**2), color="#8a939c", lw=0.8, ls=":")
    for ax in axes.flat:
        ax.set_facecolor("white")
        ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(h_pad=2.0, w_pad=2.0)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
