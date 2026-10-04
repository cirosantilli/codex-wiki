"""Original lossless-layer calculation; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes the same-basename opaque PNG to caller CWD; preserves supplied MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def layer_matrix(delta, impedance):
    c, s = np.cos(delta), np.sin(delta)
    m = np.empty((len(delta), 2, 2), dtype=complex)
    m[:, 0, 0] = m[:, 1, 1] = c
    m[:, 0, 1] = 1j * s / impedance
    m[:, 1, 0] = 1j * impedance * s
    return m


def transmission(nu, count):
    delta = np.pi * nu / 2
    cell = layer_matrix(delta, 1) @ layer_matrix(delta, 4)
    total = np.linalg.matrix_power(cell, count)
    denominator = total[:, 0, 0] + total[:, 1, 1] - total[:, 0, 1] - total[:, 1, 0]
    return np.abs(2 / denominator) ** 2


def main():
    edge = 2 * np.arcsin(0.8) / np.pi
    nu = np.unique(np.r_[np.linspace(0, 2, 4001), edge, 2 - edge, 1])
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.3), layout='constrained', facecolor='white')
    ax = axes[0]
    ax.axvspan(edge, 2 - edge, color='0.5', alpha=0.12, label='Infinite-cell stop band')
    for count in [1, 4, 8]:
        ax.semilogy(nu, transmission(nu, count), label=f'{count} cell(s)')
    ax.set(xlabel=r'$\nu=2\omega\tau/\pi$', ylabel='Transmitted energy fraction',
           title='Quarter-wave cells: impedance ratio 4', xlim=(0, 2), ylim=(5e-10, 1.3))
    ax.grid(alpha=0.2)
    ax.legend(fontsize=8, loc='lower left')
    n = np.arange(7)
    axes[1].stem(2 * n + 1, 0.64 * 0.36 ** n, basefmt='k-')
    axes[1].set(xlabel=r'Arrival time / slab one-way time $\tau$',
                ylabel='Transmitted velocity impulse coefficient',
                title='One slab: delayed transmitted multiples', xlim=(0, 14), ylim=(0, 0.7))
    axes[1].grid(alpha=0.2)
    axes[1].text(3.5, 0.53, r'$a_n=0.64(0.36)^n$' + '\n' + r'$t_n=(2n+1)\tau$', fontsize=11)
    fig.savefig(Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
