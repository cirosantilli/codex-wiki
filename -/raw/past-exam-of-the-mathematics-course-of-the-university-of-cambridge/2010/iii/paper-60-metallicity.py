"""Compare analytic metallicity distributions; tested with Python 3.14.

Requires the repository's NumPy and Matplotlib versions. Writes an opaque PNG
basename to the caller's working directory, preserving caller MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 5, 801)
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), dpi=120,
                             facecolor='white', constrained_layout=True)
    closed = '#286090'
    infall = '#bf5d19'
    axes[0].plot(x, np.exp(-x), color=closed, label='Closed box')
    axes[0].plot([0, 2, 2, 5], [.5, .5, 0, 0], color=infall,
                 label='Pristine infall: rate = half the star formation rate')
    axes[1].plot(x, 1 - np.exp(-x), color=closed, label='Closed box')
    axes[1].plot(x, np.minimum(x/2, 1), color=infall, label='Half-rate infall')
    axes[0].set_ylabel('Probability density per unit Z/y')
    axes[1].set_ylabel('Cumulative fraction of surviving stars')
    axes[0].set_title('Linear metallicity distribution')
    axes[1].set_title('Cumulative distribution')
    for ax in axes:
        ax.set_facecolor('white')
        ax.set_xlabel('Metallicity / yield, Z/y')
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 1.07)
        ax.grid(alpha=.22)
    axes[0].legend(fontsize=7, loc='upper right')
    axes[1].legend(fontsize=8, loc='lower right')
    fig.suptitle('Same yield; normalized after complete gas exhaustion', fontsize=11)
    fig.savefig('paper-60-metallicity.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
