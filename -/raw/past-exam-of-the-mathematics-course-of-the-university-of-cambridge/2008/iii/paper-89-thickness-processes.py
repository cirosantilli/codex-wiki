#!/usr/bin/env python3
"""Illustrative thickness transports; Python 3, NumPy and Matplotlib.
Write paper-89-thickness-processes.png to the caller's working directory.
"""
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def gamma_density(h, scale=0.2):
    return h ** 6 * np.exp(-h / scale) / (math.factorial(6) * scale ** 7)


h = np.linspace(0, 6, 2401)
g0 = gamma_density(h)
initial = np.sqrt(np.maximum(h * h - 0.64, 0))
grown = np.zeros_like(h)
valid = initial > 0
grown[valid] = gamma_density(initial[valid]) * h[valid] / initial[valid]
mechanical = 0.6 * g0 + 0.1 * gamma_density(h / 2)
fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.5), constrained_layout=True)
curves = [gamma_density(h, 0.3), grown, mechanical]
colors = ['#24688c', '#18764d', '#a65126']
titles = ['Advection: thicker incoming ice', 'Thermodynamics: winter growth', 'Mechanics: double-thickness stacks']
labels = ['Incoming distribution', 'After growth', 'Continuous part after stacking']
for ax, curve, color, title, label in zip(axes, curves, colors, titles, labels):
    ax.plot(h, g0, '--', color='#777777', lw=1.6, label='Initial distribution')
    ax.plot(h, curve, color=color, lw=2, label=label)
    ax.set(xlim=(0, 6), ylim=(0, 1.22), xlabel='Thickness h (m)', title=title)
    ax.grid(alpha=0.15)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(fontsize=7.5, frameon=False, loc='upper right')
axes[0].set_ylabel('Area density g(h) (per metre)')
axes[2].annotate('Open water: area 0.20\n(point mass, not density)', xy=(0, 0.04),
                 xytext=(2.8, 0.8), fontsize=8, color='#a65126',
                 arrowprops={'arrowstyle': '->', 'color': '#a65126'})
fig.savefig('paper-89-thickness-processes.png', dpi=110, facecolor='white')
