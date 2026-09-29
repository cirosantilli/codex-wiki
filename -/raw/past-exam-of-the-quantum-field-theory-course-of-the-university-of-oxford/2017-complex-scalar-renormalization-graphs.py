"""Original oriented complex-scalar graphs; Python 3.14/numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
plt.rcParams.update({'font.size':11})
fig,axs=plt.subplots(2,5,figsize=(14,6.3),layout='constrained',facecolor='white')
col='#126782';ct='#a43838'
def edge(ax,a,b,rad=0):ax.add_patch(FancyArrowPatch(a,b,connectionstyle=f'arc3,rad={rad}',arrowstyle='-|>',mutation_scale=11,lw=1.8,color=col,shrinkA=0,shrinkB=0))
def dot(ax,p,counter=False):ax.plot(*p,marker='x' if counter else 'o',color=ct if counter else col,ms=10 if counter else 6,mew=2)
def ends(ax,p,types,left,labels=None):
 sign=-1 if left else 1
 for j,typ in enumerate(types):
  y=p[1] if len(types)==1 else (.13 if j==0 else .83)
  out=(sign*1.02,y)
  edge(ax,out,p) if typ=='phi' else edge(ax,p,out)
  if labels:ax.text(out[0],out[1]+.10,labels[j],ha='center',fontsize=10)
def contact(ax,counter=False):
 p=(0,.48);ends(ax,p,['phi','phi'],True);ends(ax,p,['star','star'],False);dot(ax,p,counter)
def bubble(ax,kind):
 a=(-.45,.48);b=(.45,.48)
 if kind=='s':
  ends(ax,a,['phi','phi'],True,['1','2']);ends(ax,b,['star','star'],False,['3','4'])
  edge(ax,a,b,.65);edge(ax,a,b,-.65)
 else:
  swapped=kind=='u'
  ends(ax,a,['phi','star'],True,['1','4' if swapped else '3']);ends(ax,b,['phi','star'],False,['2','3' if swapped else '4'])
  edge(ax,a,b,.65);edge(ax,b,a,.65)
 dot(ax,a);dot(ax,b)
def caption(ax,s):ax.text(0,-.35,s,ha='center',va='top',fontsize=11)
ax=axs[0,0];edge(ax,(-1,.45),(1,.45));caption(ax,r'Tree inverse kernel'+'\n'+r'$i(p^2-m^2)$')
ax=axs[0,1];p=(0,.30);edge(ax,(-1,.30),p);edge(ax,p,(1,.30));ax.add_patch(Circle((0,.58),.28,fill=False,color=col,lw=1.8));edge(ax,(.28,.58),(.24,.73));dot(ax,p);caption(ax,'Directed tadpole\nS = 1; order g')
ax=axs[0,2];edge(ax,(-1,.45),(1,.45));dot(ax,(0,.45),True);caption(ax,r'Mass counterterm'+'\n'+r'$-i\delta_{m^2}$')
axs[0,3].text(0,.6,'Two-point vertex',ha='center',weight='bold');axs[0,3].text(0,.08,'No momentum-dependent\none-loop correction',ha='center')
axs[0,4].text(0,.6,'Arrow key',ha='center',weight='bold');axs[0,4].text(0,.05,r'$\phi$ legs enter; $\phi^*$ legs leave'+'\n'+r'Each interaction: 2 in, 2 out',ha='center',fontsize=10)
ax=axs[1,0];contact(ax);caption(ax,r'Tree contact'+'\n'+r'$-ig\mu^\epsilon$')
ax=axs[1,1];bubble(ax,'s');caption(ax,'s-channel bubble\nS = 2')
ax=axs[1,2];bubble(ax,'t');caption(ax,'t-channel bubble\nS = 1')
ax=axs[1,3];bubble(ax,'u');caption(ax,'u-channel bubble\nS = 1')
ax=axs[1,4];contact(ax,True);caption(ax,r'Coupling counterterm'+'\n'+r'$-i\mu^\epsilon g\delta_g$')
for ax in axs.flat:ax.set(xlim=(-1.25,1.25),ylim=(-.95,1.2));ax.set_aspect('equal');ax.axis('off');ax.set_facecolor('white')
fig.suptitle('Complex scalar quartic theory: tree + one loop + counterterm (amputated vertices)',fontsize=16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
