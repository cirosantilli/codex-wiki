"""Original chromosome/DNA ledger; Python 3.14 / matplotlib 3.10.7.

Run from _media. One stroke = one double-stranded nuclear DNA molecule.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(12, 6.6), dpi=100, facecolor='white')
ax.set(xlim=(0, 12), ylim=(0, 6.6))
ax.axis('off')
ax.text(6, 6.25, 'Count chromosomes separately from DNA copies',
        ha='center', fontsize=19, weight='bold', color='#18354b')
ax.text(6, 5.88, 'Hypothetical diploid cell (2n = 4) • Nuclear DNA only • One stroke = one double-stranded DNA molecule',
        ha='center', fontsize=11)
for x, label in [(1.5, 'Counting compartment'), (4.7, 'Chromosome identities'),
                 (7.4, 'Chromosomes'), (9.25, 'DNA molecules'), (10.95, 'DNA amount')]:
    ax.text(x, 5.33, label, weight='bold', fontsize=12, ha='center')

colors = ['#2456a6', '#cc512d', '#2456a6', '#cc512d']
names = ['A', 'a', 'B', 'b']

def stroke(x, y, color, replicated=False):
    if replicated:
        for sign in [-1, 1]:
            ax.plot([x+sign*.085, x+sign*.024, x+sign*.085],
                    [y+.18, y, y-.18], color=color, lw=4, solid_capstyle='round')
        ax.plot([x-.024, x+.024], [y, y], color='#253447', lw=2.5)
    else:
        ax.plot([x, x], [y-.18, y+.18], color=color, lw=4, solid_capstyle='round')

ys = [4.67, 3.66, 2.65, 1.64]
rows = [('G₁ parent', 'Before S phase', '4', '4', '2C'),
        ('Prophase / metaphase', 'After S phase; one cell', '4', '8', '4C'),
        ('Anaphase: whole cell', 'Sisters separated; still one cell', '8', '8', '4C total'),
        ('Each completed daughter', 'After mitosis + cytokinesis', '4', '4', '2C each')]
for i, (y, row) in enumerate(zip(ys, rows)):
    ax.add_patch(FancyBboxPatch((.2, y-.43), 11.6, .86, boxstyle='round,pad=.02',
                               edgecolor='#d6dee6', facecolor=['#f4f7fb', '#edf4fd', '#fff3df', '#eef7f0'][i]))
    ax.text(.42, y+.12, row[0], fontsize=12, weight='bold', va='center')
    ax.text(.42, y-.17, row[1], fontsize=10, color='#526879', va='center')
    for x, value in zip([7.4, 9.25, 10.95], row[2:]):
        ax.text(x, y, value, ha='center', va='center', fontsize=17, weight='bold', color='#18354b')
    if i == 2:
        for shift in [-.72, .72]:
            for x, color, name in zip([-.43, -.15, .15, .43], colors, names):
                stroke(4.7+shift+x, y+.04, color)
                ax.text(4.7+shift+x, y-.28, name, ha='center', fontsize=10, color=color, weight='bold')
        ax.plot([4.7, 4.7], [y-.35, y+.35], ls=':', color='#8595a4', lw=1)
    else:
        for x, color, name in zip([3.98, 4.46, 4.94, 5.42], colors, names):
            stroke(x, y+.04, color, replicated=i == 1)
            ax.text(x, y-.29, name, ha='center', fontsize=10, color=color, weight='bold')

ax.text(6, .77, 'No new DNA is made at sister separation: 8 molecules → 4 in one daughter + 4 in the other.',
        ha='center', fontsize=12, weight='bold', color='#18354b')
ax.text(6, .38, 'Each daughter receives A, a, B, b: both homologues of both pairs. Faithful segregation and no mutations assumed.',
        ha='center', fontsize=11, color='#526879')
fig.subplots_adjust(left=.015, right=.985, bottom=.015, top=.985)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
