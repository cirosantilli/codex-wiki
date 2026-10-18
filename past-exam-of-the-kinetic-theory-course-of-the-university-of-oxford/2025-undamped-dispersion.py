"""Plot the exact undamped dispersion branches for Oxford A15089H1 (2025).

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7, as specified in
this repository's pyproject.toml. Run from the intended output directory;
this script writes only 2025-undamped-dispersion.png in the current directory.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def branches(k, v0=1.0, v1=0.5, v2=0.56):
    """Return omega/omega_pe, with k in units of inverse lambda_De."""
    delta = v2 - v1
    upper_edge = v0 + delta
    a = v0**2 + delta * (v0 - v1)
    b = v0 * v1 * upper_edge
    result = []
    for wavenumber in k:
        if wavenumber == 0:
            result.append([-np.sqrt(a) / v0, 0.0, np.sqrt(a) / v0])
            continue
        q = -np.expm1(-wavenumber**2)
        roots = np.roots([q, -q * v2, -a, b])
        if np.max(np.abs(roots.imag)) > 1e-10:
            raise ValueError("Expected three real phase velocities")
        u = np.sort(roots.real)
        if not (u[0] < -v0 and v1 < u[1] < v2 and u[2] > upper_edge):
            raise ValueError("A root left its undamped interval")
        result.append(wavenumber * u / v0)
    return np.array(result).T


def main():
    plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    k = np.linspace(0, 3, 601)
    omega_minus, omega_acoustic, omega_plus = branches(k)
    fig, ax = plt.subplots(figsize=(9.2, 5.7), layout="constrained")
    blue, orange, teal = "#2463a7", "#c56813", "#147d71"
    ax.fill_between(k, 0.5 * k, 0.56 * k, color=orange, alpha=0.17)
    ax.plot(k, omega_plus, color=blue, linewidth=2.5, label="Positive Langmuir branch")
    ax.plot(k, omega_acoustic, color=orange, linewidth=2.5, label="Electron acoustic branch")
    ax.plot(k, omega_minus, color=teal, linewidth=2.5, label="Negative Langmuir branch")
    for slope, color in [(1.06, blue), (0.5, orange), (-1, teal)]:
        ax.plot(k, slope * k, color=color, linestyle=(0, (4, 3)),
                linewidth=1.1, alpha=0.7, zorder=1)
    cutoff = np.sqrt(1.03)
    ax.scatter([0, 0, 0], [cutoff, 0, -cutoff], s=22,
               color=[blue, orange, teal], zorder=5, clip_on=False)
    ax.axhline(0, color="#909090", linewidth=0.7)
    ax.set(xlim=(0, 3.05), ylim=(-3.35, 3.55),
           xlabel=r"Wavenumber $k\lambda_{\mathrm{De}}$",
           ylabel=r"Frequency $\omega/\omega_{\mathrm{pe}}$",
           title="Three undamped branches of a plasma with a velocity plateau")
    ax.text(1.78, 2.8, r"$u>v_0+\delta$", color=blue)
    ax.text(1.9, 0.63, r"$v_1<u<v_2$", color=orange)
    ax.text(1.92, -2.63, r"$u<-v_0$", color=teal)
    ax.text(0.03, 0.02, r"$v_1/v_0=0.50,\quad \delta/v_0=0.06$",
            transform=ax.transAxes, fontsize=11, va="bottom")
    ax.text(0.98, 0.02, "Dashed: short-wavelength limits",
            transform=ax.transAxes, fontsize=10, ha="right", va="bottom", color="#555555")
    ax.grid(alpha=0.15)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.96)
    fig.savefig(Path("2025-undamped-dispersion.png"), dpi=125, transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
