"""Original delta-shell scattering-length sketch; save the PNG to cwd.

Tested with Python 3.14; dependencies are listed in the root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7, 4.2), layout='constrained')
left = np.linspace(-5, -1.025, 650)
mid = np.linspace(-.975, 0, 650)
right = np.linspace(0, 4, 650)
ax.plot(left, left/(1+left), color='#ad4b20', linewidth=2.2, label='Attraction: $g<0$')
ax.plot(mid, mid/(1+mid), color='#ad4b20', linewidth=2.2)
ax.plot(right, right/(1+right), color='#2465a6', linewidth=2.2, label='Repulsion: $g>0$')
ax.axvline(-1, color='#555555', linestyle='--', linewidth=1.2)
ax.axhline(1, color='#777777', linestyle=':', linewidth=1.2, label=r'$a_0/R\to1$')
ax.axhline(0, color='black', linewidth=.65)
ax.axvline(0, color='black', linewidth=.65)
ax.scatter([0], [0], s=24, color='black', zorder=4)
ax.annotate('Bound-state threshold', xy=(-1, 4.4), xytext=(-4.7, 4.9), arrowprops={'arrowstyle':'->', 'color':'#555555'}, fontsize=10)
ax.text(-4.75, 2.0, '$g<-1$: one S-wave bound state', fontsize=10, color='#87401e')
ax.set(xlim=(-5,4), ylim=(-5,6), xticks=[-5,-3,-1,0,2,4], yticks=[-4,-2,0,1,2,4,6], xlabel=r'$g=2mV_0R/\hbar^2$', ylabel=r'$a_0/R=g/(1+g)$', title='Delta-shell scattering length')
ax.spines[['top','right']].set_visible(False)
ax.legend(loc='upper right', frameon=True)
ax.grid(alpha=.17)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=170, facecolor='white')
