"""Exact infinite-well densities; not measured data.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Writes the matching PNG basename to the current working directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white",
                         "axes.facecolor": "white", "axes.spines.top": False,
                         "axes.spines.right": False})
    u = np.linspace(0, 1, 2001)
    phi1, phi2 = np.sqrt(2) * np.sin(np.pi * u), np.sqrt(2) * np.sin(2 * np.pi * u)
    theta = [0, np.pi / 2, np.pi]
    colors = ["#245b92", "#17775b", "#ac4c10"]
    labels = [r"$\theta=0$", r"$\theta=\pi/2$", r"$\theta=\pi$"]
    styles = ["-", "--", ":"]
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.6), sharey=True)
    for phase, color, label, style in zip(theta, colors, labels, styles):
        pure = np.abs(phi2 * np.exp(-4j * phase / 3)) ** 2
        coherent = np.abs((phi1 + np.exp(-1j * phase) * phi2) / np.sqrt(2)) ** 2
        analytic = np.sin(np.pi * u) ** 2 + np.sin(2 * np.pi * u) ** 2
        analytic += 2 * np.sin(np.pi * u) * np.sin(2 * np.pi * u) * np.cos(phase)
        assert np.allclose(coherent, analytic)
        assert np.isclose(np.trapezoid(pure, u), 1)
        assert np.isclose(np.trapezoid(coherent, u), 1)
        assert np.all(coherent >= 0)
        axes[0].plot(u, pure, color=color, ls=style, lw=3, label=label)
        axes[1].plot(u, coherent, color=color, lw=2.7, label=label)
    mixed = (phi1 ** 2 + phi2 ** 2) / 2
    axes[1].plot(u, mixed, color="#353535", lw=1.6, ls="--", zorder=5,
                 label="Incoherent mixture")
    axes[0].set_title(r"One excited eigenstate: $\phi_2$", pad=13)
    axes[1].set_title(r"Two energies: $(\phi_1+\phi_2)/\sqrt{2}$ initially", pad=13)
    for ax in axes:
        ax.set(xlim=(0, 1), ylim=(0, 4.2), xlabel=r"Position $u=x/L$")
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
        ax.grid(alpha=0.17)
        ax.legend(frameon=False, loc="upper right", fontsize=10,
                  ncol=2 if ax is axes[1] else 1, columnspacing=1.0)
    axes[0].set_ylabel(r"Dimensionless density $L|\psi(x,t)|^2$")
    axes[0].text(0.03, 3.90, "All three densities coincide\nEnergy outcome: E₂ with certainty",
                 va="top", fontsize=11)
    axes[1].text(0.03, 4.00, "Fixed probabilities:\n½ at E₁, ½ at E₂", va="top", fontsize=11)
    fig.suptitle("Stationary energy populations can coexist with changing position probabilities",
                 y=0.975, fontsize=14)
    fig.text(0.5, 0.083, r"$\theta=(E_2-E_1)t/\hbar=3E_1t/\hbar$ • "
             "the mixture and θ = π/2 densities coincide", ha="center", fontsize=11)
    fig.text(0.5, 0.035, "Exact analytic infinite-well model • each density integrates to one • not measured data",
             ha="center", fontsize=11)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.80, bottom=0.23, wspace=0.19)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
