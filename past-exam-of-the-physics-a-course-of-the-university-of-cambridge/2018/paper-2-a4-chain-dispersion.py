"""Original solution figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
fig, axes = plt.subplots(1, 3, figsize=(10.3, 3.5), layout="constrained")
u = np.linspace(-1, 1, 700)
w = 2*np.abs(np.sin(np.pi*u/2))
axes[0].plot(u, w, color="#1565a8", lw=2)
axes[0].set_title("One atom per cell: length d")
axes[0].set_xlabel(r"$kd/\pi$")
axes[0].set_ylabel(r"$\omega/\sqrt{K/m}$")
axes[0].text(0, .45, "acoustic", ha="center", color="#1565a8")
for ax, ratio, name in zip(axes[1:], [1., 3.], ["Equal masses: M = m", "Different masses: M = 3m"]):
    kd = u*np.pi/2
    root = np.sqrt(np.maximum(0, (1+1/ratio)**2-4/ratio*np.sin(kd)**2))
    wa = np.sqrt(np.maximum(0, 1+1/ratio-root))
    wo = np.sqrt(1+1/ratio+root)
    ax.plot(u, wa, color="#1565a8", lw=2, label="acoustic")
    ax.plot(u, wo, color="#ca6720", lw=2, label="optical")
    ax.set_title(name+"\nTwo-atom cell: length 2d")
    ax.set_xlabel(r"$2kd/\pi$")
    ax.legend(frameon=False, fontsize=8, loc="center")
for ax in axes:
    for x in [-1, 1]: ax.axvline(x, color="0.45", ls="--", lw=1)
    ax.set_xlim(-1.08, 1.08)
    ax.set_ylim(0, 2.2)
    ax.set_xticks([-1, 0, 1])
    ax.grid(alpha=.15)
fig.suptitle("Nearest-neighbour chains with equal spring constants K; dashed lines: zone edges")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=135)
