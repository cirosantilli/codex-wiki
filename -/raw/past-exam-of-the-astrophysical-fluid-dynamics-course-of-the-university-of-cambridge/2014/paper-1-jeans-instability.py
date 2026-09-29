"""Original static Jeans dispersion and collapse scalings; output PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

k = np.linspace(0, 2, 500)
contrast = np.geomspace(1, 100, 500)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), dpi=100, facecolor="white")
ax = axes[0]
ax.plot(k, k * k - 1, lw=2.5)
ax.axhline(0, color="0.4", lw=1)
ax.axvline(1, color="0.5", ls=":", lw=1)
ax.axvspan(0, 1, alpha=0.10, color="tab:red")
ax.text(0.49, 2.45, "Growing + decaying", ha="center", fontsize=10.5)
ax.text(1.48, 2.45, "Oscillatory", ha="center", fontsize=10.5)
ax.set(xlabel=r"Wavenumber $k/k_J$", ylabel=r"$\omega^2/(4\pi G\rho_0)$",
       xlim=(0, 2), ylim=(-1.2, 3.1), title="Static uniform-medium dispersion")
ax.grid(alpha=0.2)
ax = axes[1]
ax.loglog(contrast, np.sqrt(contrast), lw=2.5, label=r"Isothermal: $N_J/N_{J,0}=(\rho/\rho_0)^{1/2}$")
ax.loglog(contrast, np.ones_like(contrast), lw=2.5, label=r"Frozen isotropic field: $N_B/N_{B,0}=1$")
ax.set(xlabel=r"Density increase $\rho/\rho_0$", ylabel="Number of support masses / initial value",
       xlim=(1, 100), ylim=(0.75, 13), title="Fixed material mass during contraction")
ax.grid(alpha=0.2, which="both")
ax.legend(loc="upper left", fontsize=9)
fig.text(0.5, 0.025, "Magnetic curve assumes isotropic flux freezing; actual field support is anisotropic.",
         ha="center", fontsize=10.5)
fig.subplots_adjust(left=0.075, right=0.985, top=0.89, bottom=0.19, wspace=0.28)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white")
