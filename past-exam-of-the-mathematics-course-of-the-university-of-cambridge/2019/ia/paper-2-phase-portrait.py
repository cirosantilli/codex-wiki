#!/usr/bin/env python3
"""Draw the phase portrait for 2019 IA Paper 2, question 8."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(Path(__file__).stem + '.png')

x = np.linspace(-1.25, 1.25, 321)
y = np.linspace(-1.2, 1.2, 321)
xx, yy = np.meshgrid(x, y)
hamiltonian = xx**2 + yy**2 - yy**4
xdot = yy - 2 * yy**3
ydot = -xx

fig, ax = plt.subplots(figsize=(6.4, 5.8))
ax.streamplot(x, y, xdot, ydot, density=1.05, color='0.78', linewidth=0.65, arrowsize=0.65)
ax.contour(xx, yy, hamiltonian, levels=[-0.5, 0.0, 0.1, 0.18, 0.35, 0.6, 1.0], colors='#4477aa', linewidths=0.85)
special = ax.contour(xx, yy, hamiltonian, levels=[0.25], colors='#bb3322', linewidths=2.0)
ax.clabel(special, fmt={0.25: '$H=1/4$'}, inline=True, fontsize=10)

critical_x = np.array([0.0, 0.0, 0.0])
critical_y = np.array([0.0, 1 / np.sqrt(2), -1 / np.sqrt(2)])
ax.scatter(critical_x, critical_y, color='black', s=26, zorder=5)
ax.text(0.04, 0.04, 'center', fontsize=9)
ax.text(0.04, 1 / np.sqrt(2) + 0.03, 'saddle', fontsize=9)
ax.text(0.04, -1 / np.sqrt(2) - 0.08, 'saddle', fontsize=9)

ax.axhline(0, color='0.35', linewidth=0.6)
ax.axvline(0, color='0.35', linewidth=0.6)
ax.set(xlabel='$x$', ylabel='$y$', xlim=(-1.25, 1.25), ylim=(-1.2, 1.2), aspect='equal')
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(OUTPUT, dpi=160, facecolor="white")
