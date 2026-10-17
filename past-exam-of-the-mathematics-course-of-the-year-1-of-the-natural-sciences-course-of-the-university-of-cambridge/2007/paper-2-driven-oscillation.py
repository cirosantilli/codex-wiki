"""Calculate the full driven solution and its transient; PNG output to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    fig, axes = plt.subplots(2, 1, figsize=(8.8, 5.5), sharex=True, layout='constrained',
                             gridspec_kw={'height_ratios': [2, 1]})
    x = np.linspace(0, 5, 1601)
    steady = np.sin(5*x)
    transient = -1.25*np.exp(-3*x)*np.sin(4*x)
    axes[0].plot(x, steady+transient, lw=2.3, color='#1764ab', label='full solution')
    axes[0].plot(x, steady, '--', lw=1.3, color='#b14928', label='steady sine')
    axes[0].scatter([0], [0], color='#1764ab', s=20, zorder=4)
    axes[0].set(ylabel='$y$', title=r'$y=\sin5x-\frac{5}{4}e^{-3x}\sin4x$')
    axes[0].legend(loc='upper right', ncol=2)
    axes[1].plot(x, transient, color='#664799', linewidth=2)
    axes[1].plot(x, 1.25*np.exp(-3*x), ':', color='#888888', lw=1)
    axes[1].plot(x, -1.25*np.exp(-3*x), ':', color='#888888', lw=1)
    axes[1].set(xlabel='$x$', ylabel='transient', ylim=(-.62, .62), xlim=(0, 5))
    for ax in axes:
        ax.axhline(0, color='#888888', linewidth=.7)
        ax.grid(alpha=.18)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
