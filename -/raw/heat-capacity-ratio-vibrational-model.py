"""Analytical ideal diatomic model: active rotations and one quantum vibration.

No gas-specific parameters or measured curves; dissociation is excluded.
Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media; the output basename follows this script's basename.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    t = np.geomspace(0.08, 5.0, 700)  # t = T / Theta; rotations assumed active.
    x = 1 / t
    vib = x**2 * np.exp(-x) / (-np.expm1(-x))**2
    cv = 2.5 + vib
    cp = cv + 1
    gamma = cp / cv
    fig, axes = plt.subplots(1, 3, figsize=(11.7, 4.4), dpi=100)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.77, bottom=0.22, wspace=0.36)
    fig.suptitle("One vibrational mode changes heat capacity and γ", fontsize=17, y=0.97)
    fig.text(0.5, 0.87, "Analytical ideal diatomic model: rotations active, no dissociation — no measured data",
             ha="center", fontsize=11, color="#555555")
    cap, ratio, energy = axes
    cap.plot(t, cv, color="#2266a0", lw=2.5, label=r"$C_{V,\mathrm{m}}/R$")
    cap.plot(t, cp, color="#b45c23", lw=2.5, label=r"$C_{p,\mathrm{m}}/R$")
    cap.fill_between(t, cv, cp, color="#edf1f4")
    cap.text(0.18, 3.05, "Gap = 1", fontsize=10)
    cap.set(ylabel="Molar heat capacity / R", ylim=(2.35, 4.65))
    cap.legend(loc="upper left", fontsize=10, framealpha=1)
    cap.set_title("Mayer's relation survives", fontsize=12)

    ratio.plot(t, gamma, color="#7755a5", lw=2.5)
    ratio.axhline(7/5, color="#999999", ls=":", lw=1.2)
    ratio.axhline(9/7, color="#999999", ls=":", lw=1.2)
    ratio.text(0.11, 1.404, "7/5: vibration frozen", fontsize=9)
    ratio.text(0.11, 1.290, "9/7: classical limit", fontsize=9)
    ratio.set(ylabel=r"Heat-capacity ratio $\gamma$", ylim=(1.275, 1.425))
    ratio.set_title("More energy storage, lower γ", fontsize=12)

    reference = 0.2
    def u(theta):
        return 2.5 * theta + 1 / np.expm1(1 / theta)
    delta_u = u(t) - u(reference)
    energy.plot(t, delta_u, color="#2266a0", lw=2.5, label="Integral of varying capacity")
    energy.plot(t, 2.5 * (t-reference), "--", color="#b45c23", lw=1.9, label="Frozen-vibration approximation")
    energy.scatter([reference], [0], color="#333333", s=25, zorder=5)
    energy.set(ylabel=r"$[U(T)-U(0.2\Theta)]/(nR\Theta)$", ylim=(-0.65, 18))
    energy.set_title("Integrate to find energy", fontsize=12)
    energy.legend(loc="upper left", fontsize=8.5, framealpha=1)
    for ax in axes:
        ax.set(xscale="log", xlim=(0.08, 5), xlabel=r"Temperature $T/\Theta$")
        ax.set_xticks([0.1, 0.2, 0.5, 1, 2, 5], labels=["0.1", "0.2", "0.5", "1", "2", "5"])
        ax.grid(alpha=0.18)
    fig.text(0.5, 0.065, r"$\Theta=\hbar\omega/k_B$ sets the vibrational energy scale; "
             r"$C_{V,\mathrm{m}}/R=5/2+(\Theta/T)^2 e^{-\Theta/T}/(1-e^{-\Theta/T})^2$",
             ha="center", fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
