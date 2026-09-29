"""Phase of forced QG edge waves; tested with Python 3.14.4.

Dependencies: numpy 2.3.5, matplotlib 3.10.7 (root pyproject.toml).
Write only a PNG basename to the caller's CWD; preserve MPLCONFIGDIR.
Curves are normalized for positive f, epsilon, U0, k and t.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 2*np.pi, 801)
    fig, axes = plt.subplots(2, 1, figsize=(9, 5.5), sharex=True, facecolor='white')
    profiles = [(-np.sin(x), 'Steady response: velocity is in quadrature'),
                (-np.cos(x), 'Resonant response: velocity opposes topography')]
    for ax, (velocity, title) in zip(axes, profiles):
        ax.set_facecolor('white')
        ax.plot(x, np.cos(x), color='black', lw=2, label='Normalized topography')
        ax.plot(x, velocity, color='tab:blue', lw=2, label='Normalized meridional velocity')
        ax.axhline(0, color='0.7', lw=0.8)
        for knot in np.arange(5)*np.pi/2:
            ax.axvline(knot, color='0.85', lw=0.7)
        ax.set(ylim=(-1.25, 1.25), xlim=(0, 2*np.pi), ylabel='Normalized amplitude', title=title)
        ax.legend(loc='upper right', fontsize=9)
    axes[-1].set_xticks(np.arange(5)*np.pi/2,
                       ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    axes[-1].set_xlabel(r'$kx$ along $y=0$')
    fig.tight_layout()
    fig.savefig('paper-77-topographic-phases.png', dpi=130, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
