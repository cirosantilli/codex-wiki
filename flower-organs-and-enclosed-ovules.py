"""Original schematic of flower organs; tested with Python 3.14 / matplotlib 3.10.7.
Run from _media; writes an opaque PNG named after this generator to the CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Polygon, FancyBboxPatch

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig, axes = plt.subplots(1, 2, figsize=(10.2, 6.2), dpi=100,
                         gridspec_kw={'width_ratios': [1.4, 1]})
fig.patch.set_facecolor('white')
fig.suptitle('Flower organs and enclosed ovules', fontsize=18, y=.97)
ax, detail = axes
for a in axes:
    a.set(xlim=(0, 10), ylim=(0, 10))
    a.axis('off')
    a.set_facecolor('white')

# A schematic longitudinal section, deliberately not copied from a source image.
ax.plot([5, 5], [.7, 2.2], color='#487946', lw=12, zorder=0)
for side in [-1, 1]:
    ax.add_patch(Ellipse((5+side*1.45, 4.0), 2.1, 5.2,
                         angle=side*-35, facecolor='#f7d8e7', edgecolor='#b46b90'))
    ax.add_patch(Polygon([(5, 2), (5+side*3.1, 2.8), (5+side*1.7, 1.8)],
                         facecolor='#cce1b9', edgecolor='#487946'))
    ax.plot([5+side*1.15, 5+side*1.65], [2.3, 6.1], color='#bd862e', lw=4)
    ax.add_patch(Ellipse((5+side*1.65, 6.5), .65, 1.2,
                         angle=side*-15, facecolor='#f0c14b', edgecolor='#9d6818'))
    for dy in [-.25, 0, .25]:
        ax.add_patch(Circle((5+side*1.65, 6.5+dy), .08,
                            facecolor='#9d6818', edgecolor='none'))
ax.add_patch(Ellipse((5, 3.0), 2, 2.4, facecolor='#dceceb', edgecolor='#26675d', lw=2))
ax.add_patch(FancyBboxPatch((4.78, 3.8), .44, 3.7,
                           boxstyle='round,pad=0.02', facecolor='#dceceb',
                           edgecolor='#26675d', lw=2))
ax.add_patch(Ellipse((5, 7.65), 1.65, .58, facecolor='#98cbbb', edgecolor='#26675d', lw=2))
for x, y in [(4.6, 2.65), (5.3, 3.0), (4.75, 3.45)]:
    ax.add_patch(Ellipse((x, y), .38, .57, angle=20,
                         facecolor='#fff7c2', edgecolor='#9b852d'))

def label(text, xy, pos, align='left'):
    ax.annotate(text, xy=xy, xytext=pos, ha=align, va='center', fontsize=11,
                arrowprops={'arrowstyle': '-', 'lw': 1, 'color': '#434b52'},
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1.2})
label('Anther\nproduces pollen', (3.35, 6.55), (.1, 8.1))
label('Filament', (3.6, 4.2), (.1, 6.0))
label('Petal', (2.6, 4.7), (.1, 4.4))
label('Sepal', (2.7, 2.45), (.1, 2.45))
label('Stigma\nreceives pollen', (5.7, 7.65), (6.5, 8.85))
label('Style', (5.23, 5.65), (7.2, 6.0))
label('Ovary\nencloses ovules', (5.95, 3.0), (7.0, 4.05))
label('Ovule', (5.35, 3.0), (7.15, 2.4))
ax.text(5, .1, 'Both reproductive groups shown', ha='center', fontsize=11, color='#48515b')
ax.text(5, 9.85, 'Organ positions: schematic cutaway', ha='center', fontsize=12, weight='bold')

# Magnification is conceptual; the dashed line has no quantitative scale.
detail.text(5, 9.85, 'Inside one ovule', ha='center', fontsize=12, weight='bold')
detail.add_patch(Ellipse((4.9, 5.4), 6.8, 6.6, facecolor='#fff7d7', edgecolor='#9b852d', lw=2))
detail.add_patch(Ellipse((4.9, 5.4), 4.7, 4.8, facecolor='#edf6f3', edgecolor='#26675d', lw=2))
detail.add_patch(Ellipse((4.9, 5.8), 3.3, 2.8, facecolor='#dceceb', edgecolor='#78a59a'))
for x in [4.4, 5.4]:
    detail.add_patch(Circle((x, 6), .21, facecolor='#7157a1'))
detail.add_patch(Circle((4.9, 3.7), .43, facecolor='#ecd7ea', edgecolor='#9d559b'))
detail.add_patch(Circle((4.9, 3.7), .13, facecolor='#7157a1'))
detail.text(4.9, 7.05, 'Central cell', ha='center', fontsize=11)
detail.text(4.9, 5.1, 'Two polar nuclei', ha='center', fontsize=10)
detail.text(4.9, 2.8, 'Egg cell', ha='center', fontsize=11)
detail.text(4.9, 9.05, 'Ovule tissues', ha='center', fontsize=11)
detail.annotate('Female gametophyte\n(embryo sac)', xy=(7.2, 5.4), xytext=(5, 1.35),
                ha='center', fontsize=11, arrowprops={'arrowstyle':'-', 'color':'#434b52'})
detail.text(5, .1, 'Other embryo-sac cells omitted', ha='center', fontsize=10, color='#48515b')
fig.text(.5, .018, 'Original explanatory drawing • Not to scale • Flower structure and embryo sacs vary among species',
         ha='center', fontsize=10, color='#48515b')
fig.subplots_adjust(left=.025, right=.985, bottom=.075, top=.86, wspace=.1)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
plt.close(fig)
