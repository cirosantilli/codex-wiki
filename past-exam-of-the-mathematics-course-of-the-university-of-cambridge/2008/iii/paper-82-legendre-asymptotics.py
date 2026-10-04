"""Legendre endpoint sketch. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes paper-82-legendre-asymptotics.png to caller CWD; preserves MPLCONFIGDIR.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.gettempdir() + '/codex-wiki-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def legendre(n, x):
    coefficients = np.zeros(n + 1)
    coefficients[n] = 1
    return np.polynomial.legendre.legval(x, coefficients)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    x = np.linspace(1, 1.08, 700)
    for n in (20, 40, 80):
        axes[0].semilogy(x, legendre(n, x), label=f'n = {n}')
    axes[0].set(xlabel='x', ylabel=r'$P_n(x)$ (logarithmic scale)', title='Steep rise from the fixed endpoint value')
    axes[0].scatter([1], [1], color='black', s=20, zorder=5)
    axes[0].legend()
    nu = np.linspace(0, 8, 500)
    axes[1].plot(nu, np.i0(np.sqrt(2 * nu)), 'k--', lw=2.5, label=r'$I_0(\sqrt{2\nu})$')
    for n in (10, 30, 100):
        axes[1].plot(nu, legendre(n, 1 + nu / n**2), lw=1.5, label=f'n = {n}')
    axes[1].set(xlabel=r'$\nu=n^2(x-1)$', ylabel=r'$P_n(1+\nu/n^2)$', title='Endpoint layer on its natural scale')
    axes[1].legend()
    for ax in axes:
        ax.grid(alpha=.25)
    fig.savefig('paper-82-legendre-asymptotics.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
