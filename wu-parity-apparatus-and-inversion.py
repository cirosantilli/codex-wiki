"""Original functional Wu-experiment schematic and axial/polar parity geometry.

Historical components: Wu et al., Physical Review 105, 1413–1414 (1957), Fig. 1.
No engineering dimensions or measured asymmetry are reconstructed.
Python 3.14, matplotlib 3.10.7; run from _media to emit basename.png to CWD.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, Rectangle

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig, (ax, geo) = plt.subplots(1, 2, figsize=(14, 7.4),
                             gridspec_kw={'width_ratios': [1.22, 1]}, facecolor='white')
blue, red, green = '#176a9c', '#b44829', '#387c53'
for panel in (ax, geo):
    panel.set(xlim=(0, 1), ylim=(0, 1))
    panel.axis('off')


def box(panel, xy, w, h, label, color=blue, size=11):
    x, y = xy
    panel.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.012',
                    facecolor='#f5f8fa', edgecolor=color, linewidth=1.6))
    panel.text(x+w/2, y+h/2, label, ha='center', va='center', fontsize=size)


def arrow(panel, start, end, color=blue, width=2):
    panel.annotate('', end, start, arrowprops={'arrowstyle': '-|>', 'color': color,
                                             'lw': width, 'mutation_scale': 13})


ax.set_title('Preparation and separate readouts', fontsize=16, weight='bold', pad=17)
# A functional flow layout, intentionally distinct from the original engineering drawing.
box(ax, (.08, .77), .34, .12, 'light pipe\n→ photomultiplier')
box(ax, (.08, .54), .34, .10, 'anthracene counter')
arrow(ax, (.25, .65), (.25, .755))
ax.text(.28, .70, 'light', color=blue, fontsize=10)
box(ax, (.08, .27), .34, .12, 'CMN crystal\n⁶⁰Co surface layer')
ax.add_patch(Rectangle((.11, .39), .28, .012, color=red))
arrow(ax, (.25, .415), (.25, .525), red)
ax.text(.29, .465, r'$\beta^-$', color=red, fontsize=13)
# Holding field loop symbolizes the polarizing solenoid, not actual winding geometry.
ax.add_patch(Ellipse((.25, .33), .47, .23, fill=False, ec=green, lw=1.8, ls='--'))
arrow(ax, (.035, .24), (.035, .45), green)
ax.text(.02, .19, r'$B$ reverses', color=green, fontsize=10)
box(ax, (.60, .55), .32, .12, 'polar γ counter')
box(ax, (.60, .27), .32, .12, 'equatorial γ counter', size=10)
arrow(ax, (.43, .40), (.59, .57), green)
arrow(ax, (.43, .33), (.59, .33), green)
ax.text(.74, .47, 'γ anisotropy', ha='center', color=green)
ax.text(.74, .43, 'orientation / thermometry', ha='center', fontsize=10, color=green)
box(ax, (.08, .035), .84, .09, 'adiabatic demagnetization → cold sample', size=11)
arrow(ax, (.47, .13), (.38, .24), green)
ax.text(.51, .965, 'Functional paths • geometry not to scale', ha='center', fontsize=10, color='#555555')

geo.set_title('Invert space: r → −r', fontsize=16, weight='bold', pad=17)
geo.text(.5, .94, 'Full inversion, rather than a drawn plane mirror', ha='center', fontsize=10)
for x, label in ((.23, 'Original'), (.77, 'Parity image')):
    geo.text(x, .83, label, ha='center', weight='bold', fontsize=13)
    geo.add_patch(Ellipse((x, .53), .16, .11, fc='#eaf2f6', ec=blue))
    arrow(geo, (x, .58), (x, .76), blue, 3)
    geo.text(x+.045, .70, r'$\mathbf{J}$', color=blue, fontsize=15)
arrow(geo, (.23, .47), (.23, .27), red, 3)
geo.text(.28, .31, r'$\mathbf{p}$', color=red, fontsize=15)
arrow(geo, (.90, .58), (.90, .76), red, 3)
geo.text(.94, .67, r'$-\mathbf{p}$', color=red, fontsize=13)
# The right momentum is displaced sideways to keep both upward arrows visible.
geo.text(.77, .22, 'arrows offset for visibility', ha='center', fontsize=9, color='#555555')
arrow(geo, (.40, .53), (.59, .53), '#666666')
geo.text(.5, .58, r'$\mathcal{P}$', ha='center', fontsize=16)
geo.text(.5, .15, r'axial: $\mathbf{J}\to\mathbf{J}$     polar: $\mathbf{p}\to-\mathbf{p}$', ha='center', fontsize=13)
geo.text(.5, .06, r'$\mathbf{J}\cdot\mathbf{p}\ \to\ -\mathbf{J}\cdot\mathbf{p}$', ha='center', fontsize=17, color=red)
fig.suptitle('Polarized beta decay: a direction tied to spin', fontsize=20, weight='bold', y=.985)
fig.text(.5, .014, 'Original explanatory diagram • CMN = cerium magnesium nitrate • no measured rates shown',
         ha='center', fontsize=10, color='#555555')
fig.subplots_adjust(left=.035, right=.97, bottom=.08, top=.85, wspace=.18)
fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
