"""Original qualitative actomyosin nucleotide/affinity cycle, with timing qualification."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

fig,ax=plt.subplots(figsize=(10.6,6.1),facecolor='white');ax.set(xlim=(0,10),ylim=(0,6));ax.axis('off')
boxes=[(2,4.3,'A·M\nNucleotide-free\nStrong actin binding'),(8,4.3,'M·ATP\nDetached / low affinity'),(8,1.5,'M·ADP·Pi\nPrimed; weak actin engagement'),(2,1.5,'A·M·ADP\nStrongly attached\nPost-stroke state')]
for x,y,label in boxes:
 ax.add_patch(FancyBboxPatch((x-1.65,y-.6),3.3,1.2,boxstyle='round,pad=.03',facecolor='#e7eff5',edgecolor='#245f8a',lw=1.5))
 ax.text(x,y,label,ha='center',va='center',fontsize=12)
for a,b,label,xy in [((3.7,4.3),(6.3,4.3),'ATP binding → detachment',(5,5.0)),((8,3.65),(8,2.15),'ATP hydrolysis\nand priming',(8,2.9)),((6.3,1.5),(3.7,1.5),'Actin engagement; force-producing\ntransition coupled to Pi release',(5,.55)),((2,2.15),(2,3.65),'ADP release',(2,2.9))]:
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=17,lw=1.6,color='#a34f26'))
 ax.text(*xy,label,ha='center',va='center',fontsize=11,bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.text(5,5.65,'Myosin couples nucleotide state, actin affinity and mechanical motion',ha='center',fontsize=14,weight='bold')
fig.text(.5,.015,'A = actin; M = myosin. Exact phosphate/force-transition timing and rate-limiting steps depend on isoform and load.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.035,1,1));fig.savefig('paper-4-myosin-cycle.png',dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
