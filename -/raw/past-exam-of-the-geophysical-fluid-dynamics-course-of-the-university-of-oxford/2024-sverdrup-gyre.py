"""Original transport sketch; schematic return width, Python 3.14."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7, 5.7), layout="constrained")
fig.get_layout_engine().set(rect=(0, 0.08, 1, 0.92))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
x = np.linspace(0, 1, 401)
y = np.linspace(0, 1, 301)
xx, yy = np.meshgrid(x, y)
delta = 0.055
decay = np.exp(-xx / delta)
end = np.exp(-1 / delta)
shape = 1 - xx - (decay - end) / (1 - end)
psi = np.sin(np.pi * yy) * shape
u = -np.pi * np.cos(np.pi * yy) * shape
v = np.sin(np.pi * yy) * (-1 + decay / (delta * (1 - end)))
ax.axvspan(0, 3 * delta, facecolor="#f5e1bc", alpha=0.8)
ax.contour(xx, yy, psi, levels=np.linspace(0.08, 0.78, 9), colors="#23748a", linewidths=1.4)
ax.streamplot(x, y, u, v, color="#23748a", density=0.65, linewidth=0, arrowsize=1.7)
ax.text(0.035, 0.5, "northward return", rotation=90, va="center", fontsize=11)
ax.text(0.67, 0.52, "broad southward\ninterior transport", ha="center", fontsize=11,
        bbox={"facecolor": "white", "alpha": 0.88, "edgecolor": "none"})
ax.annotate("westerlies", xy=(0.9, 1.07), xytext=(0.15, 1.07),
            arrowprops={"arrowstyle": "->", "lw": 2}, fontsize=11, annotation_clip=False)
ax.annotate("trade winds", xy=(0.1, -0.13), xytext=(0.68, -0.13),
            arrowprops={"arrowstyle": "->", "lw": 2}, fontsize=11, annotation_clip=False)
ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="x / basin width (eastward)",
       ylabel="y / basin length (northward)", title="Northern subtropical gyre: clockwise circulation")
ax.set_aspect(0.9)
fig.text(0.5, 0.02, "Return width exaggerated; contours and arrows show an illustrative closed transport field.",
         ha="center", fontsize=9)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120,
            facecolor="white", metadata={"Software": "codex-wiki figure generator"})
plt.close(fig)
