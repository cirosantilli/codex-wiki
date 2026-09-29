"""Generate this figure in cwd, normally the mirrored _media directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from math import erf, sqrt, pi
x = np.linspace(-3.6, 3.6, 800)
y = np.array([sqrt(pi) * (1 + erf(t)) / 2 for t in x])
fig, ax = plt.subplots(figsize=(7.5, 4), layout="constrained")
ax.plot(x, y, color="#176b9c", linewidth=2.4)
ax.axhline(0, color="0.5", linewidth=0.8)
ax.axhline(sqrt(pi), color="0.5", linewidth=0.8, linestyle="--")
ax.axvline(0, color="0.5", linewidth=0.8)
ax.scatter([0], [sqrt(pi)/2], color="#b33b35", s=35, zorder=4)
ax.annotate(r"$(0,\sqrt{\pi}/2)$", xy=(0, sqrt(pi)/2), xytext=(-2.6, 1.25), arrowprops={"arrowstyle": "->", "color": "0.4"})
ax.set(xlabel=r"$x$", ylabel=r"$y(x)$", xlim=(-3.6, 3.6), ylim=(-0.08, 1.95), title="Integral of a Gaussian from minus infinity")
ax.set_yticks([0, sqrt(pi)/2, sqrt(pi)], ["0", r"$\sqrt{\pi}/2$", r"$\sqrt{\pi}$"])
ax.grid(alpha=0.15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
