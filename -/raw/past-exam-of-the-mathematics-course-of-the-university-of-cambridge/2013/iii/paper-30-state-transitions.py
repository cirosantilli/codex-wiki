"""Render the fitted progressive model. Python 3.14, matplotlib 3.10.7.

Writes only paper-30-state-transitions.png to the caller's current directory.
Matplotlib respects the caller's MPLCONFIGDIR; this script does not replace it.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(8, 3.6), dpi=100, facecolor='white')
ax.set_facecolor('white')
ax.set_xlim(0, 8)
ax.set_ylim(0, 3.6)
ax.axis('off')
centres = [(1.25, 2.25), (4, 2.25), (6.75, 2.25)]
labels = ['1: mild cognitive\nimpairment', '2: dementia', '3: death\n(absorbing)']
for (x, y), label in zip(centres, labels):
    ax.add_patch(FancyBboxPatch((x-.95,y-.48),1.9,.96,boxstyle='round,pad=0.08',edgecolor='#29485b',facecolor='#eaf2f6',linewidth=1.7))
    ax.text(x,y,label,ha='center',va='center',fontsize=11,color='#193747')
for left, right, text in [(2.3,2.95,'0.1849'),(5.05,5.7,'0.06143')]:
    ax.add_patch(FancyArrowPatch((left,2.25),(right,2.25),arrowstyle='-|>',mutation_scale=17,linewidth=1.7,color='#29485b'))
    ax.text((left+right)/2,2.67,text,ha='center',fontsize=11)
ax.add_patch(FancyArrowPatch((1.25,1.67),(6.75,1.67),connectionstyle='arc3,rad=0.33',arrowstyle='-|>',mutation_scale=17,linewidth=1.7,color='#29485b'))
ax.text(4,.43,'0.01935',ha='center',fontsize=11)
ax.text(4,3.18,'Progressive model: fitted transition intensities',ha='center',fontsize=13)
ax.text(4,.12,'All rates in years⁻¹. No recovery arrows; death is absorbing.',ha='center',fontsize=10)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig('paper-30-state-transitions.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
