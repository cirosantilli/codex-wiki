"""Original independent-orientation thermodynamics; write PNG to cwd."""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.002, 3.0, 1600)
x = 1 / t
w = np.exp(-x)
capacity = 2 * x**2 * w / (2 + w)**2
entropy = np.log(2 + w) + x * w / (2 + w)
lo, hi = 2.0, 3.0
for _ in range(80):
    z = (lo + hi) / 2
    derivative = 2 / z - (2 * np.exp(z) - 1) / (2 * np.exp(z) + 1)
    if derivative > 0:
        lo = z
    else:
        hi = z
xpeak = (lo + hi) / 2
tpeak = 1 / xpeak
cpeak = 2 * xpeak**2 * np.exp(-xpeak) / (2 + np.exp(-xpeak))**2

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
ax = axes[0]
ax.plot(t, capacity, color="#245c9f", lw=2)
ax.plot([tpeak], [cpeak], "o", color="#245c9f")
ax.annotate(f"peak: {tpeak:.3f}, {cpeak:.3f}",
            (tpeak, cpeak), (0.9, 0.20),
            arrowprops={"arrowstyle": "-", "color": "0.4"}, fontsize=10)
ax.set(xlim=(0, 3), ylim=(0, 0.27), xlabel=r"$k_{\rm B}T/\delta$",
       ylabel=r"$C_V/(Nk_{\rm B})$", title="Finite-level heat-capacity peak")
ax = axes[1]
ax.plot(t, entropy, color="#21633d", lw=2)
ax.axhline(np.log(2), color="0.45", ls="--", lw=1)
ax.axhline(np.log(3), color="0.45", ls="--", lw=1)
ax.text(1.9, np.log(2) + 0.012, r"$\ln 2$: two ground states", fontsize=9, ha="center")
ax.text(1.9, np.log(3) - 0.035, r"$\ln 3$: equal populations", fontsize=9, ha="center")
ax.set(xlim=(0, 3), ylim=(0.65, 1.13), xlabel=r"$k_{\rm B}T/\delta$",
       ylabel=r"$S/(Nk_{\rm B})$", title="Residual entropy and saturation")
for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.18)
fig.savefig("paper-2-orientation-thermodynamics.png", dpi=150, facecolor="white")
plt.close(fig)
