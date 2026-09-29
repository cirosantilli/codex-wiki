#!/usr/bin/env python3
"""Generate paper-342-kitaev-ellipse-winding.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


k = np.linspace(-np.pi, np.pi, 700)
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5), layout="constrained")
for ax, mu, title in zip(axes, (0.0, -3.0), ("topological: $|\\mu|<2t$", "trivial: $\\mu<-2t$")):
    dy = -2 * np.sin(k)
    dz = -2 * np.cos(k) - mu
    ax.plot(dz, dy, color="#1f77b4", linewidth=2.7)
    ax.scatter([0], [0], marker="x", s=90, linewidths=2.5, color="#d62728", zorder=4, label="origin")
    for index in (80, 270, 470):
        ax.annotate("", (dz[index + 10], dy[index + 10]), (dz[index], dy[index]), arrowprops={"arrowstyle": "->", "color": "#1f77b4", "lw": 1.8})
    ax.axhline(0, color="0.8", linewidth=0.8)
    ax.axvline(0, color="0.8", linewidth=0.8)
    ax.set(xlabel="$d_z(k)$", ylabel="$d_y(k)$", title=title, aspect="equal", xlim=(-3.3, 5.6), ylim=(-2.8, 2.8))
    ax.grid(alpha=0.18)
axes[0].text(0.08, 0.08, "winding number $1$", transform=axes[0].transAxes)
axes[1].text(0.08, 0.08, "winding number $0$", transform=axes[1].transAxes)
fig.suptitle("Kitaev-chain Bogoliubov–de Gennes vector as $k$ crosses the Brillouin zone")
fig.savefig(Path(Path(__file__).stem + ".png"), dpi=100, facecolor="white")
plt.close(fig)
