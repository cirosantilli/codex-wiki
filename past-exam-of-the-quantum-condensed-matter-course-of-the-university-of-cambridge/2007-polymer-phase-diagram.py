"""Original Flory-Huggins phase diagram; coexistence from a common tangent.

The inner bisections find the two stable stationary concentrations for a
trial chemical potential. The outer one equates their grand potentials.
Only NumPy and Matplotlib are required; output goes to the current directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

N = 1000
critical_phi = 1 / (1 + np.sqrt(N))
critical_chi = 0.5 * (1 + 1 / np.sqrt(N))**2


def free_energy(phi, chi):
    return phi / N * np.log(phi) + (1 - phi) * np.log1p(-phi) + chi * phi * (1 - phi)


def chemical_potential(phi, chi):
    return (np.log(phi) + 1) / N - np.log1p(-phi) - 1 + chi * (1 - 2 * phi)


def bisect(function, lower, upper, iterations=65):
    left_value = function(lower)
    right_value = function(upper)
    assert left_value * right_value <= 0, (lower, upper, left_value, right_value)
    for _ in range(iterations):
        middle = (lower + upper) / 2
        value = function(middle)
        if value * left_value > 0:
            lower, left_value = middle, value
        else:
            upper = middle
    return (lower + upper) / 2


def coexistence(chi):
    roots = np.sort(np.roots([2 * chi * N, N - 1 - 2 * chi * N, 1]))
    spin_low, spin_high = roots

    def phases(mu):
        low = np.exp(bisect(lambda u: chemical_potential(np.exp(u), chi) - mu,
                            -700, np.log(spin_low)))
        high = bisect(lambda p: chemical_potential(p, chi) - mu,
                      spin_high, 1 - 1e-12)
        return low, high

    def difference(mu):
        low, high = phases(mu)
        return free_energy(high, chi) - mu * high - free_energy(low, chi) + mu * low

    # Stay just inside the metastability limits to avoid roundoff at double roots.
    minimum = chemical_potential(spin_high, chi)
    maximum = chemical_potential(spin_low, chi)
    pad = (maximum - minimum) * 1e-9
    mu = bisect(difference, minimum + pad, maximum - pad)
    low, high = phases(mu)
    assert low < spin_low < spin_high < high
    assert abs(chemical_potential(low, chi) - chemical_potential(high, chi)) < 1e-10
    assert abs(difference(mu)) < 1e-10
    return low, high, spin_low, spin_high


chis = np.linspace(critical_chi + 0.00015, 0.61, 180)
branches = np.array([coexistence(chi) for chi in chis])
fig, ax = plt.subplots(figsize=(8.5, 5.2), layout="constrained")
ax.fill_betweenx(chis, branches[:, 0], branches[:, 1], color="#e6edf8",
                 label="two-phase equilibrium")
ax.fill_betweenx(chis, branches[:, 2], branches[:, 3], color="#f8d2c5",
                 label="unstable homogeneous state")
for column in [0, 1]:
    ax.plot(np.r_[critical_phi, branches[:, column]], np.r_[critical_chi, chis],
            color="#245b9f", lw=2, label="binodal" if column == 0 else None)
for column in [2, 3]:
    ax.plot(np.r_[critical_phi, branches[:, column]], np.r_[critical_chi, chis],
            color="#b55032", lw=1.6, ls="--", label="spinodal" if column == 2 else None)
ax.axhline(0.5, color="#447747", lw=1.3, ls=":", label=r"theta condition $\chi=1/2$")
ax.plot(critical_phi, critical_chi, "o", color="black", ms=5)
ax.annotate("critical point", (critical_phi, critical_chi), xytext=(0.002, 0.518),
            arrowprops={"arrowstyle": "->", "lw": 0.8}, fontsize=10)
ax.text(1.6e-10, 0.492, "good solvent", color="#447747", fontsize=10)
ax.text(1.6e-10, 0.505, "poorer solvent above the theta line", fontsize=10)
ax.text(0.012, 0.584, "unstable", color="#873e29", fontsize=10)
ax.text(5e-7, 0.574, "metastable", color="#245b9f", fontsize=10)
ax.set(xscale="log", xlim=(1e-10, 1), ylim=(0.48, 0.612),
       xlabel=r"Polymer volume fraction $\phi$ (log scale)",
       ylabel=r"Interaction parameter $\chi$ (larger = poorer solvent)",
       title=r"Flory-Huggins polymer solution, $N=1000$")
ax.legend(loc="upper left", fontsize=9, framealpha=0.96)
ax.grid(alpha=0.12)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
