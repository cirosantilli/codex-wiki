from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':13})
fig,ax=plt.subplots(figsize=(8,4.9),dpi=130,facecolor='white')
initial=np.array([30.,100.]);colors=['#2268a3','#26764e','#b13939']
handles=[]
for frac,bh,col in zip([.25,.1,.05],[[26,60],[28,70],[29,80]],colors):
 final=np.array(bh);amin=2*frac**.4*initial**2/final;amax=50*(final/50)**.75
 ax.plot(initial,amin,'o-',color=col,lw=2,ms=6)
 ax.plot(initial,amax,'s--',color=col,lw=2,ms=5)
 handles.append(Line2D([0],[0],color=col,lw=2,label=fr'$Z/Z_\odot=1/{round(1/frac)}$'))
 for xi,lo,hi in zip(initial,amin,amax):
  if lo<hi:ax.plot([xi,xi],[lo,hi],color=col,lw=6,alpha=.22)
legend1=ax.legend(handles=handles,loc='upper left',fontsize=10,frameon=False);ax.add_artist(legend1)
ax.legend(handles=[Line2D([0],[0],color='0.25',marker='o',ls='-',label='Wind-expanded minimum'),Line2D([0],[0],color='0.25',marker='s',ls='--',label='Merger upper bound')],loc='lower right',fontsize=10,frameon=True,facecolor='white')
ax.set(xlim=(24,107),ylim=(0,210),xlabel=r'Initial mass of each star $M^0/M_\odot$',ylabel=r'Separation bound $a/R_\odot$',title='Overlap requires the minimum to lie below the merger bound')
ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
