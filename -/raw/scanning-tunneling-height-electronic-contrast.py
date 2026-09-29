"""Compare two exactly degenerate STM toy surfaces.

Python 3.14, numpy 2.3.5, matplotlib 3.10.7. Run from _media.
All distances below are in nm; all profiles and scales are chosen, not measured.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 2, 801)
    kappa, a, s0 = 10.0, 0.020, 0.50
    q = np.cos(2 * np.pi * x)
    h_a, h_b = a * q, np.zeros_like(x)
    rho_a, rho_b = np.ones_like(x), np.exp(2 * kappa * a * q)
    z_a = h_a + np.log(rho_a) / (2 * kappa) + s0
    z_b = h_b + np.log(rho_b) / (2 * kappa) + s0
    i0 = np.exp(-2 * kappa * s0)
    current_a = rho_a * np.exp(-2 * kappa * (s0 - h_a)) / i0
    current_b = rho_b * np.exp(-2 * kappa * (s0 - h_b)) / i0
    np.testing.assert_allclose(z_a, z_b, atol=1e-14)
    np.testing.assert_allclose(current_a, current_b, atol=1e-14)
    assert np.all(rho_b > 0) and np.all(z_b - h_b > 0)
    plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})
    fig, axs = plt.subplots(2, 2, figsize=(10, 7), dpi=120, facecolor="white")
    blue, orange = "#23629a", "#bf5719"

    def pair(ax, ya, yb):
        ax.plot(x, ya, color=blue, lw=2.8, label="A: corrugated, ρ = 1")
        ax.plot(x, yb, color=orange, lw=2.0, ls="--", label="B: flat, varying ρ")

    pair(axs[0, 0], h_a, h_b)
    axs[0, 0].set(title="Chosen geometric heights", ylabel="h (nm)", ylim=(-0.027, 0.033))
    axs[0, 0].legend(loc="upper right", fontsize=9)
    pair(axs[0, 1], rho_a, rho_b)
    axs[0, 1].set(title="Chosen electronic factors", ylabel="ρ (dimensionless)", ylim=(0.58, 1.62))
    pair(axs[1, 0], z_a, z_b)
    axs[1, 0].set(title="Same recorded height at constant current", ylabel="z (nm)", ylim=(0.472, 0.535))
    axs[1, 0].text(0.5, 0.92, "Both: z = 0.50 + 0.020 cos(2πx)",
                   transform=axs[1, 0].transAxes, ha="center", fontsize=9)
    pair(axs[1, 1], current_a, current_b)
    axs[1, 1].axhline(1, color="#555555", ls=":", lw=1.4)
    axs[1, 1].text(0.5, 0.92, "At fixed z = 0.50 nm: both exp[0.4 cos(2πx)]",
                   transform=axs[1, 1].transAxes, ha="center", fontsize=9)
    axs[1, 1].text(0.5, 0.025, "Dotted: feedback holds I / I₀ = 1",
                   transform=axs[1, 1].transAxes, ha="center", fontsize=9)
    axs[1, 1].set(title="Same current contrast at fixed height", ylabel="I / I₀", ylim=(0.55, 1.65))
    for ax in axs.flat:
        ax.set(xlabel="Lateral position x (nm)", xlim=(0, 2))
        ax.grid(alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("An STM height map does not uniquely determine geometric height", fontsize=15, y=0.98)
    fig.text(0.5, 0.027, "Chosen toy model: I = C ρ exp[−2κ(z−h)],  κ = 10 nm⁻¹,  I₀ / C = exp(−10)\n"
             "ρB = exp[0.4 cos(2πx)] > 0; constant barrier, low fixed bias; no measured data",
             ha="center", va="center", fontsize=10)
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.14, top=0.88, hspace=0.52, wspace=0.28)
    fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
