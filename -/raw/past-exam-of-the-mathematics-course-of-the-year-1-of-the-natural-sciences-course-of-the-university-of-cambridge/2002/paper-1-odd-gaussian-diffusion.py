"""Original time profiles of an odd Gaussian pair under heat diffusion."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-9, 9, 1600)
fig, ax = plt.subplots(figsize=(7.2, 4.4), layout="constrained")
for t, color in zip([0, .5, 2, 6], ["#245f96", "#b76628", "#618537", "#985990"]):
    s = 1+4*t
    u = (np.exp(-(x-2)**2/s)-np.exp(-(x+2)**2/s))/np.sqrt(s)
    ax.plot(x, u, color=color, lw=2, label=f"t = {t:g}")
ax.axhline(0, color="#666666", lw=.8)
ax.axvline(0, color="#666666", lw=.8)
ax.set(xlim=(-9, 9), ylim=(-1.08, 1.08), xlabel="x", ylabel=r"$\theta(x,t)$",
       title="Opposite Gaussian lobes broaden and flatten")
ax.grid(alpha=.15)
ax.legend(frameon=False, loc="upper left")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
