"""Plot Question 5(b)'s exact and Euler decay curves; write PNG to CWD.

Tested with Python 3.14.4, matplotlib 3.10.7+dfsg1, numpy 2.3.5.
Dependencies are documented in the repository's top-level pyproject.toml.
Run: python /absolute/path/to/discrete-main-2015-euler-stability.py
"""
from pathlib import Path
import os

os.environ.setdefault('MPLCONFIGDIR', str(Path.cwd() / '.discrete-main-2015-matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
    decay_rate = 8.0
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), layout='constrained')
    fig.set_facecolor('white')
    t = np.linspace(0, 1, 401)
    exact = 2 * np.exp(-decay_rate * t)
    panels = [
        ('Unstable and neutral', [(3, '#c23b22'), (4, '#b07700')]),
        ('Stable: damped oscillation or monotone decay', [(5, '#8053a1'), (16, '#007d79')]),
    ]
    for ax, (title, cases) in zip(axes, panels):
        ax.set_facecolor('white')
        ax.plot(t, exact, color='#202020', linewidth=2, label=r'Exact $2e^{-8t}$')
        for steps, colour in cases:
            grid = np.arange(steps + 1) / steps
            factor = 1 - decay_rate / steps
            values = 2 * factor ** np.arange(steps + 1)
            ax.plot(grid, values, 'o-', markersize=4, color=colour,
                    label=f'N = {steps}, factor = {factor:.2f}')
        ax.axhline(0, color='#777777', linewidth=0.6)
        ax.set(xlim=(0, 1), xlabel='x', ylabel='y', title=title)
        ax.grid(alpha=0.2)
        ax.legend(fontsize=9, loc='best')
    axes[0].set_ylim(-10, 6)
    axes[1].set_ylim(-1.4, 2.3)
    fig.suptitle('Forward Euler for exponential decay: stability requires N > 4', fontsize=13)
    fig.savefig(Path.cwd() / 'discrete-main-2015-euler-stability.png', dpi=120,
                facecolor='white', transparent=False, metadata={'Software': 'Matplotlib'})
    plt.close(fig)


if __name__ == '__main__':
    main()
