"""Original IgG chain and binding cartoons; Python 3.14, matplotlib 3.10.7.

Run from _media; writes the matching PNG to the current working directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle, Circle

HEAVY, LIGHT = '#2478a5', '#da8c32'
VH, VL, EPITOPE = '#104762', '#864c16', '#a53773'
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, (architecture, binding) = plt.subplots(1, 2, figsize=(12, 5.5), facecolor='white')
fig.subplots_adjust(left=.025, right=.985, top=.91, bottom=.12, wspace=.08)
for ax in (architecture, binding):
    ax.set(xlim=(0, 10), ylim=(0, 8)); ax.axis('off')

def segment(ax, points, color, width=10):
    ax.plot(*zip(*points), color=color, lw=width, solid_capstyle='round')

architecture.set_title('Conventional IgG: four chains, two sites', fontsize=13, pad=12)
for sign in (-1, 1):
    x = 5 + sign*.28
    segment(architecture, [(x, 1.7), (x, 3.7), (5+sign*2.3, 6.1)], HEAVY)
    segment(architecture, [(5+sign*1.75, 5.45), (5+sign*2.3, 6.1)], VH)
    segment(architecture, [(5+sign*2.08, 4.5), (5+sign*3.1, 5.75)], LIGHT)
    segment(architecture, [(5+sign*2.65, 5.2), (5+sign*3.1, 5.75)], VL)
    architecture.add_patch(Ellipse((5+sign*2.73, 5.94), 1.55, .65,
                                    angle=-sign*45, fill=False, lw=1.5, ec=EPITOPE))
    # Heavy/light disulfide symbol joins the neighboring chains.
    segment(architecture, [(5+sign*1.55, 4.95), (5+sign*2.38, 4.87)], '#555555', 2)
for y in (2.65, 3.45):
    segment(architecture, [(4.72, y), (5.28, y)], '#555555', 2)
architecture.annotate('one paratope\n(both variable tips)', xy=(2.27, 6.0), xytext=(.1, 7.25),
                      arrowprops={'arrowstyle': '-', 'color': EPITOPE}, ha='left', color=EPITOPE)
architecture.annotate('variable regions\n(darker tips)', xy=(7.15, 5.95), xytext=(7.2, 7.1),
                      arrowprops={'arrowstyle': '-', 'color': '#333333'}, ha='center')
architecture.annotate('flexible hinge', xy=(5.3, 3.75), xytext=(6.5, 3.45),
                      arrowprops={'arrowstyle': '-', 'color': '#333333'}, ha='left')
architecture.annotate('disulfide bonds', xy=(5, 2.65), xytext=(.35, 2.7),
                      arrowprops={'arrowstyle': '-', 'color': '#555555'}, ha='left')
architecture.text(5, .95, '2 heavy chains + 2 light chains', ha='center', weight='bold')
architecture.text(5, .25, 'Paler portions: constant regions', ha='center')
for x, color, label in ((1.0, HEAVY, 'heavy'), (6.0, LIGHT, 'light')):
    architecture.plot([x, x+.5], [1.55, 1.55], lw=8, color=color)
    architecture.text(x+.7, 1.55, label, va='center')

binding.set_title('One contact versus two-arm attachment', fontsize=13, pad=12)

def attached_igg(ax, cx, cy, two):
    for sign in (-1, 1):
        segment(ax, [(cx+sign*.1, cy), (cx+sign*.1, cy+.65),
                     (cx+sign*1.15, cy+1.85)], HEAVY, 6)
        segment(ax, [(cx+sign*.95, cy+1.6), (cx+sign*1.15, cy+1.85)], VH, 6)
        segment(ax, [(cx+sign*1.02, cy+.95), (cx+sign*1.43, cy+1.57)], LIGHT, 5)
        segment(ax, [(cx+sign*1.3, cy+1.38), (cx+sign*1.43, cy+1.57)], VL, 5)
    ax.add_patch(Rectangle((cx-2, cy+2.25), 4, .22, fc='#e6e6e6', ec='#888888'))
    for sign in ((-1, 1) if two else (-1,)):
        ax.add_patch(Circle((cx+sign*1.22, cy+2.12), .14, fc=EPITOPE, ec=EPITOPE))
        ax.plot([cx+sign*1.22, cx+sign*1.22], [cy+1.9, cy+2.05], color=EPITOPE, lw=2)

attached_igg(binding, 2.35, 3.7, False)
attached_igg(binding, 7.35, 3.7, True)
binding.text(2.35, 6.65, 'one accessible epitope', ha='center')
binding.text(7.35, 6.65, 'two suitably spaced epitopes', ha='center')
binding.text(2.35, 3.35, 'one contact', ha='center', weight='bold')
binding.text(7.35, 3.35, 'two contacts', ha='center', weight='bold')
binding.text(5, 2.5, 'If one contact opens, the other can retain the IgG.', ha='center')
binding.text(5, 1.85, 'The nearby arm can bind again: avidity.', ha='center', color=EPITOPE, weight='bold')
binding.text(5, .9, 'Affinity concerns an individual site–epitope interaction.\nAvidity also depends on geometry and accessibility.', ha='center', linespacing=1.6)
fig.text(.5, .035, 'Original explanatory cartoons • no structural coordinates or physical scale', ha='center', color='#555555')
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=110, facecolor='white', transparent=False)
plt.close(fig)
