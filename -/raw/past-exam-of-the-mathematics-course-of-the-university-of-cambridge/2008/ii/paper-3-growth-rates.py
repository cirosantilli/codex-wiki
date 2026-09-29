"""Plot the fast-inhibitor dispersion curve; write PNG to the caller's cwd."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

D = 0.02
rho = 0.2
threshold = (np.sqrt(rho) - np.sqrt(D)) ** 2
k = np.linspace(-4, 4, 1201)
fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), layout="constrained")
for r, label, color in [(0.06, "Unstable: r = 0.06", "#b54826"),
                        (threshold, f"Threshold: r = {threshold:.4f}", "#455e99"),
                        (0.12, "Stable: r = 0.12", "#27805e")]:
    growth = -r - D * k**2 + rho * k**2 / (1 + k**2)
    axes[0].plot(k, growth, color=color, label=label, lw=2)
axes[0].axhline(0, color="black", lw=0.8)
axes[0].axvline(0, color="black", lw=0.6, alpha=0.4)
axes[0].set(xlabel=r"Wavenumber $k$", ylabel=r"Growth rate $\sigma(k)$",
            title=r"Even growth curves ($D=0.02$, $\rho=0.2$)")
axes[0].legend(fontsize=8, loc="lower center")
rr = np.linspace(0, 0.95, 501)
boundary = (np.sqrt(rr) + np.sqrt(D))**2
axes[1].fill_between(rr, 0, np.minimum(boundary, 1), color="#d4e7df")
axes[1].fill_between(rr, np.minimum(boundary, 1), 1, color="#f3dacd")
axes[1].plot(rr, boundary, color="#455e99", lw=2)
axes[1].text(0.12, 0.72, "Unstable", color="#9e3e22")
axes[1].text(0.58, 0.24, "Stable", color="#236446")
axes[1].set(xlim=(0, 1), ylim=(0, 1), xlabel=r"Reaction parameter $r$",
            ylabel=r"Coupling $\rho$", title=r"Zero-state stability: $\rho=(\sqrt{r}+\sqrt{D})^2$")
for ax in axes:
    ax.grid(alpha=0.2)
fig.savefig(Path.cwd() / "paper-3-growth-rates.png", dpi=110, facecolor="white")
plt.close(fig)
