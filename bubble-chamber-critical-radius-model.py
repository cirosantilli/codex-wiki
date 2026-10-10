"""Original capillarity example; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media. Chosen constants are not detector measurements.
Formation work omits latent heat and transport; it is not a full threshold model.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

SIGMA = 0.010  # J/m^2, stipulated constant
J_PER_KEV = 1.602176634e-16

def formation_work(radius, delta_p):
    return 4 * np.pi * SIGMA * radius**2 - 4 * np.pi * delta_p * radius**3 / 3

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), facecolor='white')
r = np.linspace(0, 180e-9, 700)
ax = axes[0]
delta_p = 2e5
ax.plot(r * 1e9, 4 * np.pi * SIGMA * r**2 / J_PER_KEV, color='#b35726', label='Surface cost')
ax.plot(r * 1e9, -4 * np.pi * delta_p * r**3 / 3 / J_PER_KEV, color='#477c56', label='Bulk gain')
ax.plot(r * 1e9, formation_work(r, delta_p) / J_PER_KEV, color='#26536b', lw=2.5, label='Total work')
ax.set(title='A  Two competing terms', ylabel='Formation work (keV)', ylim=(-35, 30))
ax.legend(loc='lower left', frameon=False)
ax = axes[1]
for delta_p, color, label in [(2e5, '#26536b', 'Chosen Δp = 0.20 MPa'), (4e5, '#a0447e', 'Twice Δp = 0.40 MPa')]:
    rc = 2 * SIGMA / delta_p
    gc = formation_work(rc, delta_p)
    ax.plot(r * 1e9, formation_work(r, delta_p) / J_PER_KEV, color=color, lw=2.4, label=label)
    ax.plot(rc * 1e9, gc / J_PER_KEV, 'o', color=color)
    ax.plot([rc * 1e9] * 2, [0, gc / J_PER_KEV], ':', color=color)
    ax.annotate(f'{rc * 1e9:.0f} nm; {gc / J_PER_KEV:.3f} keV', xy=(rc * 1e9, gc / J_PER_KEV), xytext=(rc * 1e9 - 32, gc / J_PER_KEV + 0.4), color=color, fontsize=10)
ax.set(title='B  Larger driving pressure lowers the barrier', ylim=(-0.6, 3.5), ylabel='Total formation work (keV)')
ax.legend(loc='lower left', frameon=False, fontsize=10)
for ax in axes:
    ax.axhline(0, color='#777', lw=0.8)
    ax.set(xlabel='Bubble radius r (nm)', xlim=(0, 180))
    ax.spines[['top', 'right']].set_visible(False)
fig.suptitle('A bubble must cross a surface-energy barrier', weight='bold', fontsize=16)
fig.text(0.5, 0.87, r'$\Delta G=4\pi\sigma r^2-4\pi\Delta p\,r^3/3$     •     chosen $\sigma=0.010$ J/m²', ha='center', fontsize=12)
fig.text(0.5, 0.035, 'Macroscopic, isothermal model. Formation work is not a complete deposited-energy threshold.', ha='center', fontsize=11)
fig.subplots_adjust(left=0.075, right=0.98, top=0.76, bottom=0.16, wspace=0.32)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
