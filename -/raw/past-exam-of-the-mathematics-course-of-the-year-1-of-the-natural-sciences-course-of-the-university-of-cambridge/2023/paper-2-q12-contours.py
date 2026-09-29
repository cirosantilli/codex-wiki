"""Generate this figure in cwd, normally the mirrored _media directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-2, 2, 501)
x, y = np.meshgrid(t, t)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), layout="constrained")
fields = [np.exp(x) + np.exp(y) - x - y, np.exp(x) - np.exp(y) - x + y]
levels = [[2.1, 2.4, 3, 4, 5, 6, 8], [-4, -2, -1, -0.3, 0, 0.3, 1, 2, 4]]
for i, (ax, field, contours) in enumerate(zip(axes, fields, levels)):
    lines = ax.contour(x, y, field, levels=contours, cmap="coolwarm", linewidths=1.3)
    ax.clabel(lines, inline=True, fontsize=8, fmt="%g")
    near = np.linspace(-0.72, 0.72, 7)
    xx, yy = np.meshgrid(near, near)
    gx = np.exp(xx) - 1
    gy = (np.exp(yy) - 1) * (1 if i == 0 else -1)
    norm = np.hypot(gx, gy)
    mask = norm > 1e-12
    gx = np.divide(gx, norm, out=np.zeros_like(gx), where=mask)
    gy = np.divide(gy, norm, out=np.zeros_like(gy), where=mask)
    ax.quiver(xx, yy, gx, gy, angles="xy", scale_units="xy", scale=8, color="black", width=0.006, zorder=4)
    ax.scatter([0], [0], color="black", s=28, zorder=5)
    ax.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(-2, 2), ylim=(-2, 2))
    ax.set_aspect("equal")
    ax.grid(alpha=0.12)
axes[0].set_title(r"Minimum: $e^x+e^y-x-y$")
axes[1].set_title(r"Saddle: $e^x-e^y-x+y$")
fig.suptitle("Level curves and directions of increasing height", fontsize=14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
