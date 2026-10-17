"""Original level curves and gradients for the triangular cubic."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 550)
y = np.linspace(-1, 0, 550)
xx, yy = np.meshgrid(x, y)
f = np.ma.masked_where(yy < xx - 1, xx * yy * (1 - xx + yy))
fig, ax = plt.subplots(figsize=(6, 5.2), layout="constrained")
levels = [-0.036, -0.03, -0.02, -0.01, -0.003]
cs = ax.contour(xx, yy, f, levels=levels, cmap="viridis", linewidths=1.6)
ax.clabel(cs, fontsize=9, fmt="%g")
ax.plot([0, 1, 0, 0], [0, 0, -1, 0], color="black", lw=1.8)
points = np.array([[0.5, 0], [0.5, -0.5], [0, -0.5]])
grads = np.array([[0, 0.25], [0.25, -0.25], [-0.25, 0]])
ax.quiver(points[:, 0], points[:, 1], grads[:, 0], grads[:, 1],
          angles="xy", scale_units="xy", scale=1, color="tab:red", width=0.006)
ax.scatter([1/3], [-1/3], color="tab:red", s=36, zorder=5)
ax.annotate(r"minimum $-1/27$", (1/3, -1/3), (0.62, -0.22),
            arrowprops={"arrowstyle": "-", "color": "0.4"}, fontsize=10)
ax.set(xlim=(-0.32, 1.12), ylim=(-1.12, 0.33), aspect="equal",
       xlabel="$x$", ylabel="$y$", title=r"$f(x,y)=xy(1-x+y)$")
ax.grid(alpha=0.16)
fig.savefig(Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white")
