"""Exact harmonic-trap equilibrium densities at a common temperature.

Write optical-trap-thermal-position.png to the working directory.
Uses the repository numpy/matplotlib dependencies; tested with Python 3.14.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def density(q, kappa):
    """Probability density per unit q, where ell = sqrt(k_B T / k_0)."""
    return np.sqrt(kappa / (2 * np.pi)) * np.exp(-0.5 * kappa * q**2)


def main():
    q = np.linspace(-4, 4, 1601)
    integration_q = np.linspace(-12, 12, 48001)
    stiffnesses = np.array([1.0, 2.0, 4.0])
    colors = ("#2469a0", "#c76720", "#27805a")
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, ax = plt.subplots(figsize=(8.8, 5.7))
    fig.subplots_adjust(left=0.11, right=0.96, bottom=0.32, top=0.77)
    fig.suptitle("Thermal force calibration model", fontsize=19, y=0.97)
    fig.text(0.5, 0.89, "Exact Gaussian position densities • common temperature • κ = k/k₀", ha="center", fontsize=12)
    for kappa, color in zip(stiffnesses, colors):
        pdf = density(integration_q, kappa)
        area = np.trapezoid(pdf, integration_q)
        mean = np.trapezoid(integration_q * pdf, integration_q)
        variance = np.trapezoid(integration_q**2 * pdf, integration_q)
        energy = np.trapezoid(0.5 * kappa * integration_q**2 * pdf, integration_q)
        np.testing.assert_allclose([area, mean, variance, energy], [1, 0, 1/kappa, 0.5], atol=2e-14)
        assert np.all(pdf >= 0)
        sigma = 1 / np.sqrt(kappa)
        ax.plot(q, density(q, kappa), lw=2.6, color=color, label=f"κ = {kappa:g}    σ/ℓ = {sigma:.3f}")
        print(f"κ={kappa:g}: area={area:.15f}, mean={mean:.3g}, variance={variance:.15f}, mean U/(k_BT)={energy:.15f}")
    ax.set(xlim=(-4, 4), ylim=(0, 0.86), xlabel=r"Displacement $q=x/\ell$, where $\ell=\sqrt{k_BT/k_0}$", ylabel=r"Probability density $p_q(q)=\ell\,p(\ell q)$")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.18)
    ax.legend(frameon=False, fontsize=11, loc="upper right")
    ax.axvline(0, color="#777777", lw=0.8, ls=":")
    fig.text(0.5, 0.14, "Each curve has total area 1. Quadrupling stiffness halves the position standard deviation.", ha="center", fontsize=11)
    fig.text(0.5, 0.065, "Model curves, not experimental data: σ² = kBT/k, so measured variance calibrates stiffness.", ha="center", fontsize=10, color="#555555")
    fig.savefig("optical-trap-thermal-position.png", dpi=110, facecolor="white", transparent=False)
    plt.close(fig)
    thermal_energy_pn_nm = 1.380649e-23 * 300 / 1e-21
    sigma_nm = np.sqrt(thermal_energy_pn_nm / 0.01)
    print(f"300 K example: kBT={thermal_energy_pn_nm:.7f} pN nm, σ={sigma_nm:.7f} nm")


if __name__ == "__main__":
    main()
