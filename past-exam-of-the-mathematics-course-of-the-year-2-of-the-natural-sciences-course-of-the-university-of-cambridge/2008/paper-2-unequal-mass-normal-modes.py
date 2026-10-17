"""Original mode-shape plot for a three-mass chain; first amplitude set to one."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

modes = [(np.array([1, np.sqrt(6), 3]), r"$1-\sqrt{2/3}$", "tab:blue"),
         (np.array([1, 0, -1]), "$1$", "tab:orange"),
         (np.array([1, -np.sqrt(6), 3]), r"$1+\sqrt{2/3}$", "tab:green")]
fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), layout="constrained", sharey=True)
for ax, (mode, value, color) in zip(axes, modes):
    ax.axhline(0, color="0.5", lw=0.8)
    ax.plot([0, 1, 2], mode, "o-", color=color, lw=2, markersize=7)
    ax.set(xticks=[0, 1, 2], xticklabels=["X (3m)", "Y (2m)", "Z (m)"],
           ylim=(-3.5, 3.6), xlim=(-0.2, 2.2),
           title=r"$\omega^2/(k/m)=$"+value)
    ax.grid(alpha=0.18)
axes[0].set_ylabel("Relative displacement, X amplitude = 1")
axes[0].text(0.5, -2.6, "all in phase", color="tab:blue", fontsize=11)
axes[1].text(0.25, 2.6, "middle mass stationary", color="tab:orange", fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
