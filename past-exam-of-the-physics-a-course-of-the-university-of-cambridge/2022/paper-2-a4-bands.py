"""Original equilibrium homojunction solution diagram, not a source-paper diagram.
Python 3.14; root NumPy/Matplotlib dependencies. Write PNG basename in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 800)
# Equal doping: the potential and its slope are continuous at the junction.
bend = np.piecewise(x, [x < -1, (x >= -1)&(x < 0), (x >= 0)&(x < 1), x >= 1],
                    [1., lambda u: 1-(u+1)**2/2, lambda u: (1-u)**2/2, 0.])
ev = .05 + bend
ec = ev+1.25
fig, (ax, charge) = plt.subplots(2, 1, figsize=(8.6, 5.8), dpi=130, sharex=True,
                                gridspec_kw={'height_ratios':[4, 1]}, facecolor='white')
for a in (ax, charge):
    a.axvspan(-1, 1, color='#f4e6bd', alpha=.7)
    a.spines[['top', 'right']].set_visible(False)
ax.plot(x, ec, color='#31688e', lw=2, label=r'$E_C$: conduction-band edge')
ax.plot(x, ev, color='#009e73', lw=2, label=r'$E_V$: valence-band edge')
ax.plot(x[x<=0], (ev+.06)[x<=0], '--', color='#b04193', lw=1.5)
ax.plot(x[x>=0], (ec-.06)[x>=0], '--', color='#d55e00', lw=1.5)
ax.axhline(1.175, color='black', ls='-.', lw=1.4)
ax.text(-2.9, 1.21, r'$\mu=E_F$ (constant)', fontsize=10)
ax.text(-2.9, 1.43, r'$E_A$: acceptors', color='#b04193', fontsize=10)
ax.text(1.2, 1.1, r'$E_D$: donors', color='#d55e00', fontsize=10)
ax.annotate('', (2.6, 1.30), (2.6, .05), arrowprops=dict(arrowstyle='<->', color='0.3'))
ax.text(2.65, .65, r'$E_g$', fontsize=11)
ax.annotate('', (-.65, 2.3), (.65, 1.3), arrowprops=dict(arrowstyle='<->', color='0.3'))
ax.text(.25, 2.0, r'Energy drop $eV_{\rm bi}$', fontsize=10)
ax.set(ylim=(-.05, 2.68), ylabel='Electron energy (schematic units)')
ax.set_yticks([])
ax.set_title('Thermal equilibrium: p side at left, n side at right', fontsize=12)
ax.legend(loc='upper right', fontsize=9, framealpha=1)
charge.plot([-3,-1,-1,0,0,1,1,3], [0,0,-1,-1,1,1,0,0], color='#31688e', lw=1.7)
charge.axhline(0, color='0.5', lw=.7)
charge.text(-.85, -.65, r'$-eN_A$', fontsize=11)
charge.text(.15, .45, r'$+eN_D$', fontsize=11)
charge.text(-2.6, .5, 'neutral p', fontsize=10)
charge.text(1.5, .5, 'neutral n', fontsize=10)
charge.set(ylim=(-1.4, 1.4), xlim=(-3,3), ylabel=r'$\rho$', xlabel='Position through junction')
charge.set_yticks([])
charge.set_xticks([-1,0,1], [r'$-x_p$', '0', r'$x_n$'])
fig.text(.51, .005, 'Shaded: depletion region; fixed ionized impurities, few mobile carriers', ha='center', fontsize=9)
fig.tight_layout(rect=(0,.025,1,1), h_pad=.6)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
