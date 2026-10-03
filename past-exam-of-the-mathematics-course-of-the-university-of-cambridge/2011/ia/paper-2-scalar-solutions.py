"""Python 3.14; numpy 2.3.5 and matplotlib 3.10.7. Emit an opaque PNG to cwd.
The caller supplies MPLCONFIGDIR; no cache location is changed here.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def rhs(y):
    return y * (y - 2) * (y + 1)

def curve(y0, sign):
    h = sign * 0.001
    x, y = 0.0, float(y0)
    pts = [(x, y)]
    for _ in range(1500):
        k1 = rhs(y)
        k2 = rhs(y + h*k1/2)
        k3 = rhs(y + h*k2/2)
        k4 = rhs(y + h*k3)
        y += h*(k1 + 2*k2 + 2*k3 + k4)/6
        x += h
        if abs(y) > 3.5:
            break
        pts.append((x, y))
    return np.asarray(pts)

fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=100, facecolor="white")
for y0 in [-1.3, -.92, -.6, -.25, .3, .8, 1.5, 1.93, 2.12]:
    a, b = curve(y0, -1), curve(y0, 1)
    xy = np.vstack([a[::-1], b[1:]])
    ax.plot(xy[:, 0], xy[:, 1], color="#2864a0", lw=1.5)
    j = min(160, len(b)-12)
    if j > 5:
        ax.annotate("", xy=b[j+10], xytext=b[j-10],
                    arrowprops=dict(arrowstyle="->", color="#2864a0", lw=1.5))
for y, label, color in [(-1, "unstable", "#a43b37"), (0, "stable", "#27754a"),
                         (2, "unstable", "#a43b37")]:
    ax.axhline(y, color=color, ls="--", lw=1.5)
    ax.text(1.02, y+.05, label, color=color, fontsize=9)
ax.set(xlim=(-1.15, 1.42), ylim=(-1.65, 2.7), xlabel="x", ylabel="y",
       title="Scalar cubic: arrows point toward increasing x")
ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd() / "paper-2-scalar-solutions.png", dpi=100,
            facecolor="white", transparent=False)
plt.close(fig)

