"""Plot a calculated cissoid, circle and tangent; write the PNG to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(6.1, 5.8), layout='constrained')
    t = np.linspace(-4, 4, 1601)
    x, y = 2*t*t/(1+t*t), 2*t**3/(1+t*t)
    ax.plot(x, y, color='#1764ab', lw=2.5, label='cissoid')
    theta = np.linspace(0, 2*np.pi, 601)
    ax.plot(1+np.cos(theta), np.sin(theta), color='#b14928', lw=1.7, label='circle')
    ax.axvline(2, color='#555555', lw=1.4, linestyle='--', label='tangent / asymptote')
    ax.scatter([0, 1, 1], [0, 1, -1], color='#333333', s=24, zorder=4)
    ax.annotate('cusp', (0, 0), xytext=(-.62, .38),
                arrowprops={'arrowstyle': '->', 'color': '#555555'})
    ax.annotate('$(1,1)$', (1, 1), xytext=(8, -15), textcoords='offset points')
    ax.annotate('$(1,-1)$', (1, -1), xytext=(8, 8), textcoords='offset points')
    ax.axhline(0, color='#999999', linewidth=.7)
    ax.set(aspect='equal', xlim=(-.75, 2.6), ylim=(-2.8, 2.8), xlabel='$x$', ylabel='$y$',
           title=r'$y^2(2-x)=x^3$')
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(alpha=.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
