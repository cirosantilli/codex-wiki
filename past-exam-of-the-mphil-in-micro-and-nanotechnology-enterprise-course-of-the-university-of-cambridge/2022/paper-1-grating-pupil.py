"""Original coherent-pupil order selection schematic; Python 3.14/matplotlib.

The horizontal coordinate is spatial frequency in units of NA/lambda.
Output is a PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 1, figsize=(7.5, 4.5), layout='constrained')
fig.patch.set_facecolor('white')
for ax, step, title in zip(axes, [.72, 1.23],
                          ['First orders admitted: periodic contrast survives',
                           'First orders rejected: only a uniform field remains']):
    ax.axvspan(-1, 1, color='#d9e9ef', zorder=0)
    ax.axvline(-1, ls='--', color='#286a85', lw=1)
    ax.axvline(1, ls='--', color='#286a85', lw=1)
    ax.axhline(0, color='.45', lw=.8)
    for m in [-1, 0, 1]:
        pos = m * step
        admitted = abs(pos) < 1
        color = '#286a85' if admitted else '#b65c38'
        ax.annotate('', (pos, .72), (pos, 0),
                    arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': color})
        ax.text(pos, .84, f'order {m:+d}' if m else 'order 0',
                ha='center', color=color, fontsize=10)
    ax.set(xlim=(-1.6, 1.6), ylim=(-.08, 1.12), yticks=[],
           xticks=[-1, 0, 1], xticklabels=['−cutoff', '0', '+cutoff'],
           title=title)
axes[-1].set_xlabel(r'Transverse field spatial frequency; $\nu_c=\mathrm{NA}/\lambda$')
fig.savefig('paper-1-grating-pupil.png', dpi=150, facecolor='white')
plt.close(fig)
