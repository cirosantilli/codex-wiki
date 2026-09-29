"""Original, dimensionless examples satisfying energy and momentum transfer."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

k = np.linspace(-1.25, 1.25, 700)
fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.1), layout="constrained")
ax = axes[0]
ax.plot(k, k*k, color="tab:blue", lw=1.8, label="conduction band")
ax.plot(k, -1-0.4*k*k, color="tab:green", lw=1.8, label="valence band")
initial = (0.25, -1-0.4*0.25**2)
final = (0.25, 0.25**2)
ax.annotate("", final, initial, arrowprops={"arrowstyle": "->", "color": "tab:red", "lw": 2})
ax.scatter(*initial, color="black", s=24, zorder=5)
ax.scatter(*final, facecolor="white", edgecolor="black", s=30, zorder=5)
ax.text(0.36, -0.55, r"$\hbar\omega$", color="tab:red", fontsize=12)
ax.text(0.04, 0.05, r"$q\simeq0$: nearly vertical", transform=ax.transAxes, fontsize=10)
ax.set(title="Photon absorption", ylim=(-1.9, 1.75))
ax.legend(fontsize=8, loc="upper left")
for ax, kf, title, text in [(axes[1], -0.9, "Acoustic-phonon emission", r"$\Delta E=\hbar v_s q$"),
                            (axes[2], 0.6, "Optical-phonon emission", r"$\Delta E=\hbar\omega_0$")]:
    ki = 1.0
    ax.plot(k, k*k, color="tab:blue", lw=1.8)
    ax.scatter([ki], [ki*ki], color="black", s=24, zorder=5)
    ax.scatter([kf], [kf*kf], facecolor="white", edgecolor="black", s=30, zorder=5)
    ax.annotate("", (kf, kf*kf), (ki, ki*ki),
                arrowprops={"arrowstyle": "->", "color": "tab:red", "lw": 2})
    ax.text(0.05, 0.20, text, transform=ax.transAxes, fontsize=11, color="tab:red")
    ax.text(0.05, 0.08, r"$q=|k_i-k_f|$", transform=ax.transAxes, fontsize=10)
    ax.set(title=title, ylim=(-0.35, 1.75))
# For E=k^2, the acoustic example has q=1.9, Delta E=0.19:
# choosing hbar*v_s=0.1 satisfies the linear phonon dispersion exactly.
# The optical example has q=0.4 and hbar*omega_0=0.64.
for ax in axes:
    ax.axhline(0, color="0.6", lw=0.7)
    ax.axvline(0, color="0.6", lw=0.7)
    ax.set(xlim=(-1.25, 1.25), xlabel="Wavevector (schematic units)",
           ylabel="Electron energy (schematic units)")
    ax.grid(alpha=0.14)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
