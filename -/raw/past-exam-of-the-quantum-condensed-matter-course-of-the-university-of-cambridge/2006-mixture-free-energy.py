"""Render the symmetric liquid-mixture free energies to the current directory."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0.00001, 0.99999, 3000)
fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.7), layout="constrained")
for ax, chi in zip(axes, [0.0, 2.0, 2.5]):
    f = phi * np.log(phi) + (1 - phi) * np.log1p(-phi) + chi * phi * (1 - phi)
    ax.plot(phi, f, color="#2369a0", lw=2)
    ax.scatter([0, 1], [0, 0], color="#2369a0", s=15)
    if chi > 2:
        lo, hi = 0.00001, 0.3
        for _ in range(70):
            mid = (lo + hi) / 2
            if np.log(mid / (1 - mid)) + chi * (1 - 2 * mid) > 0:
                hi = mid
            else:
                lo = mid
        b = (lo + hi) / 2
        fb = b * np.log(b) + (1 - b) * np.log1p(-b) + chi * b * (1 - b)
        ax.plot([b, 1 - b], [fb, fb], "--", color="#a24b25", label="Common tangent")
        ax.scatter([b, 1 - b], [fb, fb], color="#a24b25", zorder=3, label="Binodal")
        spinodal = (1 - np.sqrt(1 - 2 / chi)) / 2
        ax.axvspan(spinodal, 1 - spinodal, color="#d64f4f", alpha=0.13, label="Negative curvature")
        ax.legend(fontsize=8, loc="upper center")
        ax.set_ylim(-0.14, 0.015)
    ax.set_title(rf"$\chi={chi:g}$")
    ax.set_xlabel(r"Composition $\phi$")
    ax.set_ylabel(r"$f/(k_B T)$ per site")
    ax.set_xlim(0, 1)
    ax.grid(alpha=0.2)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
