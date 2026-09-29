"""Free electron packet; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from _media. FFT evolution independently checks the closed-form solution,
normalization, position moments and the unchanged momentum distribution.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def packet(x, tau, k0=2.0):
    """Dimensionless x/sigma_0; sigma_0=1, hbar=1, m=1/2, t=tau."""
    return (2 * np.pi) ** (-0.25) / np.sqrt(1 + 1j * tau) * np.exp(
        -(x - 2 * k0 * tau) ** 2 / (4 * (1 + 1j * tau))
        + 1j * k0 * x - 1j * k0**2 * tau
    )


def checks():
    # Periodic FFT box is much wider than every occupied packet in this check.
    x = np.linspace(-128, 128, 32768, endpoint=False)
    dx = x[1] - x[0]
    k = 2 * np.pi * np.fft.fftfreq(x.size, dx)
    a0 = np.fft.fft(packet(x, 0))
    weights = np.abs(a0) ** 2 / np.sum(np.abs(a0) ** 2)
    assert abs(np.sum(k * weights) - 2) < 1e-12
    assert abs(np.sum((k - 2) ** 2 * weights) - 0.25) < 1e-12
    results = []
    for tau in (0, 0.5, 1, 2, 3):
        evolved = np.fft.ifft(a0 * np.exp(-1j * k**2 * tau))
        rho = np.abs(evolved) ** 2
        norm = dx * np.sum(rho)
        mean = dx * np.sum(x * rho)
        variance = dx * np.sum((x - mean) ** 2 * rho)
        error = np.sqrt(dx * np.sum(np.abs(evolved - packet(x, tau)) ** 2))
        spectral_energy = np.sum(k**2 * np.abs(np.fft.fft(evolved)) ** 2) / np.sum(np.abs(a0) ** 2)
        assert abs(norm - 1) < 2e-12
        assert abs(mean - 4 * tau) < 2e-12
        assert abs(variance - (1 + tau**2)) < 2e-11
        assert error < 2e-12
        assert abs(spectral_energy - 4.25) < 2e-12
        results.append(dict(tau=tau, norm=float(norm), mean=float(mean),
                            variance=float(variance), fft_l2_error=float(error),
                            mean_dimensionless_energy=float(spectral_energy)))
    hbar, mass, sigma0, k0 = 1.054571817e-34, 9.1093837e-31, 1e-9, 2e9
    ts = 2 * mass * sigma0**2 / hbar
    speed = hbar * k0 / mass
    energy = hbar**2 / (2 * mass) * (k0**2 + 1 / (4 * sigma0**2))
    return dict(method="FFT exp(-ik^2 tau), independent of closed-form evolution",
                samples=results, t_s_fs=ts / 1e-15, speed_m_s=speed,
                momentum_sd_kg_m_s=hbar / (2 * sigma0),
                kinetic_energy_eV=energy / 1.602176634e-19)


def main():
    result = checks()
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), layout="constrained",
                             gridspec_kw={"width_ratios": [1.5, 1]})
    x = np.linspace(-7, 18, 1800)
    colors = ("#2864ad", "#c06414", "#26816e")
    for tau, color in zip((0, 1, 2), colors):
        axes[0].plot(x, np.abs(packet(x, tau)) ** 2, color=color, lw=2.3,
                     label=rf"$t={tau}t_s$" if tau else "$t=0$")
    axes[0].set(xlabel="Position x (nm)", ylabel=r"Probability density $\rho$ (nm$^{-1}$)",
                xlim=(-7, 18), ylim=(0, 0.435), title="The centre travels; the area stays one")
    axes[0].legend(frameon=False)
    tau = np.linspace(0, 2.3, 400)
    axes[1].plot(tau, np.sqrt(1 + tau**2), color=colors[0], lw=2.3, label="Free evolution")
    axes[1].axhline(1, color="#777777", ls="--", lw=1.5, label="Translation alone")
    axes[1].scatter([0, 1, 2], np.sqrt(1 + np.array([0, 1, 2]) ** 2), c=colors, zorder=3)
    axes[1].set(xlabel=r"Time $t/t_s$", ylabel=r"Position spread $\sigma_t$ (nm)",
                title=r"$\sigma_t=\sigma_0\sqrt{1+(t/t_s)^2}$", xlim=(0, 2.3), ylim=(0.85, 2.65))
    axes[1].legend(loc="upper left", frameon=False)
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.suptitle(r"Free Gaussian electron packet: $\sigma_0=1$ nm, $k_0=2$ nm$^{-1}$, $t_s=17.276$ fs", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
