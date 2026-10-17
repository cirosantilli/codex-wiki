"""Original thermoelectric trade-off/circuit models; Python 3.14/numpy/matplotlib.

Carrier curves are illustrative normalized functions, not fitted measurements.
Output is a PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig = plt.figure(figsize=(10.6, 6.7), layout='constrained')
gs = fig.add_gridspec(2, 2)
a0 = fig.add_subplot(gs[0, 0])
n = np.geomspace(.01, 100, 500)
sigma = n
seebeck = 1/(1+n**.4)
kappa = .5+.2*n
powerfactor = seebeck**2*sigma
z = powerfactor/kappa
for values, label, color in [(seebeck, r'$|S|$', '#286a85'),
                             (sigma, r'$\sigma$', '#b65c38'),
                             (kappa, r'$\kappa$', '#91709b')]:
    a0.semilogx(n, values/np.max(values), color=color, label=label)
a0.semilogx(n, z/np.max(z), 'k--', label='Z (separate normalization)')
a0.set(xlabel='Carrier concentration (normalized)', ylabel='Individually normalized value',
       title='Competing transport trends')
a0.legend(ncol=2, fontsize=8)
a0.grid(alpha=.15)
a1 = fig.add_subplot(gs[1, 0])
r = np.linspace(.001, 6, 600)
a1.plot(r, 4*r/(1+r)**2, color='#286a85', lw=2)
a1.scatter([1], [1], color='#b65c38', zorder=3)
a1.axvline(1, color='.65', ls=':')
a1.set(xlabel=r'Load ratio $R_L/R$', ylabel=r'$P/P_{\max}$',
       title='Fixed junction temperatures: maximum power at RL = R', ylim=(0, 1.12))
a1.grid(alpha=.15)
ax = fig.add_subplot(gs[:, 1])
ax.set(xlim=(0, 10), ylim=(0, 11), aspect='equal')
ax.axis('off')
ax.add_patch(Rectangle((1, 7.95), 8, .65, color='#e9b29d'))
ax.add_patch(Rectangle((1, 2.6), 8, .5, color='#b7d9e7'))
ax.text(5, 9.25, 'Hot source; TH', ha='center', fontsize=12)
ax.text(5, 1.95, 'Cold sink; TC', ha='center', fontsize=12)
for x, label, color in [(2, 'p-type', '#e5c4b5'), (6.2, 'n-type', '#b9d9e4')]:
    ax.add_patch(Rectangle((x, 3.1), 1.8, 4.5, facecolor=color, edgecolor='.3'))
    ax.text(x+.9, 5.35, label, ha='center', rotation=90, fontsize=12)
ax.plot([2.9, 2.9, 7.1, 7.1], [7.6, 8.05, 8.05, 7.6], color='.25', lw=3)
ax.plot([2.9, 2.9, 1.1, 1.1, 4.0], [3.1, 3.0, 3.0, .8, .8], color='.25', lw=2)
ax.plot([7.1, 7.1, 8.9, 8.9, 6], [3.1, 3.0, 3.0, .8, .8], color='.25', lw=2)
ax.add_patch(Rectangle((4, .45), 2, .7, facecolor='white', edgecolor='.25', lw=1.5))
ax.text(5, .8, 'Load RL', ha='center', va='center', fontsize=10)
for x in [1.3, 8.7]:
    ax.annotate('', (x, 3.25), (x, 7.8), arrowprops={'arrowstyle': '->', 'color': '#b65c38', 'lw': 1.5})
ax.text(5, 6.6, 'Heat', ha='center', color='#b65c38', fontsize=10)
ax.text(5, 4.45, 'Electrical series\nThermal parallel', ha='center', fontsize=10)
ax.text(5, 10.25, 'Ideal thermoelectric generator couple', ha='center', fontsize=13)
ax.annotate('', (3.4, .8), (1.7, .8), arrowprops={'arrowstyle': '->', 'color': '#286a85', 'lw': 1.6})
ax.text(2.6, .35, 'I', ha='center', color='#286a85', fontsize=11)
ax.text(5, -.05, 'Plates insulate electrically and conduct heat.', ha='center', fontsize=9)
fig.savefig('paper-1-thermoelectric.png', dpi=150, facecolor='white')
plt.close(fig)
