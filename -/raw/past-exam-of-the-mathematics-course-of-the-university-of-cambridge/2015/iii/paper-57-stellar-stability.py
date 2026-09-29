"""Uniform-density gas-star stability. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

gamma = np.linspace(0.65, 2.2, 500)
h = 7 * gamma - 4  # n=2, l=2
xp = (h + np.sqrt(h*h + 24)) / 2
xm = -6 / xp
fig, ax = plt.subplots(1, 2, figsize=(10.4, 4.4), dpi=100, facecolor="white")
ax[0].plot(gamma, 3*gamma-4, color="#333333", label=r"Radial: $l=0,\ n=2$")
ax[0].plot(gamma, xp, color="#2166ac", label=r"Nonradial: $l=2,\ n=2$, oscillatory")
ax[0].plot(gamma, xm, color="#b2182b", label=r"Nonradial: $l=2,\ n=2$, unstable")
ax[0].axhline(0, color="0.6", linewidth=.8)
ax[0].axvline(4/3, color="0.5", linestyle=":", linewidth=1)
ax[0].set(xlabel=r"Adiabatic exponent $\gamma$", ylabel=r"$\omega^2/\omega_d^2$", title="Compression stability does not prevent convection")
ax[0].legend(fontsize=8, loc="upper left")
ax[0].grid(alpha=.15)
r = np.linspace(0, .95, 400)
for g, color in [(4/3, "#b2182b"), (5/3, "#2166ac")]:
    ax[1].plot(r, -2*r*r/(g*(1-r*r)), color=color, label=r"$\gamma=$"+str(round(g, 3)))
ax[1].axhline(0, color="0.6", linewidth=.8)
ax[1].set(xlabel=r"Radius $r/R$", ylabel=r"$N^2/\omega_d^2$", title="The interior is buoyantly unstable")
ax[1].legend(fontsize=9)
ax[1].grid(alpha=.15)
fig.tight_layout(pad=1.5)
fig.savefig(Path.cwd() / "paper-57-stellar-stability.png", dpi=100, facecolor="white", transparent=False)
plt.close(fig)
