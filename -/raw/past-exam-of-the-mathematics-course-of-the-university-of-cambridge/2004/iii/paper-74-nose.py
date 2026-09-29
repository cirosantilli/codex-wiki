"""Quasisteady nose; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Write an opaque PNG basename to caller CWD; honor caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
f = np.linspace(0, 1 - 1e-7, 3000)
y = f - np.arctanh(f)
fig, ax = plt.subplots(figsize=(7, 3.7), layout='constrained')
ax.plot(y, f, color='#176b91', linewidth=2.2)
ax.axhline(1, color='0.45', ls='--', linewidth=1)
ax.plot([0, 1], [0, 0], color='#176b91', linewidth=2.2)
ax.scatter([0], [0], color='#176b91', zorder=3)
ax.set(xlim=(-4, .6), ylim=(-.04, 1.1), xlabel=r'$\theta y/h_N$', ylabel=r'$h/h_N$', title='Quasisteady gravity-current nose')
ax.annotate('dry tip: small-slope model fails', xy=(0, 0), xytext=(-3, .28), arrowprops={'arrowstyle': '->', 'color': '0.3'}, fontsize=10)
ax.text(-3.9, 1.02, 'upstream height', fontsize=10, color='0.35')
ax.grid(alpha=.2)
fig.savefig('paper-74-nose.png', dpi=150, facecolor='white', transparent=False)
plt.close(fig)
