"""Plot the leading thermal profile of a pulled mush; write PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    r, omega, theta_inf, concentration = 0.9, 2.0, 0.5, 10.0
    height = np.log1p(omega / theta_inf) / (r * omega)
    z_m = np.linspace(0.0, height, 300)
    z_l = np.linspace(height, height + 4.0 / r, 400)
    theta_m = -theta_inf / omega * np.expm1(r * omega * (height - z_m))
    theta_l = theta_inf * (-np.expm1(-r * (z_l - height)))
    phi = -theta_m / (concentration - theta_m)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), dpi=100, facecolor="white")
    axes[0].plot(z_m, theta_m, color="#1766aa", lw=2.5, label="Mush")
    axes[0].plot(z_l, theta_l, color="#d87922", lw=2.5, label="Liquid")
    axes[0].axhline(theta_inf, color="0.45", ls=":", lw=1)
    axes[0].set(xlabel=r"Height $\zeta=Vz/\kappa$", ylabel=r"Temperature $\theta$",
                title="Smooth temperature and heat-flux matching")
    axes[0].legend(frameon=False, loc="lower right")
    axes[1].plot(z_m, phi, color="#1766aa", lw=2.5, label="Mush")
    axes[1].plot(z_l, np.zeros_like(z_l), color="#d87922", lw=2.5, label="Liquid")
    axes[1].set(xlabel=r"Height $\zeta=Vz/\kappa$", ylabel=r"Crystal volume fraction $\varphi$",
                title="Remaining brine freezes at the lower front")
    for ax in axes:
        ax.axvline(height, color="0.5", ls="--", lw=1)
        ax.annotate("Mush–liquid interface", (height, 0.97), xycoords=("data", "axes fraction"),
                    xytext=(6, -2), textcoords="offset points", va="top", fontsize=9)
        ax.set_xlim(0, z_l[-1])
        ax.grid(alpha=0.2)
    fig.suptitle(r"$r=0.9,\ \Omega=2,\ \theta_\infty=0.5,\ \mathcal{C}=10$", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,
                dpi=100, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
