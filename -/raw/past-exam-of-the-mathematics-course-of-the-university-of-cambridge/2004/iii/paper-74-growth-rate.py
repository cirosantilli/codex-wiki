"""Coating growth rate; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Write an opaque PNG basename to caller CWD; honor caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
k = np.linspace(-1.4, 1.4, 1000)
s = k**2 - k**4
fig, ax = plt.subplots(figsize=(7, 3.7), layout='constrained')
ax.plot(k, s, color='#176b91', linewidth=2.2)
ax.axhline(0, color='0.25', linewidth=.8)
ax.axvline(0, color='0.25', linewidth=.8)
km = 1 / np.sqrt(2)
ax.scatter([-km, km], [.25, .25], color='#b84326', zorder=4)
ax.vlines([-km, km], 0, .25, ls='--', color='#b84326', linewidth=1)
ax.set(xlim=(-1.4, 1.4), ylim=(-1.05, .4), xlabel=r'$k$', ylabel=r'$s/h_0^3$', title='Capillary instability of a cylindrical coating')
ax.set_xticks([-1, -km, 0, km, 1], ['$-1$', r'$-1/\sqrt{2}$', '$0$', r'$1/\sqrt{2}$', '$1$'])
ax.text(.82, -.5, 'stable', fontsize=10)
ax.text(-.22, .31, 'unstable', fontsize=10)
ax.grid(alpha=.2)
fig.savefig('paper-74-growth-rate.png', dpi=150, facecolor='white', transparent=False)
plt.close(fig)
