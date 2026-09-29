"""Draw the original free-draining dumbbell geometry; output PNG in cwd.

Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7.
See the repository pyproject.toml. No examination artwork is reproduced.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13})
a1, a2, separation = 0.55, 1.1, 10.0
centre = a2 * separation / (a1 + a2)
fig, ax = plt.subplots(figsize=(10.8, 3.8), dpi=120, facecolor='white')
ax.set_facecolor('white')
ax.plot([a1, separation - a2], [0, 0], color='#69727a', lw=2, zorder=1)
for x, a, label in [(0, a1, '$a_1$'), (separation, a2, '$a_2$')]:
    ax.add_patch(Circle((x, 0), a, facecolor='#d8eafb', edgecolor='#225d95', lw=2, zorder=2))
    ax.plot([x, x + a], [0, 0], color='#225d95', lw=1.3, zorder=3)
    ax.text(x, -a - 0.48, label, ha='center', color='#225d95')
    ax.annotate('', xy=(x - 1.6 * a, 1.65), xytext=(x, 1.65),
                arrowprops={'arrowstyle': '-|>', 'color': '#b33332', 'lw': 2, 'mutation_scale': 16})
    ax.text(x - 0.8 * a, 2.1, r'$\mathbf{f}_i=-6\pi\mu a_i\mathbf{U}$', ha='center', color='#b33332', fontsize=12)
ax.plot(centre, 0, 'o', color='#7d318f', ms=7, zorder=4)
ax.annotate(r'$\mathbf{r}_c$', xy=(centre, 0), xytext=(centre - 0.6, -1.35),
            color='#7d318f', ha='center', arrowprops={'arrowstyle': '->', 'color': '#7d318f'})
ax.annotate('', xy=(centre + 1.3, 1.45), xytext=(centre - 1.1, 1.45),
            arrowprops={'arrowstyle': '-|>', 'color': '#187443', 'lw': 2, 'mutation_scale': 16})
ax.text(centre + 0.1, 1.9, r'$\mathbf{U}$', color='#187443', ha='center')
ax.text(0, 0.9, r'$\mathbf{r}_1$', ha='center')
ax.text(separation, 1.35, r'$\mathbf{r}_2$', ha='center')
ax.text(5, -2.1, r'$\mathbf{r}_c=\dfrac{a_1\mathbf{r}_1+a_2\mathbf{r}_2}{a_1+a_2}$',
        ha='center', color='#7d318f', fontsize=17)
ax.set_title('Free-draining approximation: the centre lies nearer the larger drag', pad=14, fontsize=14)
ax.set(xlim=(-2, 12.8), ylim=(-2.65, 2.7))
ax.set_aspect('equal', adjustable='box')
ax.axis('off')
fig.subplots_adjust(left=0.025, right=0.985, bottom=0.035, top=0.87)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
