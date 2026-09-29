"""Mode roots and decay rates; run from _media. Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def roots(zeta):
    """Dimensionless roots λ = r/ω₀ of λ² + 2ζλ + 1 = 0."""
    zeta = np.asarray(zeta, dtype=float)
    d = np.sqrt(zeta**2 - 1 + 0j)
    return -zeta + d, -zeta - d


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white',
                         'axes.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), layout='constrained')
    for zeta, color, label in [(np.linspace(0, 1, 301), '#2467a5', '0 ≤ ζ < 1'),
                               (np.linspace(1, 2, 301), '#27834d', '1 < ζ ≤ 2')]:
        for i, r in enumerate(roots(zeta)):
            assert np.max(np.abs(r*r + 2*zeta*r + 1)) < 1e-12
            axes[0].plot(r.real, r.imag, color=color, lw=2.4,
                         label=label if i == 0 else None)
    for zeta, color in [(0.25, '#2467a5'), (1, '#c13b35'), (2, '#27834d')]:
        a, b = roots(zeta)
        axes[0].scatter([a.real, b.real], [a.imag, b.imag], color=color, s=48, zorder=5)
    axes[0].annotate('ζ = 1: double root', xy=(-1, 0), xytext=(-2.95, 0.62),
                     arrowprops={'arrowstyle': '->'}, fontsize=10)
    axes[0].annotate('ζ = 0.25', xy=(-0.25, np.sqrt(1-0.25**2)),
                     xytext=(-1.55, 1.04), arrowprops={'arrowstyle': '->'}, fontsize=10)
    axes[0].text(-3.55, -0.23, 'ζ = 2: two real roots', fontsize=10)
    axes[0].set(title='Root paths as damping increases', xlim=(-3.95, 0.25),
                ylim=(-1.2, 1.25), xlabel='Real part of r/ω₀', ylabel='Imaginary part of r/ω₀')
    axes[0].axvline(0, color='#666', lw=0.8)
    axes[0].axhline(0, color='#666', lw=0.8)
    axes[0].legend(loc='lower left', fontsize=9)
    zeta = np.linspace(0, 3, 601)
    a, b = roots(zeta)
    for r in [a, b]:
        assert np.max(np.abs(r*r + 2*zeta*r + 1)) < 1e-12
    axes[1].plot(zeta, -b.real, color='#a0a0a0', lw=2.2, label='Fast root: −Re(r₋)/ω₀')
    axes[1].plot(zeta, -a.real, color='#2467a5', lw=2.6, label='Slow root: −Re(r₊)/ω₀')
    axes[1].scatter([1], [1], color='#c13b35', s=50, zorder=5)
    axes[1].axvline(1, color='#c13b35', lw=1, ls='--')
    axes[1].annotate('Largest slow-root decay rate', xy=(1, 1), xytext=(0.2, 2.5),
                     arrowprops={'arrowstyle': '->'}, fontsize=10)
    axes[1].text(1.58, 1.25, 'More damping →\nslower late response', fontsize=10)
    axes[1].set(title='Positive decay rates', xlim=(0, 3), ylim=(0, 6.05),
                xlabel='Damping ratio ζ', ylabel='Decay rate divided by ω₀')
    axes[1].legend(loc='upper left', fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.17)
    fig.suptitle('Ideal mode roots: r/ω₀ = −ζ ± √(ζ² − 1)', fontsize=14)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
