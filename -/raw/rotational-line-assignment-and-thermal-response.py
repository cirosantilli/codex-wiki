"""Stipulated spectra, independently computed fits, and rigid-rotor thermal response.

Python 3.14; numpy 2.3.5; matplotlib 3.10.7. Run from _media.
No measured data. Integrated absorption is not a pulsed FTMW peak amplitude.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

H = 6.62607015e-34
KB = 1.380649e-23
B = 5e9  # Hz
D = 2e3  # Hz; used for positions only


def frequency(m):
    return 2 * B * m - 4 * D * m**3


def thermal_response(temperature, cutoff=160):
    j = np.arange(cutoff + 1)
    weight = np.exp(-H * B * j * (j + 1) / (KB * temperature))
    q = np.sum((2 * j + 1) * weight)
    population = (2 * j + 1) * weight / q
    # Sum over M of |<J+1,M|cos(theta)|J,M>|^2 = (J+1)/3.
    # Net absorption subtracts stimulated emission per substate, then
    # multiplies by photon energy. J-independent constants cancel.
    nu = 2 * B * (j[:-1] + 1)
    area = nu * (j[:-1] + 1) * (weight[:-1] - weight[1:]) / q
    return j, population, area / area.max()


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, axes = plt.subplots(2, 2, figsize=(11, 8.5), layout='constrained')
    fig.suptitle('Synthetic line assignment and thermal response\n'
                 'Stipulated B = 5.000000 GHz, D = 2.000 kHz; no measured data', fontsize=15)
    m = np.arange(4, 8)
    nu = frequency(m)
    ax = axes[0, 0]
    ax.vlines(nu / 1e9, 0, 1, color='#2166ac', lw=2.5)
    ax.vlines(53.2, 0, .62, color='#b35806', lw=2.5)
    for n, f in zip(m, nu):
        ax.text(f / 1e9, 1.04, f'{n-1} → {n}', ha='center', fontsize=10)
    ax.text(53.2, .68, 'unrelated\n53.2 GHz', ha='center', color='#b35806', fontsize=10)
    ax.axvspan(38, 72, color='#e8eef3', alpha=.35)
    ax.set(xlim=(38, 72), ylim=(0, 1.38), yticks=[], xlabel='Frequency ν (GHz)',
           title='A  Limited band: first visible line is 3 → 4')
    ax.text(.03, .91, 'Stick heights carry no intensity information',
            transform=ax.transAxes, fontsize=9)
    ax = axes[0, 1]
    x = np.linspace(12, 67, 150)
    ax.plot(x, (B - 2 * D * x) / 1e6, color='#2166ac')
    ax.scatter(m**2, nu / (2 * m) / 1e6, color='#2166ac', zorder=3)
    ax.scatter(64, frequency(8) / 16 / 1e6, marker='*', s=140, color='#b35806', zorder=3)
    ax.text(29, 4999.89, 'Slope = −0.004 MHz\nIntercept = 5000 MHz', fontsize=10)
    ax.text(63, 4999.724, 'held-out m = 8', ha='right', color='#b35806', fontsize=10)
    ax.ticklabel_format(axis='y', useOffset=False)
    ax.set(xlabel='Assigned upper label m² = (J + 1)²', ylabel='ν / (2m) (MHz)',
           title='B  Four assignments fit one straight line')
    colors = ['#2166ac', '#b35806']
    for t, color in zip((3, 30), colors):
        j, pop, area = thermal_response(t)
        axes[1, 0].plot(j[:30], pop[:30], '.-', color=color, label=f'T = {t} K')
        axes[1, 1].plot(j[:29], area[:29], '.-', color=color, label=f'T = {t} K')
    axes[1, 0].set(xlabel='Lower-state rotational label J', ylabel='Level population P_J',
                   xlim=(0, 28), title='C  Rigid-rotor populations: sum over all M')
    axes[1, 1].set(xlabel='Lower label J of the J → J + 1 line',
                   ylabel='Integrated absorption area / its maximum', xlim=(0, 28),
                   title='D  Ideal absorption areas differ from populations')
    for ax in axes[1]:
        ax.legend(frameon=False)
        ax.grid(alpha=.2)
    fig.supxlabel('C–D: rigid energies (D = 0), thermal equilibrium, weak unsaturated absorption.\n'
                  'No nuclear-spin restrictions or instrument response; these are not FTMW peak amplitudes.', fontsize=10)
    fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
