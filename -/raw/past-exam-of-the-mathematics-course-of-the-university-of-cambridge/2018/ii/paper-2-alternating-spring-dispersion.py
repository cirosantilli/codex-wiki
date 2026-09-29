#!/usr/bin/env python3
"""Plot the phonon branches for 2018 Part II Paper 2, question 35."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


alpha = 0.35
ka = np.linspace(-np.pi / 2.0, np.pi / 2.0, 1000)
root = np.sqrt((1.0 - alpha) ** 2 + 4.0 * alpha * np.cos(ka) ** 2)
acoustic = np.sqrt(1.0 + alpha - root)
optical = np.sqrt(1.0 + alpha + root)

fig, ax = plt.subplots(figsize=(8.0, 5.0), layout="constrained")
ax.plot(ka, acoustic, linewidth=2.5, label="acoustic branch")
ax.plot(ka, optical, linewidth=2.5, label="optical branch")
for edge in (-np.pi / 2.0, np.pi / 2.0):
    ax.axvline(edge, color="0.55", linestyle=":", linewidth=1.0)
edge_low = np.sqrt(2.0 * min(1.0, alpha))
edge_high = np.sqrt(2.0 * max(1.0, alpha))
ax.annotate(
    "",
    xy=(np.pi / 2.0, edge_high),
    xytext=(np.pi / 2.0, edge_low),
    arrowprops={"arrowstyle": "<->", "color": "#7b2cbf", "linewidth": 1.8},
)
ax.text(
    np.pi / 2.0 - 0.05,
    (edge_low + edge_high) / 2.0,
    "edge gap",
    color="#7b2cbf",
    ha="right",
    va="center",
)
ax.set_xticks(
    (-np.pi / 2.0, 0.0, np.pi / 2.0),
    (r"$-\pi/2$", r"$0$", r"$\pi/2$"),
)
ax.set_xlabel(r"$ka$")
ax.set_ylabel(r"$\omega/\sqrt{\lambda/m}$")
ax.set_title(r"Alternating-spring chain, $\alpha=0.35$")
ax.set_xlim(-np.pi / 2.0, np.pi / 2.0)
ax.set_ylim(0.0, 1.75)
ax.grid(alpha=0.2)
ax.legend(loc="lower center")

output = Path(Path(__file__).stem + ".png")
fig.savefig(output, dpi=100, facecolor="white")
plt.close(fig)
