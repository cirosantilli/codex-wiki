"""Illustrate the Pease balance; write the PNG basename to caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, (ax, curve) = plt.subplots(1, 2, figsize=(10, 3.8), layout='constrained')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.add_patch(Rectangle((0, 0), .7, 2.5, color='#ded6bf'))
ax.add_patch(Rectangle((.7, 0), 5.3, 1.1, color='#d6edf8'))
ax.add_patch(Rectangle((4.1, 1.1), 1.9, .45, facecolor='#cbd5df', edgecolor='#536878'))
ax.plot([.7, 4.1], [1.1, 1.1], color='#4799c3')
ax.text(.33, 1.35, 'Coast', rotation=90, ha='center', va='center')
ax.text(2.4, .4, 'Ocean at freezing', ha='center')
ax.text(2.4, 1.32, 'Open water / frazil ice', ha='center')
ax.text(5, 1.75, 'Collected ice', ha='center')
ax.annotate('', xy=(5.7, 2.2), xytext=(1.2, 2.2), arrowprops={'arrowstyle': '->', 'lw': 1.7})
ax.text(3.45, 2.3, 'Offshore wind and drift U', ha='center')
for x in [1.3, 2.3, 3.3]:
 ax.annotate('', xy=(x, 1.12), xytext=(x, .8), arrowprops={'arrowstyle': '->', 'color': '#225d87'})
ax.text(2.35, .65, 'Ice production F', ha='center', color='#225d87')
ax.annotate('', xy=(4.1, -.16), xytext=(.7, -.16), arrowprops={'arrowstyle': '<->'})
ax.text(2.4, -.35, 'Width L(t)', ha='center')
ax.annotate('', xy=(5.9, 1.55), xytext=(5.9, 1.1), arrowprops={'arrowstyle': '<->'})
ax.text(6.02, 1.33, 'H', va='center')
ax.set_xlim(-.1, 6.5)
ax.set_ylim(-.5, 2.75)
ax.axis('off')
ax.set_title('Production balances export at the moving edge')
t = np.linspace(0, 8, 400)
U, H = .05, .1  # m/s and m; illustrative fixed drift and collection thickness.
for F_day, label, color in [(.1, 'Cool air: F = 0.10 m/day', '#226ea5'), (.05, 'Warmer air: F = 0.05 m/day', '#bf603c')]:
 F = F_day / 86400
 tau = H / F_day
 width = H * U / F / 1000
 curve.plot(t, width * (-np.expm1(-t / tau)), label=label, color=color, lw=2)
 curve.axhline(width, color=color, lw=.8, ls='--')
curve.set(xlabel='Time (days)', ylabel='Polynya width (km)', xlim=(0, 8), ylim=(0, 9.5), title='Less freezing: wider opening, longer relaxation')
curve.grid(alpha=.2)
curve.legend(loc='lower right', fontsize=8)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=125, facecolor='white', transparent=False)
plt.close(fig)
