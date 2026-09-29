"""Broken-symmetry oscillator sequences; schematic event spacing, not numeric axes.
Python 3.14/NumPy 2.3.5/Matplotlib 3.10.7; PNG basename in caller CWD.
Honors caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    fig = plt.figure(figsize=(9, 6.5), layout='constrained')
    fig.patch.set_facecolor('white')
    grid = fig.add_gridspec(3, 1, height_ratios=[1.35, .85, 2.3])
    ax = fig.add_subplot(grid[0]);ax.set_facecolor('white')
    events = ['Hopf', r'$v_-\to v_+$', r'Homoclinic\nto $v_+$', r'$v_+\to v_-$', 'Transcritical', 'Saddle-node']
    events[2] = 'Homoclinic\nto $v_+$'
    ax.annotate('', (6.4, 0), (-.5, 0), arrowprops={'arrowstyle': '->', 'lw': 1.5})
    for j, label in enumerate(events):
        ax.plot(j, 0, 'o', color='#00679c', ms=5)
        ax.text(j, .2, label, ha='center', va='bottom', fontsize=9)
        if j in [0, 4, 5]:
            ax.text(j, -.2, [r'$\lambda=1$', r'$\lambda=0$', r'$\lambda=-\varepsilon^2$'][[0, 4, 5].index(j)], ha='center', va='top', fontsize=9)
    ax.text(.5, -.65, 'Stable cycle born', ha='center', fontsize=9)
    ax.text(2.8, -.65, 'Cycle lost; basin connections separated', ha='center', fontsize=9)
    ax.set(xlim=(-.5, 6.5), ylim=(-.85, .75), title=r'$\kappa+\lambda=+1$: decreasing $\lambda$ (schematic spacing)');ax.axis('off')
    ax = fig.add_subplot(grid[1]);ax.set_facecolor('white')
    ax.annotate('', (6.4, 0), (-.5, 0), arrowprops={'arrowstyle': '->', 'lw': 1.5})
    for j, label in [(2, 'Transcritical at 0'), (4, r'Saddle-node at $-\varepsilon^2$')]:
        ax.plot(j, 0, 'o', color='#a3471b', ms=5);ax.text(j, .2, label, ha='center', fontsize=9)
    ax.text(3, -.28, 'No Hopf or periodic-orbit destruction', ha='center', fontsize=9)
    ax.set(xlim=(-.5, 6.5), ylim=(-.55, .65), title=r'$\kappa+\lambda=-1$: decreasing $\lambda$');ax.axis('off')
    ax = fig.add_subplot(grid[2]);ax.set_facecolor('white')
    u = np.linspace(-3.1, 1.1, 900);lam=u*u+2*u
    stable = (u > -1) & (u < 0)
    ax.plot(np.where(stable, lam, np.nan), u, '-', lw=2.4, color='#00679c', label='Stable')
    ax.plot(np.where(~stable, lam, np.nan), u, '--', lw=1.8, color='#a3471b', label='Saddle')
    ax.plot([0, 2.2], [0, 0], color='#00679c', lw=2.4)
    ax.plot([-1.5, 0], [0, 0], '--', color='#a3471b', lw=1.8)
    ax.plot([0, -1], [0, -1], 'ko', ms=4)
    ax.annotate('TC', (0, 0), (.25, -.5), arrowprops={'arrowstyle': '->'}, fontsize=9)
    ax.annotate('SN', (-1, -1), (-1.4, -1.7), arrowprops={'arrowstyle': '->'}, fontsize=9)
    ax.set(xlim=(-1.5, 2.2), ylim=(-3, 1), xlabel=r'$\lambda/\varepsilon^2$', ylabel=r'$v/\varepsilon$', title=r'Local steady branches for $\varepsilon>0$, fixed $\kappa<0$')
    ax.spines[['top', 'right']].set_visible(False);ax.grid(alpha=.15);ax.legend(frameon=False, loc='lower left')
    fig.savefig(Path.cwd()/'paper-60-oscillator-sequences.png', dpi=120,
                facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
