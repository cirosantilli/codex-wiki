"""Illustrate the fundamental-mode omission in A10100W1 (2016), Q5.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Uses the repository pyproject.toml dependencies. Writes basename PNG to CWD.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 1601)
tent = np.minimum(x, 1 - x)

def partial(modes):
    m = np.arange(modes)[:, None]
    odd = 2 * m + 1
    return np.sum(4 * (-1.0) ** m / (odd**2 * np.pi**2)
                  * np.sin(odd * np.pi * x), axis=0)

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), layout='constrained')
for ax in axes:
    ax.plot(x, tent, color='black', lw=2, label='Initial tent')
    ax.set(xlabel=r'$x/L$', ylabel=r'$u_0/(L\rho)$', xlim=(0, 1))
    ax.grid(alpha=.22)
for count, color in [(1, '#0072B2'), (3, '#E69F00'), (15, '#009E73')]:
    axes[0].plot(x, partial(count), lw=1.5, color=color,
                 label=f'{count} odd mode' + ('s' if count > 1 else ''))
axes[0].set_title('Correct series starts at m = 0')
axes[0].legend(fontsize=8, loc='upper right')
fundamental = 4 / np.pi**2 * np.sin(np.pi * x)
axes[1].plot(x, fundamental, '--', color='#0072B2', lw=1.5,
             label='Omitted fundamental')
axes[1].plot(x, partial(80) - fundamental, color='#D55E00', lw=2,
             label='Printed series starts at m = 1')
axes[1].set_title('Omitting the fundamental changes the profile')
axes[1].legend(fontsize=8, loc='upper right')
fig.savefig(Path(Path(__file__).stem + '.png'), dpi=130, facecolor='white',
            transparent=False)
plt.close(fig)
