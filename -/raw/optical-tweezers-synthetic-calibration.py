"""Synthetic harmonic-trap model, never measured data.

Python 3.14 / numpy 2.3.5 / matplotlib 3.10.7. Run in _media.
Stationary exact Ornstein-Uhlenbeck transitions; rectangular, demeaned,
nonoverlapping block periodograms in displacement squared per hertz.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def model():
    k_b, temperature, stiffness = 1.380649e-23, 300.0, 2.0e-5
    radius, viscosity, beta = 0.5e-6, 1.0e-3, 100.0e-9
    drag = 6 * np.pi * viscosity * radius
    tau = drag / stiffness
    sigma2 = k_b * temperature / stiffness
    dt, count = 1 / 20000, 200000
    rho = np.exp(-dt / tau)
    rng = np.random.default_rng(3817)
    x = np.empty(count)
    x[0] = np.sqrt(sigma2) * rng.normal()
    innovations = np.sqrt(sigma2 * (-np.expm1(-2 * dt / tau))) * rng.normal(size=count - 1)
    for j in range(1, count):
        x[j] = rho * x[j - 1] + innovations[j - 1]
    block_length = 4096
    blocks = x[:count // block_length * block_length].reshape(-1, block_length)
    blocks = blocks - blocks.mean(axis=1, keepdims=True)
    transformed = np.fft.rfft(blocks, axis=1)
    psd = dt / block_length * np.abs(transformed) ** 2
    psd[:, 1:-1] *= 2
    frequency = np.fft.rfftfreq(block_length, dt)
    # This is the exact Parseval check for the declared normalization, including endpoints.
    np.testing.assert_allclose(psd.sum(axis=1) * (frequency[1] - frequency[0]), np.mean(blocks ** 2, axis=1), rtol=1e-12)
    return locals()


def main():
    m = model()
    x, dt, sigma2, tau, drag, stiffness = [m[k] for k in ("x", "dt", "sigma2", "tau", "drag", "stiffness")]
    kbt, beta = m["k_b"] * m["temperature"], m["beta"]
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(2, 2, figsize=(11.2, 7.6), facecolor="white")
    blue, red = "#2367a2", "#bd4635"
    time = np.arange(len(x)) * dt
    axes[0, 0].plot(time[:400] * 1000, x[:400] * 1e9, color=blue, lw=1)
    axes[0, 0].set(xlabel="Time (ms)", ylabel="Displacement x (nm)", title="A. Synthetic equilibrium trajectory (first 20 ms)")
    axes[0, 0].axhline(0, color="0.6", lw=0.7)
    axes[0, 1].hist(x * 1e9, bins=65, density=True, color="#bdd6e8", label="Synthetic samples")
    grid = np.linspace(-60, 60, 500)
    density = np.exp(-(grid * 1e-9) ** 2 / (2 * sigma2)) / np.sqrt(2 * np.pi * sigma2) * 1e-9
    axes[0, 1].plot(grid, density, color=red, lw=2, label="Exact equilibrium density")
    axes[0, 1].set(xlabel="Displacement x (nm)", ylabel="Density (nm⁻¹)", title=f"B. Equipartition: σ = {np.sqrt(sigma2)*1e9:.2f} nm")
    axes[0, 1].legend(fontsize=9)
    f = m["frequency"][1:]
    continuous = 4 * kbt * drag / (stiffness ** 2 + (2 * np.pi * f * drag) ** 2)
    sampled = 2 * sigma2 * dt * (1 - m["rho"] ** 2) / ((1 - m["rho"]) ** 2 + 4 * m["rho"] * np.sin(np.pi * f * dt) ** 2)
    axes[1, 0].loglog(f, m["psd"].mean(axis=0)[1:] * 1e18, color="#8ab4d1", lw=0.9, label="Synthetic block-averaged PSD")
    axes[1, 0].loglog(f, continuous * 1e18, color=red, lw=1.8, label="Continuous one-sided model")
    axes[1, 0].loglog(f, sampled * 1e18, color="0.2", ls="--", lw=1.2, label="Exact sampled model (aliasing)")
    fc = 1 / (2 * np.pi * tau)
    axes[1, 0].axvline(fc, color="0.4", ls=":", lw=1)
    axes[1, 0].set(xlabel="Frequency f (Hz)", ylabel="Position PSD (nm²/Hz)", title=f"C. Corner frequency f_c = {fc:.1f} Hz", ylim=(5e-4, 2))
    axes[1, 0].legend(fontsize=8)
    speed = np.linspace(-100, 100, 101)
    displacement = drag * speed * 1e-6 / stiffness * 1e9
    axes[1, 1].plot(speed, displacement, color=blue, lw=2, label="Exact steady-drag model")
    axes[1, 1].plot([-50, 50], drag * np.array([-50, 50]) * 1e-6 / stiffness * 1e9, "o", color=red)
    axes[1, 1].axhline(0, color="0.7", lw=0.7)
    axes[1, 1].set(xlabel="Fluid speed u (µm/s)", ylabel="Mean displacement ⟨x⟩ (nm)", title="D. Drag calibration cross-check")
    axes[1, 1].text(0.04, 0.94, "At u = 50 µm/s:\n⟨x⟩ = 23.56 nm, V − V₀ = 0.2356 V\nζu = k⟨x⟩ = 0.4712 pN", transform=axes[1, 1].transAxes, va="top", fontsize=10)
    for ax in axes.flat:
        ax.spines[["right", "top"]].set_visible(False)
    fig.suptitle("Synthetic optical-trap calibration — NOT measured data", fontsize=16, y=0.98)
    fig.text(0.5, 0.018, "T = 300 K; a = 0.50 µm; η = 1.00 mPa s; k = 0.020 pN/nm; β = 100 nm/V.\n10 s at 20 kHz; exact stationary OU steps; no detector noise, exposure averaging or walls.", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.085, right=0.985, top=0.9, bottom=0.15, hspace=0.48, wspace=0.28)
    fig.savefig(Path(__file__).stem + ".png", dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
