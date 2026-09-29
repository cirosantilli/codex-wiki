"""Calculate and plot normalized finite-well envelopes without SciPy.

Tested with Python 3.14, matplotlib 3.10.7 and NumPy 2.3.5.
All values belong to the stipulated dimensionless model z0=2.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def bisect(function, left, right):
    fl = function(left)
    assert fl * function(right) < 0
    for _ in range(80):
        middle = (left + right) / 2
        fm = function(middle)
        if fl * fm <= 0:
            right = middle
        else:
            left, fl = middle, fm
    return (left + right) / 2


def states(z0=2.0):
    """Return (parity,z,w,normalization,interior probability) for z0=2."""
    even = bisect(lambda z: z * np.tan(z) - np.sqrt(z0*z0-z*z),
                  1e-10, np.pi/2 - 1e-10)
    odd = bisect(lambda z: -z / np.tan(z) - np.sqrt(z0*z0-z*z),
                 np.pi/2 + 1e-10, z0-1e-10)
    out = []
    for parity, z in [('even', even), ('odd', odd)]:
        w = np.sqrt(z0*z0-z*z)
        inside = 1 + (1 if parity == 'even' else -1)*np.sin(2*z)/(2*z)
        edge = np.cos(z) if parity == 'even' else np.sin(z)
        norm = 1 / np.sqrt(inside + edge*edge/w)
        out.append((parity, z, w, norm, norm*norm*inside))
    return out


def envelope(s, state):
    parity, z, w, norm, _ = state
    if parity == 'even':
        return norm * np.where(abs(s) <= 1, np.cos(z*s),
                               np.cos(z)*np.exp(-w*(abs(s)-1)))
    return norm * np.where(abs(s) <= 1, np.sin(z*s),
                           np.sign(s)*np.sin(z)*np.exp(-w*(abs(s)-1)))


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.1), layout='constrained')
    s = np.linspace(-5, 5, 4001)
    calculated = states()
    colors = ['#215a9a', '#a13d32']
    for ax in axes:
        ax.axvspan(-1, 1, color='#f0f7e6')
        ax.axvline(-1, color='.55', ls=':', lw=1)
        ax.axvline(1, color='.55', ls=':', lw=1)
        ax.set(xlabel=r'$s=x/a$', xlim=(-5, 5))
    left, right = axes
    left.plot([-5, -1, -1, 1, 1, 5], [1, 1, 0, 0, 1, 1], color='.25', lw=2,
              label=r'$V/V_0$')
    for state, color in zip(calculated, colors):
        parity, z, w, norm, inside = state
        energy = z*z/4
        phi = envelope(s, state)
        left.axhline(energy, color=color, lw=1, ls='--')
        left.plot(s, energy + .18*phi, color=color, lw=2,
                  label=f'{parity}: E/V₀ = {energy:.4f}')
        right.plot(s, phi*phi, color=color, lw=2,
                   label=f'{parity}: P inside = {inside:.4f}')
        right.fill_between(s, 0, phi*phi, where=abs(s) <= 1,
                           color=color, alpha=.1)
        print(f'{parity}: z={z:.12f}, w={w:.12f}, E/V0={energy:.12f}, '
              f'A={norm:.12f}, P_in={inside:.12f}')
    left.set(ylim=(-.04, 1.2), ylabel='Energy / barrier height')
    left.set_title('Bound levels and signed envelopes', weight='bold')
    left.legend(loc='upper left', fontsize=9, framealpha=1)
    left.text(0, .47, r'Envelopes drawn as $E/V_0+0.18\phi(s)$',
              ha='center', fontsize=9, color='.3')
    right.set(ylim=(0, 1), ylabel=r'Probability density $|\phi(s)|^2$')
    right.set_title('Normalization includes both tails', weight='bold')
    right.legend(loc='upper center', fontsize=9, framealpha=1)
    right.text(0, .7, r'$\int_{-\infty}^{\infty}|\phi|^2\,ds=1$', ha='center')
    fig.suptitle('Chosen finite well: constant effective mass, z₀ = 2', fontsize=14)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
