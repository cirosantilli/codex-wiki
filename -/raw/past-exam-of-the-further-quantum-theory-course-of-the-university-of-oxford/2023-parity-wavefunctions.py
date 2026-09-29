"""Draw qualitative double-well parity states; write PNG in the working directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies are already listed in the wiki's root pyproject.toml.
The normalized Gaussian superpositions illustrate parity, not an exact potential.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(-3.8, 3.8, 1201)
b, width = 1.55, 0.62
normalization = (np.pi * width**2)**(-0.25)
left = normalization * np.exp(-(x + b)**2 / (2 * width**2))
right = normalization * np.exp(-(x - b)**2 / (2 * width**2))
overlap = np.exp(-b**2 / width**2)
even = (left + right) / np.sqrt(2 * (1 + overlap))
odd = (right - left) / np.sqrt(2 * (1 - overlap))
assert np.max(np.abs(even - even[::-1])) < 1e-12
assert np.max(np.abs(odd + odd[::-1])) < 1e-12
assert abs(np.trapezoid(even**2, x) - 1) < 1e-6
assert abs(np.trapezoid(odd**2, x) - 1) < 1e-6
with plt.rc_context({'font.size': 11, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.facecolor': 'white',
                     'axes.facecolor': 'white'}):
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5), sharey=True, layout='constrained')
    for ax, y, title, color in zip(axes, (even, odd),
            ('Even ground state', 'Odd first excited state'), ('#1764a2', '#b54c24')):
        ax.axhline(0, color='#777777', lw=0.7)
        ax.axvline(0, color='#999999', lw=0.8, ls=':')
        ax.plot(x, y, color=color, lw=2.4)
        ax.set(xlabel=r'$x$ (arbitrary units)', title=title, xlim=(-3.7, 3.7), ylim=(-0.8, 0.9))
        ax.set_xticks([-b, 0, b], [r'$-b$', '0', r'$b$'])
    axes[0].set_ylabel(r'Wavefunction $\psi(x)$')
    axes[0].annotate(r'$\psi(0)>0,\quad\psi^{\prime}(0)=0$', xy=(0, even[len(x)//2]),
                     xytext=(-0.35, 0.76), ha='center', fontsize=10,
                     arrowprops={'arrowstyle': '->', 'color': '#555555'})
    axes[1].annotate(r'$\psi(0)=0$: one node', xy=(0, 0), xytext=(-0.2, 0.76),
                     ha='center', fontsize=10,
                     arrowprops={'arrowstyle': '->', 'color': '#555555'})
    fig.savefig(Path.cwd() / '2023-parity-wavefunctions.png', dpi=110, facecolor='white')
    plt.close(fig)
