"""Ideal 1D box interference; save an opaque analytic-density PNG to cwd.

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
    phi1, phi2 = np.sqrt(2) * np.sin(np.pi * u), np.sqrt(2) * np.sin(2 * np.pi * u)
    mixture = (phi1**2 + phi2**2) / 2
    h, mass, length, joule_per_ev = 6.62607015e-34, 9.1093837139e-31, 1e-9, 1.602176634e-19
    e1 = h**2 / (8 * mass * length**2) / joule_per_ev
    period_fs = h / (3 * e1 * joule_per_ev) * 1e15
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 6.6))
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.19, top=0.81,
                        hspace=0.56, wspace=0.26)
    fig.suptitle("Infinite square well — ideal model, not measurement data\n"
                 r"$\psi=(\phi_1e^{-iE_1t/\hbar}+\phi_2e^{-iE_2t/\hbar})/\sqrt{2}$"
                 f"; electron, L = 1 nm; T = {period_fs:.5f} fs", fontsize=12, y=0.97)
    for ax, fraction, color in zip(axes.flat, (0, 0.25, 0.5),
                                   ("#186c9e", "#6c4699", "#b25812")):
        relative_phase = 2 * np.pi * fraction
        psi = (phi1 + phi2 * np.exp(-1j * relative_phase)) / np.sqrt(2)
        density = np.abs(psi)**2
        left = u <= 0.5
        probability = 0.5 + 4 / (3 * np.pi) * np.cos(relative_phase)
        ax.plot(u, density, color=color, lw=2.3, label="Coherent superposition")
        ax.fill_between(u, 0, density, where=left, color=color, alpha=0.18)
        ax.plot(u, mixture, color="0.4", lw=1.6, ls="--", label="Equal statistical mixture")
        ax.set(xlim=(0, 1), ylim=(0, 3.3), xlabel=r"Position $x/L$",
               ylabel=r"$L\,|\psi(x,t)|^2$")
        ax.set_title(f"t/T = {fraction:g}; P(left half) = {probability:.6f}",
                     loc="left", fontsize=10)
        ax.grid(alpha=0.16)
    ax = axes[1, 1]
    time = np.linspace(0, 1, 801)
    pleft = 0.5 + 4 / (3 * np.pi) * np.cos(2 * np.pi * time)
    ax.plot(time, pleft, lw=2.3, color="#186c9e")
    ax.axhline(0.5, color="0.4", lw=1.6, ls="--")
    ax.scatter((0, 0.25, 0.5), 0.5 + 4 / (3 * np.pi) * np.cos(2 * np.pi * np.array((0, 0.25, 0.5))),
               c=("#186c9e", "#6c4699", "#b25812"), s=40, zorder=4)
    ax.set(xlim=(0, 1), ylim=(0, 1), xlabel=r"Time $t/T$", ylabel="P(left half)")
    ax.set_title("Relative phase redistributes probability", loc="left", fontsize=10)
    ax.grid(alpha=0.16)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, 0.055),
               ncol=2, frameon=False, fontsize=10)
    fig.text(0.5, 0.017, "Analytic densities: total probability = 1 at every time; energy populations = 1/2 each.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / "quantum-box-superposition.png", dpi=140, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
