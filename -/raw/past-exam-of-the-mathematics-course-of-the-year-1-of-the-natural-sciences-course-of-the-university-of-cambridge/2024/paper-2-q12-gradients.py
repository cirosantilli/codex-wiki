"""Generate this exam figure in cwd; run from its _media source directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are documented in the repository pyproject.toml.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

c = 2 * np.sqrt(2)
centres = [(-c, c), (0, 0), (c, c), (-c, -c), (c, -c)]
fig, axes = plt.subplots(2, 3, figsize=(10, 6.8), layout="constrained")
for ax, (a, b) in zip(axes.flat, centres):
    half = 0.65 if a == b == 0 else 0.42
    delta = np.linspace(-half, half, 13)
    dx, dy = np.meshgrid(delta, delta)
    x, y = a + dx, b + dy
    gx, gy = 6 * x**5 - 48 * x * y**2, 6 * y**5 - 48 * x**2 * y
    length = np.hypot(gx, gy)
    mask = length > 1e-10
    ux = np.divide(gx, length, out=np.zeros_like(gx), where=mask)
    uy = np.divide(gy, length, out=np.zeros_like(gy), where=mask)
    ax.quiver(x, y, ux, uy, angles="xy", scale_units="xy", scale=18 / half, color="#176b9c", width=0.006)
    ax.scatter([a], [b], color="#b33b35", s=35, zorder=4)
    if a == b == 0:
        ax.set_title("Origin: degenerate saddle")
    else:
        ax.set_title(f"Minimum at ({a:.3f}, {b:.3f})")
    ax.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(a-half*1.1,a+half*1.1), ylim=(b-half*1.1,b+half*1.1))
    ax.set_aspect("equal")
    ax.grid(alpha=0.15)
axes.flat[-1].axis("off")
fig.suptitle(r"Directions of $\nabla h$: toward increasing $h$", fontsize=14)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white")
plt.close(fig)
