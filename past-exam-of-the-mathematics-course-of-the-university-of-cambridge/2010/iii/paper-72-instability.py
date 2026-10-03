"""Kinetic freezing dispersion. Python 3.14; NumPy/Matplotlib.
Write paper-72-instability.png to caller CWD.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
S = 0.2
V = 1 - S
alpha = np.linspace(0, 4, 801)
def sigma(gamma):
    result = []
    for a in alpha:
        if a == 0:
            result.append(0.0)
            continue
        def poly(p):
            return p**3 + (S-V)*p**2 + ((gamma-1)*a*a-2*S*V)*p - S*a*a + S*V*V
        lo, hi = V/2, V + a + 2
        for _ in range(80):
            mid = (lo+hi)/2
            if poly(mid) > 0:
                hi = mid
            else:
                lo = mid
        p = (lo+hi)/2
        sg = p*p-V*p-a*a
        residual = sg*(1+S/p)-S*V+gamma*a*a+S*V*V/p
        assert abs(residual) < 1e-10
        result.append(sg)
    return np.array(result)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), facecolor="white")
for gamma in [0, 0.08, 0.25, 0.45]:
    values = sigma(gamma)
    for ax in axes:
        ax.plot(alpha, values, lw=2, label=rf"$\Gamma={gamma:g}$")
for ax in axes:
    ax.set_facecolor("white")
    ax.axhline(0, color="#777777", lw=0.8)
    ax.set_xlabel(r"Wavenumber $\alpha$")
    ax.set_ylabel(r"Growth rate $\sigma$")
    ax.grid(alpha=0.18)
axes[0].set_xlim(0, 1.3)
axes[0].set_ylim(-0.13, 0.12)
axes[0].set_title("Long-wave onset")
axes[0].legend(frameon=False, fontsize=9)
axes[1].set_xlim(0, 4)
axes[1].set_ylim(-5, 0.3)
axes[1].set_title("Short-wave capillary stabilization")
fig.suptitle(r"One-sided kinetic freezing: $S=0.2$, $V=0.8$, $\Gamma_c=0.25$")
fig.tight_layout()
fig.savefig("paper-72-instability.png", dpi=150, facecolor="white", transparent=False)
plt.close(fig)
