"""Original schematic; Python 3.14.4, matplotlib 3.10.7. Output is in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(7.6, 3.8), dpi=100, facecolor='white')
fig.subplots_adjust(left=.02, right=.98, bottom=.08, top=.96)
ax.set(xlim=(0,10), ylim=(0,5))
ax.axis('off')
nodes = {'prior': (1.65,3.7,'Prior aggression'),
         'family': (1.65,1.15,'Family / peer\nenvironment'),
         'media': (5.1,2.45,'Violent-media\nexposure'),
         'later': (8.5,2.45,'Later aggression')}
def arrow(start, end, rad=0, color='#53616c', dashed=False):
    patch=FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=15,
                         linewidth=1.8,connectionstyle=f'arc3,rad={rad}',
                         color=color,linestyle='--' if dashed else '-')
    ax.add_patch(patch)
arrow((2.9,3.7),(7.3,2.85),rad=-.21)
arrow((2.9,1.15),(7.3,2.05),rad=.22)
arrow((2.9,3.4),(3.85,2.85))
arrow((2.9,1.45),(3.85,2.05))
arrow((6.35,2.45),(7.25,2.45),color='#af4428',dashed=True)
for key,(x,y,label) in nodes.items():
    ax.add_patch(FancyBboxPatch((x-1.22,y-.45),2.44,.9,
                              boxstyle='round,pad=.04,rounding_size=.12',
                              facecolor='#f0f5f8',edgecolor='#334e68',linewidth=1.3,zorder=3))
    ax.text(x,y,label,ha='center',va='center',zorder=4)
ax.text(6.8,.85,'Hypothesized\nmedia effect',color='#af4428',ha='center',va='center',fontsize=10.5)
ax.text(5,.15,'Schematic causal hypotheses; no effect sizes or empirical estimates',ha='center',va='center',fontsize=10,color='#485563')
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
