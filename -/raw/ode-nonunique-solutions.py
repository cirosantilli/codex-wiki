"""Show valid forward delayed-start ODE solutions; tested with Python 3.14."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(7.6, 4.7), dpi=125, constrained_layout=True)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
t = np.linspace(0.0, 4.0, 801)
ax.axhline(0.0, color="#555555", linestyle="--", lw=2.0, label=r"stay forever: $y=0$")
for delay, color in zip((0.0, 1.0, 2.0), ("#bb4b20", "#2176a5", "#258568")):
    y = np.maximum(t - delay, 0.0) ** 2 / 4.0
    ax.plot(t, y, color=color, lw=2.6, label=f"wait until a = {delay:g}, then rise")
    ax.scatter([delay], [0.0], s=42, color=color, zorder=5)
    ax.scatter([4.0], [(4.0 - delay) ** 2 / 4.0], s=35, color=color, zorder=5)
ax.scatter([0.0], [0.0], facecolor="white", edgecolor="#111111", s=65, zorder=6)
ax.annotate("same initial value (0, 0)", xy=(0, 0), xytext=(0.2, 1.25),
            arrowprops={"arrowstyle": "->", "color": "#555555"}, fontsize=11)
ax.set(xlim=(-0.1, 4.15), ylim=(-0.2, 4.3), xlabel="time t ≥ 0 (dimensionless)",
       ylabel="state y (dimensionless)",
       title=r"$y'=\sqrt{|y|},\quad y(0)=0$: the start time is free")
ax.legend(loc="upper left", fontsize=10, framealpha=1)
ax.grid(alpha=0.15)
fig.savefig(Path.cwd() / "ode-nonunique-solutions.png", facecolor="white", transparent=False)
plt.close(fig)
