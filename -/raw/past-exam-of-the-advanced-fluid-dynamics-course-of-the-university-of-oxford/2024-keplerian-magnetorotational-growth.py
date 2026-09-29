"""Original ideal-MRI dispersion plot; save same-basename PNG in cwd.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
x = np.linspace(0, 2.1, 701)
a = x*x
omega_squared = a + 0.5 - 0.5*np.sqrt(1 + 16*a)
growth = np.sqrt(np.maximum(-omega_squared, 0))
fig, ax = plt.subplots(figsize=(7.6, 4.5), dpi=130, facecolor='white')
ax.set_facecolor('white')
ax.axvspan(0, np.sqrt(3), color='#e7f0fa', label='Exponentially unstable band')
ax.axvspan(np.sqrt(3), 2.1, color='#f0f3ee')
ax.plot(x, growth, color='#aa3e1f', lw=2.5)
xmax, ymax = np.sqrt(15)/4, .75
ax.plot(xmax, ymax, 'o', color='#aa3e1f', ms=6)
ax.annotate(r'$s_{\max}=3\Omega/4$', xy=(xmax, ymax), xytext=(1.22, .82),
            arrowprops={'arrowstyle': '->', 'color': '#6d3b22'}, color='#6d3b22')
ax.axvline(np.sqrt(3), ls='--', color='#68715d', lw=1.2)
ax.text(1.91, .37, 'Oscillatory\nmagnetic modes', ha='center', color='#4a5743', fontsize=11)
ax.set(xlim=(0, 2.1), ylim=(-.025, .95), xlabel=r'Vertical Alfvén frequency $k v_A/\Omega$',
       ylabel=r'Growth rate $s/\Omega$', title='Ideal magnetorotational instability in a Keplerian disk')
ax.set_xticks([0, .5, 1, 1.5, np.sqrt(3), 2], ['0', '0.5', '1', '1.5', r'$\sqrt{3}$', '2'])
ax.set_yticks([0, .25, .5, .75])
ax.spines[['top', 'right']].set_visible(False)
ax.grid(alpha=.18)
ax.legend(loc='upper left', frameon=False, fontsize=10)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
