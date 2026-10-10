"""Stipulated shell differences and attenuation; Python 3.14 / mpl 3.10.7.

No measured atomic energies or material attenuation coefficients are used.
Run from _media; output is an opaque white PNG in the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.7), dpi=120,
                             facecolor="white", layout="constrained")
    fig.suptitle("Chosen shell and filter model — not Barkla's measured spectrum", fontsize=14)
    ax = axes[0]
    for energy, label in [(0, "free electron"), (-.3, "M"), (-1.5, "L"), (-10, "K")]:
        ax.hlines(energy, .15, .85, color="#475569")
        label_y = .55 if energy == 0 else (-.45 if energy == -.3 else energy)
        ax.text(.9, label_y, label, va="center", fontsize=10)
    ax.annotate("", (.35, -10), (.35, -1.5),
                arrowprops={"arrowstyle": "->", "color": "#2563eb", "lw": 2})
    ax.annotate("", (.68, -10), (.68, -.3),
                arrowprops={"arrowstyle": "->", "color": "#b45309", "lw": 2})
    ax.text(.25, -5.5, r"$K\alpha$: 8.5", rotation=90, color="#2563eb", ha="center")
    ax.text(.59, -5.5, r"$K\beta$: 9.7", rotation=90, color="#b45309", ha="center")
    ax.set(xlim=(0, 1.5), ylim=(-11, 1.1), xticks=[],
           ylabel="Bound-state energy (keV)", title="Shell-energy differences")
    ax.text(.55, .6, "0", ha="center")
    ax.text(.1, -.35, "−0.3", va="top", fontsize=9)
    ax.text(.76, -1.7, "−1.5", va="top", fontsize=9)
    ax.text(.1, -10.2, "−10", va="top", fontsize=9)

    ax = axes[1]
    energies = np.array([8.5, 9.7])
    rates = np.array([4., 1.])
    mu = np.array([.2, .8])
    transmitted = rates * np.exp(-mu*2)
    for energy, rate, out in zip(energies, rates, transmitted):
        ax.vlines(energy-.035, 0, rate, color="#64748b", lw=3)
        ax.vlines(energy+.035, 0, out, color="#2563eb", lw=3)
    ax.plot([], [], color="#64748b", lw=3, label="input")
    ax.plot([], [], color="#2563eb", lw=3, label="after 2 mm")
    ax.legend(loc="upper right", frameon=False)
    ax.set(xlim=(8.15, 10.08), ylim=(0, 4.6), xticks=energies,
           xlabel="Photon energy (keV)", ylabel="Line rate (arbitrary unit)",
           title="Filtering changes weights")
    ax.text(8.5, 4.15, r"$K\alpha$", ha="center")
    ax.text(9.7, 1.15, r"$K\beta$", ha="center")

    ax = axes[2]
    thickness = np.linspace(0, 5, 251)
    alpha = 4*np.exp(-.2*thickness)
    beta = np.exp(-.8*thickness)
    ax.plot(thickness, alpha/4, color="#2563eb", lw=2,
            label=r"$K\alpha$ rate / input $K\alpha$ rate")
    ax.plot(thickness, alpha/(alpha+beta), color="#15803d", lw=2,
            label=r"$K\alpha$ fraction of surviving lines")
    ax.scatter([2, 2], [transmitted[0]/4, transmitted[0]/transmitted.sum()],
               c=["#2563eb", "#15803d"], zorder=3)
    ax.axvline(2, color="#94a3b8", lw=1, ls="--")
    ax.set(xlim=(0, 5), ylim=(0, 1.03), xlabel="Filter thickness (mm)",
           ylabel="Fraction", title="Purity versus remaining signal")
    ax.legend(loc="lower left", fontsize=8, frameon=False)
    ax.text(.2, .16, r"Chosen $\mu_\alpha=0.20$, $\mu_\beta=0.80\ \mathrm{mm}^{-1}$",
            fontsize=9)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
