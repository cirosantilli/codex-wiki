"""Uniform-frailty survival selection; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Write the PNG basename to the caller's working directory. Respect any supplied
MPLCONFIGDIR; no cache location is created or overridden by this generator.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 801)
survival = np.ones_like(t)
hazard = np.ones_like(t)
positive = t > 0
z = t[positive]
survival[positive] = np.exp(-z / 2) * (-np.expm1(-z)) / z
hazard[positive] = 0.5 + 1 / z - 1 / np.expm1(z)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), dpi=100, facecolor="white")
for u, color in [(0.5, "#6699aa"), (1.0, "#999999"), (1.5, "#bb9977")]:
    axes[0].plot(t, np.exp(-u * t), ls="--", lw=1.3, color=color,
                 label=fr"Fixed frailty $U={u:g}$")
axes[0].plot(t, survival, color="#173f70", lw=2.5, label="Population mixture")
axes[0].set(xlabel=r"Time $t$ ($\theta=1$)", ylabel="Probability of survival",
            xlim=(0, 10), ylim=(0, 1.03), title="Population survival averages individual survival")
axes[0].legend(frameon=False, fontsize=8)
axes[1].plot(t, hazard, color="#173f70", lw=2.5, label="Population hazard")
axes[1].axhline(1, color="#777777", lw=1.2, ls=":", label=r"Initial mean hazard $1$")
axes[1].axhline(0.5, color="#6699aa", lw=1.5, ls="--", label=r"Limiting hazard $1/2$")
axes[1].set(xlabel=r"Time $t$ ($\theta=1$)", ylabel="Hazard",
            xlim=(0, 10), ylim=(0.45, 1.07), title="Survivors increasingly have smaller frailty")
axes[1].legend(frameon=False, fontsize=8)
for ax in axes:
    ax.set_facecolor("white")
    ax.grid(alpha=0.18)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.suptitle(r"Uniform frailty $U\sim\mathrm{Unif}[1/2,3/2]$: each individual hazard is constant",
             fontsize=12)
fig.tight_layout(rect=(0, 0, 1, 0.91))
fig.savefig("paper-46-uniform-frailty.png", facecolor="white", transparent=False)
plt.close(fig)
