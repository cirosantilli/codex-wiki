"""Original Argand plot of the two quadratic root paths; output to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, ax = plt.subplots(figsize=(6.2, 5.1), layout='constrained')
    b = np.linspace(-1, 1, 601)
    for sign, color, label in [(1, '#1764ab', '$z_+$'), (-1, '#b14928', '$z_-$')]:
        y = sign*np.sqrt(1-b*b)
        ax.plot(-b, y, color=color, linewidth=2.4, label=label)
        for j in [160, 390]:
            ax.annotate('', xy=(-b[j+28], y[j+28]), xytext=(-b[j], y[j]),
                        arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 2})
    ax.axhline(0, color='#888888', linewidth=.8)
    ax.axvline(0, color='#888888', linewidth=.8)
    ax.scatter([1, -1, 0, 0], [0, 0, 1, -1], color='#333333', s=24, zorder=4)
    ax.annotate('$b=-1$', (1, 0), xytext=(5, 12), textcoords='offset points')
    ax.annotate('$b=1$', (-1, 0), xytext=(-41, 12), textcoords='offset points')
    ax.annotate('$b=0$', (0, 1), xytext=(8, 9), textcoords='offset points')
    ax.annotate('$b=0$', (0, -1), xytext=(8, -18), textcoords='offset points')
    ax.set(aspect='equal', xlim=(-1.43, 1.43), ylim=(-1.34, 1.34),
           xlabel=r'$\operatorname{Re}z$', ylabel=r'$\operatorname{Im}z$',
           title=r'$z_\pm=-b\pm i\sqrt{1-b^2}$; arrows: increasing $b$')
    ax.legend(loc='lower left')
    ax.grid(alpha=.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
