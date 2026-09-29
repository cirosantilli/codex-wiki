"""Show formal continuum scales and label a heuristic crossover explicitly."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    gamma = np.geomspace(1, 1e5, 701)
    coupling0 = .25
    cutoff = .01  # units of the isotropic Fermi energy
    coupling = coupling0*gamma**(1/3)
    gap = cutoff/np.sinh(1/coupling)
    bose = .218*gamma**(-1/3)  # pairs: mass 2m, number density n_F/2
    pair_temperature = .567*gap
    heuristic = 1/(1/pair_temperature+1/bose)
    conservative_weak_boundary = (.5/coupling0)**3
    fig, axes = plt.subplots(2, 1, figsize=(8.6, 7), sharex=True, layout="constrained")
    for ax in axes:
        ax.axvspan(conservative_weak_boundary, 1e5, color="0.94")
        ax.axvline(conservative_weak_boundary, color="0.55", ls=":")
        ax.set_xscale("log"); ax.set_yscale("log"); ax.grid(alpha=.18)
        ax.set_xlim(1, 1e5)
    axes[0].plot(gamma, gap, color="tab:blue", ls="--", label=r"Formal $\Delta$ from constant-DOS equation")
    axes[0].plot(gamma, bose, color="tab:orange", label=r"Ideal-pair $k_BT_{\rm BEC}$")
    inside = gamma <= conservative_weak_boundary
    axes[0].plot(gamma[inside], gap[inside], color="tab:blue", lw=2.3)
    axes[0].set(ylabel=r"Energy / $\varepsilon_{F0}$", title=r"Fixed density: $\lambda_0=0.25$, $\varepsilon_c=0.01\varepsilon_{F0}$")
    axes[0].legend(loc="upper left", frameon=False)
    axes[0].text(.48, .12, "Shaded: weak-coupling extrapolation\nnot a controlled large-anisotropy theory", transform=axes[0].transAxes,
                 fontsize=10, bbox={"facecolor":"white", "edgecolor":"none", "alpha":.85})
    axes[1].plot(gamma, pair_temperature, color="tab:blue", ls="--", label="Formal pair scale")
    axes[1].plot(gamma, bose, color="tab:orange", ls="--", label="Ideal-pair coherence scale")
    axes[1].plot(gamma, heuristic, color="tab:red", lw=2, label="Schematic smooth minimum")
    axes[1].set(xlabel=r"Mass anisotropy $\gamma=m_z/m$", ylabel=r"$k_BT/\varepsilon_{F0}$",
                title="Illustrative turnover; position and curve are not predictions")
    axes[1].legend(loc="upper left", frameon=False)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
