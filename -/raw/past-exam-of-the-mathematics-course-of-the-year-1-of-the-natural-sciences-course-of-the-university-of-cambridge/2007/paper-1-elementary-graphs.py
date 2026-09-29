"""Plot the elementary functions in the original 2007 IA1 solutions.

Run from the output directory; the PNG is written to the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.0), layout='constrained')
    ax = axes[0]
    x = np.linspace(0, np.pi, 501)
    ax.plot(x, np.cos(x)**2, color='#1764ab', linewidth=2.5)
    ax.scatter([0, np.pi/2, np.pi], [1, 0, 1], color='#1764ab', zorder=4)
    ax.set(xticks=[0, np.pi/2, np.pi], xticklabels=['0', r'$\pi/2$', r'$\pi$'],
           yticks=[0, .5, 1], xlabel='$x$', ylabel='$y$', title=r'$y=\cos^2x$',
           xlim=(-.08, np.pi+.08), ylim=(-.1, 1.15))
    ax.grid(alpha=.2)
    ax = axes[1]
    for start, end in [(-5, -.035), (.035, 5)]:
        x = np.linspace(start, end, 700)
        ax.plot(x, -1/np.expm1(x), color='#a33c24', linewidth=2.5)
    ax.axvline(0, color='#555555', linestyle='--', linewidth=1)
    ax.axhline(1, color='#555555', linestyle='--', linewidth=1)
    ax.axhline(0, color='#555555', linestyle='--', linewidth=1)
    ax.annotate(r'$y\to1$', xy=(-4.3, 1), xytext=(-4.3, 1.65))
    ax.annotate(r'$y\to0^-$', xy=(3.0, 0), xytext=(2.5, -.85))
    ax.set(xlim=(-5, 5), ylim=(-4, 5), xlabel='$x$', ylabel='$y$', title=r'$y=1/(1-e^x)$')
    ax.grid(alpha=.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
