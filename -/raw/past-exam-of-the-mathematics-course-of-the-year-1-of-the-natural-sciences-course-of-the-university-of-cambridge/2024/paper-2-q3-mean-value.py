"""Generate this exam figure in cwd; run from its _media source directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository pyproject.toml.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 500)
xi = 1 / np.log(2)
fig, ax = plt.subplots(figsize=(7, 4.3), layout="constrained")
ax.plot(x, np.log(x), color="#176b9c", linewidth=2.3, label=r"$y=\log x$")
ax.plot(x, (x - 1) * np.log(2), color="#b33b35", linestyle="--", label="Chord")
ax.plot(x, np.log(xi) + (x - xi) * np.log(2), color="#26834a", linestyle="-.", label=r"Tangent at $\xi=1/\log 2$")
ax.scatter([1, xi, 2], [0, np.log(xi), np.log(2)], color="#176b9c", zorder=4)
ax.axvline(xi, color="0.6", linewidth=0.8, linestyle=":")
ax.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(0.98, 2.02), ylim=(-0.035, 0.78), title="Equal chord and tangent slopes")
ax.legend(loc="upper left")
ax.grid(alpha=0.2)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
