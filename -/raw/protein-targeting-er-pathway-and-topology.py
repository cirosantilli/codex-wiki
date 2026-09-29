"""Draw ER delivery and three conditional topologies; emit PNG in the CWD.

Tested with Python 3.14, matplotlib 3.10.7. Coordinates are schematic.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse

INK = '#18354b'
BLUE = '#216b9a'
TEAL = '#087d79'
ORANGE = '#c37b16'
PURPLE = '#8056a5'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'text.color': INK, 'axes.edgecolor': INK})
fig = plt.figure(figsize=(12, 8.5), dpi=110, facecolor='white')
fig.text(.04, .96, 'Protein targeting: delivery first, topology next', fontsize=19, weight='bold')
fig.text(.04, .925, 'Common SRP-dependent ER route • original schematic, no physical scale', fontsize=11)
ax = fig.add_axes([.035, .53, .93, .36])
ax.set(xlim=(0, 12), ylim=(0, 4)); ax.axis('off')

def box(x, title, detail):
    ax.add_patch(FancyBboxPatch((x, 2.55), 3.3, 1.25, boxstyle='round,pad=.08',
                               facecolor='#f2f7fa', edgecolor='#a2b9c8'))
    ax.text(x+.16, 3.49, title, fontsize=12, weight='bold', va='center')
    ax.text(x+.16, 3.02, detail, fontsize=10.5, va='center', linespacing=1.35)
box(.15, '1  Recognition', 'Signal emerges from ribosome;\nSRP binds signal and ribosome.')
box(4.25, '2  Docking', 'SRP receptor receives cargo;\nhandoff brings chain to Sec61.')
box(8.35, '3  Crossing / insertion', 'Ribosome stays cytosolic;\ngrowing chain enters channel.')
for x in (3.6, 7.7):
    ax.annotate('', (x+.5, 3.18), (x, 3.18), arrowprops={'arrowstyle':'->', 'lw':2, 'color':INK})
# One compact cross-section relates the pathway to the two compartments.
ax.add_patch(Rectangle((.1, .86), 11.8, .36, color='#d8e6ef', zorder=0))
ax.text(.18, 1.5, 'CYTOSOL', fontsize=10, weight='bold')
ax.text(.18, .38, 'ER LUMEN', fontsize=10, weight='bold')
ax.text(1.45, 1.0, 'ER membrane', fontsize=10, va='center')
ax.add_patch(Ellipse((9.85, 1.86), 1.6, .97, facecolor='#b4c9d7', edgecolor=BLUE, lw=1.5))
ax.text(10.9, 1.92, 'ribosome', fontsize=10, va='center')
for x in (9.48, 10.03):
    ax.add_patch(FancyBboxPatch((x, .75), .24, .62, boxstyle='round,pad=.02',
                              facecolor=TEAL, edgecolor=TEAL))
ax.text(7.1, .6, 'Sec61 channel', fontsize=10, va='center')
ax.annotate('', (9.55, .9), (8.65, .66), arrowprops={'arrowstyle':'-', 'color':INK})
ax.plot([9.85,9.85,9.85,9.7,9.45,9.15,8.9], [1.68,1.22,.72,.43,.34,.43,.32], color=BLUE, lw=3)
ax.text(8.15,.12, 'growing chain', fontsize=9, color=BLUE)
fig.text(.045, .51, 'Possible final outcomes  (N → C follows each chain)', fontsize=13, weight='bold')

labels = [('A  Soluble luminal cargo', 'Cleaved leader; no retained span'),
          ('B  Cleaved leader + stop-transfer', 'Leader removed; anchor remains'),
          ('C  Internal signal anchor', 'Anchor retained; no cleavage shown')]
for i, (title, subtitle) in enumerate(labels):
    a = fig.add_axes([.035+i*.32, .105, .295, .365])
    a.set(xlim=(0, 4), ylim=(0, 4)); a.axis('off')
    a.text(0, 3.85, title, fontsize=11, weight='bold', va='top')
    a.text(0, 3.48, subtitle, fontsize=9.6, va='top')
    a.add_patch(Rectangle((0, 1.8), 4, .44, color='#d8e6ef', zorder=0))
    a.text(.08, 3.02, 'cytosol', fontsize=10)
    a.text(.08, .22, 'ER lumen', fontsize=10)
    if i == 0:
        a.plot([.75,1.15,1.5,1.85,2.2,2.55,2.9], [.92,1.12,.8,1.12,.8,1.12,.92], color=BLUE, lw=3)
        a.text(.52,.87,'N',weight='bold'); a.text(3.02,.87,'C',weight='bold')
        a.plot([2.78,3.25], [2.05,2.05], color=ORANGE, lw=5)
        a.text(2.48,1.48,'cleaved\nleader',fontsize=9,color=ORANGE,ha='center')
        a.annotate('', (2.94,1.98), (2.66,1.72), arrowprops={'arrowstyle':'-', 'color':ORANGE})
    elif i == 1:
        a.plot([.95,1.35,1.8,2.0,2.0,2.0,2.45,2.95], [.85,1.1,.85,1.1,1.8,2.5,2.65,2.5], color=BLUE, lw=3)
        a.plot([2,2], [1.8,2.24],color=TEAL,lw=7)
        a.text(.65,.72,'N',weight='bold'); a.text(3.08,2.48,'C',weight='bold')
        a.text(2.45,1.25,'retained\nstop-transfer',fontsize=9,color=TEAL)
        a.plot([.32,.63], [2.05,2.05], color=ORANGE,lw=5)
    else:
        a.plot([.65,1.15,1.65,2.0,2.0,2.0,2.45,2.95], [2.65,2.48,2.65,2.48,2.24,1.0,.85,1.08], color=BLUE,lw=3)
        a.plot([2,2], [1.8,2.24],color=PURPLE,lw=7)
        a.text(.35,2.59,'N',weight='bold'); a.text(3.1,1.02,'C',weight='bold')
        a.text(2.4,1.42,'retained\nsignal anchor',fontsize=9,color=PURPLE)
        a.text(.1,.65,'One possible orientation',fontsize=9)
fig.text(.045,.045,'ER entry alone does not specify secretion. Internal signals need not be removed or lie at the N terminus.',fontsize=10.5)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', dpi=110)
plt.close(fig)
