"""Draw Newton cooling trajectories; tested with Python 3.14, NumPy, Matplotlib."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


def cooling(t, initial):
    return 20.0 + (initial - 20.0) * np.exp(-0.1 * t)


plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.6), dpi=125, constrained_layout=True)
fig.patch.set_facecolor("white")
t = np.linspace(0.0, 30.0, 601)
colors = ("#bb4b20", "#2176a5", "#258568")

for initial, color in zip((80.0, 50.0, 5.0), colors):
    axes[0].plot(t, cooling(t, initial), color=color, lw=2.5,
                 label=f"y(0) = {initial:g} °C", zorder=3)
    axes[0].scatter([0], [initial], s=32, color=color, zorder=4)
axes[0].axhline(20.0, color="#444444", linestyle="--", lw=1.8,
               label="equilibrium: 20 °C", zorder=3)
axes[0].set(xlim=(-0.6, 30.5), ylim=(-2, 87), xlabel="time t (min)",
            ylabel="temperature y (°C)", title=r"One local law: $y'=-0.1(y-20)$")
axes[0].legend(loc="upper right", fontsize=9, framealpha=1)

axes[1].plot(t, cooling(t, 80.0), color=colors[0], lw=2.8)
axes[1].axhline(20.0, color="#444444", linestyle="--", lw=1.6)
axes[1].set(xlim=(-0.6, 30.5), ylim=(17, 87), xlabel="time t (min)",
            ylabel="temperature y (°C)", title=r"The selected trajectory: $y=20+60e^{-0.1t}$")
for moment, text_y in ((10.0, 63.0), (10.0 * np.log(6.0), 47.0)):
    value = cooling(moment, 80.0)
    axes[1].plot([moment, moment], [20.0, value], color="#aaaaaa", lw=1, linestyle=":")
    axes[1].scatter([moment], [value], color=colors[0], s=40, zorder=4)
    axes[1].annotate(f"({moment:.2f} min, {value:.2f} °C)",
                     xy=(moment, value), xytext=(moment - 5.0, text_y),
                     arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=10)
axes[1].text(29.0, 21.6, "ambient: 20 °C", ha="right", fontsize=10, color="#444444")

for ax in axes:
    ax.set_facecolor("white")
    ax.grid(alpha=0.13)

# Normalize segment lengths in display coordinates without changing dy/dt.
# This keeps the field readable even though the two axes have different units.
fig.canvas.draw()
grid_t, grid_y = np.meshgrid(np.linspace(0, 30, 19), np.arange(0, 86, 5))
points = np.column_stack((grid_t.ravel(), grid_y.ravel()))
directions = np.column_stack((np.ones(points.shape[0]), -0.1 * (points[:, 1] - 20.0)))
display = axes[0].transData.transform(points)
vectors = axes[0].transData.transform(points + directions) - display
vectors /= np.linalg.norm(vectors, axis=1)[:, None]
endpoints = np.stack((display - 6.0 * vectors, display + 6.0 * vectors), axis=1)
segments = axes[0].transData.inverted().transform(endpoints.reshape(-1, 2)).reshape(-1, 2, 2)
axes[0].add_collection(LineCollection(segments, colors="#aeb8c0", linewidths=0.9, zorder=1))
fig.savefig(Path.cwd() / "ode-cooling-direction-field.png", facecolor="white", transparent=False)
plt.close(fig)
