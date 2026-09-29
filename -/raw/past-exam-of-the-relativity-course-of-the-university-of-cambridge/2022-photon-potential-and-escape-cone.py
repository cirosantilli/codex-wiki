"""Plot dimensionless Schwarzschild photon results; output PNG to cwd."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2), facecolor='white', layout='constrained')
    x = np.linspace(2, 13, 900)
    potential = (1 - 2 / x) / x**2
    ax = axes[0]
    ax.plot(x, potential, color='#24699b', lw=2)
    ax.plot(3, 1 / 27, 'o', color='#b95629')
    ax.axvline(3, color='#b95629', ls=':', lw=1)
    ax.annotate(r'Unstable circular orbit: $r=3\mu$', xy=(3, 1 / 27),
                xytext=(4.1, 0.0325), arrowprops={'arrowstyle': '->'}, fontsize=9)
    ax.set(xlabel=r'$r/\mu$', ylabel=r'$2\mu^2V_{\rm eff}/h^2$',
           xlim=(2, 13), ylim=(0, .043), title='Exterior radial potential')
    ax.text(2.1, .003, 'Horizon', fontsize=9)
    ax.set_xticks([2, 3, 5, 7, 9, 11, 13])

    x = np.linspace(2, 3, 600)
    half_angle = np.rad2deg(np.arcsin(np.clip(3 * np.sqrt(3) / x * np.sqrt(1 - 2 / x), 0, 1)))
    ax = axes[1]
    ax.fill_between(x, 0, half_angle, color='#d5e8f4', label='Escaping outward directions')
    ax.plot(x, half_angle, '--', color='#24699b', lw=2, label='Critical ray: does not escape')
    ax.scatter([2, 3], [0, 90], facecolors='white', edgecolors='#24699b', zorder=5)
    ax.set(xlabel=r'$r/\mu$', ylabel=r'Local angle $\alpha$ (degrees)',
           xlim=(2, 3), ylim=(0, 93), title='Escape cone for a static observer')
    ax.set_yticks([0, 15, 30, 45, 60, 75, 90])
    ax.text(2.03, 83, 'Horizon endpoint is an exterior limit', fontsize=8.5)
    ax.legend(loc='lower right', fontsize=8, framealpha=0.95)
    for ax in axes:
        ax.set_facecolor('white')
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(alpha=.2)
    fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
                dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
