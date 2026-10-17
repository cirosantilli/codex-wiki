"""Original comparison of established Mtr transport and a qualified phototrophic export route."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

fig,ax=plt.subplots(figsize=(13.4,6.0),facecolor='white');ax.set(xlim=(-.2,11.8),ylim=(0,5));ax.axis('off')
xs=[.8,2.8,4.8,6.8,8.8,10.8]
hetero=['Organic donor','Inner membrane\nquinol / CymA','Periplasmic\ncarriers','MtrCAB\nouter membrane','Surface cytochrome\nand/or mediator','Mineral /\nelectrode']
photo=['Water + light','Thylakoids\nPSII → PSI','Fd / NADPH\nand metabolism','Envelope export\nroute variable','Endogenous or\nadded mediator','Electrode /\nexternal oxidant']
for y,labels,title in [(3.5,hetero,'Heterotroph: representative Shewanella respiratory route'),(1.25,photo,'Oxygenic phototroph: one possible mediated-export route')]:
 ax.text(5.5,y+.9,title,ha='center',fontsize=13,weight='bold')
 for i,(x,label) in enumerate(zip(xs,labels)):
  uncertain=y<2 and i==3
  ax.add_patch(FancyBboxPatch((x-.78,y-.43),1.56,.86,boxstyle='round,pad=.035',facecolor='#fff0dc' if uncertain else '#e6eef4',edgecolor='#a34f26' if uncertain else '#245f8a',lw=1.3))
  ax.text(x,y,label,ha='center',va='center',fontsize=10)
  if i<5:ax.add_patch(FancyArrowPatch((x+.82,y),(xs[i+1]-.82,y),arrowstyle='-|>',mutation_scale=11,lw=1.2,ls='--' if y<2 and i in [2,3] else '-',color='#a34f26' if y<2 and i in [2,3] else '#245f8a'))
ax.text(5.5,.37,'Dashed steps: do not assume a universal cyanobacterial Mtr-equivalent.\nNo added mediator does not exclude secretion of an endogenous mediator.',ha='center',fontsize=11)
fig.tight_layout();fig.savefig('paper-4-external-electrons.png',dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
