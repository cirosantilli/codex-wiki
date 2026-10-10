"""Illustrate stipulated populations, charge neutrality and arrow conventions.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is an opaque white PNG in the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

BLUE = '#2468a0'
ORANGE = '#bb6425'
GREEN = '#278354'
plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 2, figsize=(10, 6.6), dpi=120)
fig.patch.set_facecolor('white')
for ax, s, title in zip(axes, (0, 0.35), ('Equal allocation: s = 0', 'Unequal allocation: s = 0.35')):
    ax.set(xlim=(-0.6, 2.6), ylim=(-3.15, 2.35))
    ax.axis('off')
    ax.set_title(title, fontsize=15, pad=8, weight='bold')
    ax.text(1, 1.95, 'Expected electron populations', ha='center', fontsize=12)
    populations = (1-s, 1+s)
    ax.bar((0, 2), populations, bottom=0, width=0.55,
           color=(ORANGE, BLUE), alpha=0.8)
    ax.plot([-0.35, 2.35], [0, 0], color='#666666', lw=1)
    for x, n, name in zip((0, 2), populations, ('A', 'B')):
        ax.text(x, n+0.08, f'{n:g}', ha='center', fontsize=15)
        ax.text(x, -0.20, name, ha='center', fontsize=14, weight='bold')
    ax.text(1, -0.60, 'Total population = 2', ha='center')
    ax.plot([0, 2], [-1.18, -1.18], color='#888888', lw=2, zorder=0)
    for x, name, color in ((0, 'A', ORANGE), (2, 'B', BLUE)):
        ax.add_patch(Circle((x, -1.18), 0.19, facecolor='white', edgecolor=color, lw=2))
        ax.text(x, -1.18, name, ha='center', va='center', weight='bold')
    charges = ('0', '0') if s == 0 else (r'$+0.35e$', r'$-0.35e$')
    for x, label in zip((0, 2), charges):
        ax.text(x, -1.59, label, ha='center', fontsize=15)
    if s:
        ax.annotate('', xy=(1.95, -2.12), xytext=(0.05, -2.12),
                    arrowprops={'arrowstyle': '->', 'color': GREEN, 'lw': 2.5})
        ax.plot([0.08, 0.08], [-2.23, -2.01], color=GREEN, lw=2)
        ax.text(1, -1.89, 'Chemical arrow: toward negative end', ha='center', fontsize=11, color=GREEN)
        ax.annotate('', xy=(0.05, -2.75), xytext=(1.95, -2.75),
                    arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 2.5})
        ax.text(1, -2.51, r'Physical $\mathbf{p}$: negative to positive', ha='center', fontsize=11, color=BLUE)
    else:
        ax.text(1, -2.10, 'No separation of effective charge', ha='center', fontsize=12)
        ax.text(1, -2.70, r'$q_A+q_B=0,\quad \mathbf{p}=\mathbf{0}$', ha='center', fontsize=15)
fig.suptitle('Bond polarization: allocation is a model, not an electronegativity reading',
             fontsize=15, weight='bold', y=0.975)
fig.text(0.5, 0.028, 'Each effective site contributes +e. Assigned electrons contribute −e each.\n'
         'Stipulated bookkeeping only; no measured density or χ-to-charge conversion.',
         ha='center', fontsize=11, linespacing=1.6)
fig.subplots_adjust(left=0.055, right=0.96, top=0.88, bottom=0.15, wspace=0.25)
fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), facecolor='white')
plt.close(fig)
