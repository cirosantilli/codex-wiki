"""Original schematic turbulence spectrum; output basename to caller CWD.

Tested with Python 3.14.4, matplotlib 3.10.7 and numpy 2.3.5.
Uses the caller's MPLCONFIGDIR unchanged. All scales are illustrative.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    k = np.geomspace(0.025, 1600, 1000)
    kd = 250.0
    energy = k**2 / (1 + k**(11/3)) * np.exp(-(k/kd)**1.5)
    fig, ax = plt.subplots(figsize=(8.2, 4.7), facecolor='white')
    ax.set_facecolor('white')
    ax.loglog(k, energy, color='#175b8a', lw=2.7)
    ax.axvspan(0.025, 2, color='#e6edf4', alpha=1)
    ax.axvspan(2, 120, color='#e9f3ea', alpha=1)
    ax.axvspan(120, 1600, color='#fff0df', alpha=1)
    ax.loglog(k, energy, color='#175b8a', lw=2.7)
    guide = np.array([5., 70.])
    ax.loglog(guide, 0.85*guide**(-5/3), '--', color='#263238', lw=1.3)
    ax.text(8, .042, r'$E(k)\propto\varepsilon^{2/3}k^{-5/3}$', fontsize=12)
    ax.text(.14, 1.15, 'Energy-containing\neddies', ha='center', fontsize=11)
    ax.text(17, 1.15, 'Inertial range\nenergy transfer', ha='center', fontsize=11)
    ax.text(650, 1.15, 'Dissipation range\nviscous removal', ha='center', fontsize=11)
    ax.annotate(r'$k_0\sim 1/W$', xy=(1, .48), xytext=(.1, .11),
                arrowprops={'arrowstyle':'->', 'color':'#263238'}, fontsize=11)
    ax.annotate(r'$k_d\sim(\varepsilon/\nu^3)^{1/4}$', xy=(kd, .367*kd**(-5/3)),
                xytext=(12, .000055), arrowprops={'arrowstyle':'->', 'color':'#263238'}, fontsize=11)
    ax.set_xlim(.025, 1600)
    ax.set_ylim(1e-9, 5)
    ax.set_xlabel('Wavenumber k (arbitrary units)', fontsize=11)
    ax.set_ylabel('Energy spectrum E(k) (arbitrary units)', fontsize=11)
    ax.set_title('High-Reynolds-number turbulence: schematic energy spectrum', fontsize=12, pad=13)
    ax.grid(True, which='major', color='#cccccc', linewidth=.5)
    fig.tight_layout()
    fig.savefig(Path('paper-79-spectrum.png'), dpi=150, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
