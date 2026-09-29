"""Gaussian trial widths and oscillator energy contributions; opaque PNG in cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Build with: make _media/quantum-variational-gaussian.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    widths = np.array([0.5, 1.0, 2.0])
    colors = ("#b45a13", "#226f9c", "#754694")
    x = np.linspace(-4, 4, 1601)
    fig, (density_ax, energy_ax) = plt.subplots(1, 2, figsize=(9.4, 4.5))
    fig.subplots_adjust(left=0.075, right=0.98, bottom=0.19, top=0.79,
                        wspace=0.3)
    fig.suptitle("A narrow Gaussian costs kinetic energy", fontsize=15, y=0.97)
    fig.text(0.5, 0.87, r"Harmonic oscillator: $\hbar=m=\omega=1$, "
             r"$\psi_a=(a/\pi)^{1/4}e^{-ax^2/2}$", ha="center")
    for a, color in zip(widths, colors):
        density = np.sqrt(a / np.pi) * np.exp(-a * x**2)
        density_ax.plot(x, density, color=color, lw=2.3,
                        label=rf"$a={a:g}$")
    density_ax.set(xlabel=r"Position $x$", ylabel=r"Probability density $|\psi_a(x)|^2$",
                   xlim=(-4, 4), ylim=(0, 0.88))
    density_ax.set_title("Broader ← smaller a; larger a → narrower", fontsize=11)
    density_ax.legend(loc="upper left", frameon=False, fontsize=9)
    density_ax.grid(alpha=0.15)
    positions = np.arange(3)
    kinetic = widths / 4
    potential = 1 / (4 * widths)
    energy_ax.bar(positions, kinetic, width=0.55, color="#216e9b",
                  label=r"Kinetic $a/4$")
    energy_ax.bar(positions, potential, bottom=kinetic, width=0.55,
                  color="#c88229", label=r"Potential $1/(4a)$")
    for position, t, v in zip(positions, kinetic, potential):
        energy_ax.text(position, t / 2, f"{t:g}", ha="center", va="center",
                       color="white", fontsize=11)
        energy_ax.text(position, t + v / 2, f"{v:g}", ha="center", va="center",
                       color="white", fontsize=11)
        energy_ax.text(position, t + v + 0.025, f"Total {t+v:g}",
                       ha="center", fontsize=10)
    energy_ax.set(xticks=positions, xticklabels=[r"$a=1/2$", r"$a=1$", r"$a=2$"],
                  ylabel="Energy", ylim=(0, 0.86), xlabel="Trial width parameter")
    energy_ax.set_title("Best balance at a = 1", fontsize=11)
    energy_ax.legend(loc="upper center", ncol=2, frameon=False, fontsize=9)
    energy_ax.set_axisbelow(True)
    energy_ax.grid(axis="y", alpha=0.15)
    fig.text(0.5, 0.035, "All densities have unit area. At a = 1, the trial is the exact ground state.",
             ha="center", fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=130,
                transparent=False, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
