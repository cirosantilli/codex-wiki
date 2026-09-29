"""Original dimensionless two-level calculation; Python 3.14, numpy, matplotlib.

PNG output is a basename in the working directory for Makefile rendering.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

t = np.geomspace(0.025, 100, 800)
w = 3*np.exp(-1/t)
p = w/(1+w)
response = w/(t**2*(1+w)**2)
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), layout='constrained')
fig.patch.set_facecolor('white')
axes[0].semilogx(t, 1+p, color='#236e80', lw=2)
axes[0].axhline(1.75, color='#b55728', ls='--', label=r'High-$T$ limit: $7/4$')
axes[0].set(ylabel=r'$V/V_0$', ylim=(0.97, 1.83), title='Mean volume')
axes[0].legend(loc='lower right', fontsize=9)
axes[1].semilogx(t, response, color='#7f4286', lw=2)
axes[1].set(ylabel=r'$(\varepsilon/k_B)\alpha$', title='Expansion response', ylim=(0, None))
for ax in axes:
    ax.set(xlabel=r'$t=k_BT/\varepsilon$', xlim=(t[0], t[-1]))
    ax.grid(alpha=0.22)
    ax.spines[['top', 'right']].set_visible(False)
fig.savefig('paper-2-two-level-expansion.png', dpi=160, facecolor='white')
plt.close(fig)
