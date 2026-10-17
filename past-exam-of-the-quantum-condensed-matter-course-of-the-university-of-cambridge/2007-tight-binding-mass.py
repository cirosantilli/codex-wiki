"""Original effective-mass curve for overlap-weighted exponential hopping."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

s = np.linspace(0.18, 8, 900)
mass = np.exp(s) / (s**2 * (1 + s))
minimum = 1 + np.sqrt(3)
minimum_mass = np.exp(minimum) / (minimum**2 * (1 + minimum))
fig, ax = plt.subplots(figsize=(7.9, 4.7), layout="constrained")
ax.semilogy(s, mass, color="#245b9f", lw=2.3)
ax.plot(minimum, minimum_mass, "o", color="#a34828", ms=6)
ax.annotate(r"minimum at $a/a_1=1+\sqrt{3}$", xy=(minimum, minimum_mass),
            xytext=(3.4, 2.1), arrowprops={"arrowstyle": "->", "lw": 1}, fontsize=11)
ax.set(xlim=(0, 8), ylim=(0.4, 45), xlabel=r"Atomic spacing $a/a_1$",
       ylabel=r"$m^*\,/\,[\hbar^2/(4E_1a_1^2)]$",
       title="Band curvature from overlap-weighted exponential hopping")
ax.text(0.28, 29, "Small-spacing continuation\nexceeds the localized-orbital regime.",
        fontsize=9, va="top")
ax.grid(which="both", alpha=0.15)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
