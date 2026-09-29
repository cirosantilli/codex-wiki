"""Generate this exam figure in cwd; run from its _media source directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository pyproject.toml.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-4.3, 4.3, 900)
fig, ax = plt.subplots(figsize=(6, 6), layout="constrained")
c = 2 * np.sqrt(2)
ax.axhline(0, color="#176b9c", linewidth=1.7, label=r"Horizontal gradient: $h_y=0$")
ax.plot(t**2 / c, t, color="#176b9c", linewidth=1.7)
ax.plot(-t**2 / c, t, color="#176b9c", linewidth=1.7)
ax.axvline(0, color="#c46113", linewidth=1.7, linestyle="--", label=r"Vertical gradient: $h_x=0$")
ax.plot(t, t**2 / c, color="#c46113", linewidth=1.7, linestyle="--")
ax.plot(t, -t**2 / c, color="#c46113", linewidth=1.7, linestyle="--")
ax.scatter([0, c, c, -c, -c], [0, c, -c, c, -c], color="black", s=35, zorder=5, label="Stationary points")
ax.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(-4.3, 4.3), ylim=(-4.3, 4.3), title="Axis-parallel gradient loci")
ax.set_aspect("equal")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
