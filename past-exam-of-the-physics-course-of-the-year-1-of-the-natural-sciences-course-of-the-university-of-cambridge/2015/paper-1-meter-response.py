"""Original normalized meter response plots; Python 3.14, numpy, matplotlib."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), constrained_layout=True,
                         facecolor="white")
t = np.linspace(0, 14, 700)
for zeta, label, color in [(0.3, "Underdamped (0.3)", "#c55412"),
                           (1, "Critical (1)", "#1764a0"),
                           (2, "Overdamped (2)", "#197c54")]:
    if zeta < 1:
        wd = np.sqrt(1-zeta*zeta)
        y = 1-np.exp(-zeta*t)*(np.cos(wd*t)+zeta/wd*np.sin(wd*t))
    elif zeta == 1:
        y = 1-(1+t)*np.exp(-t)
    else:
        r1, r2 = -zeta+np.sqrt(zeta*zeta-1), -zeta-np.sqrt(zeta*zeta-1)
        y = 1+(r2*np.exp(r1*t)-r1*np.exp(r2*t))/(r1-r2)
    axes[0].plot(t, y, color=color, label=label, lw=2)
axes[0].axhline(1, color="0.55", ls="--", lw=0.8)
axes[0].set(xlabel=r"Normalized time $\omega_0t$",
            ylabel=r"Deflection $\theta/\theta_\infty$", title="Step from rest")
axes[0].legend(title=r"Illustrative $\gamma/\omega_0$", fontsize=8, title_fontsize=9)
x = np.geomspace(0.01, 100, 600)
axes[1].loglog(x, 1/(1+x*x), color="#1764a0", lw=2)
axes[1].set(xlabel=r"Frequency ratio $\omega/\omega_0$",
            ylabel=r"Amplitude / DC amplitude", title="Critical amplitude response")
axes[2].semilogx(x, -2*np.degrees(np.arctan(x)), color="#1764a0", lw=2)
axes[2].set(xlabel=r"Frequency ratio $\omega/\omega_0$",
            ylabel="Phase relative to drive (degrees)", title="Critical phase response",
            yticks=[0, -45, -90, -135, -180])
for ax in axes:
    ax.grid(alpha=0.22)
    ax.spines[["top", "right"]].set_visible(False)
fig.savefig("paper-1-meter-response.png", dpi=160, facecolor="white")
plt.close(fig)
