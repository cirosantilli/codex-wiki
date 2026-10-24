"""Original characteristic-region figure. Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the output directory; writes a PNG there. Dependencies in wiki pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.3), constrained_layout=True)
fig.patch.set_facecolor('white')
x = np.linspace(.001, 2, 700)
for ax, sign in zip(axes, [1, -1]):
    lower = 1 - 1 / x
    caustic = x / 4
    ax.fill_between(x, sign * lower, sign * caustic, color='#dce9f4', alpha=1)
    xf = np.linspace(.001, 2, 500)
    lowf = np.where(xf <= 1, 0, 1 - 1 / xf)
    ax.fill_between(xf, sign * lowf, sign * xf / 4, color='#6aabd1', alpha=.8)
    for s in [.15, .3, .5, .7, .9, 1]:
        times = np.linspace(-2, np.log(2), 150)
        xx = s * np.exp(times)
        yy = sign * s * (1 - np.exp(-times))
        ax.plot(xx, yy, color='#275174', lw=.8, alpha=.7)
    ax.plot(x, sign * lower, color='#d56824', lw=2, label=r'$s=1$ boundary')
    ax.plot([0, 2], [0, sign * .5], '--', color='#bd3333', lw=2, label=r'caustic: $y=\varepsilon x/4$')
    ax.plot([0, 1], [0, 0], color='black', lw=3, label='initial segment')
    ax.scatter([2], [sign * .5], s=20, color='#bd3333')
    ax.set(xlim=(0, 2.12), ylim=(-.9, .65) if sign == 1 else (-.65, .9), xlabel='$x$', ylabel='$y$', title=rf'Initial normal derivative $q_0={"+" if sign == 1 else "-"}2s$')
    ax.grid(alpha=.2)
    ax.legend(loc='lower right' if sign == 1 else 'upper right', fontsize=8, framealpha=.96)
fig.suptitle('Characteristic charts before the first fold', fontsize=15)
fig.legend(handles=[Patch(facecolor='#6aabd1', label=r'forward: $0\leq t<\log 2$'), Patch(facecolor='#dce9f4', label=r'continuation: $t<0$')], loc='outside lower center', ncol=2, frameon=False)
fig.savefig('2010-charpit-regions.png', dpi=150, facecolor='white')
