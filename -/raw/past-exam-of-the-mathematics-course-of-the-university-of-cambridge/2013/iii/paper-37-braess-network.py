"""Original Braess diagram. Python 3.14, Matplotlib 3.10.7 per root pyproject.
Writes its opaque PNG basename to cwd; respects external MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

fig,axes=plt.subplots(1,2,figsize=(10,3.6),dpi=100,facecolor='white')
pos={'O':(0,0),'U':(1,1),'V':(1,-1),'D':(2,0)}
for i,ax in enumerate(axes):
    edges=[('O','U'),('U','D'),('O','V'),('V','D')]
    if i:edges.append(('U','V'))
    for u,v in edges:
        colour='#a05618' if (u,v)==('U','V') else '#21618c'
        ax.add_patch(FancyArrowPatch(pos[u],pos[v],arrowstyle='-|>',mutation_scale=13,linewidth=2,color=colour,shrinkA=14,shrinkB=14))
    for name,(x,y) in pos.items():
        ax.add_patch(Circle((x,y),.09,facecolor='white',edgecolor='black',lw=1.3,zorder=3))
        ax.text(x,y,name,ha='center',va='center',fontsize=11,zorder=4)
    for xy,label in [((.34,.69),'delay = link flow'),((1.73,.69),'delay = 1'),((.32,-.68),'delay = 1'),((1.7,-.68),'delay = link flow')]:
        ax.text(*xy,label,ha='center',fontsize=10,bbox={'facecolor':'white','edgecolor':'none','pad':1.5})
    if i:ax.text(1.11,0,'delay = 0',ha='left',fontsize=10,color='#a05618')
    ax.set_title(['Before: half the traffic on each route','After: all traffic uses the middle route'][i],fontsize=11,pad=12)
    ax.text(1,-1.5,['Equilibrium trip time = 3/2','Equilibrium trip time = 2'][i],ha='center',fontsize=12,fontweight='bold')
    ax.set(xlim=(-.3,2.3),ylim=(-1.7,1.25),aspect='equal')
    ax.axis('off')
fig.subplots_adjust(left=.03,right=.97,bottom=.04,top=.84,wspace=.24)
fig.savefig(Path.cwd()/'paper-37-braess-network.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
