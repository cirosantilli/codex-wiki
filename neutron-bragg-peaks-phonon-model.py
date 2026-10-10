"""Chosen diffraction weights and a distinct monatomic one-phonon model.

No experimental data. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from _media; Gaussian width is illustrative, not a measured resolution.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def phonon_energy(x):
    return 10 * np.sin(np.pi * np.asarray(x) / 2)


def weight(x):
    x = np.asarray(x, dtype=float)
    return np.divide(x*x, np.sin(np.pi*x/2), out=np.zeros_like(x), where=x != 0)


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 4.8))
    fig.subplots_adjust(left=.055, right=.94, bottom=.22, top=.80, wspace=.42)
    fig.patch.set_facecolor("white")
    fig.suptitle("Chosen models: elastic order and one acoustic excitation", fontsize=16)
    ax = axes[0]
    h = np.arange(1, 7)
    for ratio, color, shift, label in [(1, "#2273aa", -.09, r"$b_2=b_1=b$"),
                                      (.5, "#cf6c22", .09, r"$b_2=b/2,\ b_1=b$")]:
        intensity = np.abs(1 + ratio * np.exp(1j*np.pi*h))**2
        # Suppress floating-point remnants of exact destructive interference.
        intensity[np.abs(intensity) < 1e-24] = 0
        ax.vlines(h+shift, 0, intensity, color=color, lw=2)
        ax.plot(h+shift, intensity, "o", color=color, ms=4, label=label)
    ax.set(title="A  Two-atom elastic cell", xlabel=r"Order $h$: $Q_h=2\pi h/a$",
           ylabel=r"Basis weight $|F_h|^2/b^2$", xticks=h, ylim=(-.12, 4.8))
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    ax.text(.04, .57, r"$d=a/2$"+"\nodd orders cancel\nwhen weights match",
            transform=ax.transAxes, fontsize=10)

    x = np.linspace(0, 1, 401)
    ax = axes[1]
    ax.plot(x, phonon_energy(x), color="#2273aa", lw=2.4)
    ax.scatter([.5, 1], phonon_energy([.5, 1]), color="#cf6c22", zorder=3)
    ax.set(title="B  Separate monatomic chain", xlabel=r"Reduced wave number $qa/\pi$",
           ylabel=r"Phonon energy $\varepsilon$ (meV)", xlim=(0, 1.02), ylim=(0, 12))
    ax.text(.04, .94, r"$a=4$ Å; $\varepsilon_*=10$ meV"+"\n"+r"$\varepsilon=\varepsilon_*\sin(qa/2)$",
            va="top", transform=ax.transAxes, fontsize=10)
    ax.grid(alpha=.2)

    ax = axes[2]
    energy = np.linspace(-1.5, 12, 451)
    sigma = .4
    signal = (weight(x)[None, :] * np.exp(-.5*((energy[:, None]-phonon_energy(x)[None, :])/sigma)**2)
              / (np.sqrt(2*np.pi)*sigma))
    mesh = ax.pcolormesh(x, energy, signal, shading="auto", cmap="magma", rasterized=True)
    ax.plot(x, phonon_energy(x), color="#76e8ec", lw=1, ls="--")
    ax.set(title="C  Chosen one-phonon readout", xlabel=r"Transfer $Qa/\pi$; here $Q=q$",
           ylabel=r"Energy transfer $E_i-E_f$ (meV)", xlim=(0, 1), ylim=(-1.5, 12))
    ax.text(.05, .95, r"$T=0$; $\sigma=0.4$ meV"+"\n"+r"$w=x^2/\sin(\pi x/2)$",
            color="white", va="top", transform=ax.transAxes, fontsize=10)
    cbar = fig.colorbar(mesh, ax=ax, fraction=.046, pad=.025)
    cbar.set_label("Model intensity (arbitrary units)")
    fig.text(.5, .055, "Original models, not data • panels A and B–C describe different lattices • independent intensity scales",
             ha="center", fontsize=10)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
