"""Cold ideal electron pressure; Python 3.14, NumPy and Matplotlib per pyproject.toml.

Emit the matching opaque PNG in the current directory. Gauss-Legendre quadrature
avoids cancellation in the closed antiderivative near the nonrelativistic limit.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def pressure_integral(x):
    """I(x) = integral_0^x t^4 / sqrt(1+t^2) dt, for positive x."""
    x = np.asarray(x, dtype=float)
    nodes, weights = np.polynomial.legendre.leggauss(160)
    u = (nodes + 1) / 2
    return x**5 * np.sum(weights * u**4 / np.sqrt(1 + (x[..., None] * u)**2), axis=-1) / 2


def main():
    x = np.geomspace(0.01, 100, 700)
    integral = pressure_integral(x)
    gamma = x**5 / (3 * np.sqrt(1 + x*x) * integral)
    assert np.all(np.diff(gamma) < 0)
    assert abs(pressure_integral(0.001) / (0.001**5 / 5) - 1) < 4e-7
    assert abs(pressure_integral(1000) / (1000**4 / 4) - 1) < 2e-6
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained')
    fig.set_facecolor('white')
    left.loglog(x, integral, color='#194c83', lw=2.6, label='Exact ideal-gas integral')
    left.loglog(x, x**5 / 5, '--', color='#c46721', label=r'Nonrelativistic: $x^5/5$')
    left.loglog(x, x**4 / 4, ':', color='#488344', lw=2, label=r'Ultrarelativistic: $x^4/4$')
    left.set(xlabel=r'$x=p_F/(m_e c)$', ylabel=r'$P/P_*=I(x)$', title='Pressure crosses between two powers')
    left.legend(loc='upper left', fontsize=9)
    right.semilogx(x, gamma, color='#194c83', lw=2.6)
    right.axhline(5/3, color='#c46721', ls='--', label=r'$5/3$: nonrelativistic')
    right.axhline(4/3, color='#488344', ls=':', lw=2, label=r'$4/3$: ultrarelativistic')
    right.set(xlabel=r'$x=p_F/(m_e c)$', ylabel=r'$d\ln P/d\ln\rho$ at fixed composition', ylim=(1.30, 1.70), title='Compression becomes less effective')
    right.set_yticks([4/3, 1.5, 5/3], [r'$4/3$', '1.5', r'$5/3$'])
    right.legend(loc='upper right', fontsize=9)
    for ax in (left, right):
        ax.axvline(1, color='0.65', lw=1)
        ax.grid(alpha=0.18)
    fig.suptitle('White-dwarf support: cold, noninteracting electrons', fontsize=14)
    fig.savefig(Path(__file__).stem + '.png', dpi=125, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
