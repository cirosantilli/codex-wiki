"""Exact two-site selection rules, not historical neutron data.

Python 3.14; matplotlib 3.10.7, numpy 2.3.5. Run from _media with
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib.
Nuclear F=1+exp(i*pi*h); magnetic F=mA-mB*exp(i*pi*h).
Sticks represent squared structure factors, not integrated cross sections.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(3, 1, figsize=(9, 7.2), sharex=True, facecolor='white')
h = np.arange(1, 7)
phase = np.exp(1j * np.pi * h)
nuclear = np.abs(1 + phase)**2
nuclear[nuclear < 1e-20] = 0
cases = [
    ('No long-range magnetic order', None),
    ('Antiferromagnetic order: $m_A=m_B=1$', (1, 1)),
    (r'Ferrimagnetic order: $m_A=2,\ m_B=1$', (2, 1)),
]
for ax, (title, moments) in zip(axes, cases):
    ax.set_title(title, loc='left', fontsize=12, pad=9)
    ax.vlines(h, 0, nuclear, colors='#176b9c', linewidth=5,
              label='Nuclear: own arbitrary units')
    if moments:
        a, b = moments
        magnetic = np.abs(a - b * phase)**2
        magnetic[magnetic < 1e-20] = 0
        ax.vlines(h, 0, magnetic, colors='#bd4828', linewidth=2,
                  linestyles='--', label='Magnetic: own arbitrary units')
        for x, y in zip(h, magnetic):
            if y:
                ax.text(x + .09, y + .1, f'{y:.0f}', color='#bd4828', fontsize=10)
    else:
        ax.text(.98, .64, 'Nuclear periodicity retained;\nmagnetic diffuse scattering omitted',
                transform=ax.transAxes, ha='right', color='#4e5964')
    ax.set(ylim=(0, 10.5), yticks=[0, 4, 9], xlim=(.45, 6.5))
    ax.grid(axis='y', color='#e9edf0', linewidth=.7)
    ax.set_axisbelow(True)
    ax.spines[['top', 'right']].set_visible(False)
axes[1].legend(loc='upper right', fontsize=9, frameon=False)
axes[-1].set(xticks=h, xlabel=r'$h=qa/\pi$  (positive nonzero reciprocal positions)')
fig.text(.015, .5, 'Squared structure factor (separate channel scales)',
         rotation=90, va='center', fontsize=11)
fig.suptitle('A doubled magnetic period adds odd-index peaks',
             fontsize=16, weight='bold', y=.985)
fig.text(.5, .018, 'Exact toy selection rules • no measured points • not the MnO reflection pattern',
         ha='center', fontsize=11, color='#4e5964')
fig.subplots_adjust(left=.10, right=.96, top=.90, bottom=.105, hspace=.52)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120,
            facecolor='white', transparent=False)
