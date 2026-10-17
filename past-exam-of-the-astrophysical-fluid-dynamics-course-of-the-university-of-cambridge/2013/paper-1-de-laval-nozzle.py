"""Invert the isentropic area-Mach law on its selected transonic branch."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def area_ratio(mach, gamma):
    return (2/(gamma+1)*(1+(gamma-1)*mach**2/2))**((gamma+1)/(2*(gamma-1)))/mach


def invert_area(area, supersonic, gamma):
    lo, hi = (1., 15.) if supersonic else (1e-6, 1.)
    for _ in range(70):
        mid = (lo+hi)/2
        if (area_ratio(mid, gamma) < area) == supersonic:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    gamma = 5/3
    z = np.linspace(-2.5, 3.5, 501)
    area = 1+.45*z*z
    mach = np.array([invert_area(a, zz >= 0, gamma) for zz, a in zip(z, area)])
    q = (gamma+1)/(2+(gamma-1)*mach**2)
    speed = mach*np.sqrt(q)
    density = q**(1/(gamma-1))
    assert np.max(np.abs(area_ratio(mach, gamma)-area)) < 1e-10
    assert np.max(np.abs(density*speed*area-1)) < 1e-10
    fig, axes = plt.subplots(3, 1, figsize=(8, 7), sharex=True, layout="constrained")
    radius = np.sqrt(area)
    axes[0].fill_between(z, -radius, radius, color="tab:blue", alpha=.12)
    axes[0].plot(z, radius, color="0.3"); axes[0].plot(z, -radius, color="0.3")
    axes[0].set(ylabel=r"Radius / throat radius", title=r"Selected choked branch, $\gamma=5/3$")
    axes[1].plot(z, mach, color="tab:purple", label=r"Mach number $u/c_s$")
    axes[1].axhline(1, color="0.4", ls="--", lw=1)
    axes[1].legend(loc="upper left"); axes[1].set(ylabel="Mach number")
    axes[2].plot(z, speed, label=r"$u/c_*$", color="tab:orange")
    axes[2].plot(z, density, label=r"$\rho/\rho_*$", color="tab:blue")
    axes[2].axhline(2, color="0.5", ls=":", label=r"Asymptotic $u/c_*=2$")
    axes[2].set(xlabel="Axial coordinate (arbitrary units)", ylabel="Normalized state")
    axes[2].legend(ncol=3, loc="upper right")
    for ax in axes:
        ax.axvline(0, color="0.6", ls="--", lw=1); ax.grid(alpha=.18)
    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=130, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
