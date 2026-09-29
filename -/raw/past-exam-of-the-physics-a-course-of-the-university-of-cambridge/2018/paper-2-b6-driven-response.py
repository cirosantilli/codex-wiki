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
fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), layout="constrained")
r = np.linspace(0, 3, 1700)
for Q, col in [(8, "#1565a8"), (1, "#ca6720"), (.25, "#33865b")]:
    R = 1/(1-r*r+1j*r/Q)
    axes[0].plot(r, abs(R), lw=1.8, label=f"Q = {Q:g}", color=col)
    axes[1].plot(r, np.angle(R)/np.pi, lw=1.8, color=col)
for ax in axes:
    ax.axvline(1, ls="--", lw=1, color="0.5")
    ax.set_xlabel(r"Drive frequency $\omega/\omega_0$")
    ax.set_xlim(0, 3)
    ax.grid(alpha=.18)
axes[0].set_ylabel(r"Normalized amplitude $k|R|$")
axes[0].set_ylim(0, 8.5)
axes[0].legend(frameon=False)
axes[0].annotate("static value = 1", xy=(0, 1), xytext=(.4, 3.2), arrowprops={"arrowstyle":"->", "color":"0.4"})
axes[0].set_title("Large Q: tall, narrow peak; small Q: no peak")
axes[1].set_ylabel(r"Phase relative to force, $\phi/\pi$")
axes[1].set_yticks([0, -.5, -1], ["0", "−1/2", "−1"])
axes[1].set_ylim(-1.05, .05)
axes[1].set_title(r"All curves pass through $-\pi/2$ at $\omega_0$")
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=135)
