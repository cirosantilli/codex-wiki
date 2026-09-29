"""Illustrative regularized colloidal potentials and their force, not data."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

h = np.geomspace(0.21, 80, 2400)  # nm
C, h0, B = 20.0, 0.3, 40.0
neutral = C * (h0**8 / (9 * h**9) - 1 / h)
neutral_force = C * (h0**8 / h**10 - 1 / h**2)
fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.2), layout="constrained")
axes[0].plot(h, neutral, color="#555555", lw=2, label="Uncharged")
axes[0].set_title("Neutral pair energy")
axes[0].set_ylim(-80, 40)
axes[0].set_ylabel(r"$U/(k_B T)$")
axes[0].annotate("Primary minimum", (0.3, -59.3), (0.7, -58), arrowprops={"arrowstyle": "->"}, fontsize=9)
axes[1].plot(h, neutral, "--", color="#777777", label="Uncharged")
axes[2].plot(h, neutral_force, "--", color="#777777", label="Uncharged")
for length, color in [(5.0, "#246faa"), (1.0, "#c04d26")]:
    energy = neutral + B * np.exp(-h / length)
    force = neutral_force + B / length * np.exp(-h / length)
    label = rf"$\lambda_D={length:g}$ nm"
    axes[1].plot(h, energy, color=color, lw=2, label=label)
    axes[2].plot(h, force, color=color, lw=2, label=label)
axes[1].set_title("Charge and salt change the barrier")
axes[1].set_ylim(-55, 35)
axes[1].set_ylabel(r"$U/(k_B T)$")
axes[1].annotate("Repulsive barrier", (3, 15), (0.6, 27), arrowprops={"arrowstyle": "->"}, fontsize=9)
axes[2].set_title("Force is minus the energy gradient")
axes[2].set_yscale("symlog", linthresh=0.1)
axes[2].set_ylim(-100, 100)
axes[2].set_ylabel(r"$F/(k_B T\,/\,\mathrm{nm})$")
axes[2].text(0.97, 0.94, "Repulsion (+)", transform=axes[2].transAxes, ha="right", fontsize=9)
axes[2].text(0.97, 0.06, "Attraction (−)", transform=axes[2].transAxes, ha="right", fontsize=9)
for ax in axes:
    ax.set_xscale("log")
    ax.set_xlim(h[0], h[-1])
    ax.set_xlabel("Surface gap h (nm)")
    ax.axhline(0, color="black", lw=0.7, alpha=0.6)
    ax.grid(alpha=0.18)
axes[1].legend(fontsize=8, loc="lower right")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
