"""Plot the signed Legendre kernel; Python 3.14, root NumPy/Matplotlib deps.

Write paper-31-moment-cancellation.png to the caller's current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    u = np.linspace(-1, 1, 1201)
    kernel = (9 - 15 * u**2) / 8
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white', 'savefig.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.5), constrained_layout=True)
    for ax, values, title in zip(
        axes, [kernel, u**2 * kernel],
        [r'Kernel: $\int K(u)\,du=1$',
         r'Second moment: $\int u^2K(u)\,du=0$'],
    ):
        ax.axhline(0, color='#555555', linewidth=0.8)
        ax.fill_between(u, 0, values, where=values >= 0, color='#3577b7', alpha=0.28)
        ax.fill_between(u, 0, values, where=values <= 0, color='#bf5c39', alpha=0.3)
        ax.plot(u, values, color='#253d55', linewidth=1.8)
        ax.plot([-1.17, -1], [0, 0], color='#253d55', linewidth=1.8)
        ax.plot([1, 1.17], [0, 0], color='#253d55', linewidth=1.8)
        ax.set(xlabel='$u$', title=title, xlim=(-1.17, 1.17))
        ax.set_xticks([-1, -0.5, 0, 0.5, 1])
        ax.grid(axis='y', alpha=0.15)
    axes[0].set_ylabel('$K(u)$')
    axes[1].set_ylabel('$u^2K(u)$')
    fig.savefig(Path('paper-31-moment-cancellation.png'), dpi=150, transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
