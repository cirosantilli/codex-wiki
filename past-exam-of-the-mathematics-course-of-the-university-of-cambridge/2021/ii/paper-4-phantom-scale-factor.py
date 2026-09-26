#!/usr/bin/env python3
"""Generate paper-4-phantom-scale-factor.png."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np



transition_time = 1.0
rip_time = 2.5

matter_time = np.linspace(0.0, transition_time, 400)
matter_scale = matter_time ** (2.0 / 3.0)

phantom_time = np.linspace(transition_time, 2.44, 600)
phantom_scale = (rip_time - transition_time) / (rip_time - phantom_time)

fig, ax = plt.subplots(figsize=(8.0, 5.2), layout="constrained")
ax.plot(matter_time, matter_scale, linewidth=2.5, label=r"matter: $a\propto t^{2/3}$")
ax.plot(
    phantom_time,
    phantom_scale,
    linewidth=2.5,
    label=r"phantom ($w=-5/3$): $a\propto(t^*-t)^{-1}$",
)
ax.axvline(transition_time, color="0.5", linestyle=":", linewidth=1.2)
ax.axvline(rip_time, color="#d62728", linestyle="--", linewidth=1.5)
ax.scatter((0.0,), (0.0,), color="black", zorder=3)
ax.annotate("Big Bang", (0.0, 0.0), xytext=(10, 12), textcoords="offset points")
ax.annotate(
    "phantom energy takes over",
    (transition_time, 1.0),
    xytext=(10, 24),
    textcoords="offset points",
    arrowprops={"arrowstyle": "->"},
)
ax.text(rip_time - 0.02, 18.0, r"Big Rip $t^*$", rotation=90, ha="right", va="top")
ax.set_xlim(0.0, 2.6)
ax.set_ylim(0.0, 20.0)
ax.set_xlabel(r"cosmic time $t$")
ax.set_ylabel(r"scale factor $a(t)$")
ax.set_title("Matter era followed by phantom-energy domination")
ax.grid(alpha=0.2)
ax.legend(loc="upper left")

output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=160, facecolor="white")
plt.close(fig)
