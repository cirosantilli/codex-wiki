"""Draw an original phase-potential model. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.

Run from _media; writes this script's basename.png to the current directory.
The horizontal levels are harmonic approximations, not computed resonances.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def main():
    h = 6.62607015e-34
    e = 1.602176634e-19
    hb = h / (2 * np.pi)
    ic, cap, s = 1e-6, 4e-12, 0.9
    ej = hb * ic / (2 * e)
    pm, pb = np.arcsin(s), np.pi - np.arcsin(s)
    wp = np.sqrt(2 * e * ic / (hb * cap)) * (1 - s * s) ** 0.25
    barrier = 2 * (np.sqrt(1 - s * s) - s * np.arccos(s))

    def potential(phi):
        return -np.cos(phi) - s * phi + np.cos(pm) + s * pm

    def root(left, right, level):
        for _ in range(70):
            middle = (left + right) / 2
            if (potential(left) - level) * (potential(middle) - level) > 0:
                left = middle
            else:
                right = middle
        return (left + right) / 2

    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(10, 6), dpi=100, facecolor='white')
    ax = fig.add_axes([0.09, 0.19, 0.64, 0.66])
    phi = np.linspace(0.45, 2.85, 1600)
    ax.plot(phi, potential(phi), color='#263b51', lw=2.6)
    ax.axhline(0, color='#aaaaaa', lw=0.8)
    ax.plot(pm, 0, 'o', color='#263b51')
    colors = ['#1565a8', '#267f9b', '#4d9486']
    for n, color in enumerate(colors):
        level = (n + 0.5) * hb * wp / ej
        left, right = root(0.45, pm, level), root(pm, pb, level)
        ax.plot([left, right], [level, level], color=color, lw=2.2)
        ax.text(left - 0.04, level, f'n = {n}', ha='right', va='center', color=color)
    lev0 = 0.5 * hb * wp / ej
    inside, outside = root(pm, pb, lev0), root(pb, 2.85, lev0)
    ax.annotate('', (outside, lev0), (inside, lev0),
                arrowprops={'arrowstyle': '->', 'color': '#1565a8', 'lw': 2,
                            'linestyle': '--'})
    ax.annotate('Tunnelling through phase barrier', (2.19, lev0), (1.65, -0.023),
                ha='center', color='#1565a8', fontsize=11,
                arrowprops={'arrowstyle': '-', 'color': '#1565a8'})
    ax.add_patch(FancyArrowPatch((pm + 0.06, 0.023), (pb + 0.22, 0.042),
                 connectionstyle='arc3,rad=-0.95', arrowstyle='->',
                 mutation_scale=15, lw=2, color='#b66c1e'))
    ax.text(1.71, 0.095, 'Thermal activation over barrier', color='#a05a0f',
            ha='center', fontsize=11)
    ax.plot([pb, pb], [0, barrier], ':', color='#7a7a7a', lw=1)
    ax.annotate('', (2.48, barrier), (2.48, 0),
                arrowprops={'arrowstyle': '<->', 'color': '#555555'})
    ax.text(2.52, barrier / 2, r'$\Delta U$', va='center')
    ax.text(pm, -0.008, r'$\phi_m$', ha='center')
    ax.text(pb, barrier + 0.003, r'$\phi_b$', ha='center')
    ax.set(xlim=(0.45, 2.85), ylim=(-0.029, 0.108),
           xlabel=r'Collective phase $\phi$ (radians)',
           ylabel=r'$[U(\phi)-U(\phi_m)]/E_J$')
    ax.set_yticks([0, .02, .04, .06, .08])
    ax.grid(axis='y', alpha=0.16)
    side = fig.add_axes([0.77, 0.23, 0.22, 0.56]); side.axis('off')
    side.text(0, 1, 'CHOSEN CIRCUIT', weight='bold', fontsize=11, va='top')
    side.text(0, .89, '$I_c = 1$ μA\n$C = 4$ pF\n$I_b/I_c = 0.90$', va='top', linespacing=1.8)
    side.text(0, .56, 'Barrier / h\n29.767 GHz\n\nOscillation frequency\n2.89608 GHz',
              va='top', linespacing=1.4, fontsize=11)
    side.text(0, .16, 'Harmonic references\n' + r'$E_n-U_m=(n+1/2)\hbar\omega_p$' + '\n\nNot exact resonances',
              va='top', linespacing=1.5, fontsize=10)
    fig.suptitle('A circuit phase can be trapped and can escape', y=.96, fontsize=17)
    fig.text(.5, .035, 'Original model • horizontal coordinate is phase, not distance through the insulator',
             ha='center', color='#555555', fontsize=11)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
