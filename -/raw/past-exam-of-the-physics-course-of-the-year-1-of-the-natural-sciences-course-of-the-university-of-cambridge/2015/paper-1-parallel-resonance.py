"""Original ideal parallel-RLC plots; Python 3.14, numpy, matplotlib.

Dimensionless Q=3 is illustrative, not an additional exam parameter.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


Q = 3.0
x = np.geomspace(0.1, 10, 1200)
b = Q*(x-1/x)
amplitude = np.sqrt(1+b*b)
lo = (np.sqrt(4+1/Q**2)-1/Q)/2
hi = (np.sqrt(4+1/Q**2)+1/Q)/2
fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), constrained_layout=True,
                         facecolor="white")
axes[0].loglog(x, amplitude, lw=2, color="#1764a0")
axes[0].scatter([1], [1], color="#c55412", zorder=3)
axes[0].set(ylabel=r"$|I_{\rm total}|/(V_0/R)$", title="Source current has a minimum")
axes[1].semilogx(x, np.degrees(np.arctan(b)), lw=2, color="#1764a0")
axes[1].axhline(0, color="0.5", lw=0.8)
axes[1].set(ylabel="Current phase relative to voltage (degrees)",
            title="Inductive to capacitive", yticks=[-90, -45, 0, 45, 90])
axes[2].semilogx(x, 1/amplitude, lw=2, color="#1764a0")
axes[2].axhline(1/np.sqrt(2), color="#c55412", ls="--", lw=1)
axes[2].axvspan(lo, hi, color="#197c54", alpha=0.14,
                label=r"Bandwidth: $\Delta\omega/\omega_0=1/Q$")
axes[2].set(ylabel=r"$|I_R|/|I_{\rm total}|$", title="Defined current-ratio band", ylim=(0, 1.08))
axes[2].legend(fontsize=8, loc="lower center")
for ax in axes:
    ax.set_xlabel(r"Frequency ratio $\omega/\omega_0$")
    ax.axvline(1, color="0.5", lw=0.8, ls=":")
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle(r"Ideal three-branch parallel RLC circuit; illustrative $Q=3$", fontsize=12)
fig.savefig("paper-1-parallel-resonance.png", dpi=160, facecolor="white")
plt.close(fig)
