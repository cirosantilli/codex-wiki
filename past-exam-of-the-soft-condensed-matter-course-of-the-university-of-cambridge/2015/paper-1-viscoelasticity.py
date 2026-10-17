"""Original Maxwell response and work cycle; Python 3.14, numpy, matplotlib."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


x = np.geomspace(0.01, 100, 700)
gp = x*x/(1+x*x)
gpp = x/(1+x*x)
fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8), constrained_layout=True,
                         facecolor="white")
axes[0].loglog(x, gp, color="#1764a0", lw=2.3, label=r"Storage $G'/G$")
axes[0].loglog(x, gpp, color="#c55412", lw=2.3, label=r"Loss $G''/G$")
axes[0].axvline(1, color="0.5", ls=":", lw=0.9)
axes[0].set(xlabel=r"Frequency $\omega\tau$", ylabel="Normalized modulus",
            title="Single-time Maxwell fluid")
axes[0].legend()
t = np.linspace(0, 2*np.pi, 600)
strain = np.cos(t)
stress = 0.5*(np.cos(t)-np.sin(t))
axes[1].fill(strain, stress, color="#1764a0", alpha=0.13)
axes[1].plot(strain, stress, color="#1764a0", lw=2)
for ti in [0.4, 2.1, 3.6, 5.2]:
    lo, hi = ti, ti+0.12
    axes[1].annotate("", xy=(np.cos(hi), .5*(np.cos(hi)-np.sin(hi))),
                     xytext=(np.cos(lo), .5*(np.cos(lo)-np.sin(lo))),
                     arrowprops={"arrowstyle": "->", "color": "#c55412", "lw": 1.8})
axes[1].set(xlabel=r"Strain $\gamma/\gamma_0$",
            ylabel=r"Stress $\sigma/(G\gamma_0)$",
            title=r"Cycle at $\omega\tau=1$")
axes[1].text(0, 0, r"Area $=\pi/2$", ha="center", fontsize=12)
axes[1].axhline(0, lw=0.6, color="0.7")
axes[1].axvline(0, lw=0.6, color="0.7")
for ax in axes:
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
fig.savefig("paper-1-viscoelasticity.png", dpi=160, facecolor="white")
plt.close(fig)
