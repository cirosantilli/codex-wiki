"""Original cylindrical field profiles; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

inner = np.linspace(0, 1, 400)
outer = np.linspace(1, 3, 500)
fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), layout="constrained", facecolor="white")
color = "#1565a8"
axes[0].plot(inner, inner, color=color, lw=2)
axes[0].plot(outer, 1 / outer, color=color, lw=2)
axes[0].set(title="Long solenoid", ylabel=r"$A_\phi/(B_0R/2)$")
axes[1].plot(inner, np.zeros_like(inner), color=color, lw=2)
axes[1].plot(outer, 1 / outer, color=color, lw=2)
axes[1].plot([1, 1], [0, 1], ":", color=color, lw=1)
axes[1].scatter([1, 1], [0, 1], facecolor="white", edgecolor=color, s=25, zorder=4)
axes[1].set(title="Rotating surface charge", ylabel=r"$E_r/(\sigma/\epsilon)$")
axes[2].plot(inner, 1 - inner**2, color=color, lw=2)
axes[2].plot(outer, np.zeros_like(outer), color=color, lw=2)
axes[2].set(title="Rotating volume charge", ylabel=r"$B_z/(\mu\rho\omega R^2/2)$")
for ax in axes:
    ax.axvline(1, ls="--", color="0.6", lw=0.9)
    ax.set(xlim=(0, 3), ylim=(-0.06, 1.13), xlabel=r"Radius $r/R$")
    ax.grid(alpha=0.15)
fig.savefig("2017-q4-cylindrical-fields.png", dpi=160, facecolor="white")
plt.close(fig)
