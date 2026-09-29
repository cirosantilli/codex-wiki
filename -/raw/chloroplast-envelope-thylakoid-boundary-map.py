"""Original chloroplast compartment diagram. Python 3.14; matplotlib 3.10.7.
Run from the output directory; writes this script's basename + .png to CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

INK = '#203342'
GREEN = '#27764c'
BLUE = '#a7d9ed'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'text.color': INK})
fig, ax = plt.subplots(figsize=(12, 7.4), dpi=110)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 12), ylim=(0, 7.4))
ax.axis('off')

def box(x, y, w, h, fc, ec=INK, lw=1.5, radius=.12):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={radius}', fc=fc, ec=ec, lw=lw)
    ax.add_patch(p)
    return p

def label(text, xy, dest, align='left', color=INK):
    ax.annotate(text, xy=dest, xytext=xy, ha=align, va='center', color=color,
                arrowprops={'arrowstyle': '-', 'color': color, 'lw': 1.2})

ax.text(.3, 7.06, 'Chloroplast: which side of which boundary?', fontsize=20, weight='bold')
ax.text(.3, 6.68, 'Original simplified section • membrane thickness and spacing enlarged', fontsize=11)
box(.45, 2.9, 6.2, 3.3, '#f2f7eb', GREEN, 2.5, .65)
box(.66, 3.11, 5.78, 2.88, '#e5f2de', GREEN, 2.5, .48)
ax.text(.98, 5.55, 'STROMA', color=GREEN, weight='bold', fontsize=14)
for y in (3.52, 3.91, 4.30):
    box(1.65, y, 2.4, .25, BLUE, GREEN, 2, .10)
ax.text(2.85, 4.86, 'granum = stack of thylakoids', ha='center', fontsize=11)
label('Outer envelope membrane', (7.2, 6.1), (6.30, 6.04))
label('Intermembrane space', (7.2, 5.65), (6.48, 5.45))
label('Inner envelope membrane', (7.2, 5.2), (6.43, 4.95))
ax.text(.48, 2.59, 'Surrounding cytosol', fontsize=12)
# Local enlargement uses two separate sacs to show intervening stromal space.
box(7.2, 3.86, 4.3, .62, BLUE, GREEN, 3)
box(7.2, 2.83, 4.3, .62, BLUE, GREEN, 3)
ax.text(9.35, 4.17, 'Thylakoid lumen', ha='center', va='center', fontsize=13)
ax.text(9.35, 3.14, 'Thylakoid lumen', ha='center', va='center', fontsize=13)
ax.text(9.35, 3.65, 'Stroma between sacs', ha='center', va='center', fontsize=12, color=GREEN)
ax.annotate('Thylakoid membrane', xy=(11.28, 4.48), xytext=(9.35, 4.76), ha='center', fontsize=11,
            arrowprops={'arrowstyle': '-', 'color': GREEN})
ax.plot([4.12, 6.86, 7.04], [4.49, 4.75, 4.50], '--', color='#94a3aa', lw=1)
ax.text(.3, 2.05, 'Constructed access route: count barriers, not bilayer leaflets', weight='bold', fontsize=14)
xs = [.35, 3.36, 6.37, 9.38]
texts = ['Cytosol', 'Envelope\nintermembrane space', 'Stroma', 'Thylakoid\nlumen']
colors = ['#f3f5f7', '#f2f7eb', '#e5f2de', BLUE]
for x, t, c in zip(xs, texts, colors):
    box(x, .75, 2.27, .8, c)
    ax.text(x+1.135, 1.15, t, ha='center', va='center', fontsize=12)
for i, t in enumerate(['outer', 'inner', 'thylakoid']):
    x0=xs[i]+2.27; x1=xs[i+1]
    ax.annotate('', xy=(x1, 1.15), xytext=(x0, 1.15), arrowprops={'arrowstyle': '->', 'color': INK, 'lw': 1.8})
    ax.text((x0+x1)/2, 1.69, t, ha='center', fontsize=10)
ax.text(6.37, .39, '2 barriers from cytosol', ha='left', fontsize=11)
ax.text(9.38, .39, '3 barriers from cytosol', ha='left', fontsize=11)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', dpi=110)
plt.close(fig)
