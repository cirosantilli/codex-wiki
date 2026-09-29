"""Ideal 1D box modes and analytic densities; save an opaque PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg MPLCONFIGDIR=/tmp.
Constants: https://physics.nist.gov/cuu/Constants/Table/allascii.txt
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    u = np.linspace(0, 1, 1601)
    h, mass, length, joule_per_ev = 6.62607015e-34, 9.1093837139e-31, 1e-9, 1.602176634e-19
    e1 = h**2 / (8 * mass * length**2) / joule_per_ev
    fig, axes = plt.subplots(3, 2, figsize=(9.2, 6.9), sharex=True)
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.15, top=0.84,
                        hspace=0.57, wspace=0.25)
    fig.suptitle("Infinite square well — ideal model, not measurement data\n"
                 r"Electron, $L=1$ nm: analytic modes and stationary densities",
                 fontsize=13, y=0.97)
    colors = ("#186c9e", "#b25812", "#6c4699")
    for row, n in enumerate((1, 2, 3)):
        mode = np.sqrt(2) * np.sin(n * np.pi * u)
        density = mode**2
        amplitude_ax, density_ax = axes[row]
        amplitude_ax.axhline(0, color="0.6", lw=0.8)
        amplitude_ax.plot(u, mode, lw=2.2, color=colors[row])
        nodes = np.arange(1, n) / n
        amplitude_ax.scatter(nodes, np.zeros_like(nodes), s=32, color="0.15", zorder=4)
        amplitude_ax.set(ylabel=r"$\sqrt{L}\,\phi_n(x)$", ylim=(-1.7, 1.7))
        amplitude_ax.set_title(rf"$n={n}$: $E_{n}={e1*n*n:.3f}$ eV; {n-1} interior node(s)",
                               loc="left", fontsize=10)
        density_ax.plot(u, density, lw=2.2, color=colors[row])
        density_ax.set(ylabel=r"$L\,|\phi_n(x)|^2$", ylim=(0, 2.35))
        density_ax.set_title("Probability density: area over x/L = 1", loc="left", fontsize=10)
        if n == 1:
            middle = (u >= 0.25) & (u <= 0.75)
            density_ax.fill_between(u, 0, density, where=middle, color=colors[row], alpha=0.23)
            density_ax.text(0.5, 0.5, r"Middle half: $1/2+1/\pi$" "\n= 0.818310",
                            ha="center", va="center", fontsize=10,
                            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.92})
        for ax in axes[row]:
            ax.set_xlim(0, 1)
            ax.set_xticks((0, 0.25, 0.5, 0.75, 1))
            ax.axvline(0, color="0.2", lw=2)
            ax.axvline(1, color="0.2", lw=2)
            ax.grid(alpha=0.16)
    for ax in axes[-1]:
        ax.set_xlabel(r"Position $x/L$")
    fig.text(0.5, 0.025, "Walls at x/L = 0 and 1; amplitudes and densities vanish outside.\n"
             "Mode sign encodes phase; density is nonnegative and does not change with time.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "quantum-box-eigenstates.png", dpi=140, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
