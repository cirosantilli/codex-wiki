"""Question 39 acoustic waveguide curves. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.

Writes its PNG basename to the current working directory; the caller selects
the output directory.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/2011-ii1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

output = Path(__file__).with_suffix('.png').name
k = np.linspace(0, 4, 500)
k_positive = np.linspace(.04, 4, 500)
fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), dpi=100, facecolor='white')
axes[0].plot(k, np.sqrt(1 + k*k), color='#185f9a', lw=2, label='dispersive mode')
axes[0].plot(k, k, color='#666666', ls='--', lw=1.7, label='zero transverse mode')
axes[0].set(xlabel=r'$k/\kappa$', ylabel=r'$\omega/(c_0\kappa)$', title='Dispersion relation', xlim=(0,4), ylim=(0,4.4))
axes[0].legend(loc='upper left', fontsize=9, frameon=False)
axes[1].plot(k_positive, np.sqrt(1+1/k_positive**2), color='#ad4e11', lw=2, label=r'phase speed $c/c_0$')
axes[1].plot(k, k/np.sqrt(1+k*k), color='#185f9a', lw=2, label=r'group speed $c_g/c_0$')
axes[1].axhline(1, color='#666666', ls='--', lw=1.7, label='nondispersive speed')
axes[1].set(xlabel=r'$k/\kappa$', ylabel='speed relative to sound', title='Phase and group velocities', xlim=(0,4), ylim=(0,4.4))
axes[1].legend(loc='upper right', fontsize=9, frameon=False)
for ax in axes:
    ax.grid(alpha=.2)
fig.subplots_adjust(left=.075, right=.98, bottom=.18, top=.88, wspace=.28)
fig.savefig(output, facecolor='white', transparent=False)
print(output)
