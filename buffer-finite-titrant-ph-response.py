"""Constant-volume equilibrium response; run from _media with Python 3.14.

Dependencies: matplotlib 3.10.7, numpy 2.3.5 (root pyproject.toml).
All values are stipulated; curves contain no experimental data.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def charge_inventory(ph, concentration, ka=1e-5, kw=1e-14):
    """A⁻ + OH⁻ − H⁺ in mol/L, with c° = 1 mol/L."""
    h = 10.0 ** (-np.asarray(ph))
    return concentration * ka / (ka + h) + kw / h - h


def equilibrium_ph(dose, concentration, initial_ph=5.0):
    """Invert strictly increasing charge inventory with bracketed bisection."""
    dose = np.asarray(dose)
    target = charge_inventory(initial_ph, concentration) + dose
    lo = np.full_like(dose, -2.0, dtype=float)
    hi = np.full_like(dose, 16.0, dtype=float)
    for _ in range(70):
        mid = (lo + hi) / 2
        below = charge_inventory(mid, concentration) < target
        lo = np.where(below, mid, lo)
        hi = np.where(below, hi, mid)
    return (lo + hi) / 2


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8), layout="constrained", facecolor="white")
    dose = np.linspace(-0.006, 0.006, 1201)
    for concentration, color in [(0.1, "#2466a8"), (0.01, "#d45d18")]:
        ph = equilibrium_ph(dose, concentration)
        axes[0].plot(dose * 1000, ph, color=color, lw=2.5, label=f"C = {concentration:.3f} mol/L")
        axes[0].scatter([2], equilibrium_ph(np.array([0.002]), concentration), color=color, zorder=3)
    axes[0].axvspan(-5, 5, color="#d45d18", alpha=0.07)
    axes[0].axvline(-5, color="#d45d18", ls=":", lw=1)
    axes[0].axvline(5, color="#d45d18", ls=":", lw=1)
    axes[0].set(xlim=(-6, 6), ylim=(2.5, 11.5), title="Finite partner inventories limit the useful range", ylabel="Equilibrium pH", xlabel="Signed added dose (mmol/L)")
    axes[0].legend(loc="upper left", frameon=False, fontsize=10)
    axes[0].text(-4.6, 9.1, "Dotted lines: dilute sample's\napproximate ±C/2 inventory", fontsize=10)
    dose = np.linspace(-0.004, 0.004, 801)
    beta0 = np.log(10) * (0.01 / 4 + 1e-5 + 1e-9)
    axes[1].plot(dose * 1000, equilibrium_ph(dose, 0.01), color="#d45d18", lw=2.5, label="Full equilibrium, C = 0.010 mol/L")
    axes[1].plot(dose * 1000, 5 + dose / beta0, color="#333333", lw=1.8, ls="--", label="Initial local approximation")
    axes[1].scatter([2], equilibrium_ph(np.array([0.002]), 0.01), color="#d45d18", zorder=3)
    axes[1].annotate("+2 mmol/L → pH 5.3668", xy=(2, float(equilibrium_ph(np.array([0.002]), 0.01)[0])), xytext=(-3.5, 5.65), arrowprops={"arrowstyle": "->", "color": "0.4"}, fontsize=10)
    axes[1].set(xlim=(-4, 4), ylim=(3.8, 6.15), title="The initial derivative predicts only small changes", ylabel="Equilibrium pH", xlabel="Signed added dose (mmol/L)")
    axes[1].legend(loc="lower right", frameon=False, fontsize=9)
    for ax in axes:
        ax.axhline(5, color="0.65", lw=0.8, zorder=0)
        ax.grid(alpha=0.18)
        ax.set_facecolor("white")
    fig.suptitle("Calculated response from pH 5: pKa = 5, Kw = 10⁻¹⁴, constant volume", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
