"""Original absorbing diffusion plots; Python 3.14, numpy, matplotlib."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 801)
odd = 2*np.arange(200)+1
fig, axes = plt.subplots(1, 2, figsize=(10, 3.9), constrained_layout=True,
                         facecolor="white")
for tau, color in [(.02, "#1764a0"), (.08, "#c55412"), (.3, "#197c54")]:
    kernel = np.sum(np.cos(odd[:, None]*np.pi*x[None, :]/2)
                    *np.exp(-odd[:, None]**2*np.pi**2*tau/4), axis=0)
    axes[0].plot(x, kernel, lw=2, color=color,
                 label=rf"$Dt/L^2={tau}$")
axes[0].set(xlabel=r"Position $x/L$", ylabel=r"Transition density $LK(x,t|0,0)$",
            title="Absorbing endpoints: missing mass is exit probability")
axes[0].legend(fontsize=9)
t = np.geomspace(.01, 3, 700)
u = np.pi**2*t/4
survival = 4/np.pi*np.sum(
    ((-1.)**np.arange(200)/odd)[:, None]*np.exp(-odd[:, None]**2*u), axis=0)
asymptote = 4/np.pi*np.exp(-u)
axes[1].semilogy(t, survival, lw=2.1, color="#1764a0", label="Full eigenfunction sum")
axes[1].semilogy(t, asymptote, lw=1.7, ls="--", color="#c55412",
                 label="Late-time first mode")
axes[1].axhline(1, color=".55", ls=":", lw=.8)
axes[1].set(xlabel=r"Time $Dt/L^2$", ylabel="Survival probability",
            title="First-mode approximation is not valid at time zero")
axes[1].legend(fontsize=9)
for ax in axes:
    ax.grid(alpha=.2)
    ax.spines[["top", "right"]].set_visible(False)
fig.savefig("paper-1-killed-diffusion.png", dpi=160, facecolor="white")
plt.close(fig)
