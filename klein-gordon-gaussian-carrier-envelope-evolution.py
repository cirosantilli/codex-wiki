#!/usr/bin/env python3
"""Original spectral-integral illustration; writes its matching PNG to CWD.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Use MPLBACKEND=Agg and a writable MPLCONFIGDIR when generating.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    c, omega_gap, k0, sigma = 1.0, 1.0, 1.0, 0.18
    omega_c = np.sqrt(omega_gap**2 + c**2 * k0**2)
    vp, vg = omega_c / k0, c**2 * k0 / omega_c
    x = np.linspace(-16, 26, 2101)
    k = np.linspace(k0 - 8 * sigma, k0 + 8 * sigma, 2401)
    omega = np.sqrt(omega_gap**2 + c**2 * k**2)
    amplitude = np.exp(-0.5 * ((k - k0) / sigma) ** 2) / (
        np.sqrt(2 * np.pi) * sigma
    )
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white"})
    fig, axes = plt.subplots(3, 1, figsize=(9.2, 6.7), sharex=True)
    for ax, time in zip(axes, (0.0, 4.0, 8.0), strict=True):
        # Chunk spatial positions to avoid a large temporary complex array.
        field = np.empty(x.size, dtype=complex)
        for start in range(0, x.size, 160):
            spatial = x[start : start + 160]
            phase = k[:, None] * spatial[None, :] - omega[:, None] * time
            field[start : start + spatial.size] = np.trapezoid(
                amplitude[:, None] * np.exp(1j * phase), k, axis=0
            )
        ax.plot(x, field.real, color="#2166ac", lw=1.4, label="Real wavefield")
        ax.plot(x, np.abs(field), color="#d97706", lw=1.8, label="Amplitude envelope")
        ax.plot(x, -np.abs(field), color="#d97706", lw=1.8)
        ax.axvline(vg * time, color="#337755", ls="--", lw=1.5, label=r"Leading centre $x=v_g t$")
        ax.axvline(vp * time, color="#934aa1", ls=":", lw=1.8, label=r"Carrier reference $x=v_p t$")
        ax.text(0.015, 0.89, rf"$t={time:g}$", transform=ax.transAxes)
        ax.set_ylim(-1.12, 1.12)
        ax.set_yticks((-1, 0, 1))
        ax.set_ylabel("Amplitude")
        ax.grid(alpha=0.15)
        ax.set_facecolor("white")
    axes[0].legend(loc="upper center", bbox_to_anchor=(0.5, 1.45), ncol=2, fontsize=10, frameon=False)
    axes[-1].set_xlabel(r"Position $x$ (dimensionless)")
    axes[-1].set_xlim(x[0], x[-1])
    fig.suptitle("Klein–Gordon packet: carrier moves through the envelope", y=0.995, fontsize=14)
    fig.text(0.5, 0.015, r"Exact spectral integral; $c=\omega_0=k_0=1$, $\sigma=0.18$. Phase marker is a reference, not a measured crest.", ha="center", fontsize=10)
    fig.tight_layout(rect=(0, 0.035, 1, 0.95), h_pad=0.7)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=120, facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
