"""Generate a schematic turbulent pair-separation plot in the working directory."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # Units: viscous length eta=1 and viscous time tau_eta=1.
    # Illustrative constants and scale ratio, rather than simulation data.
    initial, outer = 0.02, 20.0
    first = np.log(1.0 / initial)
    second = first + outer ** (2.0 / 3.0) - 1.0
    a = np.linspace(0, first, 200)
    b = np.linspace(first, second, 240)
    c = np.linspace(second, second + 22, 240)
    lengths = [initial * np.exp(a), (1 + b - first) ** 1.5,
               np.sqrt(outer**2 + outer ** (4.0 / 3.0) * (c - second))]
    colors = ['#4169a8', '#c26925', '#39885c']
    fig, ax = plt.subplots(figsize=(8.0, 4.6), dpi=120, facecolor='white')
    for times, distance, color in zip([a, b, c], lengths, colors):
        ax.plot(times, distance, lw=2.7, color=color)
    ax.set_yscale('log')
    ax.set_ylim(initial / 1.5, 110)
    ax.set_xlim(0, c[-1])
    for time in [first, second]:
        ax.axvline(time, color='#888888', ls=':', lw=1)
    for distance in [1, outer]:
        ax.axhline(distance, color='#bbbbbb', ls='--', lw=.9)
    ax.set_yticks([initial, .1, 1, outer, 100],
                 [r'$l_0$', '0.1', r'$\eta$', r'$L$', '100'])
    ax.set_xticks([0, first, second, 20, 30], ['0', r'$t_1$', r'$t_2$', '20', '30'])
    ax.text(.7, .2, 'Smooth-flow stretching\n'+r'$l\sim l_0e^{\lambda t}$',
            fontsize=10, color=colors[0])
    ax.text(first + .6, 2.6, 'Inertial-range separation\n'+r'$l^2\sim\epsilon(t-t_1)^3$',
            fontsize=10, color=colors[1])
    ax.text(second + 9, 7.0, 'Large-scale diffusion\n'+r'$l^2\sim UL(t-t_2)$',
            fontsize=10, color=colors[2])
    ax.set_title('Three regimes of turbulent pair separation', fontsize=13, pad=12)
    ax.set_xlabel(r'Time in units of $\tau_\eta$')
    ax.set_ylabel(r'Separation in units of $\eta$ (logarithmic scale)')
    ax.spines[['top', 'right']].set_visible(False)
    fig.text(.5, .015, 'Schematic continuous matching; coefficients and scale ratio are illustrative.',
             ha='center', fontsize=9, color='#555555')
    fig.tight_layout(rect=(0, .055, 1, 1))
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
