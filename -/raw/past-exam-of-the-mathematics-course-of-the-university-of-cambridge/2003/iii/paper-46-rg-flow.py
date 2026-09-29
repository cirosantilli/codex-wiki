"""Original linear RG flow sketches; Python 3.14 with root NumPy/Matplotlib.
Write paper-46-rg-flow.png to the caller's working directory.
"""
import os
import tempfile
os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="paper-46-mpl-"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10, 4.4), facecolor="white", layout="constrained")
x = np.linspace(-1.1, 1.1, 25)
y = np.linspace(-1.1, 1.1, 25)
X, Y = np.meshgrid(x, y)
axes[0].streamplot(x, y, -X, 1.2*Y, color="#48769a", density=.75, linewidth=1.1, arrowsize=1.1)
axes[0].axhline(0, color="#9c3434", lw=2, label="Critical surface in h = 0 section")
for w in [-.85, -.4, .4, .85]:
    axes[0].annotate("", (w*.6, 0), (w, 0), arrowprops={"arrowstyle":"->", "color":"#9c3434", "lw":2})
axes[0].set(xlabel="Irrelevant field w", ylabel="Relevant thermal field t", title="Attraction along the critical surface")
axes[0].legend(loc="lower center", fontsize=8)
axes[1].streamplot(x, y, 1.2*X, 1.8*Y, color="#48769a", density=.75, linewidth=1.1, arrowsize=1.1)
axes[1].set(xlabel="Relevant thermal field t", ylabel="Relevant magnetic field h", title="Repulsion in the two tuned directions")
for ax in axes:
    ax.scatter([0], [0], color="black", s=35, zorder=5)
    ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), aspect="equal")
    ax.grid(alpha=.15)
fig.savefig("paper-46-rg-flow.png", dpi=120, facecolor="white", transparent=False)
plt.close(fig)
