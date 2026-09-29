"""Charge-neutral donor model with the specified constant band parameters.

Outputs to cwd. Pure NumPy; no SciPy dependency. Densities are in cm^-3.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

KB = 1.380649e-23
HBAR = 1.054571817e-34
M_E = 9.1093837139e-31
Q_E = 1.602176634e-19
N_D = 1e15
E_B = 13.605693122994 * 0.3 / 12**2 * Q_E
E_G = 1.12 * Q_E

def densities(temperature):
    t = np.asarray(temperature, dtype=float)
    nc = 2 * (0.3 * M_E * KB * t / (2 * np.pi * HBAR**2))**1.5 / 1e6
    nv = 2 * (0.49 * M_E * KB * t / (2 * np.pi * HBAR**2))**1.5 / 1e6
    intrinsic = np.sqrt(nc * nv) * np.exp(-E_G / (2 * KB * t))
    donor_coefficient = 2 * np.exp(E_B / (KB * t)) / nc
    low = np.maximum(intrinsic, 1e-100)
    high = N_D + intrinsic
    for _ in range(130):
        middle = np.sqrt(low * high)
        residual = middle - intrinsic**2 / middle - N_D / (1 + donor_coefficient * middle)
        low, high = np.where(residual < 0, middle, low), np.where(residual >= 0, middle, high)
    electron = np.sqrt(low * high)
    return electron, intrinsic, nc, nv

def plateau_boundary(ratio, low, high):
    for _ in range(70):
        middle = (low + high) / 2
        if densities(middle)[0] < ratio * N_D:
            low = middle
        else:
            high = middle
    return (low + high) / 2

def main():
    temperature = np.geomspace(15, 1000, 1800)
    electron, intrinsic, nc, _ = densities(temperature)
    x = 1000 / temperature
    freeze = np.sqrt(N_D * nc / 2) * np.exp(-E_B / (2 * KB * temperature))
    lower = plateau_boundary(0.9, 50, 150)
    upper = plateau_boundary(1.1, 550, 700)
    fig, ax = plt.subplots(figsize=(8.0, 4.7), layout="constrained")
    ax.axvspan(1000 / upper, 1000 / lower, alpha=0.12, color="#39956b", label="Within 10% of donor density")
    ax.plot(x, np.log10(electron), color="#216ca4", lw=2.3, label="Charge-neutral electron density")
    hot, cold = temperature >= 600, temperature <= 65
    ax.plot(x[hot], np.log10(intrinsic[hot]), ":", color="#c65029", lw=2, label="Intrinsic limit")
    ax.plot(x[cold], np.log10(freeze[cold]), ":", color="#8552a3", lw=2, label="Freeze-out limit")
    ax.axhline(15, color="#555555", lw=1, ls="--")
    ax.text(35, 15.15, r"$N_D=10^{15}$ cm$^{-3}$", fontsize=10)
    ax.text(1.3, 17.15, "Intrinsic", fontsize=10)
    ax.text(6.8, 15.35, "Extrinsic plateau", ha="center", fontsize=10)
    ax.text(43, 12.7, "Freeze-out", fontsize=10)
    ax.set_xlim(0, 1000 / 15)
    ax.set_ylim(10, 18)
    ax.set_xlabel(r"Inverse temperature $1000\,\mathrm{K}/T$")
    ax.set_ylabel(r"$\log_{10}(n/\mathrm{cm}^{-3})$")
    ax.set_title("Donor ionization and intrinsic excitation")
    ax.grid(alpha=0.2)
    ax.legend(loc="lower left", fontsize=9)
    top = ax.secondary_xaxis("top", functions=(lambda x: 1000 / np.maximum(x, 1e-9), lambda t: 1000 / np.maximum(t, 1e-9)))
    top.set_xticks([300, 100, 50, 25, 15], labels=["300", "100", "50", "25", "15"])
    top.set_xlabel("Temperature (K)")
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
    plt.close(fig)

if __name__ == "__main__":
    main()
