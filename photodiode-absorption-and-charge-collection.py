"""Original junction/collection schematic. Python 3.14, matplotlib 3.10.7.
Run from _media; writes the matching opaque PNG to the working directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(10, 5.8), facecolor='white')
ax.set(xlim=(0, 10), ylim=(0, 5.8))
ax.axis('off')
ax.text(5, 5.53, 'From absorbed light to collected charge', ha='center', fontsize=18, weight='bold')
regions = [(1.35, 2.15, '#fbe5da', 'p region'), (3.5, 3, '#fff4ce', 'depletion region'), (6.5, 2.15, '#dfedf7', 'n region')]
for x, w, color, label in regions:
    ax.add_patch(Rectangle((x, 2.3), w, 2.05, facecolor=color, edgecolor='#666666'))
    ax.text(x+w/2, 4.07, label, ha='center', fontsize=12, bbox={'facecolor': color, 'edgecolor': 'none', 'pad': 2}, zorder=5)
ax.text(1.15, 3.25, 'anode', rotation=90, ha='center', va='center')
ax.text(8.85, 3.25, 'cathode', rotation=90, ha='center', va='center')
ax.plot([1.35, 1.35, 3.9], [3.1, 1.05, 1.05], color='#444444', lw=2)
ax.plot([6.1, 8.65, 8.65], [1.05, 1.05, 3.1], color='#444444', lw=2)
ax.add_patch(Rectangle((3.9, .72), 2.2, .66, facecolor='white', edgecolor='#444444', lw=2))
ax.text(5, 1.05, r'load $R_L$', ha='center', va='center')
ax.annotate('', (7.7, 1.05), (6.7, 1.05), arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': '#444444'})
ax.text(7.2, .48, 'conventional current', ha='center', fontsize=11)
ax.text(2.4, 1.59, 'external circuit', ha='center', fontsize=11)
# A photon is absorbed near the junction; the arrows are carrier collection paths.
ax.annotate('', (5, 3.45), (5, 4.87), arrowprops={'arrowstyle': '-|>', 'lw': 3, 'color': '#b02e35'})
ax.text(5, 5.02, r'photon $E_\gamma=hc/\lambda$', ha='center', color='#a6282e')
for x, text, color in [(4.62, r'$h^+$', '#bd663b'), (5.38, r'$e^-$', '#236da2')]:
    ax.add_patch(Circle((x, 3.05), .23, facecolor='white', edgecolor=color, lw=2))
    ax.text(x, 3.05, text, ha='center', va='center', color=color)
ax.annotate('', (2.25, 3.05), (4.32, 3.05), arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': '#bd663b'})
ax.annotate('', (7.75, 3.05), (5.68, 3.05), arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': '#236da2'})
ax.annotate('', (4.05, 2.56), (5.95, 2.56), arrowprops={'arrowstyle': '-|>', 'lw': 1.7, 'color': '#696047'})
ax.text(5, 2.05, 'junction electric field', ha='center', fontsize=11, color='#696047')
ax.text(5, .04, r'One collected pair transfers $q$ through the external wire, not $2q$.', ha='center', fontsize=13)
fig.subplots_adjust(left=.02, right=.98, bottom=.04, top=.98)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=130, facecolor='white', transparent=False)
plt.close(fig)
