"""Original chosen-input illustrations, not historical data.

Python 3.14; matplotlib 3.10.7, numpy 2.3.5. Run from _media.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.9), dpi=110, facecolor='white')
fig.subplots_adjust(left=.07, right=.98, bottom=.19, top=.78, wspace=.29)
fig.suptitle('Chosen calculations: propagation and complementary sensitivities', fontsize=16, y=.97)
fig.text(.5, .89, 'Illustrations only • no fitted parameters, event data or confidence bands', ha='center', color='#555555')
x = np.linspace(0, 2000, 2001)
p = 1 - np.sin(1.27*.0025*x)**2
ax.plot(x, p, color='#176c9c', lw=2)
for le, label, offset in [(20, '20 km / 1 GeV', (21, -30)), (500, '500 km / 1 GeV', (20, 30))]:
    value = 1-np.sin(1.27*.0025*le)**2
    ax.plot(le, value, 'o', color='#bd5426')
    ax.annotate(label, (le, value), xytext=offset, textcoords='offset points', fontsize=10,
                arrowprops={'arrowstyle':'-', 'color':'#777777'})
ax.set(xlim=(0, 2000), ylim=(-.05, 1.05), xlabel=r'$L/E$ (km / GeV)', ylabel=r'Survival probability $P_{\mu\mu}$',
       title=r'Two flavours in vacuum: $\theta=\pi/4$')
ax.text(.97, .96, r'$\Delta m^2=2.5\times10^{-3}\ \mathrm{eV}^2$', transform=ax.transAxes, ha='right', va='top', fontsize=10)
ax.grid(alpha=.2)
q = np.linspace(0, 5.5, 301)
bx.axvline(2, color='#bd5426', lw=2, label=r'CC: $\phi_e=2$')
bx.plot(q, 5-q, color='#247b55', lw=2, label=r'NC: $\phi_e+\phi_x=5$')
bx.plot(q, (2.45-q)/.15, color='#176c9c', lw=2, label=r'ES: $\phi_e+0.15\phi_x=2.45$')
bx.plot(2, 3, 'ko', ms=5)
bx.annotate('Chosen mixture (2, 3)', (2, 3), xytext=(2.65, 4.25), fontsize=10,
            arrowprops={'arrowstyle':'->', 'color':'#444444'})
bx.set(xlim=(0, 5.5), ylim=(0, 5.5), xlabel=r'$\phi_e$ (arbitrary flux unit)',
       ylabel=r'$\phi_x=\phi_\mu+\phi_\tau$ (same unit)', title='Independent normalized channel constraints')
bx.legend(loc='upper right', bbox_to_anchor=(1, .74), fontsize=9, framealpha=.95)
bx.grid(alpha=.2)
fig.text(.5, .055, 'Channel normalization includes target number, exposure, cross section and selection efficiency.', ha='center', fontsize=10)
fig.savefig(Path(__file__).stem+'.png', facecolor='white')
plt.close(fig)
