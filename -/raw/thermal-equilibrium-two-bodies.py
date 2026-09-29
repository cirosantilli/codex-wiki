"""Plot ideal thermal equilibration of two rigid bodies, without external losses.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes the matching PNG into the current working directory.
All capacities and the contact conductance are stipulated, not measurements.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    c1, c2, conductance = 1.0, 3.0, 0.1  # kJ/K, kJ/K, kJ/(s K)
    initial1, initial2 = 300.0, 400.0  # K
    energy = c1 * initial1 + c2 * initial2  # relative internal energy, kJ
    final = energy / (c1 + c2)
    tau = c1 * c2 / (conductance * (c1 + c2))
    time = np.linspace(0.0, 6.0 * tau, 601)
    difference = (initial2 - initial1) * np.exp(-time / tau)
    temp1 = final - c2 * difference / (c1 + c2)
    temp2 = final + c1 * difference / (c1 + c2)
    assert np.allclose(c1 * temp1 + c2 * temp2, energy)
    assert np.all(np.diff(temp1) > 0) and np.all(np.diff(temp2) < 0)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(8.2, 4.9), dpi=120)
    fig.subplots_adjust(left=0.105, right=0.965, bottom=0.24, top=0.83)
    fig.suptitle("Thermal equilibration of two finite bodies", fontsize=15)
    ax.plot(time, temp2, color="#b8531c", lw=2.7, label="Body 2: C₂ = 3 kJ/K")
    ax.plot(time, temp1, color="#216a99", lw=2.7, label="Body 1: C₁ = 1 kJ/K")
    ax.axhline(final, color="#24765c", linestyle="--", lw=1.6,
               label="Equilibrium limit: 375 K")
    ax.scatter([0, 0], [initial1, initial2], c=["#216a99", "#b8531c"], s=25, zorder=4)
    ax.axvline(tau, color="#888888", lw=1, linestyle=":")
    ax.text(tau + 0.6, 309, "τ = 7.5 s", fontsize=10, color="#555555")
    ax.set(xlim=(0, 45), ylim=(295, 407), xlabel="Time t (s)", ylabel="Temperature T (K)")
    ax.set_xticks([0, 7.5, 15, 22.5, 30, 37.5, 45])
    ax.set_yticks([300, 325, 350, 375, 400])
    ax.legend(loc="lower right", frameon=False, fontsize=10)
    ax.grid(alpha=0.18)
    fig.text(0.5, 0.125, "Isolated pair; fixed volumes; no work; G = 0.1 kJ/(s K)",
             ha="center", fontsize=10)
    fig.text(0.5, 0.070, "C₁T₁ + C₂T₂ = 1500 kJ at every time", ha="center", fontsize=10)
    fig.text(0.5, 0.025, "Ideal model with stipulated values; curves are not measurements",
             ha="center", fontsize=9, color="#555555")
    fig.savefig(Path(__file__).with_suffix(".png").name, transparent=False)
    plt.close(fig)
    print(f"Tf={final:g} K; relative E={energy:g} kJ; tau={tau:g} s")


if __name__ == "__main__":
    main()
