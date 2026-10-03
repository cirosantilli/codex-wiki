"""Python 3.14; numpy 2.3.5 and matplotlib 3.10.7. Emit an opaque PNG to cwd.
The caller supplies MPLCONFIGDIR; no cache location is changed here.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x, y = np.linspace(-2.7, 2.7, 750), np.linspace(-1.9, 1.9, 650)
X, Y = np.meshgrid(x, y)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.600001), dpi=100, facecolor="white")
for ax, a in zip(axes, [1, -1]):
    F = X*X-Y**4+2*a*Y*Y
    cs = ax.contour(X, Y, F, levels=[-3, -1, 0, .3, .7, 1, 1.7, 3, 5],
                    linewidths=1, cmap="coolwarm")
    ax.clabel(cs, inline=True, fontsize=8, fmt="%g")
    if a == 1:
        ax.contour(X, Y, F, levels=[1], colors=["black"], linewidths=1.5)
        points, labels = [(0, 0), (0, 1), (0, -1)], ["minimum", "saddle", "saddle"]
    else:
        ax.contour(X, Y, F, levels=[0], colors=["black"], linewidths=1.5)
        points, labels = [(0, 0)], ["saddle"]
    for p, label in zip(points, labels):
        ax.scatter(*p, color="black", s=18)
        ax.annotate(label, p, xytext=(8, 8), textcoords="offset points",
                    fontsize=9, bbox=dict(facecolor="white", alpha=.85, edgecolor="none"))
    ax.set(xlim=(-2.7, 2.7), ylim=(-1.9, 1.9), xlabel="x", ylabel="y",
           title=f"a = {a}, z = 0")
    ax.set_aspect("equal")
fig.suptitle("Quartic level sets; heavy curves pass through saddle points", fontsize=12)
fig.tight_layout()
fig.savefig(Path.cwd() / "paper-2-level-contours.png", dpi=100,
            facecolor="white", transparent=False)
plt.close(fig)
