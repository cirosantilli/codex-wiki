"""Matter-background CDM/radiation illustration; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/codex-wiki-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3.0, 1400)  # conformal time divided by wavelength/horizon crossing time
cdm = x**2
rad = 8.0 / (2.0 * np.pi)**2 * (1.0 - np.cos(2.0 * np.pi * x / np.sqrt(3.0)))

fig, axes = plt.subplots(2, 1, figsize=(7.1, 5.2), sharex=True, constrained_layout=True)
fig.patch.set_facecolor("white")
for ax in axes:
    ax.set_facecolor("white")
    ax.axvspan(0, 0.15, color="#e9f2f9", alpha=0.8)
    ax.axvline(1, color="#66717e", linestyle="--", linewidth=1.1)
    ax.grid(alpha=0.18)
    ax.set_xlim(0, 3)
axes[0].plot(x, cdm, color="#225b8e", linewidth=2.2)
axes[0].set_ylabel(r"$\delta_c/\varepsilon$")
axes[0].set_ylim(0, 9.25)
axes[0].text(1.06, 7.8, r"$k\tau_h=2\pi$", color="#4d5763", fontsize=10)
axes[0].text(0.3, 6.1, r"Cold matter: $\delta_c\propto\tau^2$", color="#225b8e", fontsize=11)
axes[0].set_title("Regular growing mode in the matter-background limit", fontsize=12)
axes[1].plot(x, rad, color="#b05d13", linewidth=2.2)
axes[1].set_ylabel(r"$\delta_r/\varepsilon$")
axes[1].set_ylim(-0.015, 0.48)
axes[1].axhline(8/(2*np.pi)**2, color="#b05d13", linestyle=":", alpha=0.65)
axes[1].text(0.3, 0.435, "Radiation: bounded acoustic response", color="#914b0f", fontsize=10)
axes[1].set_xlabel(r"Conformal time $\tau/\tau_h$")
axes[1].text(0.03, 0.025, r"$\delta_r\simeq\frac{4}{3}\delta_c$ at $k\tau\ll1$", fontsize=9, color="#3a4e5e")
fig.savefig(Path.cwd() / "paper-67-matter-era-horizon.png", dpi=155, facecolor="white", transparent=False)
plt.close(fig)
