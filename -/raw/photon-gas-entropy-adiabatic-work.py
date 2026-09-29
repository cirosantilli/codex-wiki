"""Original reversible expansion of an equilibrium vacuum photon gas.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: the PNG is written into CWD, using this script's stem.
Fixed two photon polarizations; no entropy exchange or production.
This is an analytic model, not a measured piston expansion.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    r = np.linspace(1, 8, 2200)  # physical volume relative to its initial value
    temperature = r**(-1 / 3)
    energy_density = temperature**4
    entropy_density = temperature**3
    energy = energy_density * r  # total internal energy, not energy density
    pressure = energy_density / 3  # p*V0/U0
    work = np.trapezoid(pressure, r)
    assert np.allclose(entropy_density * r, 1, rtol=1e-13)
    assert np.isclose(work, 1 - energy[-1], rtol=1e-6)
    assert np.allclose([temperature[-1], energy_density[-1], entropy_density[-1]],
                       [0.5, 1 / 16, 1 / 8], rtol=1e-13)
    # Differential first law: d(U/U0)/dr + p*V0/U0 = 0.
    assert np.allclose(np.gradient(energy, r, edge_order=2)[2:-2],
                       -pressure[2:-2], rtol=6e-6)

    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.6, 4.7), dpi=110)
    fig.subplots_adjust(left=0.085, right=0.975, bottom=0.19, top=0.78, wspace=0.30)
    fig.suptitle("Photon gas: conserved entropy, decreasing energy", fontsize=16, y=0.97)
    fig.text(0.5, 0.89, "Analytic reversible adiabatic expansion · fixed species · μγ = 0",
             ha="center", fontsize=11)
    colors = ("#2265a3", "#bb5a1b", "#268066")
    for values, color, label in zip(
            (temperature, energy_density, entropy_density), colors,
            (r"T/T$_0$ = r$^{-1/3}$", r"u/u$_0$ = r$^{-4/3}$", r"s/s$_0$ = r$^{-1}$")):
        left.plot(r, values, color=color, lw=2.5, label=label)
        left.plot(8, values[-1], "o", ms=5, color=color, clip_on=False)
    left.set(yscale="log", xlim=(1, 8), ylim=(0.055, 1.25),
             xlabel=r"Volume ratio r = V/V$_0$", ylabel="Ratio to initial value",
             title="Dilution and cooling")
    left.set_yticks([1 / 16, 1 / 8, 1 / 2, 1], ["1/16", "1/8", "1/2", "1"])
    left.set_xticks([1, 2, 4, 6, 8])
    left.minorticks_off()
    left.legend(loc="upper right", frameon=False, fontsize=9, labelspacing=0.22)
    left.grid(alpha=0.18)

    right.plot(r, pressure, color=colors[1], lw=2.5)
    right.fill_between(r, pressure, color=colors[1], alpha=0.22)
    right.set(xlim=(1, 8), ylim=(0, 0.36), xlabel=r"Volume ratio r = V/V$_0$",
              ylabel=r"Scaled pressure pV$_0$/U$_0$", title="The missing energy becomes work")
    right.set_xticks([1, 2, 4, 6, 8])
    right.text(0.97, 0.91, r"pV$_0$/U$_0$ = r$^{-4/3}$/3" + "\n\n"
               r"Shaded area: W/U$_0$ = 1/2" + "\n"
               r"Final U/U$_0$ = 1/2" + "\n"
               r"Total S/S$_0$ = 1",
               transform=right.transAxes, ha="right", va="top", fontsize=10)
    right.grid(alpha=0.18)
    fig.text(0.5, 0.045, "Original model, not measured data · entropy density decreases while total entropy stays fixed",
             ha="center", fontsize=10)
    output = Path(__file__).with_suffix('.png').name
    fig.savefig(output, facecolor="white", transparent=False)
    plt.close(fig)
    print(f"{output}: W/U0={work:.12g}; U_final/U0={energy[-1]:.12g}; S/S0=1")


if __name__ == "__main__":
    main()
