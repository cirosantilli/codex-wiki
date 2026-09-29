"""Render derived radiation–Lambda turning points and the critical scale factor.

Output is paper-1-radiation-lambda.png in the caller's current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'savefig.facecolor': 'white'})
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.9), layout='constrained')
    x = np.linspace(0, 4.5, 700)
    for beta, color in [(5, '#2563a7'), (4, '#ae392a')]:
        axes[0].plot(x, x*x-beta*x+beta, color=color, label=fr'$\beta={beta}$')
        axes[1].plot(x, beta*(x-2), color=color, label=fr'$\beta={beta}$')
    xm = (5-np.sqrt(5))/2
    xp = (5+np.sqrt(5))/2
    axes[0].axvspan(xm, xp, color='#2563a7', alpha=.1)
    axes[0].annotate('turnaround', (xm, 0), (.15, -2.5),
                     arrowprops={'arrowstyle': '->', 'color': '#333333'})
    axes[0].scatter([xm, xp, 2], [0, 0, 0], s=24, c=['#2563a7', '#2563a7', '#ae392a'], zorder=3)
    axes[0].set(title='Allowed expansion and turning points', xlabel=r'$x=a^2$',
                ylabel=r'$a^4H^2/H_0^2$', ylim=(-3, 7))
    axes[1].set(title='Sign of the Hubble derivative', xlabel=r'$x=a^2$',
                ylabel=r'$a^4\dot H/H_0^2$')
    for ax in axes[:2]:
        ax.axhline(0, color='#777777', lw=.8)
        ax.axvline(2, color='#888888', lw=.8, ls=':')
        ax.legend(frameon=False, loc='upper right')
    tau = np.linspace(0, 3.5, 700)
    axes[2].plot(tau, np.sqrt(2*(1-np.exp(-2*tau))), color='#ae392a', lw=2)
    axes[2].axhline(np.sqrt(2), color='#777777', ls='--', lw=1)
    axes[2].text(1.45, 1.46, r'$a\to\sqrt{2}$', color='#555555')
    axes[2].set(title=r'Critical universe: $\beta=4$', xlabel=r'$H_0t$',
                ylabel=r'$a(t)$', ylim=(0, 1.6))
    fig.savefig(Path('paper-1-radiation-lambda.png'), dpi=100, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
