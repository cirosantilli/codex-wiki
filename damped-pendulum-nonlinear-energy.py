"""Nonlinear versus linear pendulum and exact energy loss; illustrative only.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../damped-pendulum-nonlinear-energy.py
Standalone fixed-step RK4 integrates angle, velocity, and dissipated energy.
The PNG is written to the current working directory.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

C = 0.2


def solve(angle, step=0.005, duration=25.0):
    time = np.linspace(0, duration, round(duration/step) + 1)
    step = time[1] - time[0]
    state = np.empty((len(time), 3))
    state[0] = (angle, 0, 0)

    def rhs(y):
        theta, velocity, _ = y
        return np.array((velocity, -C*velocity - np.sin(theta), C*velocity*velocity))

    for i in range(len(time)-1):
        y = state[i]
        k1 = rhs(y)
        k2 = rhs(y + step*k1/2)
        k3 = rhs(y + step*k2/2)
        k4 = rhs(y + step*k3)
        state[i+1] = y + step*(k1 + 2*k2 + 2*k3 + k4)/6
    return time, state


def linear(angle, time):
    wd = np.sqrt(1 - C*C/4)
    theta = angle*np.exp(-C*time/2)*(np.cos(wd*time) + C/(2*wd)*np.sin(wd*time))
    velocity = -angle*np.exp(-C*time/2)*np.sin(wd*time)/wd
    return theta, velocity


def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": "white",
                         "axes.facecolor": "white", "savefig.facecolor": "white"})
    fig, axs = plt.subplots(2, 2, figsize=(10, 6.8), layout="constrained")
    fig.suptitle("Damped pendulum: small angles, finite angles, and energy loss", fontsize=15)
    results = {}
    for degrees, ax in zip((10, 60), axs[0]):
        angle = np.deg2rad(degrees)
        time, state = solve(angle)
        approx, approx_v = linear(angle, time)
        ax.plot(time, np.rad2deg(state[:, 0]), color="#2563eb", label="Nonlinear: sin θ")
        ax.plot(time, np.rad2deg(approx), color="#d97706", ls="--", label="Linear: θ")
        ax.axhline(0, color="#cbd5e1", lw=0.8)
        ax.set(title=f"Release from rest at {degrees}°", xlabel="Dimensionless time τ", ylabel="Angle (degrees)", xlim=(0, 25))
        ax.legend(fontsize=9, loc="upper right")
        results[degrees] = (time, state, approx, approx_v)
    time, state, approx, approx_v = results[60]
    kinetic = state[:, 1]**2/2
    potential = 2*np.sin(state[:, 0]/2)**2
    energy = kinetic + potential
    energy0 = energy[0]
    loss = state[:, 2]
    ax = axs[1, 0]
    ax.plot(time, energy/energy0, color="#111827", lw=2, label="Remaining E/E₀")
    ax.plot(time, kinetic/energy0, color="#2563eb", lw=1, label="Kinetic / E₀")
    ax.plot(time, potential/energy0, color="#16a34a", lw=1, label="Potential / E₀")
    ax.plot(time, loss/energy0, color="#9333ea", lw=1.5, label="Dissipated Q/E₀")
    ax.set(title="Exact energy balance (60°): E + Q = E₀", xlabel="Dimensionless time τ", ylabel="Fraction of initial nonlinear energy", xlim=(0, 25), ylim=(0, 1.05))
    ax.legend(fontsize=8, loc="upper right")
    ax = axs[1, 1]
    ax.semilogy(time, energy/energy0, color="#2563eb", label="Nonlinear E/E₀ (60°)")
    linear_energy = (approx*approx + approx_v*approx_v)/2
    ax.semilogy(time, linear_energy/linear_energy[0], color="#d97706", ls="--", label="Linear E/E₀ (60°)")
    ax.semilogy(time, np.exp(-C*time), color="#64748b", ls=":", label="Weak-damping average exp(−cτ)")
    ax.set(title="Energy decay is not an exact exponential", xlabel="Dimensionless time τ", ylabel="Remaining fraction (log scale)", xlim=(0, 25))
    ax.legend(fontsize=8, loc="upper right")
    for ax in axs.flat:
        ax.grid(alpha=0.17)
    fig.supxlabel("Chosen model: θ″ + 0.20 θ′ + sin θ = 0. Numerical solutions, not measured data.", fontsize=10)
    output = Path.cwd() / (Path(__file__).stem + ".png")
    fig.savefig(output, dpi=130, facecolor="white", transparent=False)
    plt.close(fig)
    for degrees, (time, state, approx, _) in results.items():
        energy = state[:, 1]**2/2 + 2*np.sin(state[:, 0]/2)**2
        residual = np.max(np.abs(energy + state[:, 2] - energy[0]))
        error = np.max(np.abs(state[:, 0] - approx))
        print(f"{degrees} deg: max angle difference={error:.10g} rad; max |E+Q-E0|={residual:.3g}; E(25)/E0={energy[-1]/energy[0]:.9f}")


if __name__ == "__main__":
    main()
