"""Gaussian mixtures with inverse-square integer weights; no moments assumed."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def density(z, sigma):
    # The omitted probability is below 0.00051; omitted components are far
    # outside the plotted ranges relative to either Gaussian width.
    out = np.zeros_like(z)
    for n in range(1, 1201):
        out += (np.exp(-0.5 * ((z - n) / sigma) ** 2)
                + np.exp(-0.5 * ((z + n) / sigma) ** 2)) / n**2
    return 3 * out / (np.pi**2 * np.sqrt(2 * np.pi) * sigma)

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), layout="constrained")
for ax, sigma, limit in zip(axes, [0.12, 6.0], [5.5, 25]):
    z = np.linspace(-limit, limit, 3001)
    ax.plot(z, density(z, sigma), color="tab:blue", lw=1.8,
            label="smoothed integer distribution")
    ax.set(xlabel="$z$", ylabel="$g(z)$", ylim=(0, None),
           title=rf"$\sigma={sigma:g}$")
    ax.grid(alpha=0.18)
    if sigma > 1:
        ax.plot(z, np.exp(-z*z/(2*sigma*sigma))/(np.sqrt(2*np.pi)*sigma),
                color="tab:orange", ls="--", label="Gaussian core approximation")
        ax.set_ylim(0, 0.071)
        ax.legend(fontsize=8)
    else:
        ax.set_xticks(np.arange(-5, 6))
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
