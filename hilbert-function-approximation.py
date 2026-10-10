"""Show the L2 projection of x squared onto affine functions; save to cwd."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12})
    x = np.linspace(-1, 1, 1201)
    f = x*x
    projected = np.full_like(x, 1/3)
    squared_error = np.trapezoid((f-projected)**2, x)
    assert np.isclose(squared_error, 8/45, atol=2e-6)
    assert abs(np.trapezoid(f-projected, x)) < 1e-6
    assert abs(np.trapezoid(x*(f-projected), x)) < 1e-12
    fig, axes = plt.subplots(1, 2, figsize=(11.3, 5.2), layout='constrained', facecolor='white')
    axes[0].plot(x, f, color='#2772aa', lw=2.5, label=r'$f(x)=x^2$')
    axes[0].plot(x, projected, color='#d47222', lw=2.5, label=r'$Pf(x)=1/3$')
    axes[0].fill_between(x, f, projected, color='#b3c7d8', alpha=.45, label='Residual gap')
    axes[0].set(xlabel='x', ylabel='Function value', ylim=(-.06, 1.1),
                title='The best affine approximation is constant')
    axes[0].legend(loc='upper center', fontsize=10)
    axes[0].grid(alpha=.2)
    axes[0].text(0, .66, r'$\langle x^2-1/3,1\rangle=0$'+'\n'+r'$\langle x^2-1/3,x\rangle=0$',
                 ha='center', fontsize=12)

    a = np.linspace(-.25, .95, 151)
    b = np.linspace(-1, 1, 151)
    aa, bb = np.meshgrid(a, b)
    error = 8/45+2*(aa-1/3)**2+(2/3)*bb*bb
    contours = axes[1].contour(aa, bb, error, levels=[.2, .3, .5, .8, 1.2],
                               colors=['#238366', '#318fb0', '#4879a4', '#926bb0', '#bc653b'])
    axes[1].clabel(contours, fontsize=10)
    axes[1].scatter([1/3], [0], color='#d47222', zorder=4)
    axes[1].annotate('Minimum = 8/45', (1/3, 0), xytext=(.1, .5),
                     arrowprops={'arrowstyle': '->'}, fontsize=11)
    axes[1].set(xlabel='Constant coefficient a', ylabel='Linear coefficient b',
                title=r'Integrated squared error for candidate $a+bx$')
    axes[1].grid(alpha=.15)
    fig.suptitle('Function approximation uses the same geometry as vector projection', fontsize=15)
    fig.savefig(Path.cwd() / 'hilbert-function-approximation.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
