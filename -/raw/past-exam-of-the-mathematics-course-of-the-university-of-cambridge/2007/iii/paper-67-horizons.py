"""Draw the requested horizons. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Writes paper-67-horizons.png to the caller's CWD; honors MPLCONFIGDIR.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def lcdm_horizon(z):
    """Return (H0*Omega_m/c) r_h using Gaussian quadrature after v=w^-2."""
    z = np.asarray(z, dtype=float)
    if np.any(z <= -1):
        raise ValueError('Use z > -1; the limiting value is computed separately.')
    nodes, weights = np.polynomial.legendre.leggauss(160)
    upper = 1 / np.sqrt(1 + z)
    w = upper[..., None] * (nodes + 1) / 2
    return .3 * upper * np.sum(weights / np.sqrt(.3 + .7 * w**6), axis=-1)


def limiting_horizon():
    return .3 * .3**(-1/3) * .7**(-1/6) * math.gamma(1/3) * math.gamma(1/6) / (3 * math.sqrt(math.pi))


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
    z = np.concatenate((np.linspace(-.999, -.94, 100), np.linspace(-.94, 2, 600)))
    fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
    ax.plot(z, 2 / np.sqrt(1 + z), color='#2563a6', lw=2.5, label='Einstein–de Sitter: matter = 1, vacuum = 0')
    ax.plot(z, lcdm_horizon(z), color='#cc6b16', lw=2.5, label='Matter = 0.3, vacuum = 0.7')
    limit = limiting_horizon()
    ax.plot([-1], [limit], 'o', color='#cc6b16', clip_on=False)
    ax.axhline(limit, color='#cc6b16', linestyle=':', alpha=.65)
    ax.annotate(f'Finite future limit: {limit:.3f}', xy=(-1, limit), xytext=(-.45, 2.8), arrowprops={'arrowstyle': '->', 'color': '#cc6b16'}, color='#a6530c')
    ax.annotate('Diverges as z → −1', xy=(-.93, 7.56), xytext=(-.36, 6.5), arrowprops={'arrowstyle': '->', 'color': '#2563a6'}, color='#2563a6')
    ax.set(xlim=(-1, 2), ylim=(0, 8), xlabel='Redshift z  (cosmic time increases to the left)', ylabel=r'$R=(H_0\Omega_{m,0}/c)\,r_h$', title=r'Comoving particle horizons: common $H_0\Omega_{m,0}$')
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(alpha=.22)
    fig.savefig(Path.cwd() / 'paper-67-horizons.png', dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
