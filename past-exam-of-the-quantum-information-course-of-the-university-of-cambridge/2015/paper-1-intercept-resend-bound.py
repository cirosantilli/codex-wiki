"""Original analytic CHSH comparison for two-sided planar intercept-resend."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

delta = np.linspace(0, np.pi, 601)
fig, ax = plt.subplots(figsize=(9, 5.2), dpi=100, facecolor="white")
ax.axhspan(-np.sqrt(2), 0, color="#e8f1fa", label="Attainable attack interval")
ax.plot(delta, -np.sqrt(2)*np.cos(delta)**2, lw=2.8, color="#245d92", label=r"Attack: $S=-\sqrt{2}\cos^2\delta$")
ax.axhline(-2*np.sqrt(2), color="#a73e32", ls="--", lw=2, label=r"Undisturbed singlet: $S=-2\sqrt{2}$")
ax.set(xlabel=r"Relative angle of Eve's measurement axes $\delta=\alpha-\beta$", ylabel="CHSH combination S",
       xlim=(0, np.pi), ylim=(-3.1, 0.2), title="The specified attack loses the singlet correlations")
ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi], ["0", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
ax.grid(alpha=0.22); ax.legend(loc="lower center", bbox_to_anchor=(0.5, 0.18), fontsize=11)
fig.subplots_adjust(left=0.1, right=0.98, bottom=0.15, top=0.89)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, facecolor="white")
