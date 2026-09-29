"""Plot the reduced one-loop magnetic integral; Python 3.14, NumPy 2.3.5, matplotlib 3.10.7.

Composite Gauss-Legendre quadrature resolves the narrowing endpoint region.
This illustrates a projected QED integral, not the full vertex calculation.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.legendre import leggauss


def integrand(x, r):
    return 2 * x * (1 - x) ** 2 / ((1 - x) ** 2 + x * r ** 2)


def integral(r, order=48):
    nodes, weights = leggauss(order)
    edges = np.unique(np.r_[0., 1 - np.logspace(0, -9, 37), 1.])
    mid = (edges[:-1] + edges[1:]) / 2
    half = np.diff(edges) / 2
    x = mid[:, None] + half[:, None] * nodes
    return float(np.sum(half[:, None] * weights * integrand(x, r)))


def main():
    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.6), facecolor='white', layout='constrained')
    x = np.linspace(0, 1, 1400)
    colors = ['#176591', '#b55b1b', '#7a4b91']
    for r, color in zip([1, .1, .01], colors):
        axes[0].plot(x, integrand(x, r), label=f'r = {r:g}', lw=2, color=color)
    axes[0].plot(x, 2 * x, '--', color='#28323c', lw=1.5, label=r'$2x$: zero-regulator limit')
    axes[0].set(xlabel='Feynman parameter x', ylabel=r'$f_r(x)$', title='Endpoint suppression narrows', xlim=(0, 1), ylim=(0, 2.08))
    axes[0].legend(loc='upper left', fontsize=10)
    ratios = np.logspace(-5, 1, 180)
    values = np.array([integral(r) for r in ratios])
    axes[1].semilogx(ratios, values, color='#176591', lw=2.5)
    axes[1].axhline(1, ls='--', color='#28323c', lw=1.5)
    for r, color in zip([1, .1, .01], colors):
        y = integral(r)
        axes[1].plot(r, y, 'o', color=color)
        axes[1].annotate(f'{y:.4f}', (r, y), xytext=(7, -17 if r < 1 else 8), textcoords='offset points', color=color, fontsize=10)
    axes[1].set(xlabel=r'Auxiliary mass ratio $r=\lambda/m$', ylabel=r'$I(r)=F_2^{(1)}(0;\lambda)/(\alpha/2\pi)$', title='The integral tends to one', ylim=(0, 1.08))
    axes[1].text(1.5e-5, .12, 'Smaller regulator  ←', color='#28323c')
    fig.suptitle(r'$I(r)=\int_0^1\frac{2x(1-x)^2}{(1-x)^2+xr^2}\,dx$', fontsize=20)
    fig.supxlabel('Auxiliary regulator values; no experimental points or physical photon-mass claim', fontsize=11)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
