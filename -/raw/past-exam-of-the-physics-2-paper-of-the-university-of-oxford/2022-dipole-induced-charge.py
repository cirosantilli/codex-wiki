"""Original leading-order grounded-plane dipole calculation; Python 3.14."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

u = np.linspace(0, 5, 1001)
sigma = (u**2 - 2) / (1 + u**2)**2.5
charge = -u**2 / (1 + u**2)**1.5
fig, axes = plt.subplots(1, 2, figsize=(9, 3.7), layout="constrained", facecolor="white")
for ax in axes:
    ax.set_facecolor("white")
    ax.axhline(0, color="0.35", linewidth=0.8)
    ax.axvline(np.sqrt(2), color="0.5", linestyle="--", linewidth=1)
    ax.set_xlim(0, 5)
    ax.set_xlabel(r"Distance along plane $a/h$")
    ax.grid(alpha=0.18)
axes[0].plot(u, sigma, color="#1f5d99", linewidth=2)
axes[0].fill_between(u, sigma, 0, where=sigma < 0, color="#1f5d99", alpha=0.13)
axes[0].fill_between(u, sigma, 0, where=sigma > 0, color="#d17624", alpha=0.5)
axes[0].set_ylabel(r"$\sigma\,/\,[qd/(2\pi h^3)]$")
axes[0].set_title("Local induced surface charge")
axes[0].annotate(r"Sign change at $a/h=\sqrt{2}$", xy=(np.sqrt(2), 0), xytext=(1.65, -0.85), arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=9)
axes[1].plot(u, charge, color="#1f5d99", linewidth=2)
axes[1].set_ylabel(r"$Q(<a)\,/\,(qd/h)$")
axes[1].set_title("Charge inside a disk of radius a")
axes[1].annotate("Outer positive charge restores\nzero total as radius tends to infinity", xy=(4.4, -4.4**2/(1+4.4**2)**1.5), xytext=(1.45, -0.11), arrowprops={"arrowstyle": "->", "color": "0.3"}, fontsize=9)
fig.suptitle(r"Dipole above a grounded plane: $+q$ at $h$, $-q$ at $h+d$, $d\ll h$", fontsize=11)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=110, facecolor="white", transparent=False)
plt.close(fig)
