"""Original independent horizontal-displacement readout, not historical data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is perrin-brownian-displacement-diffusion.png in CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    k_b, temperature, viscosity, radius = 1.380649e-23, 298.0, 1.00e-3, .250e-6
    diffusivity = k_b * temperature / (6 * np.pi * viscosity * radius) * 1e12
    rng = np.random.default_rng(1609)
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, (tracks, msd) = plt.subplots(1, 2, figsize=(11.6, 5.3), facecolor='white',
                                    gridspec_kw={'width_ratios': [1, 1.35]})
    fig.subplots_adjust(left=.08, right=.97, bottom=.20, top=.74, wspace=.32)
    fig.suptitle('A second readout: horizontal displacement', fontsize=18, y=.97)
    fig.text(.5, .86, 'Chosen bulk model: T = 298 K, η = 1.00 mPa s, a = 0.250 μm; D = %.4f μm²/s' % diffusivity,
             ha='center', fontsize=11)
    colors = ['#007c91', '#dd7223', '#6956b3']
    for j, color in enumerate(colors):
        steps = rng.normal(size=(20, 2)) * np.sqrt(2 * diffusivity)
        positions = np.vstack([np.zeros(2), np.cumsum(steps, axis=0)])
        tracks.plot(positions[:, 0], positions[:, 1], '.-', color=color, lw=1.1, markersize=4,
                    alpha=.85, label=f'Track {j + 1}')
    tracks.scatter([0], [0], marker='*', c='#253746', s=100, zorder=5)
    tracks.set(xlabel='Horizontal x (μm)', ylabel='Horizontal y (μm)')
    tracks.set_aspect('equal', adjustable='datalim')
    tracks.set_title('Three samples: 20 s, positions every 1 s', fontsize=11.5, pad=13)
    tracks.grid(alpha=.2)
    tracks.legend(frameon=False, fontsize=9, loc='upper left')

    tau = np.linspace(0, 20, 300)
    msd.plot(tau, 2 * diffusivity * tau, color=colors[0], lw=2, label='One coordinate: 2Dτ')
    msd.plot(tau, 4 * diffusivity * tau, color=colors[1], lw=2, label='Two coordinates: 4Dτ')
    lags = np.array([1., 2., 5., 10., 15., 20.])
    sample_x, sample_xy = [], []
    # Separate ensembles at each lag; independent of the three tracks and height counts.
    for lag in lags:
        displacement = rng.normal(size=(16000, 2)) * np.sqrt(2 * diffusivity * lag)
        sample_x.append(np.mean(displacement[:, 0]**2))
        sample_xy.append(np.mean(np.sum(displacement**2, axis=1)))
    msd.scatter(lags, sample_x, s=32, facecolor='white', edgecolor=colors[0], zorder=3)
    msd.scatter(lags, sample_xy, s=32, marker='s', facecolor='white', edgecolor=colors[1], zorder=3)
    msd.axvline(10, color='#718096', ls=':', lw=1)
    msd.annotate('At 10 s: 17.46 and 34.92 μm²', xy=(10, 4 * diffusivity * 10),
                 xytext=(1.5, 59), fontsize=10, arrowprops={'arrowstyle': '->', 'color': '#536170'})
    msd.set(xlabel='Lag τ (s)', ylabel='Mean squared displacement (μm²)', xlim=(0, 21), ylim=(0, 77))
    msd.set_title('Displacement statistics determine D', fontsize=12, pad=13)
    msd.legend(frameon=False, fontsize=10, loc='upper left')
    msd.grid(alpha=.2)
    fig.text(.5, .06, 'Lines: exact model laws. Open markers: separate simulated ensembles, 16,000 displacements per lag.\nJoined sample positions do not resolve the intervening motion. No historical data are plotted.',
             ha='center', fontsize=10, color='#47535e')
    output = Path.cwd() / f'{Path(__file__).stem}.png'
    fig.savefig(output, dpi=110, facecolor='white')
    plt.close(fig)
    print(output)


if __name__ == '__main__':
    main()
