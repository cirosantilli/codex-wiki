"""Schematic linearized RG flow. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.

Write the PNG basename to cwd; honor the caller's MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(9, 4), dpi=120, facecolor='white')
x = np.linspace(-1, 1, 36)
y = np.linspace(-1, 1, 36)
T, W = np.meshgrid(x, y)
left, right = axes
left.streamplot(x, y, 1.2*T, -0.9*W, color='#52636f', density=0.8,
                linewidth=0.8, arrowsize=1.15)
left.axvline(0, color='#0072b2', lw=2.6, label='Critical surface in h = 0 slice')
left.axhline(0, color='#d55e00', lw=1.6, linestyle='--', label='Repulsive thermal trajectory')
left.set(xlabel='Relevant thermal field t', ylabel='Irrelevant coordinate w',
         title='Zero-field slice: approach, then depart')
left.legend(loc='upper left', fontsize=7.4, framealpha=1)
right.streamplot(x, y, 1.2*T, 1.6*W, color='#52636f', density=0.8,
                 linewidth=0.8, arrowsize=1.15)
right.axvline(0, color='#d55e00', lw=1.3, linestyle='--')
right.axhline(0, color='#d55e00', lw=1.3, linestyle='--')
right.set(xlabel='Relevant thermal field t', ylabel='Relevant conjugate field h',
          title='Relevant plane: both fields grow')
for ax in axes:
    ax.scatter([0], [0], color='black', s=32, zorder=8)
    ax.set(xlim=(-1, 1), ylim=(-1, 1), aspect='equal')
    ax.set_facecolor('white')
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
fig.suptitle('Renormalization-group arrows point toward longer distances', fontsize=12)
fig.text(0.5, 0.025, 'The full critical surface requires t = h = 0; its other coordinates are irrelevant.',
         ha='center', fontsize=8.5)
fig.subplots_adjust(left=0.065, right=0.99, top=0.8, bottom=0.16, wspace=0.28)
fig.savefig('paper-42-rg-flows.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
