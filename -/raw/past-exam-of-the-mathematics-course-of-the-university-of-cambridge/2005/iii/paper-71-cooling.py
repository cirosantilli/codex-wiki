"""Isobaric cooling profiles; Python 3.14.4, NumPy and Matplotlib root dependencies.

Write paper-71-cooling.png to the caller's current directory.
The caller's MPLCONFIGDIR is respected without modification.
"""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

m = np.linspace(0.0, 8.0, 501)
fig, ax = plt.subplots(figsize=(7.2, 4.6), layout="constrained", facecolor="white")
ax.set_facecolor("white")
for tau, color in zip((0.25, 1.0, 4.0), ("#1769aa", "#e67300", "#388e3c")):
    profile = np.array([math.erf(z / (2 * math.sqrt(tau))) for z in m])
    ax.plot(m, profile, label=rf"$\tau={tau:g}$", color=color, linewidth=2.3)
ax.axhline(1, color="#777777", linestyle="--", linewidth=1, label="Initial hot temperature")
ax.annotate("Increasing time", xy=(3.0, 0.75), xytext=(3.0, 0.97),
            arrowprops={"arrowstyle": "->", "color": "#444444"}, ha="center")
ax.set(xlim=(0, 8), ylim=(0, 1.06), xlabel=r"Scaled mass coordinate $m$ ($\lambda_0=1$)",
       ylabel=r"Temperature $T/T_0$", title="Conductive cooling into a cold reservoir")
ax.grid(alpha=0.2)
ax.legend(loc="lower right", framealpha=1)
fig.savefig(Path.cwd() / "paper-71-cooling.png", dpi=150, facecolor="white", transparent=False)
plt.close(fig)
