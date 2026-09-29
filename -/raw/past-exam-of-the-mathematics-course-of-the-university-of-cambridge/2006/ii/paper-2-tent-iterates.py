"""Tent-map iterates; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Write PNG basename to caller CWD; preserve MPLCONFIGDIR.
Include all exact piecewise-linear knots and marked preimages.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def tent(x, mu):
    return mu*np.minimum(x, 1-x)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.2), facecolor='white')
    for ax, mu in zip(axes, [1.3, 1.6]):
        x0 = mu/(mu+1)
        xm1 = 1/(mu+1)
        xm2 = 1-1/(mu*(mu+1))
        knots = [0, 1, 0.5, 1/(2*mu), 1-1/(2*mu), xm1, xm2, x0]
        x = np.unique(np.r_[np.linspace(0, 1, 601), knots])
        ax.set_facecolor('white')
        ax.plot(x, tent(x, mu), lw=2, label=r'$F$')
        ax.plot(x, tent(tent(x, mu), mu), lw=2, label=r'$F^2$')
        ax.plot([0, 1], [0, 1], color='0.7', lw=1)
        for point, label in [(xm1, r'$x_{-1}$'), (x0, r'$x_0$'), (xm2, r'$x_{-2}$')]:
            ax.axvline(point, color='0.7', lw=0.8, ls=':')
            ax.text(point, -0.085, label, ha='center', fontsize=10)
        ax.set(xlim=(0, 1), ylim=(0, 1), xlabel=r'$x$', ylabel='Map value', title=rf'$\mu={mu}$')
        ax.legend(loc='upper left')
    fig.tight_layout()
    fig.savefig('paper-2-tent-iterates.png', dpi=135, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
