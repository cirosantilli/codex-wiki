#!/usr/bin/env python3
"""Draw the cross-section used in 2019 IA Paper 3, question 9."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT = Path(__file__).with_suffix('.svg')
plt.rcParams['svg.hashsalt'] = 'codex-wiki'

alpha = 0.55
gamma = 0.8
z0 = gamma * np.sqrt((1 - alpha**2) / (1 + gamma**2))
z = np.linspace(-z0, z0, 400)
x_circle = np.sqrt(1 - z**2)
x_hyperbola = alpha * np.sqrt(1 + z**2 / gamma**2)

fig, ax = plt.subplots(figsize=(6.2, 4.8))
ax.fill_betweenx(z, x_hyperbola, x_circle, color='#8db7d8', alpha=0.55)
ax.plot(x_circle, z, color='#225f8b', label='$x^2+z^2=1$')
ax.plot(x_hyperbola, z, color='#a14b2a', label='$x^2/\\alpha^2-z^2/(\\alpha^2\\gamma^2)=1$')
ax.scatter([alpha, 1, x_circle[0], x_circle[-1]], [0, 0, -z0, z0], color='black', s=18, zorder=4)
ax.annotate('$x_{\\min}=\\alpha$', (alpha, 0), xytext=(6, 8), textcoords='offset points')
ax.annotate('$x_{\\max}=1$', (1, 0), xytext=(-52, 8), textcoords='offset points')
ax.annotate('$(x_0,z_0)$', (x_circle[-1], z0), xytext=(5, -2), textcoords='offset points')
ax.set(xlabel='$x$', ylabel='$z$', xlim=(0, 1.08), ylim=(-0.85, 0.85))
ax.axhline(0, color='0.5', linewidth=0.6)
ax.legend(loc='lower right', fontsize=8)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(OUTPUT, metadata={'Date': None})
