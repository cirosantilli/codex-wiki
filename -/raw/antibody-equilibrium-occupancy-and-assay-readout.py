"""Stipulated 1:1 occupancy model and assay interpretation, not measured data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media; writes to CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, (curve, workflow) = plt.subplots(1, 2, figsize=(10.8, 5.4), facecolor='white',
                                     gridspec_kw={'width_ratios': [1.05, 1]})
fig.subplots_adjust(left=.075, right=.975, bottom=.18, top=.88, wspace=.28)
c = np.geomspace(.5, 2000, 500)
for kd, color in ((20, '#2478a5'), (200, '#a53773')):
    curve.semilogx(c, c/(kd+c), lw=2.5, color=color, label=rf'$K_d={kd}\,\mathrm{{nM}}$')
for value, label, offset in ((2, r'$1/11$', (8, 10)), (20, r'$1/2$', (-35, 8)),
                             (200, r'$10/11$', (6, -24))):
    theta=value/(20+value)
    curve.plot(value, theta, 'o', color='#2478a5', ms=6)
    curve.annotate(label, (value, theta), xytext=offset, textcoords='offset points', color='#104762')
curve.axhline(.5, color='#aaaaaa', lw=.7, ls=':')
curve.set(xlim=(.5, 2000), ylim=(0, 1.04), xlabel=r'Free antigen concentration $c$ (nM)',
          ylabel=r'Fraction of sites occupied $\theta$')
curve.set_xticks([1, 2, 20, 200, 2000], labels=['1', '2', '20', '200', '2000'])
curve.grid(alpha=.15)
curve.legend(loc='lower right', frameon=False)
curve.set_title(r'Stipulated equilibrium: $\theta=c/(K_d+c)$', fontsize=12, pad=16)
curve.spines[['top', 'right']].set_visible(False)
workflow.set(xlim=(0, 1), ylim=(0, 1)); workflow.axis('off')
workflow.set_title('What an assay adds to binding', fontsize=12, pad=16)
items=[(.88, 'Accessible epitopes', 'transfer, folding, surface presentation'),
       (.66, 'Binding-site occupancy', 'affinity, concentration; possible avidity'),
       (.44, 'Material retained after washing', 'detachment and rebinding'),
       (.22, 'Recorded assay signal', 'label, background, detector saturation')]
for y, title, detail in items:
    workflow.add_patch(FancyBboxPatch((.035,y-.075), .93, .15,
                      boxstyle='round,pad=.015', facecolor='#f4f7fa', edgecolor='#a0aab7'))
    workflow.text(.5, y+.02, title, ha='center', va='center', weight='bold', fontsize=10.5)
    workflow.text(.5, y-.035, detail, ha='center', va='center', fontsize=9.2, color='#444444')
for a,b in zip(items,items[1:]):
    workflow.annotate('', (.5,b[0]+.09), (.5,a[0]-.09),
                      arrowprops={'arrowstyle': '->', 'color': '#666666'})
workflow.text(.5,.035, 'Half-maximal signal need not mean half occupancy.', ha='center', fontsize=10, color='#a53773')
fig.text(.5,.065, 'Original model and conceptual workflow • invented constants • no sensorgrams or experimental signals',
         ha='center', fontsize=10, color='#555555')
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=110, facecolor='white', transparent=False)
plt.close(fig)
