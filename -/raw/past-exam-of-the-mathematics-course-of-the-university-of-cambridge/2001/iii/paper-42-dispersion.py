#!/usr/bin/env python3
"""Plot local incompressible disk-wave branches; write the PNG to caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ETA = 0.5  # kappa^2 / Omega_z^2
KMAX = 14.0


def bisect(function, low, high):
    fl = function(low)
    assert fl * function(high) <= 0
    for _ in range(90):
        mid = (low + high) / 2
        fm = function(mid)
        if fl * fm <= 0:
            high = mid
        else:
            low, fl = mid, fm
    return (low + high) / 2


def inertial_branch(order):
    epsilon = 1e-8
    if order % 2:
        j = (order - 1) // 2
        low, high = j * np.pi + epsilon, (j + .5) * np.pi - epsilon
        squared_frequency = lambda z: z / np.tan(z)
    else:
        j = order // 2 - 1
        low, high = (j + .5) * np.pi + epsilon, (j + 1) * np.pi - epsilon
        squared_frequency = lambda z: -z * np.tan(z)
    start = bisect(lambda z: squared_frequency(z) - ETA, low, high)
    phase = np.linspace(start, high, 2600)
    frequency2 = squared_frequency(phase)
    kh = phase * np.sqrt(np.maximum(0, ETA / frequency2 - 1))
    keep = kh <= KMAX
    return kh[keep], np.sqrt(frequency2[keep])


def draw():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False})
    fig, ax = plt.subplots(figsize=(9.2, 5.5), layout='constrained')
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    cutoff = bisect(lambda z: z * np.tanh(z) - ETA, 1e-8, 3.)
    q = np.linspace(cutoff, 16, 2400)
    f2 = q * np.tanh(q)
    kh = q * np.sqrt(np.maximum(0, 1 - ETA / f2))
    ax.plot(kh, np.sqrt(f2), color='#a63b25', linewidth=2.5,
            label='Even-pressure surface branch')
    q = np.linspace(1e-8, 16, 2400)
    f2 = q / np.tanh(q)
    kh = q * np.sqrt(1 - ETA / f2)
    ax.plot(kh, np.sqrt(f2), color='#d39225', linewidth=2.5,
            label='Odd-pressure surface branch')
    for order in range(1, 7):
        kh, frequency = inertial_branch(order)
        ax.plot(kh, frequency, color='#245c8b', alpha=1 - .09 * (order - 1),
                linewidth=1.5, linestyle='-' if order % 2 == 0 else '--',
                label='Inertial branches (orders 1–6)' if order == 1 else None)
    ax.axhline(np.sqrt(ETA), color='#606060', linewidth=1, linestyle=':')
    ax.text(KMAX - .15, np.sqrt(ETA) + .045, r'$\kappa/\Omega_z$',
            ha='right', color='#505050')
    ax.axhline(1, color='#d7d7d7', linewidth=.8)
    ax.text(KMAX - .15, 1.04, r'$\omega=\Omega_z$', ha='right', color='#777777')
    ax.set(xlim=(0, KMAX), ylim=(0, 4), xlabel=r'Radial wavenumber $kH$',
           ylabel=r'Frequency $\omega/\Omega_z$',
           title=r'Homogeneous incompressible disk: $\kappa^2/\Omega_z^2=1/2$')
    ax.grid(alpha=.15)
    ax.legend(loc='upper left', framealpha=.95)
    fig.savefig(Path('paper-42-dispersion.png'), dpi=150, facecolor='white',
                edgecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    draw()
