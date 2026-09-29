"""Original counting schematic. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Run from _media: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/codex-wiki-matplotlib
python ../magnetic-sublattice-order-comparison.py
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(3, 1, figsize=(9, 6.6), facecolor='white')
colors = ['#176b9c', '#bd4828']
rows = [
    ('Ferromagnetism', 1, 1, r'$m_{\rm net}=6m_0$'),
    ('Antiferromagnetism', 1, -1, r'$m_{\rm net}=0$'),
    ('Ferrimagnetism', 2, -1, r'$m_{\rm net}=3m_0$'),
]
for ax, (name, a, b, result) in zip(axes, rows):
    ax.set(xlim=(-.8, 8.2), ylim=(-1.4, 1.7))
    ax.axis('off')
    ax.text(-.7, 1.45, name, weight='bold', va='top', fontsize=14)
    ax.plot([0, 5], [0, 0], color='#d6dce1', lw=1)
    for i in range(6):
        value = a if i % 2 == 0 else b
        y0, y1 = (-.37 * value, .37 * value)
        ax.add_patch(FancyArrowPatch((i, y0), (i, y1),
                     arrowstyle='-|>', mutation_scale=19, lw=2.8,
                     color=colors[i % 2]))
        ax.text(i, -1.05, 'A' if i % 2 == 0 else 'B', ha='center',
                color=colors[i % 2], weight='bold')
    ax.text(5.65, .2, result, fontsize=16)
    ax.text(5.65, -.45, 'same six-site volume', color='#4e5964', fontsize=11)
fig.suptitle('Ordered moments: the sum does not tell the whole story',
             fontsize=16, weight='bold', y=.98)
fig.text(.5, .02, 'Stipulated site moments • arrow lengths encode magnitude • not a material structure',
         ha='center', fontsize=11, color='#4e5964')
fig.subplots_adjust(top=.88, bottom=.08, hspace=.2, left=.06, right=.98)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120,
            facecolor='white', transparent=False)
