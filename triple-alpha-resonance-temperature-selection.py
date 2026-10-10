"""Sequential triple-alpha energy bookkeeping and a narrow-resonance toy rate.

Python 3.14, NumPy and Matplotlib per pyproject.toml. Energies above thresholds
are from Fowler's 1983 Nobel lecture p. 179. Alternative shifts are chosen
sensitivity tests, with all widths, density and composition held fixed.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

KB_MEV = 8.617333262e-11
T0 = 1e8
ER = 0.3794
BE_OFFSET = ER - 0.2875


def relative_rate(temperature, shift=0):
    temperature = np.asarray(temperature, dtype=float)
    return (temperature / T0)**-3 * np.exp(-(ER + shift) / (KB_MEV * temperature) + ER / (KB_MEV * T0))


def main():
    assert relative_rate(T0) == 1
    assert np.isclose(BE_OFFSET, 0.0919)
    assert np.isclose(relative_rate(T0, 0.1), np.exp(-0.1 / (KB_MEV*T0)))
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 5), layout='constrained', gridspec_kw={'width_ratios': [1, 1.2]})
    fig.set_facecolor('white')
    left.set(xlim=(0, 1), ylim=(-0.17, 0.52), title='Sequential route to carbon', ylabel='Energy above three free alpha particles (MeV)')
    for y, color, label in [(0, '0.35', r'$3\alpha$: threshold'), (BE_OFFSET, '#c46721', r'$^{8}$Be + $\alpha$: 0.0919'), (ER, '#194c83', 'Hoyle state: 0.3794')]:
        left.hlines(y, 0.08, 0.93, color=color, lw=2)
        left.text(0.09, y+0.012, label, fontsize=10)
    left.annotate('', xy=(0.78, ER), xytext=(0.78, BE_OFFSET), arrowprops={'arrowstyle': '<->', 'color': '#194c83'})
    left.text(0.76, 0.235, '0.2875 MeV', ha='right', fontsize=10)
    left.annotate('Small electromagnetic branch\nto bound carbon levels\n(below this plotted window)', xy=(0.4, -0.15), xytext=(0.5, -0.055), ha='center', va='center', fontsize=9, arrowprops={'arrowstyle': '->', 'color': '#488344'}, color='#376834')
    left.set_xticks([])
    left.set_yticks([0, BE_OFFSET, ER], ['0', '0.0919', '0.3794'])
    temperature = np.linspace(0.8e8, 2e8, 500)
    for shift, color, style, label in [(0, '#194c83', '-', 'Reference resonance'), (-0.1, '#488344', '--', 'Chosen shift: −100 keV'), (0.1, '#c46721', ':', 'Chosen shift: +100 keV')]:
        right.semilogy(temperature/1e8, relative_rate(temperature, shift), style, color=color, lw=2.2, label=label)
    right.axhline(1, color='0.7', lw=1)
    right.axvline(1, color='0.7', lw=1)
    right.set(xlabel=r'Temperature ($10^8$ K)', ylabel=r'$r(T,E_r+\delta E)/r(T_0,E_r)$', title=r'Calculated $T^{-3}\exp[-E_r/(k_B T)]$ selection')
    right.legend(loc='lower right', fontsize=9)
    right.grid(alpha=0.18)
    fig.suptitle('Triple-alpha resonance: energies and rate sensitivity', fontsize=14)
    fig.savefig(Path(__file__).stem + '.png', dpi=125, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
