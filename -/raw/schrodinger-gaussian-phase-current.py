"""Gaussian phase and comoving current; Python 3.14, NumPy 2.3.5, MPL 3.10.7.

Run from _media. Finite differences of the complex wavefunction check current
and the PDE, while a moving-interval integral independently checks boundary flux.
"""

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def psi(x, tau):
    return (2 * np.pi) ** (-0.25) / np.sqrt(1 + 1j * tau) * np.exp(
        -(x - 4 * tau) ** 2 / (4 * (1 + 1j * tau)) + 2j * x - 4j * tau
    )


def checks():
    x = np.linspace(-20, 28, 96001)
    dx = x[1] - x[0]
    tau, dt = 1.0, 1e-5
    p = psi(x, tau)
    rho = np.abs(p) ** 2
    norm = np.trapezoid(rho, x)
    # Dimensionless hbar/m=2: current follows from the complex amplitude,
    # rather than the phase-gradient expression used in the plotted curves.
    dp = np.gradient(p, dx, edge_order=2)
    j_numeric = 2 * np.imag(np.conj(p) * dp)
    j_exact = rho * (4 + (x - 4 * tau) * tau / (1 + tau**2))
    current_error = np.max(np.abs(j_numeric - j_exact))
    rho_t = (np.abs(psi(x, tau + dt)) ** 2 - np.abs(psi(x, tau - dt)) ** 2) / (2 * dt)
    continuity_error = np.max(np.abs(rho_t + np.gradient(j_numeric, dx)))
    p_t = (psi(x, tau + dt) - psi(x, tau - dt)) / (2 * dt)
    p_xx = np.gradient(dp, dx, edge_order=2)
    pde_error = np.max(np.abs(1j * p_t + p_xx))
    # Independent quadrature in a moving window; no erf in the computation.
    y = np.linspace(-1, 1, 20001)
    def interval_probability(t):
        return np.trapezoid(np.abs(psi(y + 4 * t, t)) ** 2, y)
    numerical_loss = -(interval_probability(tau + dt) - interval_probability(tau - dt)) / (2 * dt)
    left, right = 4 * tau - 1, 4 * tau + 1
    indices = [np.argmin(abs(x - z)) for z in (left, right)]
    j_rel_numeric = j_numeric - 4 * rho
    boundary_outflux = j_rel_numeric[indices[1]] - j_rel_numeric[indices[0]]
    # Spreading from an integral of the density independently checks width.
    variance = np.trapezoid((x - 4 * tau) ** 2 * rho, x)
    assert abs(norm - 1) < 1e-12
    assert abs(variance - 2) < 1e-11
    assert current_error < 4e-7
    assert continuity_error < 1e-6
    assert pde_error < 8e-6
    assert abs(numerical_loss - boundary_outflux) < 1e-6
    assert abs(interval_probability(0) - math.erf(1 / math.sqrt(2))) < 1e-8
    assert abs(interval_probability(1) - math.erf(0.5)) < 1e-8
    return dict(norm=float(norm), position_variance=float(variance),
                max_current_error=float(current_error),
                max_continuity_residual=float(continuity_error),
                max_schrodinger_residual=float(pde_error),
                moving_interval_initial_probability=interval_probability(0),
                moving_interval_probability_at_ts=interval_probability(1),
                moving_interval_probability_loss_rate=float(numerical_loss),
                moving_boundary_outward_flux=float(boundary_outflux),
                method="complex-amplitude finite differences, density quadrature, moving-boundary flux")


def main():
    result = checks()
    plt.rcParams.update({"font.size": 11, "figure.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), layout="constrained")
    y = np.linspace(-5, 5, 1500)
    density = np.exp(-y**2 / 4) / np.sqrt(4 * np.pi)
    relative_current = density * y / 2
    axes[0].plot(y, y**2 / 8, color="#6a439b", lw=2.4)
    axes[0].set(xlabel=r"Position relative to centre $y=(x-v_0t)/\sigma_0$",
                ylabel="Spreading phase (radians)", title=r"After removing $k_0x$ and a constant: $y^2/8$",
                xlim=(-5, 5), ylim=(0, 3.4))
    axes[0].annotate("Negative slope", xy=(-3, 9 / 8), xytext=(-4.7, 2.2),
                     arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    axes[0].annotate("Positive slope", xy=(3, 9 / 8), xytext=(1.4, 2.2),
                     arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
    axes[1].axvspan(-1, 1, color="#e4e4e4", alpha=0.65, label="Moving interval")
    axes[1].plot(y, relative_current, color="#2864ad", lw=2.4)
    axes[1].axhline(0, color="#777777", lw=0.8)
    for point, direction in ((-1, -1), (1, 1)):
        axes[1].axvline(point, color="#777777", ls="--", lw=1)
        axes[1].annotate("", xy=(point + direction * 0.8, 0.025), xytext=(point, 0.025),
                         arrowprops={"arrowstyle": "->", "color": "#c06414", "lw": 2})
    axes[1].text(0, 0.16, "Probability flows out on both sides", ha="center", fontsize=10)
    axes[1].set(xlabel=r"Position relative to centre $y=(x-v_0t)/\sigma_0$",
                ylabel=r"Relative probability current $t_s(j-v_0\rho)$",
                title=r"Phase slope sets the outward flow: $(\sigma_0\rho)y/2$",
                xlim=(-5, 5), ylim=(-0.15, 0.19))
    axes[1].legend(loc="lower right", frameon=False, fontsize=10)
    for ax in axes:
        ax.grid(alpha=0.18)
    fig.suptitle(r"Spreading at $t=t_s$: remove the centre's uniform drift", fontsize=13)
    fig.savefig(Path(__file__).stem + ".png", dpi=120, facecolor="white", transparent=False)
    plt.close(fig)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
