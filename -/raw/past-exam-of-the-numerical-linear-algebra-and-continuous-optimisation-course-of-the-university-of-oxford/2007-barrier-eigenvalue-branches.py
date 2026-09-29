"""Plot an original quadratic-barrier example; write the PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11})
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.3), layout='constrained', facecolor='white')
    x = np.linspace(-.995, .995, 2001)
    for mu, color in [(.8, '#2772aa'), (.2, '#d47222'), (.05, '#218466')]:
        value = -2*x*x-mu*np.log1p(-x*x)
        radius = np.sqrt(1-mu/2)
        minimum = -2*radius*radius-mu*np.log1p(-radius*radius)
        axes[0].plot(x, value, color=color, lw=2, label=rf'$\mu={mu:g}$')
        axes[0].scatter([-radius, radius], [minimum, minimum], color=color, s=25, zorder=4)
    axes[0].scatter([0], [0], color='#333333', s=25, zorder=5)
    axes[0].annotate('The origin stays stationary', (0, 0), xytext=(-.65, 1.1),
                     arrowprops={'arrowstyle': '->', 'color': '#555555'}, fontsize=10)
    axes[0].set(xlabel=r'$x_1$ on the slice $x_2=0$', ylabel=r'$\Psi(x,\mu)$',
                title='Nonzero minimizers move toward the boundary', ylim=(-2.1, 2))
    axes[0].legend(loc='lower center', ncol=3, fontsize=9)
    axes[0].grid(alpha=.2)

    mu = np.logspace(-4, -.5, 300)
    radial = 16*(1-mu/2)/mu
    transverse = np.full_like(mu, 6)
    condition = radial/transverse
    axes[1].loglog(mu, radial, color='#2772aa', lw=2, label='Radial Hessian eigenvalue')
    axes[1].loglog(mu, transverse, color='#218466', lw=2, label='Transverse Hessian eigenvalue')
    axes[1].loglog(mu, condition, '--', color='#d47222', lw=2, label='Spectral condition number')
    axes[1].set(xlabel=r'Barrier parameter $\mu$', ylabel='Magnitude',
                title='The minimum converges while conditioning worsens')
    axes[1].legend(fontsize=9)
    axes[1].grid(alpha=.2, which='both')
    fig.suptitle(r'Original example: $A=\operatorname{diag}(-2,1)$, unit-ball logarithmic barrier', fontsize=14)
    fig.savefig(Path.cwd()/'2007-barrier-eigenvalue-branches.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
