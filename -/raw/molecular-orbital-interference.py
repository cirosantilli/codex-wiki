"""Normalized 1D Gaussian interference toy; no hydrogen energies are modelled.

Tested with Python 3.14, NumPy 2.3.5, and Matplotlib 3.10.7.
Write the opaque white same-basename PNG to the current working directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def gaussian(x, centre):
    return np.pi ** (-0.25) * np.exp(-0.5 * (x - centre) ** 2)


def main():
    a = 1.0
    overlap = np.exp(-a * a)
    x = np.linspace(-5.0, 5.0, 2001)
    phi_a, phi_b = gaussian(x, -a), gaussian(x, a)
    psi_plus = (phi_a + phi_b) / np.sqrt(2 * (1 + overlap))
    psi_minus = (phi_a - phi_b) / np.sqrt(2 * (1 - overlap))
    blue, orange = "#176b9a", "#b94e24"
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 6.0), sharex=True,
                             layout="constrained", facecolor="white")
    fig.suptitle("Orbital interference: exactly normalized 1D Gaussian toy", fontsize=15)
    fig.supxlabel("Dimensionless position x; centres at −1 and +1", fontsize=11)
    for ax in axes.flat:
        ax.set_facecolor("white")
        ax.set_xlim(-4, 4)
        ax.axvspan(-a, a, color="#edf2f5", zorder=0)
        for centre in (-a, a):
            ax.axvline(centre, color="#b5bdc3", lw=0.8, ls=":")
        ax.grid(axis="y", color="#e5e5e5", lw=0.6)
    for col, (psi, symbol, colour) in enumerate(
        [(psi_plus, "+", blue), (psi_minus, "−", orange)]
    ):
        ax = axes[0, col]
        ax.axhline(0, color="#646464", lw=0.8)
        ax.plot(x, phi_a, color="#646464", ls="--", lw=1.1, label=r"$\phi_A$")
        ax.plot(x, phi_b, color="#969696", ls=":", lw=1.5, label=r"$\phi_B$")
        ax.plot(x, psi, color=colour, lw=2.3, label=rf"$\psi_{{{symbol}}}$")
        ax.fill_between(x, 0, psi, color=colour, alpha=0.10)
        ax.set_ylim(-0.76, 0.89)
        ax.set_title("Sum: constructive at midpoint" if col == 0
                     else "Difference: cancellation at midpoint", fontsize=11)
        ax.legend(loc="lower left", ncol=3, fontsize=9, frameon=False)
        ax.set_ylabel("Signed amplitude")
        density_ax = axes[1, col]
        density_ax.plot(x, psi ** 2, color=colour, lw=2.3,
                        label=rf"$|\psi_{{{symbol}}}|^2$")
        density_ax.fill_between(x, 0, psi ** 2, color=colour, alpha=0.13)
        density_ax.set_ylim(0, 0.53)
        density_ax.set_ylabel("Probability density")
        density_ax.legend(loc="upper right", frameon=False)
        density_ax.text(0.04, 0.93, r"$\int |\psi|^2\,dx = 1$", transform=density_ax.transAxes,
                        va="top", fontsize=11)
    axes[1, 0].annotate("Midpoint density = 0.303468", (0, psi_plus[len(x) // 2] ** 2),
                        xytext=(-3.65, 0.16), fontsize=9,
                        arrowprops={"arrowstyle": "->", "color": blue})
    axes[0, 1].annotate("Zero at x = 0", (0, 0), xytext=(0.55, 0.3), fontsize=9,
                        arrowprops={"arrowstyle": "->", "color": orange})
    axes[1, 1].annotate("Midpoint density = 0", (0, 0), xytext=(0.65, 0.15), fontsize=9,
                        arrowprops={"arrowstyle": "->", "color": orange})
    fig.text(0.5, -0.045,
             "S = exp(−1) = 0.367879  •  Signs describe amplitude, not charge  •  Not actual hydrogen orbitals",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120,
                facecolor="white", transparent=False, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
