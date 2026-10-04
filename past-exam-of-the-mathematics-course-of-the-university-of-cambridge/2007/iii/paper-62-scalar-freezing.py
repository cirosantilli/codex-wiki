"""Exact massless de Sitter scalar power; Python 3.14, root NumPy/Matplotlib.

Writes the matching opaque PNG to the caller's working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7.5, 4.4), facecolor='white')
fig.subplots_adjust(left=.1, right=.985, bottom=.18, top=.9)
x = np.linspace(-1.2, 8, 601)
for ratio, color in [(1, '#24547a'), (10, '#b95734'), (100, '#4f8b55')]:
    power = 1+np.exp(2*(np.log(ratio)-x))
    ax.semilogy(x, power, lw=2.2, color=color, label=r'$k/k_0='+str(ratio)+'$')
    ax.axvline(np.log(ratio), color=color, ls=':', lw=1, alpha=.7)
ax.axhline(1, color='#444', ls='--', lw=1.2)
ax.text(5.35, 1.7, 'frozen power', fontsize=11)
ax.text(-.85, 18000, 'vacuum contribution\nredshifts at fixed k', fontsize=11)
ax.set(xlim=(-1.2,8), ylim=(.7,150000), xlabel=r'$\log(aH/k_0)$',
       ylabel=r'$\Delta_{\delta\phi}^2/(H/2\pi)^2$',
       title='Each comoving scalar mode approaches the same frozen power')
ax.legend(loc='upper right', fontsize=11)
ax.spines[['top','right']].set_visible(False)
fig.text(.5, .025, 'Dotted lines: k = aH. Constant H; the formula includes both vacuum and frozen terms.',
         ha='center', fontsize=9)
fig.savefig('paper-62-scalar-freezing.png', dpi=120, facecolor='white')
plt.close(fig)
