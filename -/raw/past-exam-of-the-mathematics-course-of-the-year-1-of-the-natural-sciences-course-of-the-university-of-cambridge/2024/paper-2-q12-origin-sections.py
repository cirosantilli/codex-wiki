"""Generate this exam figure in cwd; run from its _media source directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository pyproject.toml.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1, 1, 500)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), layout="constrained")
axes[0].plot(t, t**6, color="#176b9c", linewidth=2.3)
axes[1].plot(t, 2 * t**6 - 24 * t**4, color="#b33b35", linewidth=2.3)
axes[0].set(title=r"Axes: $h(t,0)=h(0,t)=t^6$", ylabel=r"$h$")
axes[1].set(title=r"Diagonals: $h(t,\pm t)=2t^6-24t^4$", ylabel=r"$h$")
for ax in axes:
    ax.axhline(0, color="0.6", linewidth=0.8)
    ax.axvline(0, color="0.6", linewidth=0.8)
    ax.scatter([0], [0], color="black", s=20, zorder=4)
    ax.set(xlabel=r"$t$", xlim=(-1, 1))
    ax.grid(alpha=0.2)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
