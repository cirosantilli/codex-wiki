"""Fourier reconstruction and heat-mode decay, Python 3.14.4.

Dependencies: NumPy 2.3.5, Matplotlib 3.10.7 (repository pyproject.toml).
Writes an opaque PNG with this script's basename in the current directory.
The heat profile is an illustrative example, not additional examination data.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.facecolor': 'white',
                     'axes.facecolor': 'white', 'savefig.facecolor': 'white'})
fig, axes = plt.subplots(1, 2, figsize=(10.6, 3.8), layout='constrained')
x = np.linspace(-np.pi, np.pi, 2401)
ax = axes[0]
ax.plot([-np.pi, 0], [-1, -1], color='black', linewidth=1.6)
ax.plot([0, np.pi], [1, 1], color='black', linewidth=1.6, label='Square wave')
for terms, color in [(1, '#c96d20'), (5, '#169579'), (25, '#3867b1')]:
    odd = np.arange(1, 2*terms, 2)
    partial = (4/np.pi)*(np.sin(x[:, None]*odd)/odd).sum(axis=1)
    ax.plot(x, partial, color=color, linewidth=1.1, label=f'{terms} odd mode'+('s' if terms > 1 else ''))
ax.set(xlim=(-np.pi, np.pi), ylim=(-1.45, 1.45), xlabel='Position x', ylabel='Partial sum',
       title='Fourier reconstruction')
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
              [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
ax.axhline(0, color='0.7', linewidth=0.6)
ax.grid(alpha=0.15)
ax.legend(loc='lower right', fontsize=8)

ax = axes[1]
x = np.linspace(0, 1, 501)
for t, color in [(0, '#444444'), (0.01, '#c96d20'), (0.05, '#169579'), (0.2, '#3867b1')]:
    temperature = np.exp(-np.pi**2*t)*np.sin(np.pi*x) + 0.5*np.exp(-9*np.pi**2*t)*np.sin(3*np.pi*x)
    ax.plot(x, temperature, color=color, linewidth=1.8, label=f't = {t:g}')
ax.set(xlim=(0, 1), ylim=(0, 1.35), xlabel='Position x / L', ylabel='Temperature',
       title='Heat flow: faster decay of higher modes')
ax.text(0.5, 1.28, r'$D=L=1,\quad \Theta_0=\sin(\pi x)+\frac{1}{2}\sin(3\pi x)$',
        ha='center', va='top', fontsize=9)
ax.grid(alpha=0.15)
ax.legend(loc='lower center', fontsize=8)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=110, transparent=False)
plt.close(fig)
