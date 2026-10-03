"""Conducting-square Darcy onset modes; Python 3.14, NumPy 2.3.5, mpl 3.10.7.

Writes a same-basename opaque white PNG beside this generator.
"""
from pathlib import Path
# Honour an explicitly owned MPLCONFIGDIR; otherwise Matplotlib uses its normal cache.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 241)
z = np.linspace(0, 1, 201)
X, Z = np.meshgrid(x, z)
q = 2 * np.sqrt(2) * np.pi
S = np.sin(np.pi * X) * np.sin(np.pi * Z)
phase = q * (X - .5) / 2
fields = [S * np.cos(phase), -S * np.sin(phase) / q,
          S * np.sin(phase), S * np.cos(phase) / q]
titles = [r'$\psi$ even, $\theta$ odd: stream function',
          r'$\psi$ even, $\theta$ odd: temperature',
          r'$\psi$ odd, $\theta$ even: stream function',
          r'$\psi$ odd, $\theta$ even: temperature']
fig, axes = plt.subplots(2, 2, figsize=(11, 6.8), dpi=100, facecolor='white')
for ax, field, title in zip(axes.flat, fields, titles):
    scale = np.max(np.abs(field))
    im = ax.imshow(field, extent=(0, 1, 0, 1), origin='lower', aspect='equal',
                   cmap='RdBu_r', vmin=-scale, vmax=scale)
    ax.set(title=title, xlabel='$x$', ylabel='$z$')
    ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
    fig.colorbar(im, ax=ax, fraction=.046, pad=.035)
fig.suptitle(r'Conducting-square Darcy convection: $R_c=8\pi^2$' + '\n'
             + 'Two independent real modes; arbitrary overall amplitude', fontsize=14)
fig.subplots_adjust(left=.07, right=.94, bottom=.09, top=.84, hspace=.38, wspace=.28)
fig.savefig((Path.cwd() / (Path(__file__).stem + '.png')), dpi=100,
            facecolor='white', transparent=False)
plt.close(fig)
