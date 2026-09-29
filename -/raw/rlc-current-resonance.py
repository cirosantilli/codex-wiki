"""Driven series-RLC amplitudes; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory; writes rlc-current-resonance.png there.
Here L=1 H, C=1 F, V0=1 V, so omega0=1 rad/s. R is always positive.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def amplitudes(omega, resistance, inductance=1.0, capacitance=1.0, voltage=1.0):
    """Return current and charge amplitudes, including their omega=0 limits."""
    omega = np.asarray(omega)
    charge = voltage/np.hypot(1/capacitance - inductance*omega**2, resistance*omega)
    return omega*charge, charge


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white"})
    omega = np.linspace(0, 2.5, 2501)
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.4), layout="constrained")
    for r, color in [(0.5, "#2369ad"), (1, "#c46b17"),
                     (2, "#39804a"), (4, "#9066a3")]:
        current, _ = amplitudes(omega, r)
        axes[0].plot(omega, current, color=color, lw=2.2, label=rf"$R={r:g}\,\Omega$")
        axes[0].scatter([1], [1/r], s=22, color=color, zorder=4)
    axes[0].axvline(1, color="#777777", ls=":", lw=1)
    axes[0].set(title="Current peaks at the same frequency", ylabel=r"Current amplitude $I_{\rm amp}$ (A)",
                ylim=(0, 2.15))
    axes[0].legend(frameon=False, fontsize=10)
    current, charge = amplitudes(omega, 1)
    axes[1].plot(omega, current, color="#2369ad", lw=2.3, label="Current / its peak")
    axes[1].plot(omega, charge/(2/np.sqrt(3)), color="#c46b17", lw=2.3, label="Charge / its peak")
    for w, color, name, y in [(1/np.sqrt(2), "#c46b17", "Charge peak", 0.13),
                              (np.sqrt(3)/2, "#777777", "Free ringing", 0.29),
                              (1, "#2369ad", "Current peak", 0.45)]:
        axes[1].axvline(w, color=color, ls=":", lw=1)
        axes[1].annotate(f"{name}: {w:.3f}", (w, y), xytext=(1.32, y),
                         color=color, fontsize=9,
                         arrowprops={"arrowstyle": "->", "color": color, "lw": 0.8})
    axes[1].set(title=r"Three distinct frequencies ($R=1\,\Omega$)",
                ylabel="Amplitude divided by its own peak", ylim=(0, 1.08))
    axes[1].legend(frameon=False, fontsize=9, loc="upper right")
    for ax in axes:
        ax.set(xlim=(0, 2.5), xlabel=r"Driving angular frequency $\omega/\omega_0$")
        ax.grid(alpha=0.18)
    fig.suptitle(r"Driven series RLC: fixed $L=1\,\mathrm{H}$, $C=1\,\mathrm{F}$, $V_0=1\,\mathrm{V}$", fontsize=14)
    fig.savefig("rlc-current-resonance.png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
