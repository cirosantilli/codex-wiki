"""Matched square-barrier wavefunction and exact transmission; no measured data.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media with MPLBACKEND=Agg; writes matching basename to CWD.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def transmission(energy, width):
    """V0=1, length unit hbar/sqrt(2*m*V0); continuous at energy=1."""
    energy = np.asarray(energy, dtype=float)
    delta = energy - 1.0
    factor = np.full_like(energy, width**2)
    below, above = delta < 0, delta > 0
    factor[below] = np.sinh(width * np.sqrt(-delta[below]))**2 / (-delta[below])
    factor[above] = np.sin(width * np.sqrt(delta[above]))**2 / delta[above]
    return 1.0 / (1.0 + factor / (4.0 * energy))


def matched_coefficients(energy, width):
    """Solve four interface conditions independently of transmission formula."""
    k = np.sqrt(energy)
    s = np.sqrt(complex(1.0 - energy))
    ep, em, et = np.exp(s * width), np.exp(-s * width), np.exp(1j * k * width)
    matrix = np.array([[1, -1, -1, 0], [-1j*k, -s, s, 0],
                       [0, ep, em, -et], [0, s*ep, -s*em, -1j*k*et]], complex)
    return np.linalg.solve(matrix, np.array([-1, -1j*k, 0, 0], complex))


def main():
    plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
    width, energy = 4.0, 0.5
    k, decay = np.sqrt(energy), np.sqrt(1-energy)
    r, a, b, t = matched_coefficients(energy, width)
    exact = float(transmission(energy, width))
    assert abs(abs(t)**2-exact) < 1e-12
    assert abs(abs(r)**2+abs(t)**2-1) < 1e-12
    x = np.linspace(-5, 9, 1600)
    psi = np.empty_like(x, complex)
    derivative = np.empty_like(x, complex)
    left, inside, right = x < 0, (x >= 0) & (x <= width), x > width
    psi[left] = np.exp(1j*k*x[left])+r*np.exp(-1j*k*x[left])
    derivative[left] = 1j*k*(np.exp(1j*k*x[left])-r*np.exp(-1j*k*x[left]))
    psi[inside] = a*np.exp(decay*x[inside])+b*np.exp(-decay*x[inside])
    derivative[inside] = decay*(a*np.exp(decay*x[inside])-b*np.exp(-decay*x[inside]))
    psi[right] = t*np.exp(1j*k*x[right])
    derivative[right] = 1j*k*psi[right]
    assert np.max(np.abs(np.imag(psi.conj()*derivative)/k-exact)) < 1e-12
    fig = plt.figure(figsize=(10.4, 5.8), facecolor="white", layout="constrained")
    grid = fig.add_gridspec(2, 2, height_ratios=(1, 2.2), width_ratios=(1.1, 1))
    potential = fig.add_subplot(grid[0, 0])
    wave = fig.add_subplot(grid[1, 0], sharex=potential)
    probability = fig.add_subplot(grid[:, 1])
    blue, orange = "#1764a1", "#bc531d"
    for ax in (potential, wave):
        ax.axvspan(0, width, color="#edf1f4")
        ax.set_xlim(-5, 9)
        ax.grid(alpha=0.18)
    potential.plot([-5, 0, 0, width, width, 9], [0, 0, 1, 1, 0, 0], color="#303b46", lw=2)
    potential.axhline(energy, color=orange, ls="--", label=r"$E/V_0=0.5$")
    potential.set_ylim(-0.15, 1.3)
    potential.set_ylabel(r"$V/V_0$")
    potential.tick_params(labelbottom=False)
    potential.legend(loc="upper left", fontsize=10)
    potential.set_title("Finite barrier: equal exterior potentials", fontsize=13)
    wave.plot(x, psi.real, color=blue, lw=1.8, label=r"$\mathrm{Re}\,\psi$")
    wave.plot(x, psi.imag, color=orange, lw=1.7, label=r"$\mathrm{Im}\,\psi$")
    wave.plot(x, np.abs(psi), color="#333333", ls="--", lw=1.5, label=r"$|\psi|$")
    wave.set_ylabel("Amplitude (incident amplitude = 1)")
    wave.set_xlabel(r"$x/\ell$,  $\ell=\hbar/\sqrt{2mV_0}$")
    wave.legend(loc="lower left", ncol=3, fontsize=10)
    wave.text(0.5, 0.95, f"Conserved net current:  J / Jinc = T = {exact:.4f}",
              transform=wave.transAxes, ha="center", va="top", fontsize=10,
              bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9})
    energies = np.r_[np.linspace(0.02, 0.9999, 650), 1.0, np.linspace(1.0001, 4, 1100)]
    probabilities = transmission(energies, width)
    probability.plot(energies, probabilities, color=blue, lw=2)
    probability.axvspan(0, 1, color="#edf1f4")
    probability.axvline(1, color="#666666", ls="--", lw=1)
    probability.scatter([energy, 1], [exact, float(transmission(1, width))], color=orange, zorder=4)
    resonances = 1+(np.arange(1, 3)*np.pi/width)**2
    probability.scatter(resonances, np.ones_like(resonances), color=blue, zorder=4)
    probability.text(0.1, 0.93, "Tunnelling", fontsize=11)
    probability.text(1.3, 0.87, r"$qa=n\pi$:  $T=1$", fontsize=11)
    probability.annotate(r"$T(E=V_0)=0.2$", xy=(1, 0.2), xytext=(1.6, 0.37),
                         arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=11)
    probability.set(xlim=(0, 4), ylim=(0, 1.08), xlabel=r"Energy $E/V_0$",
                    ylabel="Transmission probability T", title=r"Exact transmission, $a/\ell=4$")
    probability.grid(alpha=0.18)
    fig.suptitle("Square-barrier wavefunction and transmission — model calculations", fontsize=15)
    fig.savefig(Path.cwd()/(Path(__file__).stem+".png"), dpi=110, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
