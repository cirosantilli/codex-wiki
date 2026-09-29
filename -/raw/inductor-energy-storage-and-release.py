"""Show magnetic energy buildup and release into a closed resistive loop.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7.
Write an opaque PNG with this script's basename to the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    resistance, inductance, voltage = 2.0, 0.5, 6.0
    tau = inductance / resistance
    initial_current = voltage / resistance
    initial_energy = 0.5 * inductance * initial_current**2
    initial_power = resistance * initial_current**2
    time = np.linspace(0.0, 5.0 * tau, 2001)
    decay = np.exp(-time / tau)
    stored_charge = 0.5 * inductance * (initial_current * (1.0 - decay))**2
    stored_decay = initial_energy * decay**2
    dissipated = initial_energy * (1.0 - decay**2)
    power = initial_power * decay**2
    energy_tau = initial_energy * (1.0 - np.exp(-1.0))**2
    full_integral = initial_power * tau / 2.0
    np.testing.assert_allclose([initial_energy, initial_power, full_integral],
                               [2.25, 18.0, 2.25])
    np.testing.assert_allclose(energy_tau, 0.8990469020108881, rtol=1e-14)
    np.testing.assert_allclose(stored_decay + dissipated, initial_energy)
    np.testing.assert_allclose(2.0 * stored_decay / tau, power)
    np.testing.assert_allclose(inductance * (-initial_current * decay / tau)
                               + resistance * initial_current * decay, 0.0,
                               atol=1e-14)
    # Compare sampled power's integral with the exact finite-time heat transfer.
    np.testing.assert_allclose(np.trapezoid(power, time), dissipated[-1],
                               rtol=3e-6)

    blue, orange, green, grey = "#176997", "#b85d24", "#287d59", "#65717b"
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 5.3), dpi=120,
                             facecolor="white")
    axes[0].plot(time, stored_charge, color=blue, lw=2.6,
                 label="Stored during buildup (starts at 0 A)")
    axes[0].plot(time, stored_decay, color=orange, lw=2.6,
                 label="Stored during decay (starts at 3 A)")
    axes[0].plot(time, dissipated, color=green, ls="--", lw=2.2,
                 label="Heat accumulated during decay")
    axes[0].axhline(initial_energy, color=grey, ls=":", lw=1.1)
    axes[0].axvline(tau, color=grey, ls="--", lw=1.1, zorder=0)
    axes[0].scatter([tau], [energy_tau], color=blue, zorder=5)
    axes[0].annotate("U(τ) = 0.899047 J", (tau, energy_tau),
                     xytext=(0.43, 0.68), color=blue, fontsize=10,
                     arrowprops={"arrowstyle": "->", "color": blue})
    axes[0].text(0.76, 2.31, "Total available: 2.25 J", color=grey, fontsize=10)
    axes[0].text(tau, -0.20, r"$\tau$", ha="center", color=grey,
                 transform=axes[0].get_xaxis_transform())
    axes[0].set(title="Two experiments, the same inductor", ylabel="Energy (J)",
                ylim=(0, 2.6))
    axes[0].legend(loc="center right", bbox_to_anchor=(1.03, 0.54),
                    frameon=False, fontsize=8.5)

    axes[1].plot(time, power, color=orange, lw=2.6,
                 label=r"$P_R=18e^{-2t/\tau}$ W")
    axes[1].fill_between(time, 0, power, color=orange, alpha=0.20)
    axes[1].text(0.43, 12.5, r"$\int_0^\infty P_R\,dt=2.25$ J", fontsize=13)
    axes[1].text(0.43, 9.8, "Stored energy becomes heat", fontsize=11, color=grey)
    axes[1].text(0.43, 7.7, "Energy / power time constant: 0.125 s",
                 fontsize=9.5, color=grey)
    axes[1].scatter([tau], [initial_power * np.exp(-2.0)],
                    color=orange, zorder=5)
    axes[1].annotate("P at τ: 2.43604 W", (tau, initial_power * np.exp(-2.0)),
                     xytext=(0.46, 4.0), fontsize=10, color=orange,
                     arrowprops={"arrowstyle": "->", "color": orange})
    axes[1].set(title="Release: closed R–L loop, no battery", ylabel="Heating power (W)",
                ylim=(0, 20))
    axes[1].legend(loc="upper right", frameon=False, fontsize=10)
    for ax in axes:
        ax.set(xlim=(0, 5 * tau), xlabel="Time since each experiment starts (s)")
        ax.set_xticks(np.arange(6) * tau)
        ax.grid(alpha=0.16)
    fig.suptitle("Inductor energy: R = 2 Ω, L = 0.5 H, buildup supply = 6 V",
                 fontsize=15)
    fig.text(0.5, 0.035,
             f"Shaded area through 1.25 s: {dissipated[-1]:.5f} J    •    "
             "Integral over all time: 2.25 J    •    Current keeps a closed path",
             ha="center", fontsize=10, color=grey)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.82, bottom=0.22, wspace=0.28)
    fig.savefig(Path(__file__).with_suffix(".png").name,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
