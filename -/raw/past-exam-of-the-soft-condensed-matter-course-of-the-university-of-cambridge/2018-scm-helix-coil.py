"""Original helix-coil fraction curves. Python 3.14; NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(9.7, 4.8), facecolor='white')
colours = ['#777777', '#2582aa', '#c6852c', '#a64c70']
parameters = [1., .1, .01, .0001]
for ax, domain in zip(axes, (np.logspace(-2, 2, 3001), np.linspace(.75, 1.25, 3001))):
    for sigma, color in zip(parameters, colours):
        h = .5+(domain-1)/(2*np.sqrt((domain-1)**2+4*domain*sigma))
        ax.plot(domain, h, color=color, linewidth=2, label=fr'$\sigma={sigma:g}$')
    ax.axvline(1, linestyle=':', color='#888888', linewidth=.9)
    ax.axhline(.5, linestyle=':', color='#888888', linewidth=.9)
    ax.plot(1, .5, 'o', color='#222222', markersize=4)
    ax.set(ylim=(-.02, 1.02), xlabel='propagation factor $s$', ylabel='helical fraction $f_h$')
    ax.grid(alpha=.15)
    ax.spines[['top', 'right']].set_visible(False)
axes[0].set_xscale('log')
axes[0].set(xlim=(.01, 100), title='Coil-dominated to helix-dominated')
axes[0].legend(frameon=False, fontsize=10, loc='upper left')
axes[1].set(xlim=(.75, 1.25), title='Smaller initiation factor: sharper crossover')
axes[1].annotate(r'common midpoint $(1,\frac{1}{2})$', xy=(1, .5), xytext=(1.025, .23), fontsize=10,
                 arrowprops=dict(arrowstyle='->', color='#444444'))
fig.text(.5, .025, r'Every fixed $\sigma>0$ gives a smooth curve; $f_h\prime(1)=1/(4\sqrt{\sigma})$.',
         ha='center', fontsize=11)
fig.subplots_adjust(left=.07, right=.98, bottom=.18, top=.86, wspace=.27)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
plt.close(fig)
