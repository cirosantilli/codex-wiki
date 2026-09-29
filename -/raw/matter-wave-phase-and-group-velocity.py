"""Plot an original positive-energy wave-packet model; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media. Units are m=c=hbar=1. This scalar Fourier model illustrates
dispersion; it is not a spinor electron model or a measured particle trajectory.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False})
    p0, sigma_p = 0.75, 0.055
    e0 = np.sqrt(1 + p0**2)
    vg, vp = p0 / e0, e0 / p0
    p = np.linspace(p0 - 8 * sigma_p, p0 + 8 * sigma_p, 1801)
    weights = np.exp(-(p - p0)**2 / (4 * sigma_p**2))
    x = np.linspace(-32, 40, 2201)
    norm = np.trapezoid(weights, p)
    fig = plt.figure(figsize=(11.6, 6.2), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, width_ratios=[1.6, 1])
    for row, t in enumerate([0.0, 12.0]):
        ax = fig.add_subplot(grid[row, 0])
        phase = p[:, None] * x - np.sqrt(1 + p[:, None]**2) * t
        psi = np.trapezoid(weights[:, None] * np.exp(1j * phase), p, axis=0) / norm
        envelope = np.abs(psi)
        ax.plot(x, psi.real, color="#2563a6", lw=1.3, label=r"$\mathrm{Re}\,\Psi$")
        ax.plot(x, envelope, color="#b25c00", lw=2, label=r"envelope $|\Psi|$")
        ax.plot(x, -envelope, color="#b25c00", lw=1, alpha=0.45)
        ax.axvline(vg * t, color="#b25c00", ls="--", lw=1.4)
        ax.axvline(vp * t, color="#287147", ls=":", lw=1.7)
        ax.set(xlim=(-32, 40), ylim=(-1.14, 1.42), ylabel="Scaled amplitude",
               title=rf"$t={t:g}$: envelope center $x\simeq {vg*t:g}$; carrier phase $x={vp*t:g}$")
        ax.grid(alpha=0.17)
        if row == 0:
            ax.legend(loc="upper right", fontsize=10, framealpha=0.95)
        else:
            ax.set_xlabel(r"Position $x$  (units $\hbar/(mc)$)")
            ax.text(0.02, 0.96, "Dashed: group   ·   Dotted: one central-mode phase",
                    transform=ax.transAxes, va="top", fontsize=9)

    ax = fig.add_subplot(grid[:, 1])
    q = np.linspace(0, 1.65, 500)
    ax.plot(q, np.sqrt(1 + q**2), color="#2563a6", lw=2.4,
            label=r"$E(p)=\sqrt{1+p^2}$")
    ax.plot([0, 1.1], [0, vp * 1.1], color="#287147", ls=":", lw=2,
            label=rf"secant: $E_0/p_0={vp:.3f}$")
    ax.plot(q, e0 + vg * (q - p0), color="#b25c00", ls="--", lw=2,
            label=rf"tangent: $dE/dp={vg:.3f}$")
    ax.scatter([p0], [e0], color="black", zorder=5)
    ax.annotate(r"$p_0=0.75,\ E_0=1.25$", (p0, e0), xytext=(0.18, 1.76),
                arrowprops={"arrowstyle": "->", "color": "#555"})
    ax.set(xlim=(0, 1.65), ylim=(0, 2.08), xlabel=r"Momentum $p$  (units $mc$)",
           ylabel=r"Total energy $E$  (units $mc^2$)", title="Two slopes, two velocities")
    ax.grid(alpha=0.17)
    ax.legend(loc="lower right", fontsize=9.7)
    fig.suptitle("Matter-wave phase runs through a slower envelope", fontsize=16)
    fig.savefig(Path(__file__).stem + ".png", dpi=100, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
