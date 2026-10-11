"""Original excluded-volume isotherms, Python 3.14; pyproject dependencies.
Writes PNG basename in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6.2, 4.3), facecolor='white', layout='constrained')
v = np.linspace(1.015, 5, 800)
for ratio, color in [(.8,'#176a98'), (1.2,'#bd6720'), (1.8,'#a23b42')]:
    ax.plot(v, ratio/(v-1), color=color, lw=2, label=f'$T/T_{{\\rm ref}}={ratio:g}$')
ax.axvline(1, color='0.4', ls='--', lw=1)
ax.text(.96, 4.2, '$V=b$', rotation=90, ha='right')
ax.set(xlabel='$V/b$', ylabel='$pb/(RT_{\\rm ref})$', title='Repulsive excluded volume: monotone isotherms', xlim=(.8,5), ylim=(0,5))
ax.legend(frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
plt.close(fig)
