"""Draw pulse generator state chart and the original sampled timing sequence.
Writes PNG in cwd. Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig=plt.figure(figsize=(9,6.8),facecolor='white');gs=fig.add_gridspec(2,1,height_ratios=[1.2,1],hspace=.4)
ax=fig.add_subplot(gs[0]);ax.set(xlim=(-3,3),ylim=(-1.15,1.65),aspect='equal');ax.axis('off')
pos={'Ready':(-2,0),'Pulse':(0,.7),'Wait':(2,0)}
for s,p in pos.items():
    ax.add_patch(Circle(p,.43,facecolor='#ffe0af' if s=='Pulse' else '#e6f1fa',edgecolor='#264f70',lw=1.5))
    ax.text(*p,s+'\nz='+('1' if s=='Pulse' else '0'),ha='center',va='center')
edges=[('Ready','Pulse','10',-.1,(-1,1)),('Pulse','Ready','01,11',-.1,(-1,.03)),('Pulse','Wait','00,10',.05,(1,.8)),('Wait','Ready','01,11',-.35,(0,-.85))]
for s,t,lab,rad,loc in edges:
    ax.add_patch(FancyArrowPatch(pos[s],pos[t],shrinkA=32,shrinkB=32,connectionstyle=f'arc3,rad={rad}',arrowstyle='-|>',mutation_scale=14,color='#264f70',lw=1.4))
    ax.text(*loc,lab,ha='center',bbox={'facecolor':'white','edgecolor':'none','pad':1})
for s,lab in [('Ready','00,01,11'),('Wait','00,10')]:
    x,y=pos[s];sgn=-1 if s=='Ready' else 1
    ax.add_patch(FancyArrowPatch((x+sgn*.3,y+.3),(x+sgn*.3,y-.3),connectionstyle=f'arc3,rad={-2*sgn}',arrowstyle='-|>',mutation_scale=13,color='#264f70'))
    ax.text(x+sgn*.68,y,lab,ha='center',rotation=90,fontsize=9)
ax.annotate('start',xy=(-2.33,.3),xytext=(-2.65,1),arrowprops={'arrowstyle':'->'},ha='center')
ax.set_title('One-cycle pulse, with reset priority for ab = 11',weight='bold')
a=fig.add_subplot(gs[1]);time=np.arange(17)
as_=[0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0]
bs_=[0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0]
s='Ready';zs=[]
for av,bv in zip(as_,bs_):
    s='Ready' if bv else ('Pulse' if s=='Ready' and av else 'Ready' if s=='Ready' else 'Wait')
    zs.append(int(s=='Pulse'))
for vals,offset,col in [(as_,4,'#39688a'),(bs_,2,'#39688a'),(zs,0,'#ae6325')]:
    # Sampled inputs are shown through each edge; z is the state after that edge.
    a.step(time,np.array(vals+[vals[-1]])*.7+offset,where='post',color=col,lw=1.7)
for k in range(16):a.axvline(k,color='.85',lw=.6,zorder=-1)
a.set(xlim=(0,16),ylim=(-.2,5.1),yticks=[.3,2.3,4.3],yticklabels=['z after edge','b sampled','a sampled'],xticks=np.arange(16)+.05,xticklabels=np.arange(1,17),xlabel='Clock edge number (values held until the next edge)')
a.tick_params(axis='x',labelsize=9);a.spines[['top','right']].set_visible(False)
a.set_title('Source timing: pulses after edges 2, 10, 13 and 15',fontsize=11)
fig.savefig(Path.cwd()/'computing-prelims-2003-pulse.png',dpi=120,facecolor='white',bbox_inches='tight',metadata={'Software':'computing-prelims-2003-pulse.py'})
plt.close(fig)
