"""Original molar van der Waals calculations; Python 3.14, NumPy 2.3, Matplotlib 3.10.

Run from _media: MPLBACKEND=Agg python ../van-der-waals-molar-pressure-model.py
All constants describe a stipulated hypothetical fluid, not measured carbon dioxide.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

R, A, B = 8.314462618, 0.360, 4.00e-5
VC = 3 * B
TC = 8 * A / (27 * R * B)
PC = A / (27 * B**2)


def pressure(volume, temperature):
    return R * temperature / (volume - B) - A / volume**2


def coexistence(t):
    """Find the equal-area pressure by bisection, using the analytic integral."""
    spin = np.sort(np.roots([4 * t, -9, 6, -1]).real)
    spin = spin[spin > 1 / 3]
    q = lambda x: 8 * t / (3 * x - 1) - 3 / x**2
    low, high = q(spin[0]), q(spin[1])
    for _ in range(90):
        middle = (low + high) / 2
        roots = np.sort(np.roots([3 * middle, -(middle + 8 * t), 9, -3]).real)
        vl, vg = roots[0], roots[-1]
        area = (8 * t / 3 * np.log((3 * vg - 1) / (3 * vl - 1))
                + 3 * (1 / vg - 1 / vl) - middle * (vg - vl))
        if area > 0:
            low = middle
        else:
            high = middle
    assert abs(area) < 1e-12
    return middle, roots


def main():
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.8, 4.8), layout='constrained')
    volume = np.linspace(65, 500, 1100) * 1e-6
    left.plot(volume * 1e6, R * 360 / volume / 1e6, label='Ideal: RT / vₘ', color='#777777')
    left.plot(volume * 1e6, R * 360 / (volume - B) / 1e6,
              label='Excluded volume only', color='#b36b00')
    left.plot(volume * 1e6, pressure(volume, 360) / 1e6,
              label='With attraction', color='#176baa', lw=2)
    left.scatter([240], [pressure(240e-6, 360) / 1e6], color='#176baa', zorder=4)
    left.annotate('Worked state\n8.716 MPa', xy=(240, 8.716), xytext=(295, 15),
                  arrowprops={'arrowstyle': '->', 'color': '#176baa'})
    left.set(title='Competing corrections at 360 K', xlim=(65, 500), ylim=(0, 42),
             xlabel='Molar volume vₘ (cm³ mol⁻¹)', ylabel='Pressure (MPa)')
    left.legend(frameon=False, loc='upper right')
    v = np.linspace(52, 440, 1400) * 1e-6
    for t, color in [(1.1, '#b36b00'), (1, '#176baa')]:
        right.plot(v * 1e6, pressure(v, t * TC) / 1e6, color=color,
                   label=f'T/Tc = {t:g}', lw=2)
    qs, roots = coexistence(.9)
    vl, _, vg = roots * VC
    right.plot(v * 1e6, pressure(v, .9 * TC) / 1e6, color='#999999', ls=':',
               label='0.9: homogeneous continuation')
    stable = (v <= vl) | (v >= vg)
    right.plot(v * 1e6, np.where(stable, pressure(v, .9 * TC) / 1e6, np.nan),
               color='#278249', lw=2)
    right.hlines(qs * PC / 1e6, vl * 1e6, vg * 1e6, color='#278249', lw=3,
                  label='0.9: equilibrium coexistence')
    right.scatter([120], [PC / 1e6], color='#176baa', zorder=5)
    right.annotate('Critical point\n120 cm³ mol⁻¹, 8.333 MPa',
                   xy=(120, PC / 1e6), xytext=(165, 13.8), fontsize=9,
                   arrowprops={'arrowstyle': '->', 'color': '#176baa'})
    right.set(title=f'Critical temperature Tc = {TC:.3f} K', xlim=(52, 440), ylim=(0, 21),
              xlabel='Molar volume vₘ (cm³ mol⁻¹)', ylabel='Pressure (MPa)')
    right.legend(frameon=False, loc='upper right', fontsize=8)
    for ax in (left, right):
        ax.grid(alpha=.18)
    fig.suptitle('A hypothetical fluid: aₘ = 0.360 Pa m⁶ mol⁻²; bₘ = 40.0 cm³ mol⁻¹', fontsize=12)
    fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
