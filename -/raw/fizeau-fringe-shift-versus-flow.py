"""Original nondispersive Fizeau-model comparison, not measured data.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media to emit fizeau-fringe-shift-versus-flow.png.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


C = 299792458.0
ELL = 1.50
N_INDEX = 4 / 3
WAVELENGTH = 550e-9


def partial_drag_fringe_offset(speed):
    """Rest-to-flow offset for a signed speed; water length per beam = 2 ELL."""
    return 4 * ELL * np.asarray(speed) * (N_INDEX**2 - 1) / (C * WAVELENGTH)


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    speed = np.linspace(0, 10, 401)
    offset = partial_drag_fringe_offset(speed)
    full = 4 * ELL * speed * N_INDEX**2 / (C * WAVELENGTH)
    fig, ax = plt.subplots(figsize=(9.5, 6.3), dpi=100, facecolor='white')
    fig.subplots_adjust(left=.11, right=.97, top=.81, bottom=.15)
    fig.suptitle('Moving water produces a nonzero fringe shift',
                 fontsize=18, fontweight='bold', y=.97)
    fig.text(.5, .886,
             r'Chosen model: $\ell=1.50$ m per tube, $n=4/3$, $\lambda_0=550$ nm; no dispersion',
             ha='center', fontsize=12)
    ax.plot(speed, full, '--', color='#a14f20', lw=2.2,
            label=r'Ordinary addition: rest to flow ($n^2$)')
    ax.plot(speed, 2 * offset, color='#7a4b9d', lw=2.6,
            label=r'Partial drag: opposite flow settings ($2N$)')
    ax.plot(speed, offset, color='#1265a8', lw=2.7,
            label=r'Partial drag: rest to flow ($N$)')
    ax.axhline(0, color='#4d4d4d', lw=1.5, label='No flow effect: zero shift')
    ax.axvline(6, color='#a0a0a0', lw=1, linestyle=':')
    value = float(partial_drag_fringe_offset(6))
    ax.scatter([6, 6], [value, 2 * value], color=['#1265a8', '#7a4b9d'], s=42, zorder=5)
    ax.annotate(f'{value:.5f} fringe', xy=(6, value), xytext=(6.45, .12),
                color='#1265a8', arrowprops={'arrowstyle': '-', 'color': '#1265a8'})
    ax.annotate(f'{2*value:.5f} fringe', xy=(6, 2 * value), xytext=(6.45, .31),
                color='#7a4b9d', arrowprops={'arrowstyle': '-', 'color': '#7a4b9d'})
    ax.set(xlim=(0, 10), ylim=(-.025, .71),
           xlabel=r'Flow speed $|u|$ (m/s)', ylabel='Magnitude of fringe displacement (cycles)')
    ax.grid(alpha=.22)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='upper left', fontsize=10.5, framealpha=1, facecolor='white')
    fig.text(.5, .035, 'Calculated curves and illustrative markers; no experimental data',
             ha='center', color='#555555', fontsize=11)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
