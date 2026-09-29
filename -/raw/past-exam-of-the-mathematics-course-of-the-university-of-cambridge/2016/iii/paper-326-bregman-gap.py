#!/usr/bin/env python3
"""Draw the absolute-value Bregman gap; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6.8, 3.6), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
x = np.linspace(-1.65, 1.65, 501)
ax.plot(x, np.abs(x), color='#235b9a', linewidth=2.2, label=r'$E(x)=|x|$')
ax.axhline(0, color='#6b7280', linewidth=1.6, label=r'Supporting line for $p=0$')
ax.axvline(0, color='#aeb4bb', linewidth=.7)
ax.plot([1, 1], [0, 1], color='#b43b32', linewidth=3)
ax.scatter([1, 1], [0, 1], color='#b43b32', s=32, zorder=3)
ax.annotate(r'$D_E^0(1,0)=1$', xy=(1, .5), xytext=(.25, .58), color='#a32f29', fontsize=12,
            arrowprops={'arrowstyle':'->', 'color':'#a32f29'})
ax.set(xlim=(-1.65, 1.65), ylim=(-.17, 1.85), xlabel=r'$x$', ylabel='Function and supporting line',
       title='Bregman distance as a vertical gap')
ax.set_xticks([-1, 0, 1])
ax.set_yticks([0, 1])
ax.spines[['top', 'right']].set_visible(False)
ax.legend(loc='upper center', frameon=False, fontsize=9)
fig.tight_layout()
fig.savefig(Path.cwd() / 'paper-326-bregman-gap.png', facecolor='white', transparent=False)
plt.close(fig)
