"""Original Argand diagram for conjugation, inversion and negation."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

phi = np.pi/6
z = 2*np.exp(1j*phi)
fig, ax = plt.subplots(figsize=(6, 5.2), layout="constrained")
angle = np.linspace(0, 2*np.pi, 500)
for r in [.5, 2]:
    ax.plot(r*np.cos(angle), r*np.sin(angle), color="#aaaaaa", lw=.8, ls="--")
for value, label, offset, color in [(z, r"$z$", (7, 5), "#245f96"),
                                  (z.conjugate(), r"$z^*$", (7, -14), "#b76628"),
                                  (1/z, r"$z^{-1}$", (7, -14), "#985990"),
                                  (-z, r"$-z$", (-24, -14), "#618537")]:
    ax.plot([0, value.real], [0, value.imag], color=color, lw=1.3)
    ax.scatter([value.real], [value.imag], color=color, s=35, zorder=4)
    ax.annotate(label, (value.real, value.imag), xytext=offset,
                textcoords="offset points", fontsize=12, color=color)
arc = np.linspace(0, phi, 60)
ax.plot(.85*np.cos(arc), .85*np.sin(arc), color="#245f96", lw=1)
ax.text(.92, .17, r"$\phi$", color="#245f96", fontsize=12)
ax.axhline(0, color="#666666", lw=.8)
ax.axvline(0, color="#666666", lw=.8)
ax.set(xlim=(-2.35, 2.35), ylim=(-2.25, 2.25), xlabel="Real part", ylabel="Imaginary part",
       title=r"Illustration with $\phi=\pi/6$ and $|z|=2$", aspect="equal")
ax.grid(alpha=.13)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
plt.close(fig)
