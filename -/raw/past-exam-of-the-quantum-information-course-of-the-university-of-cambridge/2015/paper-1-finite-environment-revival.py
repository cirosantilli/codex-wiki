"""Original one-qubit environment calculation: dephasing is reversible."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi, 601); z = np.cos(2*x)
fig, ax = plt.subplots(figsize=(9, 5.2), dpi=100, facecolor="white")
ax.plot(x, z, lw=2.5, label=r"Coherence factor $z=\cos(2gt/\hbar)$")
ax.plot(x, (1+z*z)/2, lw=2.5, label=r"Reduced purity $(1+z^2)/2$")
ax.axvline(np.pi/4, color="0.4", ls=":")
ax.set(xlabel=r"Dimensionless time $gt/\hbar$", ylabel="Coherence factor / reduced-state purity", xlim=(0, np.pi), ylim=(-1.1, 1.12),
       title="A finite environment permits coherence revivals")
ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], ["0", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
ax.grid(alpha=0.22); ax.legend(loc="center", bbox_to_anchor=(0.5, 0.54), fontsize=10.5)
fig.text(0.5, 0.025, r"First orthogonal records at $gt/\hbar=\pi/4$; global evolution remains unitary.", ha="center", fontsize=10.5)
fig.subplots_adjust(left=0.1, right=0.98, bottom=0.19, top=0.89)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, facecolor="white")
